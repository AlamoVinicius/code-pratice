function Pessoa({nome, idade, profissao, image}) {  //passando os props de forma dinâmica como atributos
    return (
        <div>
            <img src={image} alt={nome}/>
            <h2>Nome: {nome}</h2>
            <p>Idade: {idade}</p>
            <p>Profissão: {profissao}</p>
        </div>
    )
}

export default Pessoa