function parimp(num) {
    if (num % 2 == 0) {
        return  'par' 
    } else {
        return 'impar'
    }
}

let seila = parimp(124122)
console.log(seila)

//--------------------//---------------
function soma(a, b) { //retonra um valor somado ou concatenado em caso de strngs
    return a + b
}

console.log(soma(13, 22))