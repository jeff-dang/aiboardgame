

// import React, { Component } from "react";
// import { Tree } from 'react-tree-graph';
// import "./css/style.css";


// export const data = {
//   name: "Colour",
//   textProps: { x: -25, y: 25 },
//   children: [
//     {
//       name: "Black",
//       pathProps: "black",
//       textProps: { x: -25, y: 25 },
//       children: []
//     },
//     {
//       name: "Blue",
//       textProps: { x: -25, y: 25 },
//       children: [
//         {
//           name: "Aquamarine",
//           textProps: { x: -25, y: 25 },
//           children: []
//         },
//         {
//           name: "Cyan",
//           textProps: { x: -25, y: 25 },
//           children: []
//         },
//         {
//           name: "Navy",
//           textProps: { x: -25, y: 25 },
//           children: []
//         },
//         {
//           name: "Turquoise",
//           textProps: { x: -25, y: 25 },
//           children: []
//         }
//       ]
//     },
//     {
//       name: "Green",
//       textProps: { x: -25, y: 25 },
//       children: []
//     },
//     {
//       name: "Purple",
//       textProps: { x: -25, y: 25 },
//       children: [
//         {
//           name: "Indigo",
//           textProps: { x: -25, y: 25 },
//           children: []
//         },
//         {
//           name: "Violet",
//           textProps: { x: -25, y: 25 },
//           children: []
//         }
//       ]
//     },
//     {
//       name: "Red",
//       textProps: { x: -25, y: 25 },
//       children: [
//         {
//           name: "Crimson",
//           textProps: { x: -25, y: 25 },
//           children: []
//         },
//         {
//           name: "Maroon",
//           textProps: { x: -25, y: 25 },
//           children: []
//         },
//         {
//           name: "Scarlet",
//           textProps: { x: -25, y: 25 },
//           children: []
//         }
//       ]
//     },
//     {
//       name: "White",
//       textProps: { x: -25, y: 25 },
//       children: []
//     },
//     {
//       name: "Yellow",
//       textProps: { x: -25, y: 25 },
//       children: []
//     }
//   ]
// };

// export default function App() {
//   <div>
//         <Tree
//           animated={true}
//           data={data}
//           nodeRadius={15}
//           margins={{ top: 20, bottom: 10, left: 20, right: 200 }}
//           height={600}
//           width={800}
//         />
//       </div>
// }

import React, { Component } from "react";
import { Tree } from 'react-tree-graph';
import "./css/style.css";

export default class Dropdown extends Component {
  render() {
    let data = {
      name: "Colour",
      textProps: { x: -25, y: 25 },
      children: [
        {
          name: "Black",
          pathProps: "black",
          textProps: { x: -25, y: 25 },
          children: []
        },
        {
          name: "Blue",
          textProps: { x: -25, y: 25 },
          children: [
            {
              name: "Aquamarine",
              textProps: { x: -25, y: 25 },
              children: []
            },
            {
              name: "Cyan",
              textProps: { x: -25, y: 25 },
              children: []
            },
            {
              name: "Navy",
              textProps: { x: -25, y: 25 },
              children: []
            },
            {
              name: "Turquoise",
              textProps: { x: -25, y: 25 },
              children: []
            }
          ]
        },
        {
          name: "Green",
          textProps: { x: -25, y: 25 },
          children: []
        },
        {
          name: "Purple",
          textProps: { x: -25, y: 25 },
          children: [
            {
              name: "Indigo",
              textProps: { x: -25, y: 25 },
              children: []
            },
            {
              name: "Violet",
              textProps: { x: -25, y: 25 },
              children: []
            }
          ]
        },
        {
          name: "Red",
          textProps: { x: -25, y: 25 },
          children: [
            {
              name: "Crimson",
              textProps: { x: -25, y: 25 },
              children: []
            },
            {
              name: "Maroon",
              textProps: { x: -25, y: 25 },
              children: []
            },
            {
              name: "Scarlet",
              textProps: { x: -25, y: 25 },
              children: []
            }
          ]
        },
        {
          name: "White",
          textProps: { x: -25, y: 25 },
          children: []
        },
        {
          name: "Yellow",
          textProps: { x: -25, y: 25 },
          children: []
        }
      ]
    };
    return (
      <div>
        <Tree
          animated={true}
          data={data}
          nodeRadius={15}
          margins={{ top: 20, bottom: 10, left: 20, right: 200 }}
          height={700}
          width={1000}
        />
      </div>
    );
  }
}