var area = window.document.getElementById("area") 
// variável area no escopo geral não é recomendável, mas neste caso irei usar só como exemplo aos estudos
// posso criar o addEventListener para despoluir o código hrml ao invés de deixar os comandos no html
area.addEventListener('click', clicking) // nesse caso sex exemplos
area.addEventListener('mouseenter', mousein)
area.addEventListener('mouseout', mousesair)
area.addEventListener('mousedown', segurando)
//preste muita atenção nas sintaxes sempre


function clicking() {
    area.innerText = "clicou gatão ;)"
    area.style.background = "rgb(61, 250, 61)"
}

function mousein() {
    area.innerText = "mouse galera!"
    area.style.background = "rgb(95, 204, 95)"
    area.style.transitionDuration = ".5s"
    area.style.color = "rgb(197, 86, 86)"
}

function segurando() {
    area.innerText = "ahhhhh me solta"
}

function mousesair() {
    area.innerText = "interact..."
    area.style.background = "lightgreen"
    area.style.color = "darkmagenta"
}