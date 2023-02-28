import React, { useState, useEffect } from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";
import {
  getAllDataExEnd,
  getAllNonZeroActions,
  getDataWithMergedActions,
  getFrequencyMapForPlayer,
  getNumberOfPlayers,
  getNumberOfSimulations,
} from "../data/getData";

ChartJS.register(ArcElement, Tooltip, Legend);

const getRandomColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

//parameter
const allData = getAllDataExEnd();
const players = getNumberOfPlayers(allData);
const numSimulations = getNumberOfSimulations(allData);

const getLabels = (allNonZeroActions) => {
  let labels = [];
  Object.entries(allNonZeroActions).forEach((action) => {
    labels.push(action[1].name);
  });
  return labels;
};

const getValues = (allNonZeroActions) => {
  let values = [];
  Object.entries(allNonZeroActions).forEach((action) => {
    values.push(action[1].frequency);
  });
  return values;
};

const getBackgroundColors = (allNonZeroActions) => {
  let backgroundColors = [];
  allNonZeroActions.forEach((action) => {
    backgroundColors.push(getRandomColor());
  });

  return backgroundColors;
};

const getBorderColors = (allNonZeroActions) => {
  let borderColors = [];
  allNonZeroActions.forEach((action) => {
    borderColors.push("#000000");
  });

  return borderColors;
};

const PieChart = ({ width, height }) => {
  const [player, setPlayer] = useState(0);
  const [numSims, setNumSims] = useState(1);
  const [freqMap, setFreqMap] = useState([]);
  const [allNonZeroActions, setAllNonZeroActions] = useState([]);
  const [data, setData] = useState({
    labels: [],
    datasets: [],
  });

  useEffect(() => {
    const mergedData = getDataWithMergedActions(allData);

    setFreqMap(getFrequencyMapForPlayer(mergedData, numSims, player));
  }, [player, numSims]);

  useEffect(() => {
    setAllNonZeroActions(getAllNonZeroActions(freqMap));
  }, [freqMap]);

  useEffect(() => {
    setData({
      labels: getLabels(allNonZeroActions),
      datasets: [
        {
          label: "# of times used",
          data: getValues(allNonZeroActions),
          backgroundColor: getBackgroundColors(allNonZeroActions),
          borderColor: getBorderColors(allNonZeroActions),
          borderWidth: 0.5,
        },
      ],
    });
  }, [allNonZeroActions]);

  return (
    <div
      style={{
        marginBottom: 20,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1>All Used Moves Frequency</h1>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
        }}
      >
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
        <span> Simulations: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setNumSims(Number(e.target.value))}
        >
          {numSimulations.map((simulation) => (
            <option key={simulation} value={simulation}>
              {simulation}
            </option>
          ))}
        </select>
      </div>
      <div style={{ overflowX: "scroll", marginTop: 20 }}>
        {
          <Pie
            data={data}
            width={width}
            height={height}
            options={{ maintainAspectRatio: false }}
          />
        }
      </div>
    </div>
  );
};

export default PieChart;
