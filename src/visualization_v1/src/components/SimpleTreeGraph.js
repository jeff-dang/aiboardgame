import React, { useEffect, useState } from "react";
import EChartsReact from "echarts-for-react";
import Data from "../data/getData";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import NumMovesSelection from "./Selections/NumMovesSelection";
import SimulationTypeSelection from "./Selections/SimulationTypeSelection";
import FromSelection from "./Selections/FromSelection";
import ToSelection from "./Selections/ToSelection";
import GameSelection from "./Selections/GameSelection";
import axios from "axios";

const dataInit = new Data();
const res = dataInit.getDataWithMergedActions(dataInit.getAllDataExEnd());
const initArr = dataInit.getMap(res, 0, 1, 0);

const getCategories = (name) => {
  if (name === "Tic Tac Toe") {
    return [
      { name: "Start", itemStyle: { color: "green" } },
      { name: "End Game", itemStyle: { color: "red" } },
      { name: "0", itemStyle: { color: "lightgreen" } },
      { name: "1", itemStyle: { color: "aqua" } },
      { name: "2", itemStyle: { color: "gold" } },
      { name: "3", itemStyle: { color: "plum" } },
      { name: "4", itemStyle: { color: "purple" } },
      { name: "5", itemStyle: { color: "lightblue" } },
      { name: "6", itemStyle: { color: "orange" } },
      { name: "7", itemStyle: { color: "lightsteelblue" } },
      { name: "8", itemStyle: { color: "gray" } },
      { name: "9", itemStyle: { color: "paleturquoise" } },
    ];
  } else {
    return [
      { name: "Start", itemStyle: { color: "green" } },
      { name: "End Game", itemStyle: { color: "red" } },
      { name: "Fill Monument", itemStyle: { color: "aqua" } },
      { name: "Move Player", itemStyle: { color: "gold" } },
      { name: "Convey", itemStyle: { color: "teal" } },
      { name: "Action Tokens", itemStyle: { color: "lightgreen" } },
      { name: "Initialization Actions", itemStyle: { color: "lightblue" } },
      { name: "Build Bridge", itemStyle: { color: "purple" } },
    ];
  }
};

const labelOptions = {
  width: 60,
  overflow: "break",
  color: "black",
  fontWeight: "bold",
};

const getCategoryIndex = (categories, action) => {
  const category = categories.findIndex((item) => {
    const name = action !== "End Game" ? action.split(", ")[1] : action;

    if (name.length < item.name.length) return false;
    return name.substring(0, item.name.length) === item.name;
  });
  return category;
};

// const generateData = (categories, dataArr, moves) => {
//   let result = [];
//   let x = 200;
//   let y = 100;
//   const incrementX = 300;
//   const incrementY = 300;
//   result.push({
//     name: "Start",
//     x,
//     y: 200,
//     label: labelOptions,
//     category: 0,
//     value: `Category: Start, Simulations: ${
//       dataArr.length > 0 ? dataArr[0].length : 0
//     }`,
//   });

//   if (dataArr.length === 0) return result;

//   dataArr.forEach((data, index) => {
//     if (index > moves) return;
//     x += incrementX;
//     let newY = y;
//     data.forEach((action, actionIndex) => {
//       newY = y + actionIndex * incrementY;
//       const categoryIndex = getCategoryIndex(categories, action);
//       if (result.findIndex((item) => item.name === action) === -1) {
//         result.push({
//           name: action,
//           x,
//           y: newY,
//           label: labelOptions,
//           category: categoryIndex,
//           value:
//             categoryIndex !== -1
//               ? `Category: ${categories[categoryIndex].name}, Simulations: 1`
//               : "None",
//         });
//       } else {
//         const index = result.findIndex((item) => item.name === action);
//         result[index].x = x;
//         result[index].value =
//           result[index].value !== "None"
//             ? `Category: ${categories[categoryIndex].name}, Simulations: ${
//                 Number(
//                   result[result.findIndex((item) => item.name === action)].value
//                     .split(", ")[1]
//                     .split(": ")[1]
//                 ) + 1
//               }`
//             : result[index].value;
//       }
//     });
//   });

//   return result;
// };

const generateData = (categories, dataArr, moves) => {
  let result = [];
  let x = 200;
  let y = 100;
  const incrementX = 500;
  // moves <= 50 ? 200 : moves <= 150 ? 300 : moves <= 250 ? 400 : 500;
  const incrementY = //dataArr.length * 400 + moves * 200;
    moves <= 15
      ? 500
      : moves <= 50
      ? 2500
      : moves <= 150
      ? 10000
      : moves <= 250
      ? 20000
      : 40000;
  result.push({
    name: "Start",
    x: x - moves * 100,
    y: 200,
    label: labelOptions,
    category: 0,
    value: `Category: Start, Simulations: ${
      dataArr.length > 0 ? dataArr.length : 0
    }`,
  });

  if (dataArr.length === 0) return result;

  dataArr.forEach((data) => {
    let newX = x + 200;
    data.forEach((action, actionIndex) => {
      if (actionIndex >= moves) return;
      newX = newX + actionIndex * incrementX;
      const categoryIndex = getCategoryIndex(categories, action);
      if (result.findIndex((item) => item.name === action) === -1) {
        result.push({
          name: action,
          x: newX,
          y,
          label: labelOptions,
          category: categoryIndex,
          value:
            categoryIndex !== -1
              ? `Category: ${categories[categoryIndex].name}, Simulations: 1`
              : "None",
        });
      } else {
        const index = result.findIndex((item) => item.name === action);
        result[index].x = Math.max(result[index].x, newX);
        result[index].value =
          result[index].value !== "None"
            ? `Category: ${categories[categoryIndex].name}, Simulations: ${
                Number(
                  result[result.findIndex((item) => item.name === action)].value
                    .split(", ")[1]
                    .split(": ")[1]
                ) + 1
              }`
            : result[index].value;
      }
    });
    y += incrementY;
  });
  console.log(result);
  return result;
};

// const generateLinks = (dataArr, moves) => {
//   let result = [];
//   if (dataArr.length === 0) return result;

//   dataArr[0].forEach((_, index) => {
//     result.push({
//       source: "Start",
//       target: dataArr[0][index],
//     });
//   });

//   for (let i = 0; i < dataArr.length - 1 && i < moves; i++) {
//     dataArr[i].forEach((action, index) => {
//       if (action !== "End Game") {
//         result.push({
//           source: action,
//           target: dataArr[i + 1][index],
//         });
//       }
//     });
//   }
//   return result;
// };

const generateLinks = (dataArr, moves) => {
  let result = [];
  if (dataArr.length === 0) return result;

  dataArr.forEach((sim) => {
    result.push({
      source: "Start",
      target: sim[0],
    });

    for (let i = 0; i < sim.length - 1 && i < moves; i++) {
      result.push({
        source: sim[i],
        target: sim[i + 1],
      });
    }
  });

  return result;
};

// const arr1 = dataInit.getMap(res, 0, 3, 0)[0];
// const arr2 = dataInit.getMap2(res, 0, 3, 0);
// console.log(generateData(getCategories("An Age Contrived"), arr1, 3));
// console.log(generateData2(getCategories("An Age Contrived"), arr2, 3));
// console.log(generateLinks(arr1, 3));
// console.log(generateLinks2(arr2, 3));

const generateOptions = (categories, dataArr, moves) => {
  const option = {
    tooltip: {},
    animationDurationUpdate: 2000,
    animationEasingUpdate: "sinusoidalInOut",
    textStyle: {
      fontSize: 9,
    },
    legend: [
      {
        data: categories.map((item) => item.name),
      },
    ],
    series: [
      {
        type: "graph",
        layout: "none",
        symbolSize: 10,
        nodeScaleRatio: 0.1,
        itemStyle: {
          color: "#ff7f50",
        },
        roam: true,
        autoCurveness: true,
        scaleLimit: {
          min: 0.3,
          max: 20,
        },
        // label: {
        //   show: true,
        // },
        edgeSymbol: ["circle", "arrow"],
        edgeSymbolSize: [4, 5],
        data: generateData(categories, dataArr, moves),
        links: generateLinks(dataArr, moves),
        lineStyle: {
          opacity: 0.9,
          width: 1,
          curveness: 0.1,
        },
        categories,
        center: moves > 2 ? ["50%", "25%"] : [],
        zoom: 1,
        // emphasis: {
        //   focus: "adjacency",
        //   scale: 2,
        // },
        // width: moves <= 200 ? 2000 : 5000,
      },
    ],
  };
  return option;
};

const SimpleTreeGraph = ({ width, height }) => {
  const [loading, setLoading] = useState(null);
  const [game, setGame] = useState("none");
  const [simulationFile, setSimulationFile] = useState("none");
  const [actionFile, setActionFile] = useState("none");
  const [showOptions, setShowOptions] = useState(null);
  const [categories, setCategories] = useState([]);
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );

  const [player, setPlayer] = useState(1);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(1);
  const [allMoves, setAllMoves] = useState([1]);
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [option, setOptions] = useState({});

  const [simType, setSimType] = useState("Aggregate");
  const [startSim, setStartSim] = useState(1);
  const [endSim, setEndSim] = useState(
    numSimulations[numSimulations.length - 1]
  );
  const [startMove, setStartMove] = useState(1);
  const [endMove, setEndMove] = useState(1);

  useEffect(() => {
    if (game !== "none") {
      setShowOptions(false);
      setCategories(getCategories(game));
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
    const maxMoves = dataInit.getNumberOfMoves(allData, start, end, player);
    const results = dataInit.getMap(mergedData, start, end, player);
    setNextMoveArray(results);

    const newAllMoves = [];
    for (let i = 1; i <= Math.max(1, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);

    if (numMoves > maxMoves) setNumMoves(maxMoves);
  }, [allData, startSim, endSim, simType, player, numSims]);

  useEffect(() => {
    if (simType === "Aggregate") {
      setOptions(generateOptions(categories, nextMoveArray, numMoves));
    } else {
      setOptions(
        generateOptions(
          categories,
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
      <h1>Tree Graph for Common Paths</h1>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          flexWrap: "wrap",
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

export default SimpleTreeGraph;
