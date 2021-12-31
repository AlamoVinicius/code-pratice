var nome = window.prompt('Escreva seu nome: ')
document.write(`Olá <strong>${nome}</strong>, seu nome tem ${nome.length} letras<br>`)
document.write(`Escrevendo seu nome em Upper case: ${nome.toUpperCase()}`)  //função para transformar em str maiuscula
/* 
n1.Tofixed(2) = converte para 2 casas reais em um dado float
n2.tofixed(2).replace('.', ',') = alem de converter para 2 casas decimais, troca o ponto para virgula.
para usar valor monetario local use: n1.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
*/