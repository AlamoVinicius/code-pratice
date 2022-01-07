let numeros = [2, 4, 5, 2, 4, 1, 522, 154]
numeros[3] = 6  // adiciona um número na posição determinada dentro dos colchetes
numeros.push(5) // adiciona um elemento na ultima posição da array
numeros.push('ii') // posso adicionar elementos de outro tipo dentro do array ?
let qtdenumeros = numeros.length // retorna a quantidade de elemntos de um array
console.log(numeros)
let ordem = numeros.sort(compararNumeros) // Com esssa função comparNumeros garante o funcionamento do método sort.
console.log(ordem)

function compararNumeros(a, b) {
    return a - b
}

/*numeros.forEach((elementos, index, array) => console.log(elementos, index, array)) //usando o foreach para percorrer todo o array e exibir os elemntos, o indíce e um array, poderia usar o for comum mas preferi usar esse for Each para ver seu funcionamento
*/

for (const posicao in numeros) {
    console.log(numeros[posicao])        
}

let pos = numeros.indexOf(522) //retonra a posição do número passado no parâmetro caso ache nenhuma correspondência ele retonra -1
console.log(numeros)
console.log(pos)

