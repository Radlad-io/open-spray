import * as p5 from "p5";
import Debug from "./Debug";
import Network from "./Network";
import Layers from "./Layers";
import State from "./State";
import Sprays from "./Sprays";
import Inputs from "./Inputs";

let instance = null;

export default class Experience {
  constructor() {
    if (instance !== null) {
      return instance;
    }
    instance = this;
    this.state = new State();
    this.inputs = new Inputs();
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
    const sprays = new Sprays(s);
    const layers = new Layers(s);
    const debug = new Debug();

    // Prevents Right-Click Menu
    document.addEventListener("contextmenu", (event) => event.preventDefault());

    // Pevents zooming during touch events
    if (!debug.active) {
      document.addEventListener(
        "touchstart",
        (event) => {
          event.preventDefault();
        },
        { passive: false }
      );
    }

    s.preload = () => {
      sprays.preload();
    };

    s.setup = () => {
      s.pixelDensity(s.displayDensity());
      sprays.sprayList.map((spray) => {
        spray.setup(layers.getLayer(state.layerIndex.get()));
      });
      s.createCanvas(window.innerWidth, window.innerHeight);
    };

    s.draw = () => {
      if (debug.active) {
        debug.fps.begin();
      }

      // s.clear();

      sprays
        .getSpray(state.sprayIndex.get())
        .draw(state.size.get(), state.color.get());

      if (debug.active) {
        debug.fps.end();
      }
    };

    s.windowResized = () => {
      s.resizeCanvas(window.innerWidth, window.innerHeight);
      layers.layers.map((layer) => {
        layer.resizeCanvas(window.innerWidth, window.innerHeight);
      });
    };
  }

  clear() {
    console.log("firing");
  }
}
