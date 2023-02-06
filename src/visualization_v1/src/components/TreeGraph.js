import React, { useEffect, useState } from "react";
import { AnimatedTree } from "react-tree-graph";
import {
  getAllDataExEnd,
  getDataWithMergedActions,
  getMap,
  getNumberOfPlayers,
  getNumberOfSimulations,
} from "../data/getData";
import "./css/style.css";

const textProps = {
  x: 0,
  y: 20,
  textAnchor: "middle",
};

const allMoves = [];
const totalMoves = 10;
for (var i = 3; i <= totalMoves; i++) {
  allMoves.push(i);
}

const allData = getAllDataExEnd();
const players = getNumberOfPlayers(allData);
const numSimulations = getNumberOfSimulations(allData);

function makeGraph(dataMap, dataArr, numMoves) {
  let moves = numMoves;
  let arr = JSON.parse(JSON.stringify(dataArr));
  let map = JSON.parse(JSON.stringify(dataMap));
  let data = { name: "Start", textProps: textProps, children: [] };
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
  console.log(data);
  return data;
}

const TreeGraph = () => {
  const [player, setPlayer] = useState(0);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(3);
  const res = getDataWithMergedActions(allData);
  const initMap = getMap(res, numSims, player)[1];
  const initArr = getMap(res, numSims, player)[0];
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [indexMap, setIndexMap] = useState(initMap);
  const [data, setData] = useState(makeGraph(initMap, initArr, numMoves));

  useEffect(() => {
    const mergedData = getDataWithMergedActions(allData);
    const results = getMap(mergedData, numSims, player);
    setNextMoveArray(results[0]);
    setIndexMap(results[1]);
  }, [player, numSims]);

  useEffect(() => {
    setData(makeGraph(indexMap, nextMoveArray, numMoves));
  }, [nextMoveArray, indexMap, numMoves]);

  return (
    <div style={{ overflowX: "scroll" }}>
      <h1>Tree Graph</h1>
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
