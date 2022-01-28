//Trabalhando com Props


function SayMyName(props) {    //devemos passar o props no parâmetro da função
    
    return (
        <div>
            <p>Good morning {props.nome}, Are you ok?</p>
        </div>
    )
}

export default SayMyName