import React, { useEffect, useState } from "react";
import EChartsReact from "echarts-for-react";
import Data from "../data/getData";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import NumMovesSelection from "./Selections/NumMovesSelection";
import GameSelection from "./Selections/GameSelection";
import axios from "axios";
import SimulationTypeSelection from "./Selections/SimulationTypeSelection";
import FromSelection from "./Selections/FromSelection";
import ToSelection from "./Selections/ToSelection";

const dataInit = new Data();
const res = dataInit.getDataWithMergedActions(dataInit.getAllDataExEnd());
const initArr = dataInit.getMap(res, 0, 1, 0);

const labelOptions = {
  width: 60,
  overflow: "break",
  color: "black",
  fontWeight: "bold",
};

// function generateData(dataMap, dataArr, numMoves) {
//   let moves = numMoves;
//   let arr = JSON.parse(JSON.stringify(dataArr));
//   let map = JSON.parse(JSON.stringify(dataMap));
//   let data = { name: "Start", children: [] };
//   if (dataArr.length === 0) return data;

//   const currLevel = data.children;
//   const queue = [];
//   let visited = new Array(arr.length);

//   for (let i = 0; i < visited.length; i++) {
//     visited[i] = false;
//   }

//   for (let i = 0; i < arr[0].length; i++) {
//     queue.push({ currLevel, index: 0 });
//   }

//   while (queue.length && moves > 0) {
//     let { currLevel, index } = queue.shift();
//     let turnName = arr[index].shift();
//     if (turnName in map) {
//       const ind = map[turnName];
//       if (arr[index].length >= 0) {
//         currLevel.push({ name: turnName, children: [] });
//         queue.push({
//           currLevel: currLevel[currLevel.length - 1].children,
//           index: ind,
//         });
//       }
//       if (arr[index].length === 0) moves--;
//     }
//   }
//   return data;
// }

function generateData(dataArr, numMoves) {
  let moves = numMoves;
  let arr = JSON.parse(JSON.stringify(dataArr));
  let data = { name: "Start", children: [] };
  if (dataArr.length === 0) return data;

  const currLevel = data.children;
  const queue = [];

  for (let i = 0; i < arr.length; i++) {
    queue.push({ currLevel, arrIndex: i, index: 0 });
  }

  while (queue.length) {
    let { currLevel, arrIndex, index } = queue.shift();
    if (index >= moves || arr[arrIndex].length == 0) continue;
    let turnName = arr[arrIndex][index];

    currLevel.push({ name: turnName, children: [] });
    if (turnName !== "End Game") {
      queue.push({
        currLevel: currLevel[currLevel.length - 1].children,
        index: index + 1,
        arrIndex,
      });
    }
  }
  console.log(data);
  return data;
}

const generateOptions = (dataArr, moves) => {
  const option = {
    tooltip: {
      trigger: "item",
      triggerOn: "mousemove",
    },
    series: [
      {
        type: "tree",
        data: [generateData(dataArr, moves)],
        top: "1%",
        left: "7%",
        bottom: "1%",
        right: "20%",
        symbolSize: 12,
        zoom: 1,
        label: {
          position: "bottom",
          verticalAlign: "middle",
          align: "middle",
          fontSize: 10,
          overflow: "break",
          width: 60,
          show: false,
        },
        leaves: {
          label: {
            position: "right",
            verticalAlign: "middle",
            align: "left",
          },
        },
        emphasis: {
          focus: "descendant",
          label: {
            show: true,
          },
        },
        expandAndCollapse: false,
        animationDuration: 550,
        animationDurationUpdate: 750,
        roam: true,
        center: [400, "50%"],
      },
    ],
  };
  return option;
};

const SimpleTreeChart = ({ width, height }) => {
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
  const [numMoves, setNumMoves] = useState(3);
  const [allMoves, setAllMoves] = useState([1]);
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [option, setOptions] = useState({});

  const [simType, setSimType] = useState("Aggregate");
  const [startSim, setStartSim] = useState(1);
  const [endSim, setEndSim] = useState(
    numSimulations[numSimulations.length - 1]
  );
  const [startMove, setStartMove] = useState(3);
  const [endMove, setEndMove] = useState(3);

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
    if (startMove > endMove) {
      setEndMove(startMove);
    }
  }, [startSim, startMove]);

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
    const results = dataInit.getMap(mergedData, start, end, player);
    setNextMoveArray(results);
    //setNextMoveMap(results[1]);
    const maxMoves = dataInit.getNumberOfMoves(allData, start, end, player);
    const newAllMoves = [];
    for (let i = 1; i <= Math.max(1, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);

    if (numMoves > maxMoves) setNumMoves(maxMoves);
  }, [allData, simType, startSim, endSim, player, numSims]);

  useEffect(() => {
    if (simType === "Aggregate") {
      setOptions(generateOptions(nextMoveArray, numMoves));
    } else {
      setOptions(
        generateOptions(
          nextMoveArray.map((sim) => sim.slice(startMove - 1, endMove)),
          endMove - startMove + 1
        )
      );
    }

    setLoading(false);
  }, [nextMoveArray, simType, startMove, endMove, numMoves]);

  return (
    <div
      style={{
        overflowX: "scroll",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        margin: "auto",
      }}
    >
      <h1>Tree Graph for All Paths</h1>
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
                <FromSelection
                  text="Moves From: "
                  setStart={setStartMove}
                  arr={allMoves}
                  simulationFile={simulationFile}
                  startVal={startMove}
                  endVal={endMove}
                />
                <ToSelection
                  text="Moves To: "
                  setEnd={setEndMove}
                  arr={allMoves}
                  simulationFile={simulationFile}
                  startVal={startMove}
                  endVal={endMove}
                />
              </>
            ) : (
              <>
                <SimulationSelection
                  setNumSims={setNumSims}
                  numSimulations={numSimulations}
                  simulationFile={simulationFile}
                  value={numSims}
                />
                <NumMovesSelection
                  setNumMoves={setNumMoves}
                  allMoves={allMoves}
                  simulationFile={simulationFile}
                  value={numMoves}
                />
              </>
            )}
          </>
        )}
      </div>
      {loading && <h2>Loading...</h2>}
      {simulationFile !== "none" && !loading && (
        <EChartsReact
          option={option}
          style={{
            height: `${height}px`,
            width: `90vw`,
          }}
        />
      )}
    </div>
  );
};

export default SimpleTreeChart;
