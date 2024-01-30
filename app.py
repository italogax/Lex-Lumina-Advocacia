from flask import Flask, request, jsonify, render_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

#Configuração do SendGrid
sg = SendGridAPIClient('mlsn.52ba50e0ee5615dca96c2a665b84facb0b9bfb3934889f7865503684c2a19666')

#Rota Raiz par servir a página inicial
@app.route('/')
def index():
    return render_template('index.html')

#Rota para receber dados do formulário e enviar e-mail
@app.route('/enviar-formulario', methods=['POST'])
def enviar_email():
    data = request.form
    nome = data.get('nome')
    email = data.get('email')
    mensagem = data.get('mensagem')

#Criar o objeto de e-mail
    mail = Mail(
        from_email='italogax13@gmail.com',
        to_emails='italogax13@gmail.com',
        subject='Teste site',
        html_content=f'<strong>Nome: {nome}<br>Email: {email}<br>Mensagem: {mensagem}</strong> '
    )

#Enviar o e-mail
    try:
        response = sg.send(mail)
        return jsonify({'message': 'E-mail enviado com sucesso!'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Errp ap emvoar p e-mail'}), 500

if __name__ == '__main__':
    app.run(debug=True)
