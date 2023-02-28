import React, { useState } from "react";
import FrequentlyUsedMoves from "./BarChart";
import HeatMapWithTooltip from "./HeatMap";
import LineChart from "./LineChart";
import MovesToScores from "./MovesToScores";
import PieChart from "./PieChart";
import TreeGraph from "./TreeGraph";

const chartOptions = {
  "Frequency Used Moves": <FrequentlyUsedMoves width={1000} height={700} />,
  "Moves vs. Scores": <MovesToScores />,
  "Heat map": <HeatMapWithTooltip width={1100} height={700} />,
  "Line Chart": <LineChart width={1100} height={700} />,
  "Pie Chart": <PieChart width={1100} height={700} />,
  "Tree Graph": <TreeGraph />,
};

const Comparison = () => {
  const [firstChart, setFirstChart] = useState(<></>);
  const [secondChart, setSecondChart] = useState(<></>);

  return (
    <div style={{ marginBottom: 20, minWidth: "80vw" }}>
      <h1 style={{ fontSize: "2em" }}>Comparison</h1>
      <span> Chart 1: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setFirstChart(chartOptions[e.target.value])}
      >
        {Object.keys(chartOptions).map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
      <span> Chart 2: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setSecondChart(chartOptions[e.target.value])}
      >
        {Object.keys(chartOptions).map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        {firstChart}
        {secondChart}
      </div>
    </div>
  );
};

export default Comparison;
