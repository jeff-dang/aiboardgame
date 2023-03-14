import React from "react";

const SimulationTypeSelection = ({ setSimType, simulationFile, value }) => {
  return (
    <>
      <span> Simulations: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setSimType(e.target.value)}
        disabled={simulationFile === "none"}
        value={value}
      >
        <option key="Aggregate" value="Aggregate">
          Aggregate
        </option>
        <option key="Individual" value="Individual">
          Individual
        </option>
      </select>
    </>
  );
};

export default SimulationTypeSelection;
