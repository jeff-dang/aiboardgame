import React from "react";

/**
 * Component for displaying the player selection
 */
const PlayerSelection = ({ setPlayer, players, simulationFile }) => {
  return (
    <>
      <span> Player: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setPlayer(Number(e.target.value))}
        disabled={simulationFile === "none"}
      >
        {players.map((player) => (
          <option key={player} value={player}>
            {player}
          </option>
        ))}
      </select>
    </>
  );
};

export default PlayerSelection;
