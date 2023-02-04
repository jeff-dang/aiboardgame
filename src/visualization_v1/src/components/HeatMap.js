import React, { useState } from "react";
import { Group } from "@visx/group";
import { scaleLinear } from "@visx/scale";
import { HeatmapCircle } from "@visx/heatmap";
import { withTooltip, Tooltip, defaultStyles } from "@visx/tooltip";
import {
  getAllDataExEnd,
  getCountMapForPlayer,
  getDataWithMergedActions,
} from "../data/getData";
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

const allData = getAllDataExEnd();
const mergedData = getDataWithMergedActions(allData);

const freqMap = getCountMapForPlayer(mergedData, 1, 0);

const getData = (freqMap, rows) => {
  const newData = [];
  let columnNum = 0;
  while (freqMap.length) {
    newData.push({ column: columnNum++, bins: freqMap.splice(0, rows) });
  }

  return newData;
};

const data = getData(freqMap, 6);

function max(data, value) {
  return Math.max(...data.map(value));
}

function min(data, value) {
  return Math.min(...data.map(value));
}

// accessors
const bins = (d) => d.bins;
const count = (d) => d.count;

const colorMax = max(data, (d) => max(bins(d), count));
const bucketSizeMax = max(data, (d) => bins(d).length);

let tooltipTimeout;

// scales
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

  const binWidth = xMax / data.length;
  const binHeight = yMax / bucketSizeMax;
  const radius = min([binWidth, binHeight], (d) => d) / 2;

  xScale.range([0, xMax]);
  yScale.range([0, yMax]);

  const { scale } = useSpring({
    from: { scale: 0 },
    to: { scale: 1 },
  });

  const AnimatedHeatMap = animated(HeatmapCircle);

  return (
    <div className="centering">
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
                        const top = bin.cy + radius + margin.top;
                        const left = bin.cx + radius + margin.left;
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
