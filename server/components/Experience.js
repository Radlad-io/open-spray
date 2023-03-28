import * as p5 from "p5";
import Network from "./Network";
import State from "./State";

let instance = null;

export default class Experience {
  constructor() {
    if (instance !== null) {
      return instance;
    }
    this.state = new State();
    this.env = import.meta.env;

    // Should be pushed down so it has access to the methods its needs
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
    let sprays = [];

    s.preload = () => {};

    s.setup = () => {
      s.createCanvas(window.innerWidth, window.innerHeight);
    };

    s.draw = () => {
      if (s.mouseIsPressed) {
        s.fill(s.color(state.color.get()));
      } else {
        s.fill(255);
      }
      s.ellipse(
        s.mouseX,
        s.mouseY,
        80 * state.size.get(),
        80 * state.size.get()
      );
    };
  }
}
