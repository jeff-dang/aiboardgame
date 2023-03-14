import React, { useState, useEffect } from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";
import Data from "../data/getData";
import { files } from "../data/getFiles";

ChartJS.register(ArcElement, Tooltip, Legend);

const getRandomColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

//parameter
const dataInit = new Data();

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
  const [simulationFile, setSimulationFile] = useState("none");
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );
  const [player, setPlayer] = useState(0);
  const [numSims, setNumSims] = useState(1);
  const [freqMap, setFreqMap] = useState([]);
  const [allNonZeroActions, setAllNonZeroActions] = useState([]);
  const [data, setData] = useState({
    labels: [],
    datasets: [],
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
    setNumSimulations(dataInit.getNumberOfSimulations(allData));
  }, [allData]);

  useEffect(() => {
    const mergedData = dataInit.getDataWithMergedActions(allData);

    setFreqMap(dataInit.getFrequencyMapForPlayer(mergedData, numSims, player));
  }, [allData, player, numSims]);

  useEffect(() => {
    setAllNonZeroActions(dataInit.getAllNonZeroActions(freqMap));
  }, [allData, freqMap]);

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
  }, [allData, allNonZeroActions]);

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
      <h1>All Used Moves Frequency</h1>
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
      )}
    </div>
  );
};

export default PieChart;
