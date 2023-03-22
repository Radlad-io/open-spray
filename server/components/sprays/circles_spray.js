export default class Circles {
  constructor(s, size) {
    this.s = s;
    this.size = size;
  }
  preload() {}
  setup() {}
  spray(size, color) {
    // this.s.clear();
    // this.s.fill(color);
    this.s.stroke(color);
    // console.log(this.s.accelerationX);
    if (this.s.touches.length > 0) {
      this.s.touches.map((touch) => {
        this.s.ellipse(touch.x, touch.y, size, size);
      });
    }
  }
}
