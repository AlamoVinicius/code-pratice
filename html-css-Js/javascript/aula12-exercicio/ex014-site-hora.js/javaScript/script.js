
function carregar() {
    var bodyimg = document.getElementById('body')
    bodyimg.style.background = 'lightblue'
    var msg = document.getElementById('msg')
    var img = document.getElementById('image')
    var data = new Date()
    var hours = data.getHours()
    var minutes = data.getMinutes()
    var title = document.querySelector('#title')
    msg.innerHTML = `Agora são ${hours} horas e ${minutes} minutos`
    

    if (hours >= 5 && hours < 12) {
        bodyimg.style.backgroundImage = 'url(images/manha.jpg)'
        bodyimg.style.backgroundRepeat = 'no-repeat'
        bodyimg.style.backgroundSize = 'cover'
        bodyimg.style.backgroundAttachment = 'fixed'
        title.innerHTML = "Bom dia!"
        msg.innerHTML += '<p>Todo dia é uma ocasião especial. Guarde apenas o que tem que ser guardado: lembranças, sorrisos, poemas, cheiros, saudades, momentos.</p>'
        img.innerHTML = '<img src="images/sol.jpg" alt="tarde">'
    
    } else if (hours >= 12 && hours < 18) {
        bodyimg.style.backgroundImage = 'url(images/tarde.jpg)'
        bodyimg.style.backgroundRepeat = 'no-repeat'
        bodyimg.style.backgroundSize = 'cover'
        bodyimg.style.backgroundAttachment = 'fixed'
        title.innerHTML = "Boa tarde!"
        msg.innerHTML += "<p>Boa Tarde... Desfrute de cada momento da sua tarde, que seja serena, tranquila e que Deus nos abençoe transbordando nossos corações de paz.</p>"
        img.innerHTML = '<img src="images/tarde2.jpg" alt="tarde">'
        
   
    } else if (hours >= 18 || hours < 5) {
        bodyimg.style.backgroundImage = 'url(images/noite.jpg)'
        bodyimg.style.backgroundRepeat = 'no-repeat'
        bodyimg.style.backgroundSize = 'cover'
        bodyimg.style.backgroundAttachment = 'fixed'
        title.innerHTML = "Boa Noite!"
        msg.innerHTML += '<p>Tenha uma excelente noite!! Acredite: aquele SONHO que você traz nos sonhos… dentro do teu coração, irá se realizar!</p>'
        img.innerHTML = '<img src="images/noite2.jpg" alt="tarde">'
    }
}