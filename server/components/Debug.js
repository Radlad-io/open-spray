import { Pane } from "tweakpane";
import * as EssentialsPlugin from "@tweakpane/plugin-essentials";
import State from "./State";
import Experience from "./Experience";

export default class Debug {
  constructor() {
    this.experience = new Experience();
    this.state = new State();
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

      this.addColorControls(
        this.state.r.get(),
        this.state.g.get(),
        this.state.b.get(),
        this.state.a.get()
      );
    }
  }
  addColorControls(r, g, b, a) {
    this.PARAMS = {
      key: {
        r,
        g,
        b,
        a,
      },
    };
    const colorControl = this.pane
      .addInput(this.PARAMS, "key", {
        picker: "inline",
        color: { alpha: true },
        expanded: true,
      })
      .on("change", (e) => {
        this.state.r.set(Math.floor(e.value.r));
        this.state.g.set(Math.floor(e.value.g));
        this.state.b.set(Math.floor(e.value.b));
        this.state.a.set(e.value.a);
        this.state.color.set([
          this.state.r.get(),
          this.state.g.get(),
          this.state.b.get(),
          this.state.a.get(),
        ]);

        // console.log(
        //   this.state.r.get(),
        //   this.state.g.get(),
        //   this.state.b.get(),
        //   this.state.a.get()
        // );

        console.log(this.state.color.get());
      });
  }
}
