import React, { Component } from "react";
import { Tree, AnimatedTree } from "react-tree-graph";
import {
  getAllDataExEnd,
  getDataWithMergedActions,
  getMap,
} from "../data/getData";
import "./css/style.css";

const textProps = { x: -25, y: 10 };

const d = getAllDataExEnd();
const d1 = getDataWithMergedActions(d);

let results = getMap(d1, 2, 0);
let result = results[0];
const map = results[1];

function makeGraph(map, arr, numMoves) {
  let data = { name: "Start", textProps, children: [] };
  const currLevel = data.children;
  const queue = [];
  let visited = new Array(arr.length);

  for (let i = 0; i < visited.length; i++) {
    visited[i] = new Array(arr[i].length);
  }

  for (let i = 0; i < visited.length; i++) {
    for (let k = 0; k < visited[i].length; k++) {
      visited[i][k] = false;
    }
  }

  for (let i = 0; i < arr[0].length; i++) {
    queue.push({ currLevel, index: 0 });
  }

  while (queue.length && numMoves > 0) {
    let { currLevel, index } = queue.shift();
    for (let j = 0; j < arr[index].length; j++) {
      if (arr[index][j] in map) {
        const ind = map[arr[index][j]];
        if (!visited[index][j]) {
          currLevel.push({ name: arr[index][j], textProps, children: [] });
          queue.push({
            currLevel: currLevel[currLevel.length - 1].children,
            index: ind,
          });
          visited[index][j] = true;
        }
      }
    }
    numMoves--;
  }

  return data;
}

export default class Dropdown extends Component {
  render() {
    const numMoves = 7;
    const data = makeGraph(map, result, numMoves);
    return (
      <div style={{ overflowX: "scroll" }}>
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
