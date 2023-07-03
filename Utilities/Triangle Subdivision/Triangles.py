class Triangle:
    def __init__(self,p1=[200,200],p2=[400,200],p3=[250,300], colour=[0,0,0]):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.colour=colour
        self.points = [self.p1,self.p2,self.p3]
        
    def drawTriangle(self):
        # line(self.p1[0],self.p1[1],self.p2[0],self.p2[1])
        # line(self.p2[0],self.p2[1],self.p3[0],self.p3[1])
        # line(self.p3[0],self.p3[1],self.p1[0],self.p1[1])
        (HSB, 360, 100, 100,255)
        noStroke()
        fill(self.colour[0],self.colour[1],self.colour[2])
        beginShape()
        vertex(self.p1[0],self.p1[1])
        vertex(self.p2[0],self.p2[1])
        vertex(self.p3[0],self.p3[1])
        endShape(CLOSE)
            
