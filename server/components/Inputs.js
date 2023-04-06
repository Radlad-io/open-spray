import State from "./State";

export default class Inputs {
  constructor() {
    this.state = new State();
    this.setKeyboardInputs();
  }

  setKeyboardInputs() {
    addEventListener("keydown", (event) => {
      switch (event.key) {
        case "ArrowUp":
          if (this.state.size.get() < 0.95) {
            this.state.size.set(this.state.size.get() + 0.05);
            console.log(this.state.size.get());
          }
          break;
        case "ArrowDown":
          if (this.state.size.get() > 0.075) {
            this.state.size.set(this.state.size.get() - 0.05);
            console.log(this.state.size.get());
          }
          break;
        case "1":
          this.state.sprayIndex.set(0);
          break;
        case "2":
          this.state.sprayIndex.set(1);
          break;
        case "3":
          this.state.sprayIndex.set(2);
          break;
        case "4":
          this.state.sprayIndex.set(3);
          break;
        case "5":
          this.state.sprayIndex.set(4);
          break;
        case "6":
          this.state.sprayIndex.set(5);
          break;
        case "7":
          this.state.sprayIndex.set(6);
          break;
        case "8":
          this.state.sprayIndex.set(7);
          break;
        case "9":
          this.state.sprayIndex.set(8);
          break;
        case "u":
          console.log(layers);
          console.log(layers[layerIndex]);
          break;
      }
    });
  }
}
