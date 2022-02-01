// ultilizando react router dom para linkar nossas pages
import styles from "./Navbar.module.css"
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <ul className={styles.list}>
      <li className={styles.item}>
        <Link to="/">Home</Link>
      </li>
      <li className={styles.item}>
        <Link to="/empresa">Empresa</Link>
      </li>
      <li className={styles.item}>
        <Link to="/contato">Contato</Link>
      </li>
    </ul>
  );
}

export default Navbar;

/*Exemplo do App.js e sua sintaxe
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Contato from "./pages/Contato";
import Empresa from "./pages/Empresa";
import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/empresa" element={<Empresa />}></Route>
        <Route path="/contato" element={<Contato />}></Route>
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
 */