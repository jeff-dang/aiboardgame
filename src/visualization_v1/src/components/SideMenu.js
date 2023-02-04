import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import { Link } from "react-router-dom";

import React from "react";

const SideMenu = () => {
  return (
    <Sidebar className="sidebar">
      <Menu>
        <MenuItem component={<Link to="/bar-chart" />}>
          Frequently Used Moves
        </MenuItem>

        <MenuItem component={<Link to="/heatmap" />}> Heat Map</MenuItem>
        <MenuItem component={<Link to="/pie-chart" />}> Pie Chart</MenuItem>
        <MenuItem component={<Link to="/line-chart" />}> Line Chart</MenuItem>
        <MenuItem component={<Link to="/tree-graph" />}> Tree Graph</MenuItem>
        <MenuItem> Move Tree </MenuItem>
        <MenuItem> Radial Graph</MenuItem>
      </Menu>
    </Sidebar>
  );
};

export default SideMenu;
