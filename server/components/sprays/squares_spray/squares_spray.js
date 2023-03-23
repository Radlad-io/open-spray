export default class Squares {
  constructor(s) {
    this.s = s;
    this.sizeOffset = 20;
    this.layer = s.createGraphics(window.innerWidth, window.innerWidth);
  }
  preload() {}
  setup() {}
  draw(size, color) {
    this.layer.noStroke();
    this.layer.fill(0);
    this.layer.square(this.s.mouseX, this.s.mouseY, size * this.sizeOffset);
    this.s.image(this.layer, 0, 0);
  }
  clear() {
    this.layer.clear();
  }
}
