// nome de todo arquivo de component deve começar com letras maiusula e as separações também, de acordo com a convenção
import Frase from './Frase'

function HelloWorld() {

    return (
        <div>
            <Frase />
            <h1>My first component</h1>
            <Frase />
        </div>
    )    //em react os return em js são feito dentro de parênteses.
    
}

export default HelloWorld