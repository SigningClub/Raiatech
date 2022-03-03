import './Main.css'
import React from "react";
import Nav from "./Nav";

export default props =>
    <React.Fragment>
        <Nav />
        <main className="content">
            Conteúdo
        </main>
    </React.Fragment>