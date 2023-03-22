import "./style.css";
import * as p5 from "p5";
import { Pane } from "tweakpane";
import * as EssentialsPlugin from "@tweakpane/plugin-essentials";
import Toastify from "toastify-js";

// const ws = new WebSocket("ws://localhost:5001");
// ws.addEventListener("open", () => {
//   Toastify({
//     text: "WebSocket connection established",
//     duration: 3000,
//     newWindow: true,
//     close: true,
//     gravity: "top",
//     position: "left",
//     stopOnFocus: true,
//   }).showToast();
//   ws.send("How are you?");
// });

// ws.addEventListener("message", function (event) {
//   console.log(event.data);
//   Toastify({
//     text: event.data,
//     duration: 3000,
//     newWindow: true,
//     close: true,
//     gravity: "top",
//     position: "left",
//     stopOnFocus: true,
//   }).showToast();
// });

const pane = new Pane();
pane.registerPlugin(EssentialsPlugin);

const fpsGraph = pane.addBlade({
  view: "fpsgraph",
  label: "fpsgraph",
  lineCount: 2,
});
const clearBtn = pane.addButton({
  title: "Clear",
  label: "Img Buffer", // optional
});

// Sprays
import Circles from "./components/sprays/circles_spray/circles_spray";
import Squares from "./components/sprays/squares_spray/squares_spray";

let sketch = (s) => {
  let size = 80;
  let brush = 0;
  let r = 255;
  let g = 0;
  let b = 0;
  let a = 0.75;
  let color;
  let sprays = [];

  // Instantiates sprays
  const cicles = new Circles(s);
  sprays.push(cicles);
  const squares = new Squares(s);
  sprays.push(squares);

  s.preload = () => {
    // Preloads anything a spray might need
    sprays.map((spray) => {
      spray.preload();
    });
  };

  const clear = () => {
    s.clear();
  };
  clearBtn.on("click", () => {
    clear();
    cicles.clear();
  });

  s.setup = () => {
    s.pixelDensity(s.displayDensity());
    s.createCanvas(window.innerWidth, window.innerHeight);
    sprays.map((spray) => {
      spray.setup();
    });
  };

  s.draw = () => {
    fpsGraph.begin();
    color = s.color(r, g, b, a);
    if (brush === 0) {
      cicles.spray(size, color);
    } else {
      squares.spray(size, color);
    }
    fpsGraph.end();
  };

  s.windowResized = () => {
    s.resizeCanvas(window.innerWidth, window.innerHeight);
  };

  addEventListener("wheel", (event) => {
    size += event.deltaY * 0.1;
  });

  addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp") {
      size += 10;
    } else if (event.key === "ArrowDown") {
      size >= 10 ? (size -= 10) : null;
    }
  });
};

const P5 = new p5(sketch);
