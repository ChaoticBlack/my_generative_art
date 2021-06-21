import uuid
import os
import random as Rand
def setup():
    size(1366, 760)
    background(0)
  
r =60
progress=15
megaCount = 0
def draw():
    global r
    global progress
    global megaCount
    numP=5000
    push()
    translate(width/2,height/2)
    x=0
    y=0
    r1=5
    r2=3
    npoint=5
    ang = TWO_PI/npoint
    Hang = ang/2.0
    beginShape()
    fill(168, 211, 255)
    noStroke()
    #choices = [0,PI/4,PI/2,PI/3]
    rotate(random(0,1)*TWO_PI*4 )
    for a in range(0,floor(TWO_PI),floor(ang)):
        sx=x+cos(a)*r2
        sy= y+sin(a)*r2
        vertex(sx,sy)
        sx = x + cos(a+Hang) * r1;
        sy = y + sin(a+Hang) * r1;
        vertex(sx,sy)
    endShape(CLOSE)
    angle = (TWO_PI)/float(numP)
    for i in range(numP):
        a = r*sin(angle*i)
        b= r*cos(angle*i)
        chance = int(random(0,100))
        if chance < 1:
                    stroke(0)
                    noStroke()
                    #fill(255)
                    push()
                    minC = 190
                    maxC=270
                    if a>0 and b>0:
                        m = map(a+b,0,height/2,minC,maxC)
                        #n = map(b,0,height/2,0,160)
                        colorMode(HSB,360,100,100,255)
                        fill(random(m-15,m+15),90,90)
                    elif a>0 and b<0:
                        m = map(a+abs(b),0,height/2,minC,maxC)
                        #n = map(b,-height/2,0,0,160)
                        colorMode(HSB,360,100,100,255)
                        fill(random(m-15,m+15),90,90)
                    elif a<0 and b<0:
                        m = map(abs(a)+abs(b),0,height/2,minC,maxC)
                        #n = map(b,-height/2,0,0,160)
                        colorMode(HSB,360,100,100,255)
                        fill(random(m-15,m+15),90,90)
                    elif a<0 and b>0:
                        m = map(abs(a)+b,0,height/2,minC,maxC)
                        #n = map(b,-height/2,0,0,160)
                        colorMode(HSB,360,100,100,255)
                        fill(random(m-15,m+15),90,90)
                    angle = random(0,1)*TWO_PI*4 
                    translate(a,b)
                    pp = floor(random(0,100))
                    if pp<2:
                        #print(pp)
                        h=random(10,45)
                        ellipse(0,0,h,h)
                    else:
                        rotate(angle)
                        h=random(10,45)
                        w=random(10,45)
                        ellipse(0,0,h,w)
                    pop()
    if progress>50:
        progress=50
    r = r+progress
    #print(progress)
    progress = progress +3
    pop() 
    if r > width+200:
        #noLoop()
        # loadPixels()
        # for i in range(width*height):
        #     c = random(-30,30)
        #     if pixels[i]!=- 16777216:
        #         r= red(pixels[i])+c
        #         g= green(pixels[i])+c
        #         b= blue(pixels[i])+c
        #         newC = color(r,g,b)
        #         pixels[i]=newC
        # updatePixels()
        filename = str(uuid.uuid4())
        saveFrame(str(megaCount)+"_"+filename+".png")
        #print(filename)
        print("done!")
        megaCount = megaCount+1
        background(0)
        r =60
        progress=15  
    if megaCount==10:
        
       noLoop()     
       dir="/home/raju/sketchbook/ego_death_replica/"
       file = sorted(os.listdir(dir))
       for i in range(len(file)-2):
           #print(i)
           img = loadImage(dir+file[i])
           tint(255,90)
           image(img,0,0)
       saveFrame("output-####.png")
