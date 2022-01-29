import { useState } from "react";   //trabalhando com useState



function Form() {
  function cadastrarUsuario(e) {
    e.preventDefault(); //Essa função trava o reload do Html para poder visualizar o evento ocorrido
    console.log(`Usuário ${name} foi cadastrado com a senha ${password}`)
  }

  const [name, setName] = useState()   //Posso passar Álamo como valor padrão dentro do useState em aspas
  const [password, setPassword] = useState() 

  return (
    //evento de submit, repare que no jsx o label é htmlFor, pois a palavra for no Js é reservada
    <div>
      <h1>Meu Cadastro</h1>
      <form onSubmit={cadastrarUsuario}>
        <div>
          <label htmlFor="name">Nome: </label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Digite o seu nome"
            onChange={(e) => setName(e.target.value)}   //sintaxe para usar o onChange
          />
        </div>
        <div>
          <label htmlFor="password">Senha: </label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Digite a sua senha"
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <div>
          <input type="submit" value="Cadastrar" />
        </div>
      </form>
    </div>
  );
}

export default Form;
