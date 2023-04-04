import gameData from "./game2.json";
import allActions from "./allActions.json";

/**
 * Class representing Data from JSON file of game data
 * Author: Hargun
 * Date: 03/03/2021
 */
export default class Data {
  /**
   * Create a Data object.
   * Default data value is the game data from the game2.json file. AllActions value also initialized to allActions.json file
   * Author: Hargun
   * Date: 03/03/2021
   */
  constructor(data = JSON.parse(JSON.stringify(gameData))) {
    this.data = data;
    this.allActions = allActions;
  }

  // Setters
  setAllData(data) {
    this.data = data;
  }

  setAllActions(actions) {
    this.allActions = actions;
  }

  // Getters
  getAllData() {
    return this.data;
  }

  getAllActions() {
    return this.allActions;
  }

  /**
   * This method returns an array of all actions in the game excluding unnecessary actions
   * Author: Hargun
   * Date: 03/03/2021
   */
  getAllDataExEnd() {
    let allDataExEnd = [];
    this.data.forEach((element) => {
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

  /**
   * This method returns an array of all actions merged with action and action_details into action field
   * Author: Hargun
   * Date: 03/03/2021
   * */
  getDataWithMergedActions(data) {
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

  /**
   * This method return simulation data from start index to end index
   * Author: Hargun
   * Date: 03/03/2021
   */
  getSimulationData(data, startIndex = 0, endIndex = 1) {
    return Object.keys(data)
      .slice(startIndex, endIndex)
      .reduce((result, key) => {
        result[key] = data[key];

        return result;
      }, {});
  }

  /**
   * This method returns an object of all actions a player has taken in the data provided
   * Author: Hargun
   * Date: 03/03/2021
   */
  getPlayerData(data, player) {
    let playerData = {};

    Object.entries(data).forEach((turn) => {
      if (turn[0] !== "meta_data") {
        if (turn[1].player == player) {
          playerData[turn[0]] = turn[1];
        }
      }
    });

    return playerData;
  }

  /**
   * This method returns an array of objects with action and frequency as keys. Frequency is set to 0.
   * Author: Hargun
   * Date: 03/03/2021
   */
  getFrequencyMap() {
    let actions = [];
    Object.entries(this.allActions).forEach((action) => {
      actions.push({ name: action[0], frequency: 0 });
    });

    return actions;
  }

  /**
   * This method fills the frequency map with the frequency of each action in the data provided, for the player provided, from start index to end index of the data
   * Author: Hargun
   * Date: 03/03/2021
   */
  getFrequencyMapForPlayer(data, startSim, endSim, player) {
    const simulationData = this.getSimulationData(data, startSim, endSim);

    let freqMap = this.getFrequencyMap();

    if (simulationData) {
      Object.entries(simulationData).forEach((simulation) => {
        const playerData = this.getPlayerData(simulation[1], player);

        Object.entries(playerData).forEach((turn) => {
          const objIndex = freqMap.findIndex(
            (obj) => obj.name == turn[1].action_details
          );
          if (objIndex !== -1) {
            freqMap[objIndex].frequency++;
          }
        });
      });
    }

    return freqMap;
  }

  /**
   * This method returns an array of objects with action and count as keys. Count is set to 0.
   * Author: Hargun
   * Date: 03/03/2021
   */
  getCountMap() {
    let actions = [];
    Object.entries(this.allActions).forEach((action) => {
      actions.push({ name: action[0], count: 0 });
    });

    return actions;
  }

  /**
   * This method fills the Count map with the count of each action in the data provided, for the player provided, from start index to end index of the data
   * Author: Hargun
   * Date: 03/03/2021
   */
  getCountMapForPlayer(data, startSim, endSim, player) {
    const simulationData = this.getSimulationData(data, startSim, endSim);

    let freqMap = this.getCountMap();
    if (simulationData) {
      Object.entries(simulationData).forEach((simulation) => {
        const playerData = this.getPlayerData(simulation[1], player);

        Object.entries(playerData).forEach((turn) => {
          const objIndex = freqMap.findIndex(
            (obj) => obj.name == turn[1].action_details
          );
          if (objIndex !== -1) {
            freqMap[objIndex].count++;
          }
        });
      });
    }
    return freqMap;
  }

  /**
   * This method returns a sorted frequency map in descending order
   * Author: Hargun
   * Date: 03/03/2021
   */
  sortFrequencyMap(freqMap) {
    freqMap.sort((a, b) => {
      if (a.frequency !== b.frequency) {
        return a.frequency < b.frequency ? 1 : -1;
      }
      return 0;
    });
  }

  /**
   * This method takes in a frequency map and returns a new map with only non-zero frequency actions
   * Author: Hargun
   * Date: 03/05/2021
   */
  getAllNonZeroActions(frequencyMap) {
    let newMap = JSON.parse(JSON.stringify(frequencyMap));
    this.sortFrequencyMap(newMap);
    const filteredMap = newMap.filter((action) => {
      return action.frequency > 0;
    });
    return filteredMap;
  }

  /**
   * This method returns an array of strings with the actions taken by the player in the data provided.
   * Each index contains the sequence of actions taken in a specific simulation.
   * Author: Hargun
   * Date: 03/05/2021
   */
  getMap(data, startSim, endSim, player) {
    let result = [];
    const simulationData = this.getSimulationData(data, startSim, endSim);

    if (simulationData) {
      let simNum = 0;
      Object.entries(simulationData).forEach((simulation) => {
        let turnNum = 1;
        const playerData = this.getPlayerData(simulation[1], player);

        const size = Object.keys(playerData).length;
        if (size > 0) {
          result.push([]);
          Object.entries(playerData).forEach((turn, index) => {
            const turnStr = `Turn ${turnNum}, ${turn[1].action_details}`;

            result[simNum].push(turnStr);
            turnNum++;

            if (index === size - 1) {
              result[simNum].push("End Game");
            }
          });
        }
        simNum++;
      });
    }
    return result;
  }

  /**
   * This method return an array of objects with the scores of each player in each simulation
   * Author: Hargun
   * Date: 03/06/2021
   */
  getScores(data, startSim, endSim) {
    const simulationData = this.getSimulationData(data, startSim, endSim);
    let result = [];
    if (simulationData) {
      Object.entries(simulationData).forEach((simulation, index) => {
        result.push({
          [`Sim ${index}`]: simulation[1].meta_data
            ? simulation[1].meta_data
            : {
                player_0: 0,
                player_1: 0,
                player_2: 0,
                player_3: 0,
                player_4: 0,
              },
        });
      });
    }
    return result;
  }

  /**
   * This method returns an array of all player ids in the data provided
   * Author: Hargun
   * Date: 03/06/2021
   */
  getNumberOfPlayers(data) {
    let players = [];
    const simulation = Object.entries(data).find((sim) => {
      return sim[1].meta_data !== undefined;
    });
    if (simulation) {
      Object.entries(simulation[1]).forEach((turn) => {
        if (turn[0] === "meta_data") {
          Object.keys(turn[1]).forEach((player) => {
            const playerNum = Number(player.split("_")[1]);

            players.push(playerNum);
          });
        }
      });
    }
    return players;
  }

  /**
   * This method returns total number of simulations in the data provided
   * Author: Hargun
   * Date: 03/06/2021
   */
  getNumberOfSimulations(data) {
    let result = Array(Object.keys(data).length)
      .fill()
      .map((_, i) => i + 1);

    return result;
  }

  /**
   * This method returns the number of moves taken by the player in the data provided
   * Author: Hargun
   * Date: 03/06/2021
   */
  getNumberOfMoves(data, startSim, endSim, player) {
    const simulationData = this.getSimulationData(data, startSim, endSim);

    let result = 2;
    if (simulationData) {
      Object.entries(simulationData).forEach((simulation) => {
        const playerData = this.getPlayerData(simulation[1], player);
        const moves = Object.keys(playerData).length;

        if (moves > result) {
          result = moves;
        }
      });
    }
    return result + 1;
  }
}
