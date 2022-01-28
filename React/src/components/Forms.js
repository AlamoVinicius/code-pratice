function Form() {
    
    function cadastrarUsuario(e) {  
        e.preventDefault()   //Essa função trava o reload do Html
        console.log('Cadastrou o usuário!')
    }

    return (  //evento de submit
        <div>
            <h1>Meu Cadastro</h1>
            <form onSubmit={cadastrarUsuario}>
                <div>
                    <input type="text" placeholder="Digite o seu nome"/>
                </div>
                <div>
                    <input type="submit" value="Cadastrar" />
                </div>
            </form>
        </div>
    )

}

export default Form