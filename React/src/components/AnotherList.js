// trabalhando com arrays, lembre se dos nomes de arquivos.js sempre começar com letra maiuscula e suas separçoes também
// lembre se de usar um array no app.js para estudar esse component
function AnotherList({ items }) {
  return (
    <>
      <h3>Lista:</h3>
      {items.length > 0 ? (
        items.map(
          (
            item,
            index //aerofunction para retornar o jxl
          ) => <p key={index}>{item}</p>
        )
      ) : (
        <p>Não há itens na lista</p>
      )}
    </>
  );
}

export default AnotherList;

//aqui usamos o if else com a sintaxe ? and : para verificar se tem items em uma lista, se sim renderizamos a lista dentre <p> se não exibimos uma informação também entre <p>
