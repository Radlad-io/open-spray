import "./style.css";
import * as p5 from "p5";
import { Pane } from "tweakpane";
import * as EssentialsPlugin from "@tweakpane/plugin-essentials";

const pane = new Pane();
pane.registerPlugin(EssentialsPlugin);
const fpsGraph = pane.addBlade({
  view: "fpsgraph",

  label: "fpsgraph",
  lineCount: 2,
});

// Sprays
import Circles from "./sprays/circles_spray";
import Squares from "./sprays/squares_spray";

let sketch = (s) => {
  let size = 80;
  let brush = 0;
  let r = 0;
  let g = 0;
  let b = 0;
  let color;

  // Instantiates sprays
  const cicles = new Circles(s);
  const squares = new Squares(s);

  s.preload = () => {
    cicles.preload();
  };

  s.setup = () => {
    s.createCanvas(window.innerWidth, window.innerHeight);
  };

  s.draw = () => {
    fpsGraph.begin();
    color = s.color(r, g, b);
    if (brush === 0) {
      cicles.spray(size, color);
    } else {
      squares.spray(size);
    }
    fpsGraph.end();
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
