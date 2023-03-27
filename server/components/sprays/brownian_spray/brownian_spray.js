export default class Squares {
  constructor(s) {
    this.s = s;
    this.name = "Squares";
    this.sizeOffset = 0.1;
    this.layer;
    this.ax = [];
    this.ay = [];
    this.num = 2000;
    this.range = 6;
  }
  preload() {}
  setup() {
    for (let i = 0; i < this.num; i++) {
      this.ax[i] = this.s.width / 2;
      this.ay[i] = this.s.height / 2;
    }
  }
  setLayer(layer) {
    this.layer = layer;
  }
  draw(size, color) {
    // Shift all elements 1 place to the left
    for (let i = 1; i < this.num; i++) {
      this.ax[i - 1] = this.ax[i];
      this.ay[i - 1] = this.ay[i];
    }

    // Put a new value at the end of the array
    this.ax[this.num - 1] += this.s.random(-this.range, this.range);
    this.ay[this.num - 1] += this.s.random(-this.range, this.range);

    // Constrain all points to the screen
    this.ax[this.num - 1] = this.s.constrain(
      this.ax[this.num - 1],
      0,
      this.s.width
    );
    this.ay[this.num - 1] = this.s.constrain(
      this.ay[this.num - 1],
      0,
      this.s.height
    );

    // Draw a line connecting the points
    for (let j = 1; j < this.num; j++) {
      let val = (j / this.num) * 204.0 + 51;
      this.layer.stroke(color);
      this.layer.strokeWeight(val * size * this.sizeOffset);
      this.layer.line(this.ax[j - 1], this.ay[j - 1], this.ax[j], this.ay[j]);
    }

    this.s.image(this.layer, 0, 0);
  }

  clear() {
    this.layer.clear();
  }
}
