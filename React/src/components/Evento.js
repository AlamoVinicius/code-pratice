import Button from './eventos/Button'

function Evento({numero}) {

    function meuEvento() {
        console.log(`Eai parceiro qual foi? ${numero}`)
    }

    function segundoEvento() {
        console.log(`Ativando o segundo evento`)
    }

    return (   //repare no Button como iremos passar o evento através de propriedade
        <div>   
            <p>Clique aqui para disparar um evento</p>
            <Button event={meuEvento} text='Primeiro Evento'/>
            <Button event={segundoEvento} text='Segundo Evento'/>
            <button onClick={meuEvento}>Ativar!</button>
        </div>
    )
}

export default Evento