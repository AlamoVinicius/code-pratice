function Saudacao({ nome }) {    // tambem posso passar o props como destructure ex: Saudacao(props) {props.nome}

    function gerarSaudacao(SomeName) {
        return `Olá , ${SomeName} Seja bem vindo`
    }

    return (
        <>{nome && <p>{gerarSaudacao(nome)}</p>}</>  //sintaxe de if sem else
    )
}

export default Saudacao


/*Exemplo de como ficaria o App.js:

import { useState } from 'react';
import './App.css';
import Saudacao from './components/Saudacao';
import SeuNome from './components/SeuNome';

function App() {
  const [nome, setNome] = useState()

  return (
    <div className="App">
      <h1>State lift</h1>
      <SeuNome setNome={setNome} />
      <Saudacao nome={nome}/>
    </div>
  );
}

export default App;*/