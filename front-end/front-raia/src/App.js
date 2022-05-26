import './App.css';
import {
  BrowserRouter,
  Routes,
  Route,
  
} from "react-router-dom";
import Layout from './pages/Layout';
import Home from './pages/Home';
import Serviços from './pages/Serviços';
import Contact from './pages/Contact';
import NoPage from './pages/NoPage';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="servicos" element={<Serviços />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}


export default App;
