#!/usr/bin/node

// class rectangle. instance rotate, double, print.

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let temp = '';
      for (let j = 0; j < this.width; j++) {
        temp += 'X';
      }
      console.log(temp);
    }
  }

  rotate () {
    const newHeight = this.width;
    const newWidth = this.height;
    this.height = newHeight;
    this.width = newWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
