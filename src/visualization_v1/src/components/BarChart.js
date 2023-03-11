import React, { useEffect, useMemo, useState } from "react";
import { Bar } from "@visx/shape";
import { Group } from "@visx/group";
import { GradientTealBlue } from "@visx/gradient";
import { scaleBand, scaleLinear } from "@visx/scale";
import { AxisBottom, AxisLeft } from "@visx/axis";
import { useSpring, animated } from "@react-spring/web";
import Data from "../data/getData";
import { files } from "../data/getFiles";

const bars = [3, 4, 5, 6, 7, 8, 9, 10];
const axisTextColor = "#000000";
const verticalMargin = 120;

const dataInit = new Data();

function getBarGraphData(frequencyMap, numBars) {
  dataInit.sortFrequencyMap(frequencyMap);

  const sliced = frequencyMap.slice(0, numBars);

  return sliced;
}

const FrequentlyUsedMoves = ({ width, height }) => {
  const xMax = width;
  const yMax = height - verticalMargin;

  const [simulationFile, setSimulationFile] = useState("none");
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
  const [toggle, setToggle] = useState(true);

  const getMove = (move) => move.name;
  const getFrequecy = (move) => move.frequency;

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
    setFreqMap(dataInit.getFrequencyMapForPlayer(mergedData, numSims, player));
    setToggle(false);
  }, [allData, player, numSims, numBars]);

  useEffect(() => {
    setData(getBarGraphData(freqMap, numBars));
    setTimeout(() => {
      setToggle(true);
    }, 400);
  }, [freqMap]);

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
        domain: [0, Math.max(...data.map(getFrequecy))],
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
        domain: [0, Math.max(...data.map(getFrequecy))],
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
            onChange={(e) => setNumBars(Number(e.target.value))}
            disabled={simulationFile === "none"}
          >
            {bars.map((bar) => (
              <option key={bar} value={bar}>
                {bar}
              </option>
            ))}
          </select>
        </div>
      </div>
      {simulationFile !== "none" && (
        <svg width={width} height={height}>
          <GradientTealBlue id="teal" />
          <rect width={width} height={height} fill="url(#teal)" rx={14} />
          <Group top={verticalMargin / 2}>
            {data.map((d) => {
              const move = getMove(d);
              const barWidth = xScale.bandwidth();
              const barHeight = yMax - (yScale(getFrequecy(d)) ?? 0);
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
                />
              );
            })}
          </Group>
          <AxisLeft
            left={20}
            top={60}
            scale={axisLeftScale}
            stroke={axisTextColor}
            tickStroke={axisTextColor}
            tickLabelProps={() => ({
              fill: axisTextColor,
              fontSize: 12,
              textAnchor: "middle",
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
              fontSize: `${numBars > 5 ? (numBars > 9 ? 7 : 8) : 11}`,
              textAnchor: "middle",
              overflow: "break",
              fontWeight: "bold",
              width: `${numBars > 4 ? 200 : 250}`,
            })}
          />
        </svg>
      )}
    </div>
  );
};

export default FrequentlyUsedMoves;
