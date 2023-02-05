import React from "react";
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Scatter } from "react-chartjs-2";
import { getMovesScoresData, getAllData } from "../data/getData";

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

const allData = getAllData();
const player = 0;

const options = {
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: "final score",
      },
    },
    x: {
      beginAtZero: true,
      title: {
        display: true,
        text: "# of moves",
      },
    },
  },
  plugins: {
    tooltip: {
      callbacks: {
        label: function (tooltipItem) {
          var label = `Simulation ${tooltipItem.dataIndex + 1}`;
          return (
            label + ": (" + tooltipItem.raw.x + ", " + tooltipItem.raw.y + ")"
          );
        },
      },
    },
  },
};

const data = {
  datasets: [
    {
      label: `Player ${player}`,
      data: getMovesScoresData(allData, player),
      backgroundColor: "rgba(255, 99, 132, 1)",
    },
  ],
};

export default function MovesToScores({ width, height }) {
  return (
    <div>
      <h1>Moves Vs. Scores</h1>
      <div style={{ overflowX: "scroll" }}>
        <Scatter options={options} width={width} height={height} data={data} />
      </div>
    </div>
  );
}
