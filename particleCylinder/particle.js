class Particle {
  constructor(x,y,z) {
    min=0
    max=1
    min = Math.ceil(min);
    max = Math.floor(max);
    this.identity=Math.floor(Math.random() * (max - min + 1)) + min;    //identity decides the colour of the particle
    this.pos= createVector(x,y,z);    //position vector of the particle
    this.vel = p5.Vector.random3D();    //particle initially has a random velocity and acceleration vector
    this.acc = p5.Vector.random3D();
    this.maxVel = 0.4;    //velocity is limited to avoid dithering effect
    this.mass = 1;      //ignore
  }

  displ(){        //draws a sphere of radius 1 at the position vector of the particle with colour assigned as per the identity
    if (this.identity==0){
      //stroke(255,0,0,50)
      fill(255,0,0,19)

    }
    else{
      //stroke(0,0,255,50)
      fill(0,0,255,19)
    }
    //strokeWeight(2)
    noStroke()
    push()
    translate(this.pos.x,this.pos.y,this.pos.z)
    sphere(1)
    pop()
  }

  update(){     //changes the velocity and acceleration as per the laws of physics
    this.vel.add(this.acc)
    this.vel.limit(this.maxVel)
    this.pos.add(this.vel)
    this.acc.mult(0)
  }

  repel(otherP){      //particles in a given radius apply a repelling force on each other
    //if you want noticeable repulsion and randomness, set r=40, G=150
    var rad=540
    var F= createVector(0,0,0)
    //var total = 0
    for (var i=0; i< otherP.length;i++){
      //console.log(typeof otherP[i])
      var distance = dist(this.pos.x,this.pos.y,this.pos.z,otherP[i].pos.x,otherP[i].pos.y,otherP[i].pos.z)
      //var distance= PVector.dist(otherP[i], this.pos);
      //console.log(distance)
      if ( distance<rad){
        var temp = p5.Vector.sub(this.pos,otherP[i].pos)
        var d=temp.mag()
        //console.log(d)
        if (d<15){
          //console.log(d)
          continue
        }
        var G=1500

        var m = G/(d*d)
        temp.normalize()
        temp.mult(m)
        F = F.add(temp)
      }   
    }
    return (F)
  }
  forces(otherP){     //computes all the forces on a particle
    var R= this.repel(otherP)
    this.acc.add(R)

  }  

   edgeCheck(){     //checks whether particle is within the constraint of the canvas
   var constraint = 200
   if (this.pos.x>constraint){
    this.pos.x=- constraint
   } 
   if (this.pos.x<-constraint){
    this.pos.x= constraint
   } 
   if (this.pos.y>constraint){
    this.pos.y=- constraint
   } 
   if (this.pos.y<-constraint){
    this.pos.y= constraint
   } 
   if (this.pos.z>constraint){
    this.pos.z=- constraint
   } 
   if (this.pos.z<-constraint){
    this.pos.z= constraint
   } 
  }

}