import React, { useEffect, useMemo, useState } from "react";
import { Bar } from "@visx/shape";
import { Group } from "@visx/group";
import { GradientTealBlue } from "@visx/gradient";
import { scaleBand, scaleLinear } from "@visx/scale";
import { withTooltip, Tooltip, defaultStyles } from "@visx/tooltip";
import { AxisBottom, AxisLeft } from "@visx/axis";
import { useSpring, animated } from "@react-spring/web";
import Data from "../data/getData";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import NumMovesSelection from "./Selections/NumMovesSelection";
import GameSelection from "./Selections/GameSelection";
import axios from "axios";
import SimulationTypeSelection from "./Selections/SimulationTypeSelection";
import FromSelection from "./Selections/FromSelection";
import ToSelection from "./Selections/ToSelection";

const tooltipStyles = {
  ...defaultStyles,
  minWidth: 60,
  backgroundColor: "rgba(0,0,0,0.9)",
  color: "white",
};

const axisTextColor = "#000000";
const verticalMargin = 120;

const dataInit = new Data();

function getBarGraphData(frequencyMap, numBars) {
  dataInit.sortFrequencyMap(frequencyMap);

  const sliced = frequencyMap.slice(0, numBars);

  return sliced;
}

function getMaxBars(allNonZeroActions) {
  const max =
    allNonZeroActions.length > 2 ? Math.min(10, allNonZeroActions.length) : 3;

  let bars = [];
  for (let i = 3; i <= max; i++) {
    bars.push(i);
  }

  return bars;
}

let tooltipTimeout;

/**
 * BarGraphRaw is a component that renders a bar chart.
 */
const BarGraphRaw = ({
  width,
  height,
  tooltipOpen,
  tooltipLeft,
  tooltipTop,
  tooltipData,
  hideTooltip,
  showTooltip,
}) => {
  const xMax = width;
  const yMax = height - verticalMargin;

  const [loading, setLoading] = useState(null);
  const [game, setGame] = useState("none");
  const [simulationFile, setSimulationFile] = useState("none");
  const [actionFile, setActionFile] = useState("none");
  const [showOptions, setShowOptions] = useState(null);
  const [allData, setAllData] = useState(dataInit.getAllDataExEnd());
  const [players, setPlayers] = useState(dataInit.getNumberOfPlayers(allData));
  const [numSimulations, setNumSimulations] = useState(
    dataInit.getNumberOfSimulations(allData)
  );

  const [player, setPlayer] = useState(0);
  const [data, setData] = useState([]);
  const [freqMap, setFreqMap] = useState([]);
  const [numBars, setNumBars] = useState(3);
  const [numSims, setNumSims] = useState(1);

  const [allNonZeroActions, setAllNonZeroActions] = useState([]);
  const [bars, setBars] = useState([3, 4, 5, 6, 7, 8, 9, 10]);
  const [toggle, setToggle] = useState(true);

  const [simType, setSimType] = useState("Aggregate");
  const [startSim, setStartSim] = useState(1);
  const [endSim, setEndSim] = useState(
    numSimulations[numSimulations.length - 1]
  );

  const getMove = (move) => move.name;
  const getFrequency = (move) => move.frequency;

  useEffect(() => {
    if (game !== "none") {
      setShowOptions(false);
      setTimeout(() => {
        setShowOptions(true);
      }, [10]);
      setSimulationFile("none");
    }
  }, [game]);

  useEffect(() => {
    if (simulationFile === "none") return;
    const setFile = async () => {
      try {
        loading !== null && setLoading(true);
        const simResponse = await axios.get(simulationFile);
        const simdata = simResponse.data;
        const actionsResponse = await axios.get(actionFile);
        const actions = actionsResponse.data;
        dataInit.setAllData(simdata);
        dataInit.setAllActions(actions);
        setAllData(dataInit.getAllDataExEnd());
      } catch (e) {
        console.log(e);
      }
    };

    setFile();
  }, [simulationFile]);

  useEffect(() => {
    setPlayers(dataInit.getNumberOfPlayers(allData));
    setNumSimulations(dataInit.getNumberOfSimulations(allData));
  }, [allData]);

  useEffect(() => {
    setPlayer(players[0]);
  }, [players]);

  useEffect(() => {
    if (startSim > endSim) {
      setEndSim(startSim);
    }
  }, [startSim]);

  useEffect(() => {
    let start = startSim - 1;
    let end = endSim;

    if (simType === "Aggregate") {
      start = 0;
      end = numSims;
    } else {
      start = startSim - 1;
      end = endSim;
    }
    const mergedData = dataInit.getDataWithMergedActions(allData);
    setFreqMap(
      dataInit.getFrequencyMapForPlayer(mergedData, start, end, player)
    );
    setToggle(false);
  }, [allData, simType, startSim, endSim, player, numSims, numBars]);

  useEffect(() => {
    setAllNonZeroActions(dataInit.getAllNonZeroActions(freqMap));
  }, [freqMap]);

  useEffect(() => {
    setBars(getMaxBars(allNonZeroActions));
  }, [allNonZeroActions]);

  useEffect(() => {
    if (numBars > bars[bars.length - 1]) {
      setNumBars(bars[bars.length - 1]);
    }
  }, [bars]);

  useEffect(() => {
    setData(getBarGraphData(freqMap, numBars));
    setLoading(false);
    setTimeout(() => {
      setToggle(true);
    }, 400);
  }, [freqMap, numBars]);

  const axisBottomScale = useMemo(
    () =>
      scaleBand({
        domain: data.map(getMove),
        padding: 0.2,
      }),
    [data]
  );

  const axisLeftScale = useMemo(
    () =>
      scaleLinear({
        domain: [0, Math.max(...data.map(getFrequency))],
        nice: true,
        padding: 0.2,
      }),
    [data]
  );

  const xScale = useMemo(
    () =>
      scaleBand({
        range: [0, xMax],
        round: true,
        domain: data.map(getMove),
        padding: 0.4,
      }),
    [xMax, data]
  );
  const yScale = useMemo(
    () =>
      scaleLinear({
        range: [yMax, 0],
        round: true,
        domain: [0, Math.max(...data.map(getFrequency))],
      }),
    [yMax, data]
  );

  const { scale } = useSpring({
    from: { scale: 0 },
    to: { scale: toggle ? 1 : 0 },
  });

  const AnimatedBar = animated(Bar);

  axisBottomScale.rangeRound([0, xMax]);
  axisLeftScale.rangeRound([yMax, 0]);

  return (
    <div
      style={{
        marginBottom: 20,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        margin: "auto",
      }}
    >
      <div>
        <h1> Frequently Used Moves</h1>
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <GameSelection setGame={setGame} />
          {showOptions && (
            <>
              <SimulationFileSelection
                game={game}
                setSimulationFile={setSimulationFile}
                setActionFile={setActionFile}
              />
              <SimulationTypeSelection
                setSimType={setSimType}
                value={simType}
                simulationFile={simulationFile}
              />
              <PlayerSelection
                setPlayer={setPlayer}
                players={players}
                simulationFile={simulationFile}
              />
              {simType === "Subset" ? (
                <>
                  <FromSelection
                    text="Sim From: "
                    setStart={setStartSim}
                    arr={numSimulations}
                    simulationFile={simulationFile}
                    startVal={startSim}
                    endVal={endSim}
                  />
                  <ToSelection
                    text="Sim To: "
                    setEnd={setEndSim}
                    arr={numSimulations}
                    simulationFile={simulationFile}
                    startVal={startSim}
                    endVal={endSim}
                  />
                </>
              ) : (
                <SimulationSelection
                  setNumSims={setNumSims}
                  numSimulations={numSimulations}
                  simulationFile={simulationFile}
                  value={numSims}
                />
              )}
              <NumMovesSelection
                setNumMoves={setNumBars}
                allMoves={bars}
                simulationFile={simulationFile}
                value={numBars}
              />
            </>
          )}
        </div>
      </div>
      {loading && <h2>Loading...</h2>}
      {simulationFile !== "none" && !loading && (
        <svg width={width} height={height}>
          <GradientTealBlue id="teal" />
          <rect width={width} height={height} fill="url(#teal)" rx={14} />
          <Group top={verticalMargin / 2}>
            {data.map((d) => {
              const move = getMove(d);
              const barWidth = xScale.bandwidth();
              const barHeight = yMax - (yScale(getFrequency(d)) ?? 0);
              const barX = xScale(move);
              //const barY = yMax - barHeight;
              return (
                <AnimatedBar
                  key={`bar-${move}`}
                  x={barX}
                  y={scale.to((s) => yMax - s * barHeight)}
                  width={barWidth}
                  height={scale.to((s) => s * barHeight)}
                  fill="rgba(30, 105, 98, 0.7)"
                  onMouseLeave={() => {
                    tooltipTimeout = window.setTimeout(() => {
                      hideTooltip();
                    }, 200);
                  }}
                  onMouseMove={() => {
                    if (tooltipTimeout) clearTimeout(tooltipTimeout);
                    const top = yMax - barHeight + verticalMargin + 20;
                    const left = barX - 10;
                    showTooltip({
                      tooltipData: getFrequency(d),
                      tooltipTop: top,
                      tooltipLeft: left,
                    });
                  }}
                />
              );
            })}
          </Group>
          <AxisLeft
            left={40}
            top={60}
            scale={axisLeftScale}
            stroke={axisTextColor}
            tickStroke={axisTextColor}
            tickLabelProps={() => ({
              fill: axisTextColor,
              fontSize: `${numSims > 20 ? 8 : 10}`,
              overflow: "break",
              textAnchor: "end",
              fontWeight: "bold",
            })}
          />
          <AxisBottom
            top={yMax + 60}
            scale={axisBottomScale}
            stroke={axisTextColor}
            tickStroke={axisTextColor}
            tickLabelProps={() => ({
              fill: axisTextColor,
              fontSize: `${numBars > 5 ? (numBars > 9 ? 7 : 8) : 10}`,
              textAnchor: "middle",
              overflow: "break",
              fontWeight: "bold",
              width: `${numBars > 4 ? 200 : 300}`,
              dy: "1.25em",
            })}
          />
        </svg>
      )}
      {tooltipOpen && tooltipData && (
        <Tooltip top={tooltipTop} left={tooltipLeft} style={tooltipStyles}>
          <div>{tooltipData}</div>
        </Tooltip>
      )}
    </div>
  );
};

/**
 * Component that renders the BarGraphRaw with tooltip
 */
const BarGraphToolTip = withTooltip(BarGraphRaw);

/**
 * Component that renders the BarGraphToolTip
 */
const FrequentlyUsedMoves = ({ width, height }) => {
  return (
    <div style={{ margin: "auto" }}>
      <BarGraphToolTip width={width} height={height} />
    </div>
  );
};

export default FrequentlyUsedMoves;
