import React from "react";
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
import { getAllData, getScores } from "../data/getData";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  maintainAspectRatio: false,
  responsive: true,
  plugins: {
    legend: {
      position: "top",
    },
    title: {
      display: true,
      text: "Simulation VS Scores",
    },
  },
};

//paramters
const numSims = 2;

const allData = getAllData();
const scoreData = getScores(allData, numSims);

let labels = [];

scoreData.forEach((sim) => {
  labels.push(Object.keys(sim)[0]);
});

const getPlayerScore = (sim, player) => {
  const index = scoreData.findIndex((e) => Object.keys(e)[0] === sim);

  const simData = scoreData[index];

  return Object.values(simData)[0][player];
};

const getPlayers = () => {
  const simData = scoreData[0];

  return Object.keys(Object.values(simData)[0]);
};

const getRandomColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

const getDataSet = () => {
  let dataSet = [];

  const players = getPlayers();

  players.forEach((player) => {
    const color = getRandomColor();
    const data = {
      label: player,
      data: labels.map((sim) => getPlayerScore(sim, player)),
      borderColor: color,
      backgroundColor: color,
    };
    dataSet.push(data);
  });
  return dataSet;
};

export const data = {
  labels,
  datasets: getDataSet(),
};

export default function LineChart() {
  return (
    <div style={{ overflowX: "scroll" }}>
      <Line options={options} width={numSims * 1000} height={600} data={data} />
    </div>
  );
}
