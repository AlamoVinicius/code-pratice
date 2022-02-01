// para trabalhar com condição usamos o useState
import { useState } from "react";

function Condiciional() {
  const [email, setEmail] = useState();
  const [userEmail, setUserEmail] = useState()

  function enviarEmail(e) {
    e.preventDefault(); //função que irá impedir o submit
    setUserEmail(email)
  }

  function limparEmail(e) {   //basta colocar uma strg vazia para limpar
    setUserEmail('')    
  }

  return (
    <div>
      <h2>Cadastre o seu email:</h2>
      <form>
        <input
          type="email"
          placeholder="Digite o seu email..."
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit" onClick={enviarEmail}>
          Enviar-email
        </button>
        {userEmail && (    //if checando se tem algo no userEmail se true exibi uma nova div
            <div>
                <p>o e-mail do usuário é: {userEmail}</p>
                <button onClick={limparEmail}>Limpar E-mail</button>
            </div>
        )}

      </form>
    </div>
  );
}

export default Condiciional;
