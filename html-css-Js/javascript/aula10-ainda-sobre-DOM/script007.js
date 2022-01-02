function somar() {
    var tn1 = document.querySelector('#txtn1')
    var tn2 = document.querySelector('#txtn2')
    var res = document.querySelector('#res')
    var n1 = Number(tn1.value)  //use value para obter o valor dentro da váriavel
    var n2 = Number(tn2.value)
    var s = n1 + n2
    res.innerHTML = s
}