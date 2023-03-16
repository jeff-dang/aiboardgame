import React from "react";

const ToSelection = ({
  text,
  setEnd,
  arr,
  simulationFile,
  startVal,
  endVal,
}) => {
  const len = arr.length;
  return (
    <>
      <span>{text} </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setEnd(Number(e.target.value))}
        disabled={simulationFile === "none"}
        value={endVal}
      >
        {arr.slice(startVal - 1, len).map((simulation) => (
          <option key={simulation} value={simulation}>
            {simulation}
          </option>
        ))}
      </select>
    </>
  );
};

export default ToSelection;
