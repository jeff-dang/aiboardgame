import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import { Link } from "react-router-dom";

import React from "react";

const SideMenu = () => {
  return (
    <Sidebar className="sidebar">
      <Menu>
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
        <MenuItem component={<Link to="/tree-graph" />}> Tree Graph</MenuItem>
      </Menu>
    </Sidebar>
  );
};

export default SideMenu;