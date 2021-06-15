def setup():
    size(700,700)
    background(0)
    

def draw():

    background(0)
    noLoop()
    rectMode(CENTER)
    #noFill()
    #stroke(0)
    noStroke()
    h=8
    for x in range(0-h,width+h,h):
        for y in range(0-h,height+h,h):
            r=random(0,100)
            fill(random(0,250),random(0,100),random(0,100))
            if r<30:
                push()
                rectMode(CENTER)
                xoff=0.0005*x
                yoff=0.0005*y
                n=noise(xoff,yoff)
                angle=n*2*PI
                translate(x,y)
                rotate(PI/4)
                rect(0,0,h,h)
                pop()
            else:
                rect(x,y,h,h)
                
