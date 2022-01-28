import './App.css';
import Frase from './components/Frase';
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';

function App() {

  const name = "Michael Jackson"

  return (
    <div className="App">
      <h1>Inserindo CSS</h1>
      <Frase/>
      <Frase/>
      <SayMyName nome='Álamo' />
      <SayMyName nome='Jonas' />
      <SayMyName nome={name} />
      <Pessoa nome='Álamo' idade='26' profissao='programador' image="https://via.placeholder.com/150"/>
    </div> //dessa forma passando a prop como nome=atr acessamos a propriedade
  );
}

export default App;
