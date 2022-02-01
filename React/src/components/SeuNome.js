//trabalhando com State lif no elemento pai , neste caso usamos o useState no app.js
// continuação no arquivo saudacao.js
function SeuNome({ setNome }) {
  return (
    <div>
      <p>Digite seu nome</p>
      <input
        type="text"
        placeholder="Digite o seu nome"
        onChange={(evento) => setNome(evento.target.value)}
      />
    </div>
  );
}

export default SeuNome;
