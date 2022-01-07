function exibir_tabuada() {
    var num = Number(document.querySelector('#strnumber').value)
    var res = document.querySelector('#seltab')

    if (num <= 0 || num > 100) {
        alert('[erro] valor inválido')
    } else {
        let r = 0
        res.innerHTML = ''
        for (let index = 1; index <= 10; index++) {
            r = num * index
            let item = document.createElement('option')
            item.text = `${num} x ${index} = ${r}`
            item.value = `res${index}`
            res.appendChild(item) // aqui adiciona o item como filho do res
        }
    }
}

