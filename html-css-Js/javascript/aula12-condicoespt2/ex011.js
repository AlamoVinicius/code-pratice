var idade = 65

if (idade < 16) {
    console.log(`Com ${idade} anos o voto é proibido! `)
} else if (idade < 18 || idade > 65) {
    console.log(`Com ${idade} anos o voto é opcional!`)
} else {
    console.log(`Com ${idade} anos o voto é obrigatório!`)
}