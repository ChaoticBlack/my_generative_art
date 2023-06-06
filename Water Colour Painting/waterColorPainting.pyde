#dd_library('pdf')
import random as Rand

#global img
def setup():
    size(1200,1000)
    Rand.seed(1)
    randomSeed(1)
    #print("hi")
    background(255)
    #global img
    #img=loadImage("Paper.jpg")
    #print(type(img))
    
        
            
class hexagon:
    def __init__(self,x,y,l,b,c):
        self.pos=PVector(x,y)
        #self.radius=r
        self.vertices=[]
        self.C=c
        # angle=TWO_PI/8
        # i=0
        # while i<TWO_PI:
        #     sx= self.pos.x + cos(i) * self.radius
        #     sy= self.pos.y + sin(i) * self.radius
        #     #sy=0*self.radius
        #     self.vertices.append((sx,sy))
        #     i=i+angle
        
        # v1X=x
        # v1Y=y
        for i in range(y,y+b,200):
            self.vertices.append((x,i))
            #self.vertices.append((x+l,i))
            
        for i in range(x,x+l,200):
            self.vertices.append((i,y+b))
            #self.vertices.append((i,y))
            
        for i in range(y+b,y,-200):
            self.vertices.append((x+l,i))
            
        for i in range(x+l,x,-200):
            self.vertices.append((i,y))
            
        #print(len(self.vertices))
        # v2X=v1X
        # v2Y=v1Y+b
        # self.vertices.append((v2X,v2Y))
        # v3X=v2X+l
        # v3Y=v2Y
        # self.vertices.append((v3X,v3Y))
        # v4X=v1X+l
        # v4Y=v1Y
        # self.vertices.append((v4X,v4Y))
            
        
    def displ(self):
        global img
        #colour = random(self.C-50,self.C+50)
        fill(self.C,12)
        #247,206,118
        noStroke()
        beginShape()
        #texture(img)
        for i in range(len(self.vertices)):
            vertex(self.vertices[i][0],self.vertices[i][1])
        endShape(CLOSE)
    
    def addVertices(self):
        #self.vertices=self.vertices
        newV=[]
        #Rand.seed(10)
        for i in range(len(self.vertices)):
            newV.append(self.vertices[i])
            if i == len(self.vertices)-1:
                t=0
            else:
                t=i+1
            d=dist(self.vertices[i][0],self.vertices[i][1],self.vertices[t][0],self.vertices[t][1])
            # print(l)
            u=Rand.gauss(0.5,0.2)
            rX= (1-u)*self.vertices[i][0]+u*self.vertices[t][0]         #random points on the polygon
            rY= (1-u)*self.vertices[i][1]+u*self.vertices[t][1]
            
           #  push()
           # # translate(self.pos.x,self.pos.y)
           #  strokeWeight(10)
           #  point(rX,rY)
           #  pop()
            l=Rand.gauss(d/2,0.2*d)                                 #random length
            push()
            translate(self.vertices[i][0],self.vertices[i][1])
            d1= dist(0,0,rX,rY)
            rotate(asin(-rY/d1))
            angle=Rand.gauss(90,180)                              #random angle
            #angle=random(0,360)
            #print(angle)
            fX= rX + l*cos(radians(angle))
            fY= rY + l*sin(radians(angle))
            pop()
            newV.append((fX,fY))
            #self.vertices.insert(i+1,(fX,fY))
        # #print(self.vertices)
        self.vertices=newV
        #print("drawList",self.vertices)


class Stars:
    def __init__(self):
        self.x=random(0,1200)
        self.y=random(0,1000)
        self.r=random(4,6)
        
    def displ(self):
        push()
        noFill()
        stroke(255,30)
        strokeWeight(5)
        circle(self.x,self.y,self.r)
        #circle(280,160,6)
        pop()


starList=[]
for i in range(40):
    starList.append(Stars())

count=0
megaCount=0
#obj=[]
# c1=color(247,206,118)
# c2=color(147,106,118)
# obj1=hexagon(450,450,170,c1)
# obj2=hexagon(300,350,170,c2)

def initObj():
    objObj=[]
    x=0
    y=0          #only increase y
    b=400
    #cArr = [color(245,176,126),color(236,141,120),color(203,77,35)]
    cArr= [color(12,15,76),color(93,151,181),color(37,102,153)]
    # 7,33,66
    #27,112,153
    for i in range(3):
        obj= hexagon(x,y,1200,b,cArr[i])
        objObj.append(obj)
        y=y+330
        b=b-80
        
    return objObj

def moon():
    push()
    beginShape();
    noStroke()
    fill(255,30)
    translate(288.0, 149.0)
    rotate(1.5*PI/2)
    vertex(0.0, 0.0);
    bezierVertex(0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
    bezierVertex(0.0, 0.0, 288.0-215.0, 149.0-114.0, 288.0-197.0, 149.0-171.0);
    bezierVertex(288.0-179.0, 149.0-228.0, 288.0-245.0, 149.0-254.0, 288.0-245.0, 149.0-254.0);
    bezierVertex(288.0-245.0, 149.0-254.0,288.0- 208.0, 149.0-207.0, 288.0-231.0, 149.0-176.0);
    bezierVertex(288.0-254.0, 149.0-145.0, 288.0-288.0, 149.0-152.0, 288.0-288.0, 149.0-152.0);
    endShape();
    pop()
        
circleCount=0        
objObj=initObj() 
big=0  
def draw():
    global objObj
    global count
    global circleCount
    global megaCount
    global starList
    global big
    #if count==0:
        # big = createGraphics(3000, 3000);  
        # big.beginDraw();                   # Start drawing to the PGraphics object 
        # big.background(255);               # Set the background
        
    #print("done")
    for i in range(len(objObj)):
        objObj[i].addVertices()
    count=count+1
    if count==15:           #15
        # obj1.displ()
        # obj2.displ()
        if circleCount%2==0:
            # push()
            # noFill()
            # stroke(255,20)
            # strokeWeight(5)
            # circle(450,260,6)
            # circle(280,160,6)
            # pop()
            for i in range(len(starList)):
                starList[i].displ()
            moon()
        circleCount=circleCount+1
        for i in range(len(objObj)):
            objObj[i].displ()
        count=0
        print(megaCount)
        saveFrame("C:/Users/User/Documents/Processing/waterColor/#####.tif")
        megaCount=megaCount+1
        # obj1=hexagon(450,450,170,c1)
        # obj2=hexagon(300,350,170,c2)
        objObj=initObj()
    if megaCount==40:
        noLoop()
        # big.endDraw();                      
        # big.save("big.tif");
        print("done")
        # saveFrame("newPC.png")
