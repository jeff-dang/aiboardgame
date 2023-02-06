import gameData from "./game2.json";
import allActions from "./allActions.json";

const allData = JSON.parse(JSON.stringify(gameData));

export function getAllData() {
  return allData;
}

export function getAllDataExEnd() {
  let allDataExEnd = [];
  allData.forEach((element) => {
    let elemData = {};

    Object.entries(element).forEach((turn) => {
      if (
        turn[1].action !== "End Turn" &&
        turn[1].action !== "Action Turn" &&
        turn[1].action !== "Convey Turn"
      ) {
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
      if (turn[0] !== "meta_data") {
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
    if (turn[0] !== "meta_data") {
      if (turn[1].player === player) {
        playerData[turn[0]] = turn[1];
      }
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

export function getCountMap() {
  let actions = [];
  Object.entries(allActions).forEach((action) => {
    actions.push({ name: action[0], count: 0 });
  });

  return actions;
}

export function sortFrequencyMap(freqMap) {
  freqMap.sort((a, b) => {
    if (a.frequency !== b.frequency) {
      return a.frequency < b.frequency ? 1 : -1;
    }
    return 0;
  });
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
    result.push({ [`Sim ${index}`]: simulation[1].meta_data });
  });

  return result;
}

export function getMovesScoresData(data, player) {
  let result = [];
  Object.entries(data).forEach((simulation) => {
    const playerData = getPlayerData(simulation[1], player);
    const moves = Object.keys(playerData).length;

    const score = simulation[1].meta_data[`player_${player}`];
    result.push({ x: moves, y: score });
  });

  return result;
}

export function getNumberOfPlayers(data) {
  let players = [];
  const simulation = Object.entries(data)[0];
  Object.entries(simulation[1]).forEach((turn) => {
    if (turn[0] === "meta_data") {
      Object.keys(turn[1]).forEach((player) => {
        const playerNum = Number(player.split("_")[1]);

        players.push(playerNum);
      });
    }
  });

  return players;
}

export function getNumberOfSimulations(data) {
  let result = Array(Object.keys(data).length)
    .fill()
    .map((_, i) => i + 1);

  return result;
}

export function getNumberOfMoves(data, numSims, player) {
  const simulationData = Object.fromEntries(
    Object.entries(data).slice(0, numSims)
  );

  let result = 2;
  Object.entries(simulationData).forEach((simulation) => {
    const playerData = getPlayerData(simulation[1], player);
    const moves = Object.keys(playerData).length;

    if (moves > result) {
      result = moves;
    }
  });
  return result + 1;
}
