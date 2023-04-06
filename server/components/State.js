let instance = null;

export default class State {
  constructor() {
    if (instance !== null) {
      return instance;
    }
    instance = this;
    this.dev = import.meta.env.dev || false;
    this.setState();
  }

  setState() {
    this.r = {
      value: 0,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.g = {
      value: 255,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.b = {
      value: 255,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.a = {
      value: 1,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.color = {
      value: [this.r.get(), this.g.get(), this.b.get(), this.a.get()],
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.size = {
      value: 0.5,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.sprayIndex = {
      value: 0,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.layerIndex = {
      value: 0,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
  }
}
