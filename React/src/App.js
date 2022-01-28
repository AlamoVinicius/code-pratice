import './App.css';
import Frase from './components/Frase';
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';
import List from './components/List';
import Evento from './components/Evento'
import Form from './components/Forms';

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
      <List/>
      <h2>Testando eventos</h2>
      <Evento numero='1'/>
      <Evento numero='2'/>
      <Form/>
    </div> //dessa forma passando a prop como nome=atr acessamos a propriedade
  );
}

export default App;
