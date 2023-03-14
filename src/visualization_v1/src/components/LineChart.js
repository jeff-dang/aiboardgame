import React, { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
import Data from "../data/getData";
import { files } from "../data/getFiles";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const dataInit = new Data();

export const options = {
  maintainAspectRatio: false,
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
  },
};

const getLabels = (scoreData) => {
  let labels = [];
  scoreData.forEach((sim) => {
    labels.push(Object.keys(sim)[0]);
  });

  return labels;
};

const getPlayerScore = (scoreData, sim, player) => {
  console.log(scoreData);
  const index = scoreData.findIndex((e) => Object.keys(e)[0] === sim);

  const simData = scoreData[index];

  return Object.values(simData)[0][player];
};

const getPlayers = (scoreData) => {
  const simData = scoreData[0];

  return Object.keys(Object.values(simData)[0]);
};

const getRandomColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

const getDataSet = (scoreData, labels) => {
  let dataSet = [];

  const players = getPlayers(scoreData);
  players.forEach((player) => {
    const color = getRandomColor();
    const data = {
      label: player,
      data: labels.map((sim) => getPlayerScore(scoreData, sim, player)),
      borderColor: color,
      backgroundColor: color,
    };
    dataSet.push(data);
  });
  return dataSet;
};

export default function LineChart({ width, height }) {
  const [simulationFile, setSimulationFile] = useState("none");
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );

  const [numSims, setNumSims] = useState(1);
  const [scoreData, setScoreData] = useState(
    dataInit.getScores(allData, numSims)
  );
  const labels = getLabels(scoreData);
  const [data, setData] = useState({
    labels: labels,
    datasets: getDataSet(scoreData, labels),
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
    setNumSimulations(dataInit.getNumberOfSimulations(allData));
  }, [allData]);

  useEffect(() => {
    setScoreData(dataInit.getScores(allData, numSims));
  }, [allData, numSims]);

  useEffect(() => {
    setData({
      labels: labels,
      datasets: getDataSet(scoreData, labels),
    });
  }, [scoreData]);

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
      <h1>Simulation vs. Scores for All Players</h1>
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
        <span> Simulations: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setNumSims(Number(e.target.value))}
          disabled={simulationFile === "none"}
        >
          {numSimulations.map((simulation) => (
            <option key={simulation} value={simulation}>
              {simulation}
            </option>
          ))}
        </select>
      </div>
      {simulationFile !== "none" && (
        <div style={{ overflowX: "scroll" }}>
          <Line options={options} width={width} height={height} data={data} />
        </div>
      )}
    </div>
  );
}
