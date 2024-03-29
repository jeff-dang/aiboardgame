import React, { useEffect, useMemo, useState } from "react";
import { Group } from "@visx/group";
import { scaleLinear } from "@visx/scale";
import { HeatmapCircle } from "@visx/heatmap";
import { withTooltip, Tooltip, defaultStyles } from "@visx/tooltip";
import Data from "../data/getData";
import { useSpring, animated } from "@react-spring/web";
import SimulationFileSelection from "./Selections/SimulationFileSelection";
import SimulationSelection from "./Selections/SimulationSelection";
import PlayerSelection from "./Selections/PlayerSelection";
import axios from "axios";
import GameSelection from "./Selections/GameSelection";
import SimulationTypeSelection from "./Selections/SimulationTypeSelection";
import FromSelection from "./Selections/FromSelection";
import ToSelection from "./Selections/ToSelection";

const tooltipStyles = {
  ...defaultStyles,
  minWidth: 60,
  backgroundColor: "rgba(0,0,0,0.9)",
  color: "white",
};

const hot1 = "#77312f";
const hot2 = "#f33d15";
const background = "#9de3d4";

const dataInit = new Data();

const getData = (freqMap, rows) => {
  const newData = [];
  let columnNum = 0;
  while (freqMap.length) {
    newData.push({ column: columnNum++, bins: freqMap.splice(0, rows) });
  }

  return newData;
};

function max(data, value) {
  return Math.max(...data.map(value));
}

function min(data, value) {
  return Math.min(...data.map(value));
}

let tooltipTimeout;

const defaultMargin = { top: 10, left: 40, right: 20, bottom: 10 };

/**
 * Component for rendering a heatmap.
 */
const HeatMap = ({
  width,
  height,
  margin = defaultMargin,
  separation = 20,
  tooltipOpen,
  tooltipLeft,
  tooltipTop,
  tooltipData,
  hideTooltip,
  showTooltip,
}) => {
  const size =
    width > margin.left + margin.right
      ? width - margin.left - margin.right - separation
      : width;
  const xMax = size;
  const yMax = height - margin.bottom - margin.top;

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

  const [numSims, setNumSims] = useState(1);
  const [player, setPlayer] = useState(0);
  const [freqMap, setFreqMap] = useState([]);
  const [data, setData] = useState([]);
  const [toggle, setToggle] = useState(true);

  const [simType, setSimType] = useState("Aggregate");
  const [startSim, setStartSim] = useState(1);
  const [endSim, setEndSim] = useState(
    numSimulations[numSimulations.length - 1]
  );

  // accessors
  const bins = (d) => d.bins;
  const count = (d) => d.count;

  const colorMax = useMemo(() => max(data, (d) => max(bins(d), count)), [data]);
  const bucketSizeMax = useMemo(() => max(data, (d) => bins(d).length), [data]);

  const binWidth = xMax / data.length;
  const binHeight = yMax / bucketSizeMax;
  const radius = min([binWidth, binHeight], (d) => d) / 2;

  const xScale = scaleLinear({
    domain: [0, data.length],
  });

  const yScale = scaleLinear({
    domain: [0, bucketSizeMax],
  });
  const circleColorScale = scaleLinear({
    range: [hot1, hot2],
    domain: [0, colorMax],
  });

  const opacityScale = scaleLinear({
    range: [0.06, 1],
    domain: [0, colorMax],
  });

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
    setFreqMap(dataInit.getCountMapForPlayer(mergedData, start, end, player));
    setToggle(false);
  }, [allData, simType, startSim, endSim, player, numSims]);

  useEffect(() => {
    setData(getData(freqMap, 6));
    setLoading(false);
    setTimeout(() => {
      setToggle(true);
    }, 500);
  }, [freqMap]);

  xScale.range([0, xMax]);
  yScale.range([0, yMax]);

  const { scale } = useSpring({
    from: { scale: 0 },
    to: { scale: toggle ? 1 : 0 },
  });

  const AnimatedHeatMap = animated(HeatmapCircle);

  return (
    <div
      style={{
        marginBottom: 20,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div>
        <h1>Heat Map of All Moves</h1>
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
            </>
          )}
        </div>
      </div>
      {loading && <h2>Loading...</h2>}
      {simulationFile !== "none" && !loading && (
        <svg width={width} height={height}>
          <rect
            x={0}
            y={0}
            width={width}
            height={height}
            rx={14}
            fill={background}
          />
          <Group top={margin.top} left={margin.left}>
            <AnimatedHeatMap
              data={data}
              xScale={(d) => xScale(d) ?? 0}
              yScale={(d) => yScale(d) ?? 0}
              colorScale={circleColorScale}
              opacityScale={opacityScale}
              radius={scale.to((s) => s * radius)}
              gap={2}
            >
              {(heatmap) =>
                heatmap.map((heatmapBins) =>
                  heatmapBins.map((bin) => (
                    <>
                      <circle
                        key={`heatmap-circle-${bin.row}-${bin.column}`}
                        className="visx-heatmap-circle"
                        cx={bin.cx}
                        cy={bin.cy}
                        r={bin.r}
                        fill={bin.color}
                        fillOpacity={bin.opacity}
                        onMouseLeave={() => {
                          tooltipTimeout = window.setTimeout(() => {
                            hideTooltip();
                          }, 300);
                        }}
                        onMouseMove={() => {
                          if (tooltipTimeout) clearTimeout(tooltipTimeout);
                          const top = bin.cy + radius * 2 + margin.top;
                          const left = bin.cx + margin.left;
                          showTooltip({
                            tooltipData: bin.bin,
                            tooltipTop: top,
                            tooltipLeft: left,
                          });
                        }}
                      />
                    </>
                  ))
                )
              }
            </AnimatedHeatMap>
          </Group>
        </svg>
      )}
      {tooltipOpen && tooltipData && (
        <Tooltip top={tooltipTop} left={tooltipLeft} style={tooltipStyles}>
          <div>
            <strong>{tooltipData.name}</strong>
          </div>
          <div>{tooltipData.count}</div>
        </Tooltip>
      )}
    </div>
  );
};

/**
 * Component to display the heatmap with tooltip
 */
const HeatMapToolTip = withTooltip(HeatMap);

/**
 * Component that renders the HeatMapWithToolTip
 */
const HeatMapWithToolTip = ({ width, height }) => {
  return (
    <div style={{ margin: "auto" }}>
      <HeatMapToolTip width={width} height={height} />
    </div>
  );
};

export default HeatMapWithToolTip;
