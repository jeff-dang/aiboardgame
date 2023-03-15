import React from "react";

const SimulationTypeSelection = ({ setSimType, simulationFile, value }) => {
  return (
    <>
      <span> Type: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setSimType(e.target.value)}
        disabled={simulationFile === "none"}
        value={value}
      >
        <option key="Aggregate" value="Aggregate">
          Aggregate
        </option>
        {/* <option key="Individual" value="Individual">
          Individual
        </option> */}
        <option key="Subset" value="Subset">
          Subset
        </option>
      </select>
    </>
  );
};

export default SimulationTypeSelection;
