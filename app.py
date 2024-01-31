from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configurações do servidor.
smtp_server = "smtp.zoho.com"
smtp_port = 587
smtp_user = "italogax@zohomail.com"
smtp_password = "C9zwJHSBAAKM"

#Rota Raiz par servir a página inicial
@app.route('/')
def index():
    return render_template('index.html')

#Rota para receber dados do formulário e enviar e-mail
@app.route('/enviar-formulario', methods=['POST'])
def enviar_formulario():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    #Configurando a mensagem de e-mail
    email_msg = MIMEMultipart()
    email_msg['From'] = smtp_user
    email_msg['To'] = "italogax13@gmail.com"
    email_msg['Subject'] = "Novo Contato do Site"
    corpo = f"Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}"
    email_msg.attach(MIMEText(corpo, 'plain'))
    
    # Envia o e-mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, "italogax13@gmail.com", email_msg.as_string())

    return jsonify({'mensagem': 'E-mail enviado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
