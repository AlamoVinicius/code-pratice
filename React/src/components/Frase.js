import styles from './Frase.module.css'

function Frase() {
    return (
        <div className={styles.FraseContainer}>
            <p className={styles.FraseContent}>Este é um componente que contém uma frase</p>
        </div>
    )
}

export default Frase