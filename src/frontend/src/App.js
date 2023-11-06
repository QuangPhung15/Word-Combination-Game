import { BrowserRouter, Routes, Route } from "react-router-dom";
import Lose from './Lose/Lose.js';
import Win from './Win/Win.js';
import Start from './Start/Start.js';
import Game from './Game/Game.js';
import NoPage from "./NoPage.js";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Start />} />
        <Route path="game" element={<Game />} />
        <Route path="win" element={<Win />} />
        <Route path="lose" element={<Lose />} />
        <Route path="*" element={<NoPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;