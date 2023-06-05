class boids:
    def __init__ (self):
        # print(":hi")
        self.position = PVector(random(width),random(height))
        # self.position = PVector(width/2,height/2)
        self.velocity = PVector.random2D()
        self.velocity.setMag(random(0.2,0.4))
        self.accel = PVector.random2D()
        # self.accel.setMag(random(0.002,0.005))
        self.locality = 50
        self.maxForce = 1
        self.maxSpeed = 5
        self.trail=[]
        self.r= random(0,255)
        self.g=random(0,255)
        self.b=random(0,255)
        
    def align(self, flock):
        avg = PVector(0,0)
        count=0
        for i in flock:
            d = dist(self.position.x,self.position.y,i.position.x,i.position.y)
            if(self!=i and d<=self.locality):
                avg.add(i.velocity)
                count=count+1
        if count!=0:    
            avg.div(count)
            avg.setMag(self.maxSpeed)
            avg.sub(self.velocity)
            avg.limit(self.maxForce)
        return avg

    def cohesion(self, flock):
        avg = PVector(0,0)
        count=0
        for i in flock:
            d = dist(self.position.x,self.position.y,i.position.x,i.position.y)
            if(self!=i and d<=self.locality):
                avg.add(i.position)
                count=count+1
        if count!=0:    
            avg.div(count)
            avg.sub(self.position)
            avg.setMag(self.maxSpeed)
            avg.sub(self.velocity)
            avg.limit(self.maxForce)
        return avg
        
        

    def separation(self, flock):
        #print("HI")
        avg = PVector(0,0)
        count=0
        for i in flock:
            d = dist(self.position.x,self.position.y,i.position.x,i.position.y)
            if(self!=i and d<=self.locality and d!=0):
                # diff=PVector(0,0)
                diff = PVector.sub(self.position,i.position)
                diff.div(d*d)
                avg.add(diff)
                count=count+1
        if count!=0:    
            avg.div(count)
            avg.setMag(self.maxSpeed)
            # avg.sub(self.position)
            avg.sub(self.velocity)
            avg.limit(self.maxForce)
        return avg
        
            
    def culmination(self,flock):
        # print("hi")
        alignment = self.align(flock)
        cohes = self.cohesion(flock)
        sep = self.separation(flock)
        self.accel.add(alignment)
        self.accel.add(cohes)
        self.accel.add(sep)
    
    def edges(self):
        
        # if(self.position.x>width or self.position.x<0 or self.position.y<0 or self.position.y>height):
        #     # self.position.x=0
        #     self.accel.mult(-1)
        #     self.velocity.mult(-1)
        if(self.position.x>width):
            self.position.x=0
        if(self.position.x<0):
            self.position.x=width
            # self.accel.mult(-1)
            # self.velocity.mult(-1)
        if(self.position.y>height):
            self.position.y=0
            # self.accel.mult(-1)
            # self.velocity.mult(-1)
        if(self.position.y<0):
            self.position.y=height
            # self.accel.mult(-1)
            # self.velocity.mult(-1)
        # # print("hi")
    
    def update(self):
        # print("hi")
        self.position.add(self.velocity)
        self.velocity.add(self.accel)
        self.velocity.limit(self.maxSpeed)
        self.accel.mult(0)
    
    def show(self):
        strokeWeight(5)
        stroke(255)
        temp = [self.position.x,self.position.y]
        self.trail.append(temp)
        if(len(self.trail)==13):
            self.trail=self.trail[1:]
        a=30
        w=2
        for i in self.trail:
            stroke(self.r,self.g,self.b,a)
            strokeWeight(w)
            a=a+4
            w=w+1
            point(i[0],i[1])
