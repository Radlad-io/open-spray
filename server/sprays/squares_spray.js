export default class Squares {
  constructor() {}
  spray(sk, dia) {
    if (sk.mouseIsPressed) {
      sk.fill(0);
    } else {
      sk.fill(255);
    }
    sk.square(sk.mouseX, sk.mouseY, dia);
  }
}
