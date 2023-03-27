let instance = null;

export default class State {
  constructor() {
    if (instance !== null) {
      return instance;
    }

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
      value: 0.75,
      get() {
        return this.value;
      },
      set(value) {
        this.value = value;
      },
    };
    this.color = {
      value: [this.r, this.g, this.b, this.a],
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
  }
}
