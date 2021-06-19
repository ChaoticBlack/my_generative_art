//Shivam Rajput
//16/6/2021


var upper=120
var lower=-120
var step= 40
var count=0
var angle =0
var objList = new Array()

function setup() {
  createCanvas(900, 800,WEBGL);
  background(0)
  for (var i=lower;i<upper;i=i+step){
    for (var j=lower;j<upper;j=j+step){
      for (var k=lower;k<upper;k=k+step){
        objList.push(new Particle(i,j,k))
      }
    }
  }
}

function draw() {
  count=count+1
  if (count==1500){       //if you want more iterations, increase the value of count
    noLoop()
    console.log("done")
    save("final.png")
    //saveCanvas("myCanvas")
  }
  stroke(255)
  //rotateX(angle)
  rotateY(angle)        //rotating along Y to give it the cylindical look. Play around with other axes to get varied shapes
  //rotateY by PI/4 to get cube
  //rotateZ(angle)
  for (var i =0; i < objList.length;i++){
    //objList[i].displ()
    objList[i].forces(objList)
    objList[i].update()
    objList[i].edgeCheck()
    objList[i].displ()
    //console.log(i)
  }
  angle=angle+0.009
}
