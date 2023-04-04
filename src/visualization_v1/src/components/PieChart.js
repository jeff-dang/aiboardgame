import React, { useState, useEffect } from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";
import Data from "../data/getData";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import GameSelection from "./Selections/GameSelection";
import axios from "axios";
import SimulationTypeSelection from "./Selections/SimulationTypeSelection";
import FromSelection from "./Selections/FromSelection";
import ToSelection from "./Selections/ToSelection";

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

/**
 * Component for displaying a pie chart of the frequency of actions taken by a player
 */
const PieChart = ({ width, height }) => {
  const [loading, setLoading] = useState(null);
  const [game, setGame] = useState("none");
  const [simulationFile, setSimulationFile] = useState("none");
  const [actionFile, setActionFile] = useState("none");
  const [showOptions, setShowOptions] = useState(null);
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

  const [simType, setSimType] = useState("Aggregate");
  const [startSim, setStartSim] = useState(1);
  const [endSim, setEndSim] = useState(
    numSimulations[numSimulations.length - 1]
  );

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
    setNumSimulations(dataInit.getNumberOfSimulations(allData));
  }, [allData]);

  useEffect(() => {
    setPlayer(players[0]);
  }, [players]);

  useEffect(() => {
    if (startSim > endSim) {
      setEndSim(startSim);
    }
  }, [startSim]);

  useEffect(() => {
    let start = startSim - 1;
    let end = endSim;

    if (simType === "Aggregate") {
      start = 0;
      end = numSims;
    } else {
      start = startSim - 1;
      end = endSim;
    }
    const mergedData = dataInit.getDataWithMergedActions(allData);

    setFreqMap(
      dataInit.getFrequencyMapForPlayer(mergedData, start, end, player)
    );
  }, [allData, simType, startSim, endSim, player, numSims]);

  useEffect(() => {
    setAllNonZeroActions(dataInit.getAllNonZeroActions(freqMap));
    setLoading(false);
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
            <SimulationTypeSelection
              setSimType={setSimType}
              value={simType}
              simulationFile={simulationFile}
            />
            <PlayerSelection
              setPlayer={setPlayer}
              players={players}
              simulationFile={simulationFile}
            />
            {simType === "Subset" ? (
              <>
                <FromSelection
                  text="Sim From: "
                  setStart={setStartSim}
                  arr={numSimulations}
                  simulationFile={simulationFile}
                  startVal={startSim}
                  endVal={endSim}
                />
                <ToSelection
                  text="Sim To: "
                  setEnd={setEndSim}
                  arr={numSimulations}
                  simulationFile={simulationFile}
                  startVal={startSim}
                  endVal={endSim}
                />
              </>
            ) : (
              <SimulationSelection
                setNumSims={setNumSims}
                numSimulations={numSimulations}
                simulationFile={simulationFile}
                value={numSims}
              />
            )}
          </>
        )}
      </div>
      {loading && <h2>Loading...</h2>}
      {simulationFile !== "none" && !loading && (
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
