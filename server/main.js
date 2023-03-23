import "./style.css";
import * as p5 from "p5";
import { Pane } from "tweakpane";
import * as EssentialsPlugin from "@tweakpane/plugin-essentials";
import Toastify from "toastify-js";

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

document.addEventListener("contextmenu", (event) => event.preventDefault());

// Sprays
import Circles from "./components/sprays/circles_spray/circles_spray";
import Squares from "./components/sprays/squares_spray/squares_spray";
import Standard from "./components/sprays/standard_spray/standard_spray";

const sketch = (s) => {
  // FIXME: size should be between 0 & 1
  let size = 0.5;
  let spray = 0;
  let r = 255;
  let g = 0;
  let b = 0;
  let a = 0.51;
  let color = s.color(r, g, b, a);
  let sprays = [];

  const PARAMS = {
    key: "#ff0055ff",
  };

  // const pane = new Pane();
  pane.addInput(PARAMS, "key", {
    picker: "inline",
    expanded: true,
    onchange: (e) => {
      console.log(e);
    },
  });

  // Instantiates sprays
  const cicles = new Circles(s);
  sprays.push(cicles);
  const squares = new Squares(s);
  sprays.push(squares);
  const standard = new Standard(s);
  sprays.push(standard);

  s.preload = () => {
    // Preloads anything a spray might need
    sprays.map((spray) => {
      spray.preload();
    });
  };

  const clear = () => {
    s.clear();
    sprays.map((spray) => {
      spray.clear();
    });
  };

  clearBtn.on("click", () => {
    clear();
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
    if (spray === 0) {
      standard.draw(size, color);
    } else {
      squares.draw(size, color);
    }
    fpsGraph.end();
  };

  s.windowResized = () => {
    s.resizeCanvas(window.innerWidth, window.innerHeight);
  };

  // addEventListener("wheel", (event) => {
  //   size += event.deltaY * 0.01;
  // });

  addEventListener("keydown", (event) => {
    switch (event.key) {
      case "ArrowUp":
        if (size < 1) {
          size += 0.1;
          console.log(size);
        }
        break;
      case "ArrowDown":
        if (size > 0.2) {
          size -= 0.1;
          console.log(size);
        }
        break;
      case "1":
        switchSpray(0);
        break;
      case "2":
        switchSpray(1);
        break;
      case "3":
        console.log(3);
        break;
      case "4":
        console.log(4);
        break;
      case "5":
        console.log(5);
        break;
      case "6":
        console.log(6);
        break;
      case "7":
        console.log(7);
        break;
      case "8":
        console.log(8);
        break;
      case "9":
        console.log(9);
        break;
    }
  });
  function switchSpray(index) {
    spray = index;
    Toastify({
      text: "Switched Brush",
      duration: 3000,
      newWindow: true,
      close: true,
      gravity: "bottom",
      position: "right",
      stopOnFocus: true,
      style: {
        background: "linear-gradient(to right, #333, #555)",
      },
    }).showToast();
  }
};

const P5 = new p5(sketch);
