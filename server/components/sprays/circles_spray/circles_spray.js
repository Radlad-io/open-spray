export default class Circles {
  constructor(s, size) {
    this.s = s;
    this.size = size;
    this.layer = s.createGraphics(window.innerWidth, window.innerWidth);
    this.mask = s.createGraphics(window.innerWidth, window.innerWidth);
  }
  preload() {}
  setup() {}
  spray(size, color) {
    if (this.s.touches.length > 0) {
      this.s.touches.map((touch) => {
        this.layer.noStroke();
        this.layer.fill(255, 1);
        this.layer.ellipse(touch.x, touch.y, size, size);

        this.mask.fill(color);
        this.mask.noStroke();
        this.mask.ellipse(touch.x, touch.y, size, size);
      });
    }
    this.s.image(this.layer, 0, 0);
    this.s.image(this.mask, 0, 0);
  }

  clear() {
    this.layer.clear();
    this.mask.clear();
  }
}
