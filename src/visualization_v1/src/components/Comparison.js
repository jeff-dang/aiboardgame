import React, { useState } from "react";
import FrequentlyUsedMoves from "./BarChart";
import HeatMapWithTooltip from "./HeatMap";
import LineChart from "./LineChart";
import MovesToScores from "./MovesToScores";
import PieChart from "./PieChart";
import SimpleTreeGraph from "./SimpleTreeGraph";
import TreeChart from "./TreeChart";

const width = 1100;
const height = 700;

const chartOptions = {
  "Frequency Used Moves": <FrequentlyUsedMoves width={width} height={height} />,
  "Moves vs. Scores": <MovesToScores width={width} height={height} />,
  "Heat map": <HeatMapWithTooltip width={width} height={height} />,
  "Line Chart": <LineChart width={width} height={height} />,
  "Pie Chart": <PieChart width={width} height={height} />,
  "Tree - Individual Paths": <TreeChart width={width} height={height} />,
  "Tree - Common Paths": <SimpleTreeGraph width={width} height={height} />,
};
// "Alt Tree Chart": <SimpleTreeChart width={width} height={height} />,

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
        defaultValue={"none"}
      >
        <option disabled value={"none"}>
          None
        </option>
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
        defaultValue={"none"}
      >
        <option disabled value={"none"}>
          None
        </option>
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
