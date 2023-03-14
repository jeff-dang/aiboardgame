import React from "react";
import { files } from "../../data/getFiles";

const SimulationFileSelection = ({ setSimulationFile }) => {
  return (
    <>
      <span> Simulation File: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setSimulationFile(e.target.value)}
        defaultValue={"none"}
      >
        <option disabled value={"none"}>
          None
        </option>
        {files.map((filename) => (
          <option key={filename} value={filename}>
            {filename}
          </option>
        ))}
      </select>
    </>
  );
};

export default SimulationFileSelection;
