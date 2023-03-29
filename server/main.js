import "./style.css";

import Experience from "./components/Experience";

new Experience();

// // Prevents pinch zoom, gesture based nav and right-click menu on touch
document.addEventListener("contextmenu", (event) => event.preventDefault());
// document.addEventListener(
//   "touchstart",
//   (event) => {
//     event.preventDefault();
//   },
//   { passive: false }
// );

// // Sprays

// const sketch = (s) => {
//   // FIXME: size should be between 0 & 1
//   let size = 0.5;
//   let sprayIndex = 0;
//   let r = 255;
//   let g = 200;
//   let b = 100;
//   let a = 0.51;
//   let color;
//   let sprays = [];
//   let layers = [];
//   let layerIndex = 0;

//   const PARAMS = {
//     key: { r, g, b, a },
//   };

//   // const pane = new Pane();
//   const test = pane.addInput(PARAMS, "key", {
//     picker: "inline",
//     expanded: true,
//     onchange: (e) => {
//       console.log(e);
//     },
//   });

//   pane.on("change", (e) => {
//     console.log(e.value);
//     r = Math.floor(e.value.r);
//     g = Math.floor(e.value.g);
//     b = Math.floor(e.value.b);
//     a = e.value.a;
//   });

//   // Instantiates sprays
//   const cicles = new Circles(s);
//   sprays.push(cicles);
//   const squares = new Squares(s);
//   sprays.push(squares);
//   const standard = new Standard(s);
//   sprays.push(standard);
//   const brownian = new Brownian(s);
//   sprays.push(brownian);

//   s.preload = () => {
//     // Preloads anything a spray might need
//     sprays.map((spray) => {
//       spray.preload();
//     });
//   };

//   const clear = () => {
//     s.clear();
//     sprays.map((spray) => {
//       spray.clear();
//     });
//   };

//   clearBtn.on("click", () => {
//     clear();
//   });

//   s.setup = () => {
//     color = s.color(r, g, b, a);
//     s.pixelDensity(s.displayDensity());
//     s.createCanvas(window.innerWidth, window.innerHeight);
//     sprays.map((spray) => {
//       spray.setup();
//     });
//     layers.push(s.createGraphics(window.innerWidth, window.innerWidth));
//     sprays[sprayIndex].setLayer(layers[layerIndex]);
//   };

//   s.draw = () => {
//     fpsGraph.begin();
//     color = s.color(r, g, b, a);
//     sprays[sprayIndex].draw(size, color, layers[layerIndex]);
//     fpsGraph.end();
//   };

//   s.windowResized = () => {
//     s.resizeCanvas(window.innerWidth, window.innerHeight);
//   };

//   addEventListener("keydown", (event) => {
//     switch (event.key) {
//       case "ArrowUp":
//         if (size < 1) {
//           size += 0.05;
//           console.log(size);
//         }
//         break;
//       case "ArrowDown":
//         if (size > 0) {
//           size -= 0.05;
//           console.log(size);
//         }
//         break;
//       case "1":
//         switchSpray(0);
//         break;
//       case "2":
//         switchSpray(1);
//         break;
//       case "3":
//         switchSpray(2);
//         break;
//       case "4":
//         switchSpray(3);
//         break;
//       case "5":
//         console.log(5);
//         break;
//       case "6":
//         console.log(6);
//         break;
//       case "7":
//         console.log(7);
//         break;
//       case "8":
//         console.log(8);
//         break;
//       case "9":
//         console.log(9);
//         break;
//       case "u":
//         console.log(layers);
//         console.log(layers[layerIndex]);
//         break;
//     }
//   });
//   function switchSpray(index) {
//     if (index === sprayIndex) {
//       return;
//     }

//     sprayIndex = index;

//     // Creates new layer appends to layer array
//     layers.push(s.createGraphics(window.innerWidth, window.innerHeight));
//     console.log(layers);
//     layerIndex++;

//     // Passes new layer to spray
//     console.log("# of layers: " + layers.length);
//     sprays[sprayIndex].setLayer(layers[layerIndex]);

// const P5 = new p5(sketch);
