import "./style.css";
import * as p5 from "p5";
import Circles from "./sprays/circles_spray";
import Squares from "./sprays/squares_spray";

const cicles = new Circles();
const squares = new Squares();

let dia = 80;
let brush = 1;

let s = (sk) => {
  sk.setup = () => {
    sk.createCanvas(window.innerWidth, window.innerHeight);
  };

  sk.draw = () => {
    if (brush === 0) {
      cicles.spray(sk, dia);
    } else {
      squares.spray(sk, dia);
    }
  };
};

addEventListener("wheel", (event) => {
  dia += event.deltaY * 0.1;
});

addEventListener("keypress", (event) => {
  console.log(event);
  if (event.key === "s") {
    brush = 1;
  } else {
    brush = 0;
  }
});

const P5 = new p5(s);
