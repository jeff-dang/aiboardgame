import Data from "../data/getData";
import {
  mockData,
  mockDataExEnd,
  mockDataMerged,
  mockPlayer0Data,
  mockSimulationData,
  mockFrequencyMapForPlayer0,
  mockCountMapForPlayer0,
  mockNonZeroFreqMapPlayer0,
  mockScoresData,
  mockFrequencyMap,
  mockCountMap,
  mockMapData,
  mockResultsData,
} from "./mockData";

const data = new Data(mockData);

describe("getAllData", () => {
  it("should get all data", () => {
    expect(data.getAllData()).toEqual(mockData);
  });
});

describe("getAllDataExEnd", () => {
  it("should get all data exclduing end turn, action turn and convey turn", () => {
    expect(data.getAllDataExEnd()).toEqual(mockDataExEnd);
  });
});

describe("getDataWithMergedActions", () => {
  it("should merge all action and action_details into action_details", () => {
    expect(data.getDataWithMergedActions(mockDataExEnd)).toEqual(
      mockDataMerged
    );
  });
});

describe("getSimulationData", () => {
  it("should return first 2 simulations", () => {
    expect(data.getSimulationData(mockDataMerged, 2)).toEqual(
      mockSimulationData
    );
  });
});

describe("getPlayerData", () => {
  it("should return only player 0's data for the first simulation", () => {
    expect(data.getPlayerData(mockSimulationData[0], 0)).toEqual(
      mockPlayer0Data
    );
  });
});

describe("getFrequencyMap", () => {
  it("should return frequency map structure", () => {
    expect(data.getFrequencyMap()).toEqual(mockFrequencyMap);
  });
});

describe("getCountMap", () => {
  it("should return count map structure", () => {
    expect(data.getCountMap()).toEqual(mockCountMap);
  });
});

describe("getFrequencyMapForPlayer", () => {
  it("should return only player 0's Frequency Map for actions", () => {
    expect(data.getFrequencyMapForPlayer(mockDataMerged, 2, 0)).toEqual(
      mockFrequencyMapForPlayer0
    );
  });
});

describe("getCountMapForPlayer", () => {
  it("should return only player 0's Count Map for actions", () => {
    expect(data.getCountMapForPlayer(mockDataMerged, 2, 0)).toEqual(
      mockCountMapForPlayer0
    );
  });
});

describe("getAllNonZeroActions", () => {
  it("should return all non zero player 0's actions in the frequency map", () => {
    expect(data.getAllNonZeroActions(mockFrequencyMapForPlayer0)).toEqual(
      mockNonZeroFreqMapPlayer0
    );
  });
});

describe("getScores", () => {
  it("should return scores data for simulations", () => {
    expect(data.getScores(mockDataMerged, 2)).toEqual(mockScoresData);
  });
});

describe("getNumberOfPlayers", () => {
  it("should return an array of players ids", () => {
    expect(data.getNumberOfPlayers(mockDataMerged)).toEqual([0, 1, 2, 3, 4]);
  });
});

describe("getNumberOfSimulations", () => {
  it("should return an array of simulation ids", () => {
    expect(data.getNumberOfSimulations(mockDataMerged)).toEqual([1, 2]);
  });
});

describe("getNumberOfMoves", () => {
  it("should return number of moves for player 0 for 2 simulations", () => {
    expect(data.getNumberOfMoves(mockDataMerged, 2, 0)).toEqual(4);
  });
});

describe("getMap", () => {
  const [result, map] = data.getMap(mockDataMerged, 2, 0);
  it("should return a frequency map for player 0's actions with 2 simulations", () => {
    expect(map).toEqual(mockMapData);
  });

  it("should return a 2d array for player 0's actions with 2 simulations where index is the move number and value is the actions used on that move number", () => {
    expect(result).toEqual(mockResultsData);
  });
});
