import random as Rand

class Particles:
    def __init__ (self,a,b):
        # rand=Rand.randint(1,100)
        # if rand<0:
        #     self.pos = PVector(random(700),random(700))
        #     self.identity=100
        #     self.mass=100
        # else:
        # self.pos = PVector(random(700),random(700))
        #print(self.pos)
        self.pos =PVector(a,b)
        self.vel = PVector.random2D()
        self.acc= PVector.random2D()
        self.mass=1
        self.maxVel=2
        self.identity = Rand.randint(0,1)
        self.prevPos = [0,0]
        self.away=1
        
    
    def displ(self):
        #noStroke()
        # if self.identity==100:
        #     push()
        #     noFill()
        #     strokeWeight(1)
        #     stroke(255)
        #     circle(self.pos.x,self.pos.y,50)
        #     pop()
            # return
        if self.identity == 0:
            stroke(255,0,0,100)
        # elif self.identity == 1:
        #     stroke(0,0,255)
        else:
            stroke(0,0,255,100)
        strokeWeight(4) 
        if(dist(self.pos.x,self.pos.y,self.prevPos[0],self.prevPos[1])<10):   
            line(self.pos.x,self.pos.y,self.prevPos[0],self.prevPos[1])

        
    def update(self):
        # if self.identity == 100:
        #     return
        self.prevPos[0]=self.pos.x
        self.prevPos[1]=self.pos.y
        self.vel.add(self.acc)
        #self.vel= constrain(self.vel,3,10)
        self.vel.limit(self.maxVel)
        #self.vel.limit(self.maxSpeed)
        self.pos.add(self.vel)
        self.acc.mult(0)
        # if self.vel.mag()<self.minVel:
        #     self.vel=self.minVel
        
        
#otherP[i].identity!=self.identity and
    def attract(self, otherP):
        if self.identity==100:
            #F=blackHole(otherP)
            return 
        rad=60
        F = PVector() 
        total=0
        for i in range(len(otherP)):
            distance=dist(self.pos.x,self.pos.y,otherP[i].pos.x,otherP[i].pos.y)
            if otherP[i]!=self and  distance<rad and otherP[i].identity!=self.identity:
                temp= PVector.sub(otherP[i].pos,self.pos)
                d=temp.mag()
                if d<15:
                    continue
                G=150
                m=G*(otherP[i].mass*self.mass)/(d*d)
                temp.normalize()
                temp.mult(m)
                F.add(temp)
            
        return F
    
    
    def repel(self, otherP):
        rad=50
        F = PVector() 
        total=0
        for i in range(len(otherP)):
            distance=dist(self.pos.x,self.pos.y,otherP[i].pos.x,otherP[i].pos.y)
            if otherP[i]!=self and distance<rad and otherP[i].identity==self.identity:
                temp= PVector.sub(self.pos,otherP[i].pos)
                d=temp.mag()
                if d<15:
                    continue
                G=280
                m=G/(d*d)
                temp.normalize()
                temp.mult(m)
                F.add(temp)
            
        return F
    
    # def repel(self, otherP):
    #     rad=10
    #     F = PVector() 
    #     total=0
    #     for i in range(len(otherP)):
    #         d=dist(self.pos.x,self.pos.y,otherP[i].pos.x,otherP[i].pos.y)
    #         if otherP[i]==self and otherP[i].identity!=self.identity and d<rad:
    #             F.sub(otherP[i].vel)
    #             total=total+1
    #     if total>0:
    #         F.div(total)
    #         #self.vel=F
    #         F.sub(self.vel)
            
    #     return F
    
    def forces(self,otherP):
        if self.identity==100:
            return
        A = self.attract(otherP)
        R= self.repel(otherP)
        self.acc.add(A)
        self.acc.add(R)
   
        
   #USE BELOW FUNCTION IF YOU WANT POINT TO COME BACK ON CANVAS     
    # def edgeCheck(self):
    #     if self.pos.x > width:
    #         self.pos.x = 0
    #         #self.updatePrevPos()
    #     if self.pos.x < 0:
    #         self.pos.x = 700
    #         #self.updatePrevPos()
    #     if self.pos.y > height:
    #         self.pos.y = 0
    #         #self.updatePrevPos()
    #     if self.pos.y < 0:
    #         self.pos.y = 700
    #         #self.updatePrevPos()
            
            
#USE THIS FUNCT IF YOU WANT POINT TO GET LOST
    def edgeCheck(self):
        if self.pos.x > width or self.pos.x < 0 or self.pos.y < 0 or self.pos.y > height:
            self.away=0      
