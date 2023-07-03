def setup():
    size(1000,1000)
    background(0)
    
    
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
    stroke(255)
    noFill()
    bezier(x1,y1,x2,y2,x3,y3,x4,y4)


def perlinNoiseCircle(Cx,Cy,radius, n):
    stroke(255)
    strokeWeight(10)
    noFill()
    noiseMax=2
    noises=[]
    # noiseMax=radius/(radius/2)
    print(noiseMax)
    angle=0
    beginShape()
    while angle<TWO_PI:
        xoff = map(cos(angle),-1,1,0,noiseMax)
        yoff = map(sin(angle),-1,1,0,noiseMax)
        noises.append([xoff,yoff])
        r = map(noise(xoff,yoff),0,1,radius-10,radius+20)
        x= Cx+r*cos(angle)
        y=Cy+r*sin(angle)
        vertex(x,y)
        angle=angle+0.1
    endShape(CLOSE)
    while n-1:
        n=n-1
        angle=0
        radius=radius+40
        beginShape()
        i=0
        while angle<TWO_PI:
            i=i+1
            xoff = noises[i][0]
            yoff = noises[i][1]
            noises.append([xoff,yoff])
            r = map(noise(xoff,yoff),0,1,radius-10,radius+20)
            x= Cx+r*cos(angle)
            y=Cy+r*sin(angle)
            vertex(x,y)
            angle=angle+0.1
        endShape(CLOSE)

def drawRoughCircle(Cx,Cy,radius,roughness):
    n=8
    angle=TWO_PI/n
    points=[]
    stroke(255)
    noFill()
    beginShape()
    # vertex(Cx+radius,Cy)
    for i in range(n+n):
        theta = i*angle
        x=Cx+radius*cos(theta)
        y=Cy+radius*sin(theta)
        r=random(1,10)
        if r<2:
            x,y=rough(x,y,roughness)
        points.append([x,y])
        push()
        stroke(255,0,0)
        strokeWeight(5)
        point(x,y)
        pop()
        curveVertex(x,y)
    # curveVertex(points[-2][0],points[-2][1])
    # vertex(Cx,Cy+radius)
    endShape()
    # lastJoin = [points[-2],points[-1],points[1],points[2]]
    # beginShape()
    # for p in lastJoin:
    #     curveVertex(p[0],p[1])
    # endShape()
    
def drawRect(p1,p2,p3,p4):
        # fill(self.colour[0],self.colour[1],self.colour[2])
        # beginShape()
        # vertex(p1[0],p1[1])
        # vertex(p2[0],p2[1])
        # vertex(p4[0],p4[1])
        # vertex(p3[0],p3[1])
        # endShape(CLOSE)
        stroke(255)
        rough=20
        drawRoughLine(p1[0],p1[1],p2[0],p2[1],rough)
        drawRoughLine(p2[0],p2[1],p4[0],p4[1],rough)
        drawRoughLine(p3[0],p3[1],p4[0],p4[1],rough)
        drawRoughLine(p3[0],p3[1],p1[0],p1[1],rough)
   
            
def dashedLine(p1,p2):
    direction = [p2[0] - p1[0], p2[1] - p1[1]]
    # Calculate the length of the line segment
    leng = dist(p1[0], p1[1], p2[0], p2[1])
    # Normalize the direction vector
    direction_mag = dist(0, 0, direction[0], direction[1])
    direction = [direction[0] / direction_mag, direction[1] / direction_mag]
    # Define the dash length and gap length
    dash_length = 10
    gap_length = 10
    # Calculate the number of dash and gap segments
    num_segments = int(leng / (dash_length + gap_length))
    # Calculate the step size for each segment
    step = [direction[0] * (dash_length + gap_length), direction[1] * (dash_length + gap_length)]
    # Draw the dashed line
    current = p1
    for i in range(num_segments):
        # Draw the dash segment
        line(current[0], current[1], current[0] + direction[0] * dash_length, current[1] + direction[1] * dash_length)
        # Move to the next position
        current[0] += step[0]
        current[1] += step[1]
            
    
def draw():
    noLoop()
    background(0)
    x1=50
    y1=250
    x4=550
    y4=250
    roughness = 20
    # drawRoughLine(x1,y1,x4,y4,roughness)
    # perlinNoiseCircle(500,500,60,3)
    # drawRoughCircle(500,500,350,roughness)
    p1=[100,100]
    p2=[500,100]
    p3=[100,500]
    p4 =[500,500]
    drawRect(p1,p2,p3,p4)
    p1 = [0, 200]
    p2 = [500, 500]
    dashedLine(p1,p2)
    
    
    
    
