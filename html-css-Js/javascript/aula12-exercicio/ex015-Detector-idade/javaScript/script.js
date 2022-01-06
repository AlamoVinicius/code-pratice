function verificar() {
    var data = new Date()
    var anoatual = data.getFullYear()
    var anonasc = document.getElementById('ano')
    var saida = document.querySelector("#saida")

    if (Number(anonasc.value) > anoatual) {
        window.alert('[erro] ano inválido')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = anoatual - Number(anonasc.value)
        var genero = ''
        //criando uma tag imagem com JavaScript
        var img = document.createElement('img')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 14) {
                // criança
                img.setAttribute('src', 'images/childman.png')
            } else if (idade < 22) {
                // jovem
                img.setAttribute('src', 'images/youngman.png')
            } else if (idade < 55) {
                // adulto
                img.setAttribute('src', 'images/man.png')
            } else {
                // idoso
                img.setAttribute('src', 'images/oldman.png')
            }


        } else {
            genero = 'Mulher'
            if (idade >= 0 && idade < 12) {
                // criança
                img.setAttribute('src', 'images/childwoman.png')
            } else if (idade < 21) {
                // jovem
                img.setAttribute('src', 'images/younggirl.png')
            } else if (idade < 55) {
                // adulto
                img.setAttribute('src', 'images/woman.png')
            } else {
                // idoso
                img.setAttribute('src', 'images/oldwoman.png')
            }
        }
        saida.style.textAlign = 'center'
        saida.innerHTML = `Você é um(a) ${genero} com ${idade} anos, provável aparência: `
        saida.appendChild(img)  // adicionar a váriavel apos inner.html, criando uma tag dinamicamente
    }
}