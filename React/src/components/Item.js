import PropTypes from 'prop-types'


function Item({marca, ano_lancamento}) {
    return (
        <>
            <li>{marca} - {ano_lancamento}</li>
        </>
    )
}

// trabalhando com prototypes validation e default props
Item.propTypes = {    // atenção para o p de prop deve ser mínuscula    
    marca: PropTypes.string.isRequired,  //is requires ou seja é requirida ou oubrigatória
    ano_lancamento: PropTypes.number,
}

Item.defaultProps = {
    marca: 'faltou a marca',
    ano_lancamento: 0,
}


export default Item