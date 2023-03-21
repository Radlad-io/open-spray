export default class Circles {
  constructor() {}
  spray(sk, dia) {
    if (sk.mouseIsPressed) {
      sk.fill(0);
    } else {
      sk.fill(255);
    }
    sk.ellipse(sk.mouseX, sk.mouseY, dia, dia);
  }
}
