import React, { useEffect, useState } from "react";
//import * as data from "./data.json";
import styled from "styled-components";
import { Tree, TreeNode } from "react-organizational-chart";
import _ from "underscore";
import Data from "../data/getData";
import { files } from "../data/getFiles";

const StyledNode = styled.div`
  padding: 5px;
  border-radius: 8px;
  display: inline-block;
  border: 1px solid red;
  background: skyblue;
`;
const StyledNode2 = styled.div`
  padding: 5px;
  border-radius: 8px;
  display: inline-block;
  border: 1px solid red;
  background: green;
  color: #fff;
`;

const dataInit = new Data();

function makeGraph(dataMap, dataArr, numMoves) {
  let moves = numMoves;
  let arr = JSON.parse(JSON.stringify(dataArr));
  let map = JSON.parse(JSON.stringify(dataMap));
  let data = { name: "Start", child: [] };
  if (dataArr.length === 0) return data;

  const currLevel = data.child;
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
        const newName =
          turnName !== "End Game" ? turnName.split(", ")[1] : turnName;
        currLevel.push({ name: newName, child: [] });
        queue.push({
          currLevel: currLevel[currLevel.length - 1].child,
          index: ind,
        });
      }
      if (arr[index].length === 0) moves--;
    }
  }
  return data;
}

export default function TreeChart(props) {
  // const [selected, setSelected] = useState("");
  const [simulationFile, setSimulationFile] = useState("none");
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );

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
    fetch(simulationFile)
      .then((response) => response.json())
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
    setIndexMap(results[1]);
    const maxMoves = dataInit.getNumberOfMoves(allData, numSims, player);
    const newAllMoves = [];
    for (let i = 3; i <= Math.max(3, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);

    if (numMoves > maxMoves) setNumMoves(maxMoves);
  }, [allData, player, numSims]);

  useEffect(() => {
    setData(makeGraph(indexMap, nextMoveArray, numMoves));
  }, [nextMoveArray, indexMap, numMoves]);

  // useEffect(() => {
  //   const s = _.clone(data);
  //   const setChecked = (obj, c = false) => {
  //     obj.checked = c ? c : selected === obj.name;

  //     if (obj.child) {
  //       obj.child.map((obj2) => {
  //         obj2.checked = obj.checked ? obj.checked : selected === obj2.name;
  //         return setChecked(obj2, obj.checked);
  //       });
  //     }
  //     return obj;
  //   };
  //   setData(setChecked(s));
  // }, [selected]);
  const getLabel = (name, checked) => {
    const Name = () => (
      <span
      // className="selectable"
      // onClick={() => {
      //   setSelected(name);
      // }}
      >
        {name}
      </span>
    );
    return checked ? (
      <StyledNode2>
        <Name />
      </StyledNode2>
    ) : (
      <StyledNode>
        <Name />
      </StyledNode>
    );
  };
  const getTreenode = (child) => {
    return child.map((obj) => {
      return (
        <TreeNode label={getLabel(obj.name, obj.checked)}>
          {obj.child && getTreenode(obj.child)}
        </TreeNode>
      );
    });
  };
  return (
    <div
      style={{
        overflow: "scroll",
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
        <span> Simulation File: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setSimulationFile(e.target.value)}
          defaultValue={"none"}
        >
          <option disabled value={"none"}>
            None
          </option>
          {files.map((filename) => (
            <option key={filename} value={filename}>
              {filename}
            </option>
          ))}
        </select>
        <span> Player: </span>
        <select
          style={{ margin: 10 }}
          onChange={(e) => setPlayer(Number(e.target.value))}
          disabled={simulationFile === "none"}
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
          disabled={simulationFile === "none"}
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
          disabled={simulationFile === "none"}
        >
          {allMoves.map((move) => (
            <option key={move} value={move}>
              {move}
            </option>
          ))}
        </select>
      </div>
      {simulationFile !== "none" && (
        <Tree
        // onClick={() => {
        //   setSelected(info.name);
        // }}
        // label={getLabel(info.name, info.checked)}
        >
          {getTreenode(data.child)}
        </Tree>
      )}
    </div>
  );
}
