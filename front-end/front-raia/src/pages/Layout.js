import { Outlet } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Container, Nav } from "react-bootstrap"
import "../css/NavRaia.css"
const Layout = () => {
    return (
        <>
            <Navbar bg="dark" variant="dark">
                <Container fluid>
                    <Navbar.Brand href="/">
                        <span className="font-size">
                            <span className="font-color">R</span>AIA<span className="font-color">T</span>ECH</span>
                    </Navbar.Brand>
                    <Nav className="position-navbar">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="/Serviços">Serviços</Nav.Link>
                        <Nav.Link href="/login">Login</Nav.Link>
                        <Nav.Link href="/criar-conta">Criar Conta</Nav.Link>
                        <Nav.Link href="/download">Dowload App</Nav.Link>

                    </Nav>
                </Container>
            </Navbar>

            <Outlet />
        </>
    )
};

export default Layout;