function Button(props) {    // passando eventos como props
    return <button onClick={props.event}>{props.text}</button>
}

export default Button