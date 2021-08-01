import random as Rand
w=0
part=0
def setup():    
    global w
    size(1000,700)
    w=width+16
   # dx=(TWO_PI/period)*xspacing
    #print(w/xspacing)
    #yvalues= [None for _ in range(w/xspacing)]
    #yvalues.append(w/xspacing)
    background(0)
    
class Wave:
    def __init__ (self):
        global w
        global part
        w=1500+16
        self.xspacing = 1
        self.theta=-100
        self.amplitude=random(70,150)
        self.period=random(500,640)
        self.dx=(TWO_PI/self.period)*self.xspacing
        self.yvalues= [None for _ in range(w/self.xspacing)]
        self.ypos = 900- part
        part = part+100
        #self.ypos= random(self.ypos-800,self.ypos+800)
        # colourArr = ["#003B00","#008F11","#00FF41"]
        # self.colour = (Rand.choice(colourArr))
        # self.colour = color(random(150,200),random(5,25),random(5,25))

    def calcWave(self):
        self.theta=self.theta+random(0,1)
        x=self.theta
        for i in range(len(self.yvalues)):
            self.yvalues[i]=sin(x)*self.amplitude
            x=x+self.dx
     
    def renderWave(self):
         
         colorMode(HSB, 360, 100, 100, 1.0)
        #self.colour= color(m,90,90)
         for x in range(len(self.yvalues)):
             push()
             #200,268
             h = map(self.ypos+self.yvalues[x],0,1200,200,268)
             s = map(self.ypos+self.yvalues[x],0,1200,50,90)
            # translate(x*self.xspacing,self.ypos+self.yvalues[x])
             rotate(PI/6)

             #fill(m,90,90)
             stroke(h,s,90)

             #noStroke()

             #point(x*self.xspacing,self.ypos+self.yvalues[x])
             # ellipse(x*self.xspacing,self.ypos+self.yvalues[x],4,4)
             # ellipse(x*self.xspacing,self.ypos+self.yvalues[x]-40,4,4)
             for i in range(width):
                point(x*self.xspacing,self.ypos+self.yvalues[x]-i)
             #point(x*self.xspacing,self.ypos+self.yvalues[x]-40)
             pop()   


obj=[]
for i in range(18):
    obj.append(Wave())

def draw():
    global obj
    noLoop()
    background(0,33,200)
    for i in range(len(obj)):
        obj[i].calcWave()
        #print(len(yvalues))
        obj[i].renderWave()
    print("done")    
    #delay(40)

    save("output.png")
    # print(obj.amplitude)
    # print(obj.period)
    
    
