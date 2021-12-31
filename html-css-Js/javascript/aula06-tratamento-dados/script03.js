var n1 = Number.parseInt(window.prompt('Digite um número'))
var n2 = Number.parseInt(window.prompt("Digite mais um número"))
var s = n1 + n2    // + pode ser para adição ou concatenação , é necessario converter para tipo number para ser realizado uma soma
window.alert(`A soma é: ${String(s)}`)
/* Para converter usamos o comando Number.parselInt(n) para inteiro 
e ParselFloat(n) para número real , porêm podemos usar apenas Number(n) para simplificar caso o timpo não importa
- para converter para string: String(n) ou  n.toString()
para formatar uma template string use a string com crases (``) e ${s}*/