export default class Circles {
  constructor(s) {
    this.s = s;
    this.name = "Circles";
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
        this.layer.ellipse(
          touch.x,
          touch.y,
          size * this.sizeOffset,
          size * this.sizeOffset
        );
      });
    }
    this.s.image(this.layer, 0, 0);
  }

  clear() {
    this.layer.clear();
  }
}
