import React, { useMemo } from "react";
import { Bar } from "@visx/shape";
import { Group } from "@visx/group";
import { GradientTealBlue, GradientPurpleRed } from "@visx/gradient";
import { scaleBand, scaleLinear } from "@visx/scale";
import { AxisBottom, AxisLeft } from "@visx/axis";
import { useSpring, animated } from "@react-spring/web";
import {
  getAllDataExEnd,
  getFrequencyMapForPlayer,
  getDataWithMergedActions,
  sortFrequencyMap,
} from "../data/getData";

const allData = getAllDataExEnd();
const mergedData = getDataWithMergedActions(allData);

const freqMap = getFrequencyMapForPlayer(mergedData, 1, 0);

const data = getBarGraphData(freqMap, 5);

function getBarGraphData(frequencyMap, numBars) {
  // const freqMap = JSON.parse(JSON.stringify(frequencyMap));

  sortFrequencyMap(frequencyMap);

  const sliced = frequencyMap.slice(0, numBars);

  return sliced;
}

const axisTextColor = "#000000";
const getMove = (move) => move.name;
const getFrequecy = (move) => move.frequency;

const axisBottomScale = scaleBand({
  domain: data.map(getMove),
  padding: 0.2,
});

const axisLeftScale = scaleLinear({
  domain: [0, Math.max(...data.map(getFrequecy))],
  nice: true,
  padding: 0.2,
});

const verticalMargin = 120;

const FrequentlyUsedMoves = ({ width, height }) => {
  const xMax = width;
  const yMax = height - verticalMargin;

  const xScale = useMemo(
    () =>
      scaleBand({
        range: [0, xMax],
        round: true,
        domain: data.map(getMove),
        padding: 0.4,
      }),
    [xMax]
  );
  const yScale = useMemo(
    () =>
      scaleLinear({
        range: [yMax, 0],
        round: true,
        domain: [0, Math.max(...data.map(getFrequecy))],
      }),
    [yMax]
  );

  const { scale } = useSpring({
    from: { scale: 0 },
    to: { scale: 1 },
  });
  const AnimatedBar = animated(Bar);

  axisBottomScale.rangeRound([0, xMax]);
  axisLeftScale.rangeRound([yMax, 0]);

  return (
    <div className="centering">
      <h1> Frequently Used Moves</h1>
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
          })}
        />
        <AxisBottom
          top={yMax + 60}
          scale={axisBottomScale}
          stroke={axisTextColor}
          tickStroke={axisTextColor}
          tickLabelProps={() => ({
            fill: axisTextColor,
            fontSize: 12,
            textAnchor: "middle",
          })}
        />
      </svg>
    </div>
  );
};

export default FrequentlyUsedMoves;
