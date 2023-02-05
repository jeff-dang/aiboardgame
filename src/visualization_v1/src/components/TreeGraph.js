import React, { Component } from "react";
import { Tree, AnimatedTree } from "react-tree-graph";
import {
  getAllDataExEnd,
  getDataWithMergedActions,
  getMap,
} from "../data/getData";
import "./css/style.css";

const textProps = { x: -45, y: 20 };

const allData = getAllDataExEnd();
const mergedData = getDataWithMergedActions(allData);

let results = getMap(mergedData, 2, 0);
let result = results[0];
const map = results[1];

function makeGraph(map, arr, numMoves) {
  let data = { name: "Start", textProps: { x: -25, y: 20 }, children: [] };
  const currLevel = data.children;
  const queue = [];
  let visited = new Array(arr.length);

  for (let i = 0; i < visited.length; i++) {
    visited[i] = false;
  }

  for (let i = 0; i < arr[0].length; i++) {
    queue.push({ currLevel, index: 0 });
  }

  while (queue.length && numMoves > 0) {
    let { currLevel, index } = queue.shift();
    let turnName = result[index].shift();
    if (turnName in map) {
      const ind = map[turnName];
      if (result[index].length >= 0) {
        currLevel.push({ name: turnName, textProps, children: [] });
        queue.push({
          currLevel: currLevel[currLevel.length - 1].children,
          index: ind,
        });
      }
      if (result[index].length == 0) numMoves--;
    }
  }

  return data;
}

export default class Dropdown extends Component {
  render() {
    // change moves here
    const numMoves = 7;
    const data = makeGraph(map, result, numMoves);
    return (
      <div style={{ overflowX: "scroll" }}>
        <h1>Tree Graph</h1>
        <AnimatedTree
          data={data}
          nodeRadius={100}
          margins={{ top: 20, bottom: 10, left: 20, right: 200 }}
          height={700}
          width={numMoves * 250}
        />
      </div>
    );
  }
}
