function verificar() {
    var pais = document.querySelector("#country")
    var res = document.getElementById('res')
    pais = pais.value.toUpperCase()
    res.innerHTML = `<p>país de origem: ${pais}</p>`


    if (pais == 'BRASIL') {
        res.innerHTML += `<p>Nacionalidade: Brasileiro</p>`
    } else {
        res.innerHTML += `<p>Nacionalidade: Estrangeiro</p>`
    }
    
    res.style.width = '60vw'
    res.style.border = 'solid black'
    res.style.padding = '10px'
    res.style.marginTop = '30px'
}