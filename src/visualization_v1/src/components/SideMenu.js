import { Sidebar, Menu, MenuItem } from "react-pro-sidebar";
import { Link } from "react-router-dom";

import React from "react";

/**
 * Component for displaying the side menu
 */
const SideMenu = () => {
  return (
    <Sidebar className="sidebar">
      <Menu>
        <MenuItem component={<Link to="/" />}>Home</MenuItem>
        <MenuItem component={<Link to="/freq-used" />}>
          Frequently Used Moves
        </MenuItem>
        <MenuItem component={<Link to="/moves-scores" />}>
          Moves vs. Scores
        </MenuItem>
        <MenuItem component={<Link to="/heatmap" />}> Heat Map</MenuItem>
        <MenuItem component={<Link to="/pie-chart" />}>
          {" "}
          All Used Moves Frequency
        </MenuItem>
        <MenuItem component={<Link to="/line-chart" />}>
          {" "}
          Simulation vs. Scores
        </MenuItem>
        {/* <MenuItem component={<Link to="/tree-graph" />}> Tree Graph</MenuItem>*/}
        <MenuItem component={<Link to="/tree-chart" />}>
          Tree - Individual Paths
        </MenuItem>
        {/* <MenuItem component={<Link to="/tree-chart" />}>
          Alt Tree Chart
        </MenuItem> */}
        <MenuItem component={<Link to="/tree-graph" />}>
          Tree - Common Paths
        </MenuItem>
        <MenuItem component={<Link to="/comparison" />}>Comparison</MenuItem>
      </Menu>
    </Sidebar>
  );
};

export default SideMenu;
