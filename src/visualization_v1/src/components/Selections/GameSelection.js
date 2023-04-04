import React from "react";
import { files } from "../../data/getFiles";

/**
 * Component for displaying the game selection
 */
const GameSelection = ({ setGame }) => {
  const games = [...new Set(files.map((item) => item.game))];
  return (
    <>
      <span> Game: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => setGame(e.target.value)}
        defaultValue={"none"}
      >
        <option disabled value={"none"}>
          None
        </option>
        {games.map((game) => (
          <option key={game} value={game}>
            {game}
          </option>
        ))}
      </select>
    </>
  );
};

export default GameSelection;
