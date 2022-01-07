var lista_definitiva = []
let number = (document.querySelector('#txtnumero'))
var area_resultados = document.querySelector("#resp")


function adicionar() {
    if (number.value < 0 || number.value > 100) {
        alert('erro, números abaixo de 0 ou maior que 100 não permitido')
    } else if (lista_definitiva.indexOf(number.value) != -1) {
        alert('erro, valor já informado')
    } else {
        lista_definitiva.push(number.value)
        let msg_lista = document.querySelector('#lista')
        let element = document.createElement('option')
        element.text = `Numero ${number.value} adicionado com sucesso`
        msg_lista.appendChild(element)
        area_resultados.innerHTML = ''
        if (lista_definitiva.length > 10) {
            msg_lista.setAttribute('size', `10`)
        } else {
             msg_lista.setAttribute('size', `${lista_definitiva.length}`) //altera o tamanho da minha select te acordo com a quantidade de elementos dentro do array
        }
        number.value = ''
        number.focus()
    }
    
}


function verifique() {
    if (lista_definitiva.length == 0) {
        alert('erro, Adicione valores para verificar')
    } else {
        let maior = lista_definitiva[0]
        let menor = lista_definitiva[0]
        let soma = 0
        let media = 0

        for (let pos in lista_definitiva){
            soma += Number(lista_definitiva[pos])
            if (lista_definitiva[pos] > maior)
            maior = lista_definitiva[pos]
            if (lista_definitiva[pos] < menor) {
                menor = lista_definitiva[pos]
            }
        }

        area_resultados.innerHTML = ''
        area_resultados.innerHTML += `<p>Ao todo foram adicionado ${lista_definitiva.length} valores</p>`
        area_resultados.innerHTML += `<p>O maior número adicionado foi ${maior}</p>`
        area_resultados.innerHTML += `<p>O menor número adicionado foi ${menor}</p>`
        area_resultados.innerHTML += `<p>A soma total dos valores é ${soma}</p>`
        area_resultados.innerHTML += `<p>A média total é de ${soma/lista_definitiva.length}</p>`
    }
}
