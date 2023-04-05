import React from "react";
import { files } from "../../data/getFiles";

/**
 * Component for displaying the simulation file selection
 */
const SimulationFileSelection = ({
  game,
  setSimulationFile,
  setActionFile,
}) => {
  return (
    <>
      <span> File: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => {
          const file = files.find((file) => file.name === e.target.value);

          setSimulationFile(file.filename);
          setActionFile(file.actionFile);
        }}
        defaultValue={"none"}
        disabled={game === "none"}
      >
        <option disabled value={"none"}>
          None
        </option>
        {files
          .filter((file) => file.game === game)
          .map((filename) => (
            <option key={filename.name} value={filename.name}>
              {filename.name}
            </option>
          ))}
      </select>
    </>
  );
};

export default SimulationFileSelection;
