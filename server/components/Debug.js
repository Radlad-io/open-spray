import { Pane } from "tweakpane";
import * as EssentialsPlugin from "@tweakpane/plugin-essentials";

export default class Debug {
  constructor() {
    this.environment = import.meta.env.MODE;
    this.active = window.location.hash === "#debug";

    if (this.active) {
      this.pane = new Pane();
      this.pane.registerPlugin(EssentialsPlugin);

      this.fps = this.pane.addBlade({
        view: "fpsgraph",
        label: "fpsgraph",
        lineCount: 2,
      });
    }
  }
}
