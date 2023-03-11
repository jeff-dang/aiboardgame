import React, { useEffect, useState } from "react";
import EChartsReact from "echarts-for-react";
import Data from "../data/getData";

const dataInit = new Data();
const allData = dataInit.getAllDataExEnd();
const players = dataInit.getNumberOfPlayers(allData);
const numSimulations = dataInit.getNumberOfSimulations(allData);

const categories = [
  { name: "Start", itemStyle: { color: "green" } },
  { name: "End Game", itemStyle: { color: "red" } },
  { name: "Fill Monument", itemStyle: { color: "aqua" } },
  { name: "Move Player", itemStyle: { color: "yellow" } },
];

const labelOptions = {
  width: 60,
  overflow: "break",
  color: "black",
  fontWeight: "bold",
};

const generateData = (dataArr, moves) => {
  let result = [];
  let x = 200;
  let y = 100;
  const incrementX = 300;
  const incrementY = 300;
  result.push({ name: "Start", x, y: 200, label: labelOptions, category: 0 });
  dataArr.forEach((data, index) => {
    if (index >= moves) return;
    x += incrementX;
    let newY = y;
    data.forEach((action, actionIndex) => {
      newY = y + actionIndex * incrementY;
      if (result.findIndex((item) => item.name === action) === -1) {
        const category = categories.findIndex((item) => {
          const name = action !== "End Game" ? action.split(", ")[1] : action;
          console.log(name);
          if (name.length < item.name.length) return false;
          return name.substring(0, item.name.length) === item.name;
        });

        result.push({
          name: action,
          x,
          y: newY,
          label: labelOptions,
          category,
        });
      } else {
        result[result.findIndex((item) => item.name === action)].x = x;
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
    animationEasingUpdate: "quinticInOut",
    textStyle: {
      fontSize: 11,
    },
    series: [
      {
        type: "graph",
        layout: "none",
        symbolSize: 80,
        itemStyle: {
          color: "#ff7f50",
        },
        roam: true,
        scaleLimit: {
          min: 1,
          max: 3,
        },
        label: {
          show: true,
        },
        edgeSymbol: ["circle", "arrow"],
        edgeSymbolSize: [4, 10],
        edgeLabel: {
          fontSize: 20,
        },

        data: generateData(dataArr, moves),
        links: generateLinks(dataArr, moves),
        lineStyle: {
          opacity: 0.9,
          width: 2,
          curveness: 0.1,
        },
        categories,
      },
    ],
  };
  return option;
};

const SimpleTreeGraph = ({ width = 1100, height = 700 }) => {
  const [player, setPlayer] = useState(0);
  const [numSims, setNumSims] = useState(1);
  const [numMoves, setNumMoves] = useState(3);
  const [allMoves, setAllMoves] = useState([3]);
  const res = dataInit.getDataWithMergedActions(allData);
  const initArr = dataInit.getMap(res, numSims, player)[0];
  const [nextMoveArray, setNextMoveArray] = useState(initArr);
  const [option, setOptions] = useState(generateOptions(initArr, numMoves));

  useEffect(() => {
    const mergedData = dataInit.getDataWithMergedActions(allData);
    const results = dataInit.getMap(mergedData, numSims, player);
    setNextMoveArray(results[0]);
    const maxMoves = dataInit.getNumberOfMoves(allData, numSims, player);
    const newAllMoves = [];
    for (let i = 3; i <= Math.max(3, maxMoves); i++) {
      newAllMoves.push(i);
    }
    setAllMoves(newAllMoves);
  }, [player, numSims]);

  useEffect(() => {
    setOptions(generateOptions(nextMoveArray, numMoves));
  }, [nextMoveArray, numMoves]);

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
      <EChartsReact
        option={option}
        style={{
          height: `${height}px`,
          width: `${width}px`,
        }}
      />
    </div>
  );
};

export default SimpleTreeGraph;
