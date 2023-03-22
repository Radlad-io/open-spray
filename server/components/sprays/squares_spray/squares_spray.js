export default class Squares {
  constructor(s, size) {
    this.s = s;
    this.size = size;
  }
  preload() {}
  setup() {}
  spray(size, color) {
    if (this.s.mouseIsPressed) {
      this.s.fill(0);
    } else {
      this.s.fill(255);
    }
    this.s.square(this.s.mouseX, this.s.mouseY, size);
  }
}
