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
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import axios from "axios";
import GameSelection from "./Selections/GameSelection";

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

const dataInit = new Data();

function getMovesScoresData(data, player) {
  let result = [];
  Object.entries(data).forEach((simulation) => {
    const playerData = dataInit.getPlayerData(simulation[1], player);
    const moves = Object.keys(playerData).length;

    console.log(simulation[1]);
    const score = simulation[1].meta_data
      ? simulation[1].meta_data[`player_${player}`]
      : 0;
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
  const [loading, setLoading] = useState(null);
  const [game, setGame] = useState("none");
  const [simulationFile, setSimulationFile] = useState("none");
  const [actionFile, setActionFile] = useState("none");
  const [showOptions, setShowOptions] = useState(null);
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
    if (game !== "none") {
      setShowOptions(false);
      setTimeout(() => {
        setShowOptions(true);
      }, [10]);
      setSimulationFile("none");
    }
  }, [game]);

  useEffect(() => {
    if (simulationFile === "none") return;
    const setFile = async () => {
      try {
        loading !== null && setLoading(true);
        const simResponse = await axios.get(simulationFile);
        const simdata = simResponse.data;
        const actionsResponse = await axios.get(actionFile);
        const actions = actionsResponse.data;
        dataInit.setAllData(simdata);
        dataInit.setAllActions(actions);
        setAllData(dataInit.getAllDataExEnd());
      } catch (e) {
        console.log(e);
      }
    };

    setFile();
  }, [simulationFile]);

  useEffect(() => {
    setPlayers(dataInit.getNumberOfPlayers(allData));
  }, [allData]);

  useEffect(() => {
    setPlayer(players[0]);
  }, [players]);

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
    setLoading(false);
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
          justifyContent: "center",
        }}
      >
        <GameSelection setGame={setGame} />
        {showOptions && (
          <>
            <SimulationFileSelection
              game={game}
              setSimulationFile={setSimulationFile}
              setActionFile={setActionFile}
            />
            <PlayerSelection
              setPlayer={setPlayer}
              players={players}
              simulationFile={simulationFile}
            />
          </>
        )}
      </div>
      {loading && <h2>Loading...</h2>}
      {simulationFile !== "none" && !loading && (
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
