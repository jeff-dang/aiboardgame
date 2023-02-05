import gameData from "./game.json";
import allActions from "./allActions.json";

const allData = gameData;

const d = getAllDataExEnd();
const d1 = getDataWithMergedActions(d);

// const result = getMap2(d1, 2, 0);
// // let result = results[0];
// // const map = results[1];
// console.log(result);
// // const f = getFrequencyMapForPlayer(d1, 1, 0);

getScores(allData, 2);

export function getAllData() {
  return allData;
}

export function getAllDataExEnd() {
  let allDataExEnd = [];
  allData.forEach((element) => {
    let elemData = {};

    Object.entries(element).filter((turn) => {
      if (turn[1].action !== "End Turn") {
        elemData[turn[0]] = turn[1];
      }
    });
    allDataExEnd.push(elemData);
  });
  return allDataExEnd;
}

export function getDataWithMergedActions(data) {
  let newData = JSON.parse(JSON.stringify(data));
  let allDataMerged = [];
  newData.forEach((element) => {
    Object.entries(element).forEach((turn) => {
      if (turn[0] !== "metadata") {
        const actionDetail = turn[1].action_details;
        turn[1].action_details = `${turn[1].action} ${actionDetail}`;
      }
    });

    allDataMerged.push(element);
  });

  return allDataMerged;
}

// must be a simulation data
export function getPlayerData(data, player) {
  let playerData = {};

  Object.entries(data).forEach((turn) => {
    if (turn[1].player === player) {
      playerData[turn[0]] = turn[1];
    }
  });
  return playerData;
}

export function getFrequencyMap() {
  let actions = [];
  Object.entries(allActions).forEach((action) => {
    actions.push({ name: action[0], frequency: 0 });
  });

  return actions;
}

export function getFrequencyMapForPlayer(data, numSims, player) {
  const simulationData = Object.fromEntries(
    Object.entries(data).slice(0, numSims)
  );

  let freqMap = getFrequencyMap();
  Object.entries(simulationData).forEach((simulation) => {
    const playerData = getPlayerData(simulation[1], player);

    Object.entries(playerData).forEach((turn) => {
      const objIndex = freqMap.findIndex(
        (obj) => obj.name === turn[1].action_details
      );
      freqMap[objIndex].frequency++;
    });
  });

  return freqMap;
}

export function getBarGraphData(frequencyMap, numBars) {
  const freqMap = JSON.parse(JSON.stringify(frequencyMap));

  sortFrequencyMap(freqMap);

  const sliced = freqMap.slice(0, numBars);

  return sliced;
}

export function sortFrequencyMap(freqMap) {
  freqMap.sort((a, b) => {
    if (a.frequency != b.frequency) {
      return a.frequency < b.frequency ? 1 : -1;
    }
    return 0;
  });
}

export function getCountMap() {
  let actions = [];
  Object.entries(allActions).forEach((action) => {
    actions.push({ name: action[0], count: 0 });
  });

  return actions;
}

export function getCountMapForPlayer(data, numSims, player) {
  const simulationData = Object.fromEntries(
    Object.entries(data).slice(0, numSims)
  );

  let freqMap = getCountMap();
  Object.entries(simulationData).forEach((simulation) => {
    const playerData = getPlayerData(simulation[1], player);

    Object.entries(playerData).forEach((turn) => {
      const objIndex = freqMap.findIndex(
        (obj) => obj.name === turn[1].action_details
      );
      freqMap[objIndex].count++;
    });
  });

  return freqMap;
}

export function getAllNonZeroActions(frequencyMap) {
  let newMap = JSON.parse(JSON.stringify(frequencyMap));
  sortFrequencyMap(newMap);
  const filteredMap = newMap.filter((action) => {
    return action.frequency > 0;
  });
  return filteredMap;
}

export function getMap(data, numSims, player) {
  let result = [];
  let map = {};
  const simulationData = Object.fromEntries(
    Object.entries(data).slice(0, numSims)
  );

  Object.entries(simulationData).forEach((simulation) => {
    let turnNum = 1;
    const playerData = getPlayerData(simulation[1], player);
    const size = Object.keys(playerData).length;
    Object.entries(playerData).forEach((turn, index) => {
      const turnStr = `Turn ${turnNum}, ${turn[1].action_details}`;
      if (!map.hasOwnProperty(turnStr)) {
        map[turnStr] = turnNum;
        result.push([]);
      }

      result[index].push(turnStr);
      turnNum++;

      if (index === size - 1) {
        if (!map.hasOwnProperty("End Game")) {
          map["End Game"] = turnNum;
          result.push([]);
        }
        result[turnNum - 1].push("End Game");
      }
    });
  });

  return [result, map];
}

export function getScores(data, numSims) {
  const simulationData = Object.fromEntries(
    Object.entries(data).slice(0, numSims)
  );
  let result = [];
  Object.entries(simulationData).forEach((simulation, index) => {
    result.push({ [`Sim ${index}`]: simulation[1].metadata });
  });

  return result;
}
