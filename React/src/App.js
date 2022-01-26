
import './App.css';
import HelloWorld from './components/HelloWorld.js';

function App() {
  const name = 'Álamo'  //posso criar váriaveis com react e usalos no jsx
//posso usar funcionalidades do js no jsx também, no caso da soma

  function sum(a , b) {  // posso usar também funções para reaproveitar o bloco de códigos
    return a + b
  }

  const url = 'https://via.placeholder.com/150'

  return (
    <div className="App">
      <h1>Olá React</h1>
      <p>First app made with Reactive</p>
      <p>Ola {name}</p>
      <p>Soma {sum(4, 7)}</p>
      <img src={url} alt="quadrado de 150px"/>
      <HelloWorld/>   
    </div>
  );
}

export default App;
