import './App.css';
import Condiciional from './components/Condicional';



function App() {

  return (
    <div className="App">
      <h1>Renderização condicional</h1>
      <Condiciional/>
    </div> //dessa forma passando a prop como nome=atr acessamos a propriedade
  );
}

export default App;
