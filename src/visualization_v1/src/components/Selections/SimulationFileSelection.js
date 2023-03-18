import React from "react";
import { files } from "../../data/getFiles";

const SimulationFileSelection = ({ setSimulationFile }) => {
  return (
    <>
      <span> Simulation File: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => {
          const file = files.find((file) => file.name === e.target.value);

          setSimulationFile(file.filename);
        }}
        defaultValue={"none"}
      >
        <option disabled value={"none"}>
          None
        </option>
        {files.map((filename) => (
          <option key={filename.name} value={filename.name}>
            {filename.name}
          </option>
        ))}
      </select>
    </>
  );
};

export default SimulationFileSelection;
