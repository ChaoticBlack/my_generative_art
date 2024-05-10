
class Rectangle:
    def __init__(self,p1=[100,100],p2=[500,100],p3=[100,500],p4 =[500,500], colour = [0,0,0]):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.points = [self.p1,self.p2,self.p3,self.p4]
        self.oppositeLines1 = [[self.p1,self.p2],[self.p3,self.p4]]
        self.oppositeLines2 = [[self.p3,self.p1],[self.p2,self.p4]]
        self.oppositeLines = [self.oppositeLines1,self.oppositeLines2]
        self.colour=colour
        # print(self.oppositeLines[0])
        
    def drawRect(self):
        colorMode(HSB,360,100,100)
        fill(self.colour[0],self.colour[1],self.colour[2])
        # fill(random(0,255),random(0,255),random(0,255))
        # noFill()
        beginShape()
        noStroke()
        vertex(self.p1[0],self.p1[1])
        vertex(self.p2[0],self.p2[1])
        vertex(self.p4[0],self.p4[1])
        vertex(self.p3[0],self.p3[1])
        endShape(CLOSE)
            
    def roughRect(self):
        # rough= random(18,24)
        rough= random(25,38)
        drawRoughLine(self.p1[0],self.p1[1],self.p2[0],self.p2[1],rough)
        drawRoughLine(self.p2[0],self.p2[1],self.p4[0],self.p4[1],rough)
        drawRoughLine(self.p3[0],self.p3[1],self.p4[0],self.p4[1],rough)
        drawRoughLine(self.p3[0],self.p3[1],self.p1[0],self.p1[1],rough)
        
                        
def rough(center_x, center_y, radius):
    # Generate random angle in radians
    angle = random(0, TWO_PI)
    # circle(center_x,center_y,radius)
    # Generate random radius within the circle's radius
    random_radius = sqrt(random(0, 1)) * radius

    # Calculate coordinates of the random point
    x = center_x + random_radius * cos(angle)
    y = center_y + random_radius * sin(angle)

    return x, y


def drawRoughLine(x1,y1,x4,y4,roughness):
    m=0.75 
    n=1-m
    x2=(m*x1+n*x4)//(m+n)
    y2=(m*y1+n*y4)//(m+n)
    x2,y2=rough(x2,y2,roughness)
    m=0.50 
    n=1-m
    x3=(m*x1+n*x4)//(m+n)
    y3=(m*y1+n*y4)//(m+n)
    x3,y3=rough(x3,y3,roughness)
    # stroke(255)
    noFill()
    stroke(0)
    strokeWeight(9)
    # fill(0,0,0)
    bezier(x1,y1,x2,y2,x3,y3,x4,y4)
