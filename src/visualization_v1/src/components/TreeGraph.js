import React, { useEffect, useState } from "react";
import { AnimatedTree } from "react-tree-graph";
import Data from "../data/getData";
import "./css/style.css";

const textProps = {
  x: 0,
  y: 20,
  textAnchor: "middle",
};

const dataInit = new Data();
const allData = dataInit.getAllDataExEnd();
const players = dataInit.getNumberOfPlayers(allData);
const numSimulations = dataInit.getNumberOfSimulations(allData);

function makeGraph(dataMap, dataArr, numMoves) {
  let moves = numMoves;
  let arr = JSON.parse(JSON.stringify(dataArr));
  let map = JSON.parse(JSON.stringify(dataMap));
  let data = { name: "Start", textProps: textProps, children: [] };
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
        currLevel.push({ name: turnName, textProps, children: [] });
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

const TreeGraph = () => {
  const [player, setPlayer] = useState(0);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(3);
  const res = dataInit.getDataWithMergedActions(allData);
  const initMap = dataInit.getMap(res, numSims, player)[1];
  const initArr = dataInit.getMap(res, numSims, player)[0];
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [indexMap, setIndexMap] = useState(initMap);
  const [data, setData] = useState(makeGraph(initMap, initArr, numMoves));
  const [allMoves, setAllMoves] = useState([3]);

  useEffect(() => {
    const mergedData = dataInit.getDataWithMergedActions(allData);
    const results = dataInit.getMap(mergedData, numSims, player);
    setNextMoveArray(results[0]);
    setIndexMap(results[1]);
    const maxMoves = dataInit.getNumberOfMoves(allData, numSims, player);
    const newAllMoves = [];
    for (let i = 3; i <= Math.max(3, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);
  }, [player, numSims]);

  useEffect(() => {
    setData(makeGraph(indexMap, nextMoveArray, numMoves));
  }, [nextMoveArray, indexMap, numMoves]);

  return (
    <div
      style={{
        overflowX: "scroll",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1>Tree Graph</h1>
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
        <span> Number of Moves: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setNumMoves(Number(e.target.value))}
        >
          {allMoves.map((move) => (
            <option key={move} value={move}>
              {move}
            </option>
          ))}
        </select>
      </div>
      <AnimatedTree
        data={data}
        nodeRadius={20}
        margins={{ top: 20, bottom: 10, left: 20, right: 200 }}
        height={700}
        width={numMoves * 300}
      />
    </div>
  );
};

export default TreeGraph;
