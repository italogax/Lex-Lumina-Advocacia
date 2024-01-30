document.getElementById('meuFormulario').addEventListener('submit', function(e) {
    e.preventDefault(); //Impede o envio tradicional do formulário.

    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var mensagem = document.getElementById('mensagem').value;

    if (!nome || !email || !mensagem) {
        alert('Todos os campos são obrigatorios!')
    } else {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/enviar-formulario", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (this.readyState == XMLHttpRequest.DONE && this.status == 200) {
                alert("E-mail enviado com sucesso!");
            }
        } 

        xhr.send(`nome=${nome}&email=${email}&mensagem=${mensagem}`);
    }
});