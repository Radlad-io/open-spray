export default class Squares {
  constructor(s) {
    this.s = s;
    this.name = "Squares";
    this.sizeOffset = 50;
    this.layer;
  }
  preload() {}
  setup() {}
  setLayer(layer) {
    this.layer = layer;
  }
  draw(size, color) {
    if (this.s.touches.length > 0) {
      this.s.touches.map((touch) => {
        this.layer.stroke(0);
        this.layer.fill(color);
        this.layer.square(touch.x, touch.y, size * this.sizeOffset);
      });
    }

    this.s.image(this.layer, 0, 0);
  }

  clear() {
    this.layer.clear();
  }
}
