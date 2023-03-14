import React from "react";

const SimulationSelection = ({
  setNumSims,
  numSimulations,
  simulationFile,
  value,
}) => {
  return (
    <>
      <span> Simulations: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => {
          if (e.target.value === "all") {
            setNumSims(numSimulations[numSimulations.length - 1]);
          } else {
            setNumSims(Number(e.target.value));
          }
        }}
        disabled={simulationFile === "none"}
        value={value}
      >
        <option key="all" value="all">
          All
        </option>
        {numSimulations.map((simulation) => (
          <option key={simulation} value={simulation}>
            {simulation}
          </option>
        ))}
      </select>
    </>
  );
};

export default SimulationSelection;
