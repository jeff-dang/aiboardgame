import React, { useState, useEffect } from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";
import {
  getAllDataExEnd,
  getAllNonZeroActions,
  getDataWithMergedActions,
  getFrequencyMapForPlayer,
} from "../data/getData";

ChartJS.register(ArcElement, Tooltip, Legend);

const getRandomColor = () => {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
};

const d = getAllDataExEnd();
const d1 = getDataWithMergedActions(d);

const f = getFrequencyMapForPlayer(d1, 1, 0);

const allNonZeroActions = getAllNonZeroActions(f);

const getLabels = () => {
  let labels = [];
  Object.entries(allNonZeroActions).forEach((action) => {
    labels.push(action[1].name);
  });
  return labels;
};

const getValues = () => {
  let values = [];
  Object.entries(allNonZeroActions).forEach((action) => {
    values.push(action[1].frequency);
  });
  return values;
};

const getBackgroundColors = () => {
  let backgroundColors = [];
  allNonZeroActions.forEach((action) => {
    backgroundColors.push(getRandomColor());
  });

  return backgroundColors;
};

const getBorderColors = () => {
  let borderColors = [];
  allNonZeroActions.forEach((action) => {
    borderColors.push("#000000");
  });

  return borderColors;
};

const data = {
  labels: getLabels(),
  datasets: [
    {
      label: "# of times used",
      data: getValues(),
      backgroundColor: getBackgroundColors(),
      borderColor: getBorderColors(),
      borderWidth: 0.5,
    },
  ],
};

const PieChart = () => {
  return (
    <div>
      {
        <Pie
          data={data}
          width={1200}
          height={700}
          options={{ maintainAspectRatio: false }}
        />
      }
    </div>
  );
};

export default PieChart;
