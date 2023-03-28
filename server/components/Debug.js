import { Pane } from "tweakpane";
import * as EssentialsPlugin from "@tweakpane/plugin-essentials";
import Experience from "./Experience";

export default class Debug {
  constructor() {
    this.experience = new Experience();
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

      this.clearBtn = this.pane.addButton({
        title: "Clear",
        label: "Img Buffer", // optional
      });

      this.clearBtn.on("click", () => {
        this.experience.clear();
      });
    }
  }
}
