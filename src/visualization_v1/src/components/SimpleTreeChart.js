import React, { useEffect, useState } from "react";
import EChartsReact from "echarts-for-react";
import Data from "../data/getData";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import NumMovesSelection from "./Selections/NumMovesSelection";

const dataInit = new Data();

const categories = [
  { name: "Start", itemStyle: { color: "green" } },
  { name: "End Game", itemStyle: { color: "red" } },
  { name: "Fill Monument", itemStyle: { color: "aqua" } },
  { name: "Move Player", itemStyle: { color: "yellow" } },
  { name: "Convey", itemStyle: { color: "teal" } },
  { name: "Action Tokens", itemStyle: { color: "lightgreen" } },
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

function generateData(dataMap, dataArr, numMoves) {
  let moves = numMoves;
  let arr = JSON.parse(JSON.stringify(dataArr));
  let map = JSON.parse(JSON.stringify(dataMap));
  let data = { name: "Start", children: [] };
  if (dataArr.length === 0) return data;

  const currLevel = data.children;
  const queue = [];
  let visited = new Array(arr.length);

  for (let i = 0; i < visited.length; i++) {
    visited[i] = false;
  }

  for (let i = 0; i < arr[0].length; i++) {
    queue.push({ currLevel, index: 0 });
  }

  while (queue.length && moves > 0) {
    let { currLevel, index } = queue.shift();
    let turnName = arr[index].shift();
    if (turnName in map) {
      const ind = map[turnName];
      if (arr[index].length >= 0) {
        currLevel.push({ name: turnName, children: [] });
        queue.push({
          currLevel: currLevel[currLevel.length - 1].children,
          index: ind,
        });
      }
      if (arr[index].length === 0) moves--;
    }
  }
  return data;
}

const generateOptions = (dataMap, dataArr, moves) => {
  const option = {
    tooltip: {
      trigger: "item",
      triggerOn: "mousemove",
    },
    series: [
      {
        type: "tree",
        data: [generateData(dataMap, dataArr, moves)],
        top: "1%",
        left: "7%",
        bottom: "1%",
        right: "20%",
        symbolSize: 7,
        label: {
          position: "left",
          verticalAlign: "middle",
          align: "right",
          fontSize: 9,
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
        },
        expandAndCollapse: false,
        animationDuration: 550,
        animationDurationUpdate: 750,
        roam: true,
        center: [200, "50%"],
      },
    ],
  };
  return option;
};

const SimpleTreeChart = ({ width, height }) => {
  const [loading, setLoading] = useState(null);
  const [simulationFile, setSimulationFile] = useState("none");
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );

  const [player, setPlayer] = useState(0);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(3);
  const [allMoves, setAllMoves] = useState([3]);

  const res = dataInit.getDataWithMergedActions(allData);
  const initArr = dataInit.getMap(res, numSims, player)[0];
  const initMap = dataInit.getMap(res, numSims, player)[1];
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [nextMoveMap, setNextMoveMap] = useState(initMap);
  const [option, setOptions] = useState(
    generateOptions(initMap, initArr, numMoves)
  );

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
    const mergedData = dataInit.getDataWithMergedActions(allData);
    const results = dataInit.getMap(mergedData, numSims, player);
    setNextMoveArray(results[0]);
    setNextMoveMap(results[1]);
    const maxMoves = dataInit.getNumberOfMoves(allData, numSims, player);
    const newAllMoves = [];
    for (let i = 3; i <= Math.max(3, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);

    if (numMoves > maxMoves) setNumMoves(maxMoves);
  }, [allData, player, numSims]);

  useEffect(() => {
    setOptions(generateOptions(nextMoveMap, nextMoveArray, numMoves));
    setLoading(false);
  }, [nextMoveMap, nextMoveArray, numMoves]);

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
        }}
      >
        <SimulationFileSelection setSimulationFile={setSimulationFile} />
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
            width: `${numMoves * 300}px`,
          }}
        />
      )}
    </div>
  );
};

export default SimpleTreeChart;
