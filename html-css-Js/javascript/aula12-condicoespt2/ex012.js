var timenow = new Date()
var hora = timenow.getHours()

console.log(`Agora são exatamente ${hora} horas`)
if (hora > 0 && hora < 5) {
    console.log("boa madrugada")
} else if (hora > 5 && hora < 12) {
    console.log("Bom dia!")
} else if (hora < 18) {
    console.log("Boa tarde!")
} else if (hora <= 23.59) {
    console.log("Boa noite")
}