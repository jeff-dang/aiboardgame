import React from "react";

/**
 * Component for displaying the number of moves selection
 */
const NumMovesSelection = ({
  setNumMoves,
  allMoves,
  simulationFile,
  value,
}) => {
  return (
    <>
      <span> Number of Moves: </span>
      <select
        style={{ margin: 10 }}
        onChange={(e) => {
          if (e.target.value === "all") {
            setNumMoves(allMoves[allMoves.length - 1]);
          } else {
            setNumMoves(Number(e.target.value));
          }
        }}
        disabled={simulationFile === "none"}
        value={value}
      >
        <option key="all" value="all">
          All
        </option>
        {allMoves.map((move) => (
          <option key={move} value={move}>
            {move}
          </option>
        ))}
      </select>
    </>
  );
};

export default NumMovesSelection;
