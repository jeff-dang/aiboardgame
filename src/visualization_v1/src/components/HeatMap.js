import React, { useEffect, useMemo, useState } from "react";
import { Group } from "@visx/group";
import { scaleLinear } from "@visx/scale";
import { HeatmapCircle } from "@visx/heatmap";
import { withTooltip, Tooltip, defaultStyles } from "@visx/tooltip";
import Data from "../data/getData";
import { useSpring, animated } from "@react-spring/web";
const tooltipStyles = {
  ...defaultStyles,
  minWidth: 60,
  backgroundColor: "rgba(0,0,0,0.9)",
  color: "white",
};

const hot1 = "#77312f";
const hot2 = "#f33d15";
const background = "#9de3d4"; //"#28272c";

const dataInit = new Data();
const allData = dataInit.getAllDataExEnd();
const players = dataInit.getNumberOfPlayers(allData);
const numSimulations = dataInit.getNumberOfSimulations(allData);

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

  const [numSims, setNumSims] = useState(1);
  const [player, setPlayer] = useState(0);
  const [freqMap, setFreqMap] = useState([]);
  const [data, setData] = useState([]);
  const [toggle, setToggle] = useState(true);

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
    range: [0.1, 1],
    domain: [0, colorMax],
  });

  useEffect(() => {
    const mergedData = dataInit.getDataWithMergedActions(allData);
    setFreqMap(dataInit.getCountMapForPlayer(mergedData, numSims, player));
    setToggle(false);
  }, [player, numSims]);

  useEffect(() => {
    setData(getData(freqMap, 6));
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
      className="centering"
      style={{
        marginBottom: 20,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <h1>Heat Map of All Moves</h1>
      <div
        style={{ display: "flex", flexDirection: "row", alignItems: "center" }}
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
      </div>
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

const HeatMapWithTooltip = withTooltip(HeatMap);

export default HeatMapWithTooltip;
