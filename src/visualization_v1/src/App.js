import "./App.css";

import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import SideMenu from "./components/SideMenu";
import HeatMapWithTooltip from "./components/HeatMap";
import Piechart from "./components/PieChart";
import LineChart from "./components/LineChart";
import TreeGraph from "./components/TreeGraph";
import TreeChart from "./components/TreeChart";
import React from "react";
import "./data/getData";
import FrequentlyUsedMoves from "./components/BarChart";
import MovesToScores from "./components/MovesToScores";
import Comparison from "./components/Comparison";

function App() {
  return (
    <div style={{ marginTop: 20 }} className="title">
      <div className="page">
        <SideMenu />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/freq-used"
            element={<FrequentlyUsedMoves width={1000} height={700} />}
          />
          <Route
            path="/moves-scores"
            element={<MovesToScores width={1100} height={700} />}
          />
          <Route
            path="/heatmap"
            element={<HeatMapWithTooltip width={1000} height={700} />}
          />
          <Route
            path="/pie-chart"
            element={<Piechart width={1100} height={700} />}
          />
          <Route
            path="/line-chart"
            element={<LineChart width={1100} height={700} />}
          />
          <Route
            path="/tree-graph"
            element={<TreeGraph width={1100} height={700} />}
          />
          <Route
            path="/tree-chart"
            element={<TreeChart width={1100} height={700} />}
          />
          <Route path="/comparison" element={<Comparison />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
