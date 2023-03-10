import React, { useEffect, useState } from "react";
import * as data from "./data.json";
import styled from "styled-components";
import { Tree, TreeNode } from "react-organizational-chart";
import _ from "underscore";
const StyledNode = styled.div`
  padding: 5px;
  border-radius: 8px;
  display: inline-block;
  border: 1px solid red;
  background: skyblue;
`;
const StyledNode2 = styled.div`
  padding: 5px;
  border-radius: 8px;
  display: inline-block;
  border: 1px solid red;
  background: green;
  color: #fff;
`;
export default function TreeChart(props) {
  const [info, setInfo] = useState(data);
  const [selected, setSelected] = useState("");
  useEffect(() => {
    const s = _.clone(data);
    const setChecked = (obj, c = false) => {
      // if(obj.checked && selected === obj.name){
      // obj.checked = false
      // } else {
      obj.checked = c ? c : selected === obj.name;
      // }
      if (obj.child) {
        obj.child.map((obj2) => {
          // if(obj2.checked && selected === obj2.name){
          // obj2.checked = false
          // } else {
          obj2.checked = obj.checked ? obj.checked : selected === obj2.name;
          // }
          return setChecked(obj2, obj.checked);
        });
      }
      return obj;
    };
    setInfo(setChecked(s));
  }, [selected]);
  const getLabel = (name, checked) => {
    const Name = () => (
      <span
        className="selectable"
        onClick={() => {
          setSelected(name);
        }}
      >
        {name}
      </span>
    );
    return checked ? (
      <StyledNode2>
        <Name />
      </StyledNode2>
    ) : (
      <StyledNode>
        <Name />
      </StyledNode>
    );
  };
  const getTreenode = (child) => {
    return child.map((obj) => {
      return (
        <TreeNode label={getLabel(obj.name, obj.checked)}>
          {obj.child && getTreenode(obj.child)}
        </TreeNode>
      );
    });
  };
  return (
    <div>
      <h1>{selected}</h1>
      <Tree
        onClick={() => {
          setSelected(info.name);
        }}
        label={getLabel(info.name, info.checked)}
      >
        {getTreenode(info.child)}
      </Tree>
    </div>
  );
}