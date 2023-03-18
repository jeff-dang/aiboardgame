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

const dataInit = new Data();
const res = dataInit.getDataWithMergedActions(dataInit.getAllDataExEnd());
const initArr = dataInit.getMap(res, 0, 1, 0)[0];

const categories = [
  { name: "Start", itemStyle: { color: "green" } },
  { name: "End Game", itemStyle: { color: "red" } },
  { name: "Fill Monument", itemStyle: { color: "aqua" } },
  { name: "Move Player", itemStyle: { color: "yellow" } },
  { name: "Convey", itemStyle: { color: "teal" } },
  { name: "Action Tokens", itemStyle: { color: "lightgreen" } },
  { name: "Initialization Actions", itemStyle: { color: "lightblue" } },
];

// const categories = [
//   { name: "Start", itemStyle: { color: "green" } },
//   { name: "End Game", itemStyle: { color: "red" } },
//   { name: "0", itemStyle: { color: "lightgreen" } },
//   { name: "1", itemStyle: { color: "aqua" } },
//   { name: "2", itemStyle: { color: "yellow" } },
//   { name: "3", itemStyle: { color: "teal" } },
//   { name: "4", itemStyle: { color: "lightgreen" } },
//   { name: "5", itemStyle: { color: "lightblue" } },
//   { name: "6", itemStyle: { color: "lightblue" } },
//   { name: "7", itemStyle: { color: "lightblue" } },
//   { name: "8", itemStyle: { color: "lightblue" } },
//   { name: "9", itemStyle: { color: "lightblue" } },
// ];

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
          value:
            categoryIndex !== -1
              ? `Category: ${categories[categoryIndex].name}, Simulations: 1`
              : "None",
        });
      } else {
        const index = result.findIndex((item) => item.name === action);
        result[index].x = x;
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
        nodeScaleRatio: 0.2,
        itemStyle: {
          color: "#ff7f50",
        },
        roam: true,
        autoCurveness: true,
        scaleLimit: {
          min: 0.7,
          max: 10,
        },
        // label: {
        //   show: true,
        // },
        edgeSymbol: ["circle", "arrow"],
        edgeSymbolSize: [4, 5],
        data: generateData(dataArr, moves),
        links: generateLinks(dataArr, moves),
        lineStyle: {
          opacity: 0.9,
          width: 1,
          curveness: 0.1,
        },
        categories,
        center: moves > 2 ? ["50%", "25%"] : [],
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
  const [player, setPlayer] = useState(1);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(1);
  const [allMoves, setAllMoves] = useState([1]);
  const [startSim, setStartSim] = useState(1);
  const [endSim, setEndSim] = useState(
    numSimulations[numSimulations.length - 1]
  );
  const [startMove, setStartMove] = useState(3);
  const [endMove, setEndMove] = useState(3);

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
    if (startSim > endSim) {
      setEndSim(startSim);
    }
    if (startMove > endMove) {
      setEndMove(startMove);
    }
  }, [startSim, startMove]);

  useEffect(() => {
    let mergedData;
    let maxMoves;
    let start = startSim - 1;
    let end = endSim;

    if (simType === "Aggregate") {
      start = 0;
      end = numSims;
      mergedData = dataInit.getDataWithMergedActions(allData);
      maxMoves = dataInit.getNumberOfMoves(allData, start, end, player);
    } else {
      start = startSim - 1;
      end = endSim;

      mergedData = dataInit.getDataWithMergedActions(allData);
      maxMoves = dataInit.getNumberOfMoves(allData, start, end, player);
    }
    const results = dataInit.getMap(mergedData, start, end, player);
    setNextMoveArray(results[0]);

    const newAllMoves = [];
    for (let i = 1; i <= Math.max(1, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);

    if (numMoves > maxMoves) setNumMoves(maxMoves);
  }, [allData, startSim, endSim, simType, player, numSims]);

  useEffect(() => {
    if (simType === "Aggregate") {
      setOptions(generateOptions(nextMoveArray, numMoves));
    } else {
      console.log(startMove, endMove, nextMoveArray);
      setOptions(
        generateOptions(
          nextMoveArray.slice(startMove - 1, endMove),
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
