/* para acessarmos o documento podemos usar o widow.document e alterar várias caracteriscas da página usando 
os métodos getElemnts com suas devidas funções.*/
var p1 = window.document.getElementsByTagName('p')[1]
// nesse exemplo eu acesso o documento p da posição 0, e com isso eu posso alterar ou escrever com o próximo comando
var corpo = window.document.body
window.document.write(p1.innerText) // estou mandando escrever o conteudo da minha váriavel p1
p1.style.color = 'black' //alterando a cor da váriavel para preto 
corpo.style.background = 'pink'
document.write('<br>' + p1.innerHTML) //innerHtml pega todo as marcações do html
// window.alert(p1.innerText) = para inserir um alerta no browser
// posso usar o getbyId para acessar um id especifica

// método recomendável por getbyselector:
var d = document.querySelector('div#msg')
d.style.background = 'black'  //usando querySelector por id