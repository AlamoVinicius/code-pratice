function contar() {
    var inicio = Number(document.querySelector('#number_initial').value)
    var final = Number(document.querySelector('#number_final').value)
    var passo = Number(document.querySelector('#passo').value)
    var res = document.querySelector('#res')

    if (inicio == 0 || final == 0 || passo == 0) {
        res.style.color = 'red'
        res.innerHTML = '[ERRO] Dados inválidos valor 0 não permitido'
    } else if (passo > final) {
        res.style.color = 'red'
        res.innerHTML = '[ERRO] Valor do passo maior que o final, contagem não realizada'
    } else {
        res.innerHTML = ''
        res.style.color = 'black'
        res.style.background = 'rgba(211, 211, 211, 0.5)'
        res.style.border = '1px solid rgba(0, 0, 0, 0.377)'
        res.style.boxShadow = 'inset 0px 0px 7px rgba(0, 0, 0, 0.692)'

        if (inicio < final) {
            for (let index = inicio; index <= final; index += passo) {
                res.innerHTML += `${index}`
                res.innerHTML += (index != final) ? ' ➜ ' : ''
            }
        } else {
            for (let index = inicio; index >= final; index -= passo) {
                res.innerHTML += index
                res.innerHTML += (index != final) ? ' ➜ ' : ''
            }
        }

    }
}


/*#res {
    margin-top: 10px;
    background-color: rgba(211, 211, 211, 0.5);
    border: 1px solid rgba(0, 0, 0, 0.377);
    padding: 10px;
    text-align: justify;
    box-shadow: inset 0px 0px 7px rgba(0, 0, 0, 0.692);
}
*/