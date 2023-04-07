export default class Squares {
  constructor(s) {
    this.s = s;
    this.name = "Squares";
    this.sizeOffset = 50;
    this.layer;
  }
  preload() {}
  setup(layerIndex) {
    this.setLayer(layerIndex);
  }
  setLayer(layer) {
    this.layer = layer;
  }
  draw(size, color) {
    this.layer.noStroke();
    this.layer.fill(color);
    if (this.s.touches.length > 0) {
      this.s.touches.map((touch) => {
        this.layer.square(touch.x, touch.y, size * this.sizeOffset);
      });
    } else if (this.s.mouseIsPressed) {
      this.layer.square(this.s.mouseX, this.s.mouseY, size * this.sizeOffset);
    }
    this.s.image(this.layer, 0, 0);
  }

  clear() {
    this.layer.clear();
  }
}
