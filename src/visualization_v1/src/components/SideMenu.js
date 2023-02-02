import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import { Link } from "react-router-dom";

import React from "react";

const SideMenu = () => {
  return (
    <Sidebar className="sidebar">
      <Menu>
        <SubMenu label="Charts">
          <MenuItem component={<Link to="/bar-chart" />}>
            Frequently Used Moves
          </MenuItem>
          <MenuItem> Line charts </MenuItem>
        </SubMenu>
        <MenuItem component={<Link to="/heatmap" />}> Heat Map</MenuItem>
        <MenuItem> Move Tree </MenuItem>
        <MenuItem> Radial Graph</MenuItem>
      </Menu>
    </Sidebar>
  );
};

export default SideMenu;
