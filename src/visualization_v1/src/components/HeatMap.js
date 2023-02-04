import React, { useState } from "react";
import { Group } from "@visx/group";
import { scaleLinear } from "@visx/scale";
import { HeatmapCircle } from "@visx/heatmap";
import { withTooltip, Tooltip, defaultStyles } from "@visx/tooltip";
const tooltipStyles = {
  ...defaultStyles,
  minWidth: 60,
  backgroundColor: "rgba(0,0,0,0.9)",
  color: "white",
};

const hot1 = "#77312f";
const hot2 = "#f33d15";
const background = "#28272c";

const data = [
  {
    column: 0,
    bins: [
      { name: "move1", count: 5 },
      { name: "move2", count: 200 },
      { name: "move3", count: 300 },
      { name: "move4", count: 400 },
    ],
  },
  {
    column: 1,
    bins: [
      { name: "move5", count: 100 },
      { name: "move6", count: 200 },
      { name: "move7", count: 300 },
      { name: "move8", count: 400 },
    ],
  },
  {
    column: 2,
    bins: [
      { name: "move9", count: 100 },
      { name: "move10", count: 200 },
      { name: "move11", count: 300 },
      { name: "move12", count: 400 },
    ],
  },
  {
    column: 3,
    bins: [
      { name: "move13", count: 100 },
      { name: "move14", count: 200 },
      { name: "move15", count: 300 },
      { name: "move16", count: 500 },
    ],
  },
];

console.log(data);

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
          <HeatmapCircle
            data={data}
            xScale={(d) => xScale(d) ?? 0}
            yScale={(d) => yScale(d) ?? 0}
            colorScale={circleColorScale}
            opacityScale={opacityScale}
            radius={radius}
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
          </HeatmapCircle>
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
