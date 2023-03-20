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
import SimpleTreeGraph from "./components/SimpleTreeGraph";
import SimpleTreeChart from "./components/SimpleTreeChart";

const width = 1100;
const height = 700;

function App() {
  return (
    <div style={{ marginTop: 20 }} className="title">
      <div className="page">
        <SideMenu />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/freq-used"
            element={<FrequentlyUsedMoves width={width} height={height} />}
          />
          <Route
            path="/moves-scores"
            element={<MovesToScores width={width} height={height} />}
          />
          <Route
            path="/heatmap"
            element={<HeatMapWithTooltip width={width} height={height} />}
          />
          <Route
            path="/pie-chart"
            element={<Piechart width={width} height={height} />}
          />
          <Route
            path="/line-chart"
            element={<LineChart width={width} height={height} />}
          />
          <Route
            path="/tree-graph"
            element={<SimpleTreeGraph width={width} height={height} />}
          />
          <Route
            path="/tree-chart"
            element={<SimpleTreeChart width={width} height={height} />}
          />
          {/* <Route
            path="/tree-chart"
            element={<TreeChart width={width} height={height} />}
          /> */}
          <Route path="/comparison" element={<Comparison />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
