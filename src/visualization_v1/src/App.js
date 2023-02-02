import "./App.css";

import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import BarChart from "./components/BarChart";
import SideMenu from "./components/SideMenu";
import HeatMapWithTooltip from "./components/HeatMap";

function App() {
  return (
    <div className="title">
      <h1>An Age Contrived</h1>
      <div className="page">
        <SideMenu />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/bar-chart"
            element={<BarChart width={1000} height={700} />}
          />
          <Route
            path="/heatmap"
            element={<HeatMapWithTooltip width={1000} height={700} />}
          />
        </Routes>
      </div>
    </div>
  );
}

export default App;
