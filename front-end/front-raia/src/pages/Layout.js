import { Outlet, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import { Navbar, Container, Nav } from "react-bootstrap";
import "../css/NavRaia.css";
const Layout = () => {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container fluid>
          <Navbar.Brand href="/">
            <span className="font-size">
              <span className="font-color">R</span>AIA
              <span className="font-color">T</span>ECH
            </span>
          </Navbar.Brand>
          <Nav className="position-navbar">
            <Nav.Link>
              <Link to={"/"}>Home</Link>
            </Nav.Link>
            <Nav.Link>
              <Link to={"/servicos"}>Serviços</Link>
            </Nav.Link>
            <Nav.Link>
              <Link to={"/login"}>Login</Link>
            </Nav.Link>
            <Nav.Link>
              <Link to={"/contact"}>Criar Conta</Link>
            </Nav.Link>
            <Nav.Link>
              <Link to={"/download"}>Dowload App</Link>
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <Outlet />
    </>
  );
};

export default Layout;
