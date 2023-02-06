import React, { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Scatter } from "react-chartjs-2";
import {
  getMovesScoresData,
  getAllData,
  getNumberOfPlayers,
} from "../data/getData";

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

const allData = getAllData();
const players = getNumberOfPlayers(allData);

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
          return `${label}: (${tooltipItem.raw.x} moves, ${tooltipItem.raw.y} score)`;
        },
      },
    },
  },
};

export default function MovesToScores({ width, height }) {
  const [player, setPlayer] = useState(0);
  const [data, setData] = useState({
    datasets: [
      {
        label: `Player ${player}`,
        data: getMovesScoresData(allData, player),
        backgroundColor: "rgba(255, 99, 132, 1)",
      },
    ],
  });

  useEffect(() => {
    setData({
      datasets: [
        {
          label: `Player ${player}`,
          data: getMovesScoresData(allData, player),
          backgroundColor: "rgba(255, 99, 132, 1)",
        },
      ],
    });
  }, [player]);

  return (
    <div style={{ marginBottom: 20 }}>
      <h1>Moves Vs. Scores</h1>
      <span> Player: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setPlayer(Number(e.target.value))}
      >
        {players.map((player) => (
          <option key={player} value={player}>
            {player}
          </option>
        ))}
      </select>
      <div style={{ overflowX: "scroll" }}>
        <Scatter options={options} width={width} height={height} data={data} />
      </div>
    </div>
  );
}
