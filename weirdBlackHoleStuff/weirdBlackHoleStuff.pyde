import random as Rand
def setup():
    size(700,700)
    background(0)
    
r=60
def draw():
    global r
    #background(255)
    #noLoop()
    translate(width/2,height/2)
    rectMode(CENTER)
    #noStroke()
    #beginShape()
    i=0
    count=0
    cPallette = ["#855988","#6b4984", "#483475","#2b2f77", "#141852","#070b34"]        #choose anyone pallette or add your own!
    cPallette = ["#ec544c","#f37588", "#5c1c34","#4f53a2", "#bf6d9d","#3e2f63"]
    while i < 360:
        #r=100
        x= r* cos(radians(i))
        y=r* sin(radians(i))
        #point(x,y)
        push()
        translate(x,y)
        # n= noise(i*random(0,10))
        # angle= n* TWO_PI *4
        rotate(i)
        rectMode(CENTER)
        noStroke()
        Rand.shuffle(cPallette)
        fill(cPallette[0])
        s=random(1,2.3)
        # if r<100:
        #     scale(r*r/1000)
        # else:
        scale(r*r/(r**02))
        rect(0,0,50,50)          #change the dimensions of rectangle and circle to get different results
        circle(random(-5,5),random(-5,5),65)
        pop()
        i=i+2
        count=count+1
        # push()
        # fill(random(0,255),random(0,255),random(0,255))
        # translate(x,y)
        # rotate(i)
        # #vertex(x,y)
        # h=random(18,23)
        # rect(0,0,h,h)
        # i=i+1
        # pop()
        
    #endShape()
    r=r+8
    if r >width:
        noLoop()
        print("done")
        name= random(0,100)
        name= str(name)
        
        saveFrame(name+".png")
    #print(count)
