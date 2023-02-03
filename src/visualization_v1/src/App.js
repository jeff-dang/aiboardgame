import "./App.css";

import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import BarChart from "./components/BarChart";
import SideMenu from "./components/SideMenu";
import HeatMapWithTooltip from "./components/HeatMap";
import Piechart from "./components/PieChart";
import LineChart from "./components/LineChart";
import TreeGraph from "./components/TreeGraph";
import React, {useState, useEffect} from 'react'
import axios from "axios";

function App() {
  const [gameJSON, setGameJSON] = useState([])
  useEffect(() => {
    axios.get("/data/game.json")
    .then((res)=>
    {
    console.log(res)
    setGameJSON(res);
  })
    .catch((err)=>console.log(err));
  }, []);
  console.log("kajsldjaskljd");
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
          <Route
            
            path="/pie-chart"
            element={
            <Piechart 
            gameJSON = {gameJSON}
            setGameJSON = {setGameJSON} 
            width={800} 
            height={600} />}
          />
          <Route
            path="/line-chart"
            element={<LineChart width={600} height={400} />}
          />
          <Route
            path="/tree-graph"
            element={<TreeGraph width={600} height={400} />}
          />
        </Routes>
      </div>
    </div>
  );
}

export default App;
