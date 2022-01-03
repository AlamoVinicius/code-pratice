function calcular() {    
    var strvel = window.document.querySelector('#strvel')
    var res = document.getElementById('res')
    strvel = Number(strvel.value)
    res.innerHTML = `<p>Sua velocidade atual é: <strong>${strvel}</strong> km/h</p>`

    res.style.display = 'inline-block'
    res.style.backgroundColor = 'Lightgrey'
    res.style.border = 'solid black'
    res.style.padding = '10px'
    res.style.marginTop = '30px'

    if (strvel > 60) {
        res.innerHTML += 'Velocidade acima do limite <strong>multado</strong>!'
    } else {
        res.innerHTML += 'Velocidade permitida dirija com segurança'
    }
    res.innerHTML += "<p>Dirija sempre com o cinto de segurança!!</p>"

}