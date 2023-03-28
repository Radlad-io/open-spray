import Toastify from "toastify-js";

let instance = null;

export default class Notification {
  constructor() {
    if (instance === null) {
      instance = this;
    }

    instance = this;
    this.defaultDuration = 3000;
  }

  showToast(Message) {
    Toastify({
      text: Message,
      duration: this.defaultDuration,
      newWindow: true,
      close: false,
      gravity: "bottom",
      position: "left",
      stopOnFocus: true,
    }).showToast();
  }
}
