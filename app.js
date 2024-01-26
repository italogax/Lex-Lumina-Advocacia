const express = require('express');
const app = express();
const path = require('path');

// Configuração para servir arquivos estáticos da pasta 'public'
app.use(express.static(path.join(__dirname, 'public')));

// Rota para a página inicial
app.get('/', (req, res) => {
    // Envia o arquivo 'index.html' como resposta
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

const port = 3000;
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});

//Body-Parser
const bodyParser = require('body-parser');

//Configuração do body-parser
app.use(bodyParser.urlencoded({ extended: true}));

//Criando rotass POST para o formulário
app.post('/enviar-formulario', (req, res) => {
    const dadosFormulario = req.body;
    console.log(dadosFormulario); //Aqui os dados são processados.
    
    //Enviando resposta para o frontend, como uma página de agradecimento ou uma mensagem de confirmação.
    res.send('Formulário recebido');
})