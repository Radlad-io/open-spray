import State from "./State";

export default class Layers {
  constructor(s) {
    this.s = s;
    this.state = new State();
    this.layers = [];
    this.index = 0;
    this.layers.push(
      this.s.createGraphics(window.innerWidth, window.innerHeight)
    );
  }

  addLayer() {
    this.layers.push(
      this.s.createGraphics(window.innerWidth, window.innerHeight)
    );
    this.index++;
  }

  getLayer(index) {
    return this.layers[index];
  }
}
