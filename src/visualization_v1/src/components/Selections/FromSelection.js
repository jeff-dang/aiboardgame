import React from "react";

const FromSelection = ({
  text,
  setStart,
  arr,
  simulationFile,
  startVal,
  endVal,
}) => {
  return (
    <>
      <span>{text}</span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setStart(Number(e.target.value))}
        disabled={simulationFile === "none"}
        value={startVal}
      >
        {arr.map((simulation) => (
          <option key={simulation} value={simulation}>
            {simulation}
          </option>
        ))}
      </select>
    </>
  );
};

export default FromSelection;
