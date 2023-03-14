import React, { useEffect, useState } from "react";
import EChartsReact from "echarts-for-react";
import Data from "../data/getData";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import NumMovesSelection from "./Selections/NumMovesSelection";
import SimulationTypeSelection from "./Selections/SimulationTypeSelection";

const dataInit = new Data();

const categories = [
  { name: "Start", itemStyle: { color: "green" } },
  { name: "End Game", itemStyle: { color: "red" } },
  { name: "Fill Monument", itemStyle: { color: "aqua" } },
  { name: "Move Player", itemStyle: { color: "yellow" } },
  { name: "Convey", itemStyle: { color: "teal" } },
  { name: "Action Tokens", itemStyle: { color: "lightgreen" } },
  { name: "Initialization Actions", itemStyle: { color: "lightblue" } },
];

const labelOptions = {
  width: 60,
  overflow: "break",
  color: "black",
  fontWeight: "bold",
};

const getCategoryIndex = (action) => {
  const category = categories.findIndex((item) => {
    const name = action !== "End Game" ? action.split(", ")[1] : action;

    if (name.length < item.name.length) return false;
    return name.substring(0, item.name.length) === item.name;
  });
  return category;
};

const generateData = (dataArr, moves) => {
  let result = [];
  let x = 200;
  let y = 100;
  const incrementX = 300;
  const incrementY = 300;
  console.log(dataArr);
  result.push({
    name: "Start",
    x,
    y: 200,
    label: labelOptions,
    category: 0,
    value: `Category: Start, Simulations: ${
      dataArr.length > 0 ? dataArr[0].length : 0
    }`,
  });

  if (dataArr.length === 0) return result;

  dataArr.forEach((data, index) => {
    if (index >= moves) return;
    x += incrementX;
    let newY = y;
    data.forEach((action, actionIndex) => {
      newY = y + actionIndex * incrementY;
      const categoryIndex = getCategoryIndex(action);
      if (result.findIndex((item) => item.name === action) === -1) {
        result.push({
          name: action,
          x,
          y: newY,
          label: labelOptions,
          category: categoryIndex,
          value: `Category: ${categories[categoryIndex].name}, Simulations: 1`,
        });
      } else {
        const index = result.findIndex((item) => item.name === action);
        result[index].x = x;
        result[index].value = `Category: ${
          categories[categoryIndex].name
        }, Simulations: ${
          Number(
            result[result.findIndex((item) => item.name === action)].value
              .split(", ")[1]
              .split(": ")[1]
          ) + 1
        }`;
      }
    });
  });

  return result;
};

const generateLinks = (dataArr, moves) => {
  let result = [];
  if (dataArr.length === 0) return result;

  dataArr[0].forEach((_, index) => {
    result.push({
      source: "Start",
      target: dataArr[0][index],
    });
  });

  for (let i = 0; i < dataArr.length - 1 && i < moves; i++) {
    dataArr[i].forEach((action, index) => {
      if (action !== "End Game") {
        result.push({
          source: action,
          target: dataArr[i + 1][index],
        });
      }
    });
  }
  return result;
};

const generateOptions = (dataArr, moves) => {
  const option = {
    tooltip: {},
    animationDurationUpdate: 2000,
    animationEasingUpdate: "sinusoidalInOut",
    textStyle: {
      fontSize: 9,
    },
    series: [
      {
        type: "graph",
        layout: "none",
        symbolSize: 10,
        nodeScaleRatio: 0.2,
        itemStyle: {
          color: "#ff7f50",
        },
        roam: true,
        autoCurveness: true,
        scaleLimit: {
          min: 0.7,
          max: 6,
        },
        // label: {
        //   show: true,
        // },
        edgeSymbol: ["circle", "arrow"],
        edgeSymbolSize: [4, 4],
        data: generateData(dataArr, moves),
        links: generateLinks(dataArr, moves),
        lineStyle: {
          opacity: 0.9,
          width: 1,
          curveness: 0.1,
        },
        categories,
        center: ["50%", "25%"],
        zoom: 1,
      },
    ],
  };
  return option;
};

const SimpleTreeGraph = ({ width, height }) => {
  const [loading, setLoading] = useState(null);
  const [simulationFile, setSimulationFile] = useState("none");
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );
  const [simType, setSimType] = useState("Aggregate");
  const [player, setPlayer] = useState(4);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(3);
  const [allMoves, setAllMoves] = useState([3]);

  const res = dataInit.getDataWithMergedActions(allData);
  const initArr = dataInit.getMap(res, numSims, player)[0];
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [option, setOptions] = useState(generateOptions(initArr, numMoves));

  useEffect(() => {
    fetch(simulationFile)
      .then((response) => {
        loading !== null && setLoading(true);
        return response.json();
      })
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
    let mergedData;
    let maxMoves;
    let sims = numSims;
    if (simType === "Aggregate") {
      mergedData = dataInit.getDataWithMergedActions(allData);
      maxMoves = dataInit.getNumberOfMoves(allData, sims, player);
    } else {
      mergedData = dataInit.getDataWithMergedActions([allData[numSims - 1]]);
      sims = 1;
      maxMoves = dataInit.getNumberOfMoves(
        [allData[numSims - 1]],
        sims,
        player
      );
    }
    const results = dataInit.getMap(mergedData, sims, player);
    setNextMoveArray(results[0]);

    const newAllMoves = [];
    for (let i = 3; i <= Math.max(3, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);

    if (numMoves > maxMoves) setNumMoves(maxMoves);
  }, [allData, simType, player, numSims]);

  useEffect(() => {
    setOptions(generateOptions(nextMoveArray, numMoves));
    setLoading(false);
  }, [nextMoveArray, numMoves]);

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
        }}
      >
        <SimulationFileSelection setSimulationFile={setSimulationFile} />
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
