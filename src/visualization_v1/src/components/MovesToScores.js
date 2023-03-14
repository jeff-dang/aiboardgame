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
import Data from "../data/getData";
import { files } from "../data/getFiles";

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

const dataInit = new Data();

function getMovesScoresData(data, player) {
  let result = [];
  Object.entries(data).forEach((simulation) => {
    const playerData = dataInit.getPlayerData(simulation[1], player);
    const moves = Object.keys(playerData).length;

    const score = simulation[1].meta_data[`player_${player}`];
    result.push({ x: moves, y: score });
  });

  return result;
}

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
  const [simulationFile, setSimulationFile] = useState("none");
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));

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
    fetch(simulationFile)
      .then((response) => response.json())
      .then((data) => {
        dataInit.setAllData(data);
        setAllData(dataInit.getAllDataExEnd());
      })
      .catch((error) => {
        console.log(error);
      });
  }, [simulationFile]);

  useEffect(() => {
    setPlayers(dataInit.getNumberOfPlayers(allData));
  }, [allData]);

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
  }, [allData, player]);

  return (
    <div
      style={{
        marginBottom: 20,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        margin: "auto",
      }}
    >
      <h1>Moves Vs. Scores</h1>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
        }}
      >
        <span> Simulation File: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setSimulationFile(e.target.value)}
          defaultValue={"none"}
        >
          <option disabled value={"none"}>
            None
          </option>
          {files.map((filename) => (
            <option key={filename} value={filename}>
              {filename}
            </option>
          ))}
        </select>
        <span> Player: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setPlayer(Number(e.target.value))}
          disabled={simulationFile === "none"}
        >
          {players.map((player) => (
            <option key={player} value={player}>
              {player}
            </option>
          ))}
        </select>
      </div>
      {simulationFile !== "none" && (
        <div style={{ overflowX: "scroll" }}>
          <Scatter
            options={options}
            width={width}
            height={height}
            data={data}
          />
        </div>
      )}
    </div>
  );
}
