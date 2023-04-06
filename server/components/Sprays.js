import State from "./State";
import Circles from "./sprays/circles_spray/circles_spray";
import Squares from "./sprays/squares_spray/squares_spray";
import Standard from "./sprays/standard_spray/standard_spray";
import Brownian from "./sprays/brownian_spray/brownian_spray";

export default class Sprays {
  constructor(s) {
    this.s = s;
    this.state = new State();
    this.index = this.state.sprayIndex.get();
    console.log(this.index);
    this.sprayList = [
      new Circles(this.s),
      new Squares(this.s),
      new Standard(this.s),
      new Brownian(this.s),
    ];

    this.spray;
    this.setSpray(this.index);
    console.log(this.spray);
  }

  getSpray(index) {
    return this.sprayList[index];
  }

  setSpray(index) {
    this.spray = this.sprayList[index];
  }
}
