import Item from './Item'

function List() {    //trabalhando com fragments
    return (
        <>
            <h1>Minha lista</h1>
            <ul>
                <Item marca='Ford' ano_lancamento={1985}/>
                <Item marca='bmw' ano_lancamento={1989}/>
                <Item marca='Renault' ano_lancamento={1976}/>
                <Item/>
            </ul>
        </>
    )
}

export default List

// para passar props de formato number devemos passar entre chaves dentro do jsx