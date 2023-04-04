import * as p5 from "p5";
import Debug from "./Debug";
import Network from "./Network";
import State from "./State";

let instance = null;

export default class Experience {
  constructor() {
    if (instance !== null) {
      return instance;
    }
    instance = this;
    this.state = new State();
    this.env = import.meta.env;

    // Should be pushed down so it has access
    // to the methods its needs
    // when mqtt messages are sent
    this.network = new Network(
      this.env.VITE_MQTT_URL,
      this.env.VITE_MQTT_USERNAME,
      this.env.VITE_MQTT_TOKEN,
      this.env.VITE_MQTT_TOPIC
    );
    this.sketch = this.P5 = new p5(this.sketch);
  }

  sketch(s) {
    const state = new State();
    const debug = new Debug();
    let sprays = [];

    s.preload = () => {};

    s.setup = () => {
      s.createCanvas(window.innerWidth, window.innerHeight);
    };

    s.draw = () => {
      if (debug.active) {
        debug.fps.begin();
      }
      if (s.mouseIsPressed) {
        s.fill(...state.color.get());
        s.ellipse(
          s.mouseX,
          s.mouseY,
          80 * state.size.get(),
          80 * state.size.get()
        );
      }
      if (debug.active) {
        debug.fps.end();
      }
    };
  }

  clear() {
    console.log("firing");
  }
}
