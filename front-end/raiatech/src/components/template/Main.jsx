import './Main.css'
import React from "react";
import Nav from "./Nav";
import LoginForm from "../views/LoginForm";
import 'bootstrap/dist/css/bootstrap.min.css'

// eslint-disable-next-line import/no-anonymous-default-export
export default props =>
    <React.Fragment>
        <Nav />
        <main className="content">
            <LoginForm />
        </main>
    </React.Fragment>