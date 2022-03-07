import './LoginForm.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Component } from "react";

export default class LoginForm extends Component {

    // eslint-disable-next-line no-useless-constructor
    constructor(props) {
        super(props);
    }
    
    render() {
        return (
                <form className="form">
                    <input type="text" className={"input"} placeholder={"Digite o nome de usuário ou email"}/>
                    <input type="text" className={"input"} placeholder={"Insira sua senha"}/>
                    <a href={"/"} className={""}>
                        Perdeu sua senha?
                    </a>
                    <label>
                        Lembre-se de mim
                        <input type={"checkbox"} />
                    </label>
                    <button className={"botao-enviar"}>
                        Entrar
                    </button>
                </form>
        )
    }
}