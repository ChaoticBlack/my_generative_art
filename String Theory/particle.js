
class Particle {
  constructor() {
    this.pos = createVector(random(width), random(height));
    this.vel = createVector(0, 0);
    this.acc = createVector(0, 0);
    this.maxspeed = 4;
    // var m = map(this.pos.x, 0,width,200,240)
    // this.colour = random(m-25,m+25)
    this.prevPos = this.pos.copy();
  }

  update() {
    this.vel.add(this.acc);
    this.vel.limit(this.maxspeed);
    this.pos.add(this.vel);
    this.acc.mult(0);
  }

  follow(vectors) {
    var x = floor(this.pos.x / scl);
    var y = floor(this.pos.y / scl);
    var index = x + y * cols;
    var force = vectors[index];
    this.applyForce(force);
  }

  applyForce(force) {
    this.acc.add(force);
  }

  show() {
  	push();
  	colorMode(HSB, 360, 100, 100,255);
    let colours = this.colorChoosing(this.pos.x,this.pos.y)
  	//var m = map(this.pos.y, 0,height,160,240)
  	//var h = random(m-10,m+10)
    stroke(colours[0],colours[1],colours[2],10);
    //stroke(255,10)
    strokeWeight(1);
    line(this.pos.x, this.pos.y, this.prevPos.x, this.prevPos.y);
    this.updatePrev();
    pop();
  }

  updatePrev() {
    this.prevPos.x = this.pos.x;
    this.prevPos.y = this.pos.y;
  }

  edges() {
    if (this.pos.x > width) {
      this.pos.x = 0;
      this.updatePrev();
    }
    if (this.pos.x < 0) {
      this.pos.x = width;
      this.updatePrev();
    }
    if (this.pos.y > height) {
      this.pos.y = 0;
      this.updatePrev();
    }
    if (this.pos.y < 0) {
      this.pos.y = height;
      this.updatePrev();
    }

  }
  colorChoosing(xCurr, yCurr) {
  let anchors = [[0, 0], [width, 0], [width / 2, height / 2], [0, height], [width, height]];
  let distances = [];
  let minD = 999999999999999;
  let maxD = -1;

  for (let i = 0; i < anchors.length; i++) {
    let d = dist(xCurr, yCurr, anchors[i][0], anchors[i][1]);
    distances.push(d);

    if (minD > d) {
      minD = d;
    }

    if (maxD < d) {
      maxD = d;
    }
  }

  // let minD = Math.min(distances)
  // let maxD = Math.max(distances)

  let adjDist = distances.map((x) => x - minD);
  let distRange = maxD - minD;
  let wDist = adjDist.map((x) => x / distRange);
  let sumDist = wDist.reduce((a, b) => a + b, 0);
  let nwDist = wDist.map((x) => x / sumDist);
  let cumulationList = [];
  let maxProb = 0;
  let cumulation = 0;
  // let colorArr = [[217, 77, 100], [265, 76, 93], [334, 100, 100], [19, 97, 98], [44, 96, 100]];   //1
  // let colorArr = [[278, 33, 100],[274, 51, 100],[273, 65, 87],[272, 77, 75],[270, 84, 60]];       //2
  // let colorArr = [[50, 100, 100],[47, 100, 99],[209, 100, 62],[217, 100, 42],[212, 100, 53]]    //good
  // let colorArr = [[12, 68, 93],[214, 52, 50],[202, 30, 85],[182, 11, 99],[218, 37, 25]]    //3
  // let colorArr = [[165, 100, 50],[137, 71, 58],[81, 87, 73],[65, 100, 82],[60, 87, 94]]    //4
  // let colorArr = [[176, 100, 66],[176, 64, 84],[56, 87, 99],[47, 91, 96],[29, 100, 91]]    //5
  // let colorArr = [[209, 36, 100],[208, 26, 100],[338, 31, 100],[337, 22, 100],[278, 18, 86]]   //6
  // let colorArr = [[358, 65, 100],[44, 77, 100],[83, 81, 79],[203, 87, 77],[265, 48, 58]]   //7
  // let colorArr = [[300, 16, 100],[275, 22, 100],[255, 29, 100],[233, 28, 100],[221, 27, 100]]    //8
  let colorArr = [[178, 96, 75],[178, 70, 80],[179, 52, 85],[184, 35, 94],[174, 23, 100]]    //9
  let comboList = [];
  for (let i = 0; i < nwDist.length; i++) {
    comboList.push([nwDist[i], colorArr[i]]);
  }

  comboList.sort((a, b) => a[0] - b[0]);

  for (let i = 0; i < comboList.length; i++) {
    cumulation += comboList[i][0];
    cumulationList.push(cumulation);
  }

  let r = random(0, 1);
  let index = -1;

  for (let i = 0; i < cumulationList.length; i++) {
    if (cumulationList[i] > r) {
      index = i;
      break;
    }
  }

  return comboList[index][1];
}
}

