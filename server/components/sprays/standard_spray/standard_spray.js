export default class Standard {
  constructor(s) {
    this.s = s;
    this.layer = s.createGraphics(window.innerWidth, window.innerWidth);
    this.contactDuration = 1;
    this.previousTouches = [];
  }
  // Runs once on preload
  preload() {}

  // Runs once on setup
  setup() {}

  // Runs on Draw call
  draw(size, color) {
    if (this.s.touches.length > 0) {
      // Increases
      this.layer.stroke(color, 5);
      if (this.contactDuration < 2) {
        this.contactDuration += 0.02;
      }

      this.s.touches.map((touch, index) => {
        if (this.previousTouches[touch.id] === undefined) {
          this.previousTouches[touch.id] = { ...touch };
        }

        // Cumulative distance moved
        const weight = Math.abs(
          touch.x -
            this.previousTouches[touch.id].x +
            touch.y -
            this.previousTouches[touch.id].y
        );

        // Calc stroke weight based distance moved, contact length and size factor
        this.layer.strokeWeight(weight * size * (this.contactDuration / 2));

        this.layer.line(
          touch.x,
          touch.y,
          this.previousTouches[touch.id].x,
          this.previousTouches[touch.id].y
        );
      });

      this.previousTouches = [];
      this.s.touches.map((touch) => {
        this.previousTouches.push({ ...touch });
      });
    }

    if (this.s.touches.length === 0) {
      this.previousTouches = [];
      this.contactDuration = 1;
    }

    this.s.image(this.layer, 0, 0);
  }

  clear() {
    this.layer.clear();
  }
}
