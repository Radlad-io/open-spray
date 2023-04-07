export default class OldSchool {
  constructor(s) {
    this.s = s;
    this.name = "Old School";
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
    const [r, g, b, a] = color;

    // TODO: Im not sure this is actually the spread
    if (this.s.mouseIsPressed) {
      let spread = this.layer.random(2, 10);
      for (var i = 0; i < 50; i++) {
        var d =
          this.s.dist(
            this.s.pmouseX,
            this.s.pmouseY,
            this.s.mouseX,
            this.s.mouseY
          ) * 0.7;
        let x = this.s.random(-d, d);
        let y = this.s.random(-d, d);
        this.layer.fill(
          [
            Math.floor(r * this.s.random(0.9, 1.15)),
            Math.floor(g * this.s.random(0.9, 1.15)),
            Math.floor(b * this.s.random(0.9, 1.15)),
            a,
          ],
          10
        );
        this.layer.ellipse(
          this.s.mouseX + x,
          this.s.mouseY + y,
          this.s.random(10, spread)
        );
        spread *= 0.9;
      }
    }
    this.s.image(this.layer, 0, 0);
  }

  clear() {
    this.layer.clear();
  }
}
