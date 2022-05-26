import "../css/NavRaia.css";
import { Container, Button, Col, Row } from "react-bootstrap";
const Home = () => {
  return <div className="background-color"><Container>
    <Col>
        <h1 className="front-text">Sua Plataforma Educacional </h1>
        <h1 className="front-text">Gamificada com Realidade Aumentada </h1>
        <h1 className="front-text">Raia Tech </h1>
    
        <Button className="cta" href="download" variant="primary">Teste</Button>
      
    </Col>
  </Container>
  <footer/>
  </div>;
};

export default Home;