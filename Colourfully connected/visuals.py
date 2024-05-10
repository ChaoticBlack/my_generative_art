import random as rd
# lineColors = [[18,90,64],[34,93,75],[60,100,59],[52,92,38],[1,80,38]]
lineColors = [[25,75,55],[34,59,82],[82,62,39],[30,59,80],[43,90,72],[18,90,64],[34,93,75],[60,100,59],[52,92,38],[1,80,38]]
    
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
    colorMode(HSB,360,100,100)
    m=0.75 +random(-0.1,0.1)
    n=1-m
    x2=(m*x1+n*x4)//(m+n)
    y2=(m*y1+n*y4)//(m+n)
    x2,y2=rough(x2,y2,roughness)
    m=0.50 +random(-0.1,0.1)
    n=1-m
    x3=(m*x1+n*x4)//(m+n)
    y3=(m*y1+n*y4)//(m+n)
    x3,y3=rough(x3,y3,roughness)
    index=int(random(0,len(lineColors)))
    stroke(lineColors[index][0],lineColors[index][1],lineColors[index][2])
    # stroke(0)
    strokeWeight(random(5,10))
    noFill()
    bezier(x1,y1,x2,y2,x3,y3,x4,y4)


def drawRoughCircle(Cx,Cy,radius,roughness):
    n=5
    angle=TWO_PI/n
    points=[]
    stroke(0)
    noFill()
    beginShape()
    for i in range(n+2):
        theta = i*angle
        x=Cx+radius*cos(theta)
        y=Cy+radius*sin(theta)
        if random(1,10)<2:
            x,y=rough(x,y,roughness)
        points.append([x,y])
        push()
        stroke(255,0,0)
        strokeWeight(random(4,8))
        point(x,y)
        pop()
        curveVertex(x,y)
    curveVertex(points[-2][0],points[-2][1])
    endShape()


def concentricCircles(x,y,roughness):
    strokeWeight(8)  #randomize this
    stroke(random(0,255),random(0,255),random(0,255))
    noFill()
    numCircles = int(random(1,1))
    # print(numCircles)
    rad=80
    for i in range(numCircles):
        drawRoughCircle(x,y,rad,roughness)
        rad=rad-20
        
        
def perlinNoiseCircle(Cx,Cy,radius, n):
    colorMode(HSB,360,100,100)
    # [157, 29, 89]
    circleColors = [[163, 47, 78],[6, 29, 89],[157, 29, 89],[16, 43, 100],[199, 11, 93],[5, 48, 100],[47, 29, 89],[277,9,100],[40, 99, 99],[36, 66, 100],[9, 44, 100],[190, 28, 83]]
    # rd.shuffle(circleColors)
    index=int(random(0,len(circleColors)))
    strokeWeight(1)
    # stroke(0)
    isEdgeColorSame = random(0,10) 
    if isEdgeColorSame <8:
        stroke(circleColors[index][0],circleColors[index][1],circleColors[index][2])
    else:
        index=int(random(0,len(circleColors)))
        stroke(circleColors[index][0],circleColors[index][1],circleColors[index][2])
        
    fillInside =random(0,10)
    if fillInside<9.5:
        fill(circleColors[index][0],circleColors[index][1],circleColors[index][2])
    else:
        noFill()
        strokeWeight(5)
    
    # fill(random(0,255),random(0,255),random(0,255))
    if n==2:
        noiseMax=random(0.2,1.1)
    if n==1:
        noiseMax = random(0.000,0.01)
    noises=[]
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
    index=int(random(0,len(circleColors)))
    # stroke(0)
    isEdgeColorSame = random(0,10)
    if isEdgeColorSame <8:
        stroke(circleColors[index][0],circleColors[index][1],circleColors[index][2])
    else:
        index= (index+1)%len(circleColors)
        stroke(circleColors[index][0],circleColors[index][1],circleColors[index][2])
    
    fillInside =random(0,10)
    if fillInside<9.5:
        fill(circleColors[index][0],circleColors[index][1],circleColors[index][2])
    else:
        noFill()
        strokeWeight(5)
        
    while n-1:
        n=n-1
        # if n==0:
            #set as background colour
            # noFill()
        angle=0
        radius=radius-20
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
        
def dashedLine(p1,p2):
    colorMode(HSB,360,100,100)
    index=int(random(0,len(lineColors)))
    stroke(lineColors[index][0],lineColors[index][1],lineColors[index][2])
    strokeWeight(random(4,8))
    direction = [p2[0] - p1[0], p2[1] - p1[1]]
    # Calculate the length of the line segment
    leng = dist(p1[0], p1[1], p2[0], p2[1])
    # Normalize the direction vector
    direction_mag = dist(0, 0, direction[0], direction[1])
    direction = [direction[0] / direction_mag, direction[1] / direction_mag]
    # Define the dash length and gap length
    dash_length = random(1,12)
    gap_length = dash_length+ random(9,19)
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
 
