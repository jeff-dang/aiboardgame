import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';


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
      position: 'top',
    },
    title: {
      display: true,
      text: 'Round VS Scores',
    },
  },
};

const labels = ['turn 1', 'turn 2', 'turn 3', 'turn 4', 'turn 5', 'turn 6', 'turn 7'];

export const data = {
  labels,
  datasets: [
    {
      label: 'player 0',
      data: labels.map(() => Math.random()),
      borderColor: 'rgb(553, 162, 23)',
      backgroundColor: 'rgba(553, 162, 23)',
    },
    {
      label: 'player 1',
      data: labels.map(() => Math.random()),
      borderColor: 'rgb(99, 255, 132)',
      backgroundColor: 'rgba(99, 255, 132)',
    },
    {
      label: 'player 2',
      data: labels.map(() => Math.random()),
      borderColor: 'red',
      backgroundColor: 'red',
    },
    {
      label: 'player 3',
      data: labels.map(() => Math.random()),
      borderColor: 'rgb(53, 162, 235)',
      backgroundColor: 'rgba(53, 162, 235, 0.5)',
    },
  ],
};

export default function App() {
  return <Line options={options} width={800}
  height={600} data={data} />;
}