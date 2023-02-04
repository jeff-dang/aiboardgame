import gameData from "./game.json";
import allActions from "./allActions.json";

const allData = gameData;

// const d = getAllDataExEnd();
// const d1 = getDataWithMergedActions(d);

// const f = getFrequencyMapForPlayer(d1, 1, 0);

// getAllNonZeroActions(f);

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
      const actionDetail = turn[1].action_details;
      turn[1].action_details = `${turn[1].action} ${actionDetail}`;
    });
    allDataMerged.push(element);
  });

  return allDataMerged;
}

export function getSimulationData(simulationData, simulation) {
  return simulationData[simulation];
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

export function getAllNonZeroActions(frequencyMap) {
  let newMap = JSON.parse(JSON.stringify(frequencyMap));
  sortFrequencyMap(newMap);
  const filteredMap = newMap.filter((action) => {
    return action.frequency > 0;
  });
  return filteredMap;
}
