import random as rd
import math
# import circle
xLeft,xRight,yTop,yBot, res, numRows, numCols, grid =0,0,0,0,0,0,0,0
startingPoints = []
spaceGrid = []
dsep=54
spaceCellSize = dsep
percent = 14
borderXL,borderXR,borderYT,borderYB = 0,0,0,0
# backgroundCol = [9,12,92]   #pinkish
backgroundCol = [135,34,60]    #mintish
def setup():
    size(1900,1900)
    colorMode(HSB, 360, 100, 100,255)
    smooth(8)
    background(backgroundCol[0],backgroundCol[1],backgroundCol[2])
    global xLeft,xRight,yTop,yBot,res,numRows, numCols, grid, startingPoints, spaceCellSize,spaceGrid, borderXL,borderXR,borderYT,borderYB,percent
    #####INITIAL VALUES
    xLeft = int(width*-0.1)
    xRight = int(width*1.1)
    yTop = int(height*-0.1)
    yBot = int(height*1.1)
    res = int(width*0.005)
    
    ### Frame
    borderXL = int(width/percent)
    borderYT = int(height/percent)
    borderXR = width - int(width/percent)
    borderYB = height - int(height/percent)

    seedNo = int(random(3,10000))
    print("seed = ", seedNo)
    noiseSeed(seedNo)
    # noiseDetail(24)
    
    ###DEFINE VECTOR GRID
    numRows = int((yBot-yTop)/res)
    numCols = int((xRight-xLeft)/res)
    defaultAngle = PI*0.25
    grid = [[0 for _ in range(numCols)] for _ in range(numRows)]

    ###### ASSIGN ANGLES
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            scaledX=i*0.005
            scaledY=j*0.005
            angle=noise(scaledX,scaledY)*TWO_PI
            grid[i][j]=angle
        
    ##### GENERATE STARTING POINTS
    for i in range(xLeft,xRight,25):
        for j in range(yTop,yBot,25):
            startingPoints.append([i,j])
            
    ###DEFINE SPACE GRID
    spaceRows = int((yBot-yTop)/spaceCellSize)
    spaceCols = int((xRight-xLeft)/spaceCellSize)
    spaceGrid = [[[] for _ in range(spaceCols)] for _ in range(spaceRows)]
    # print(spaceGrid)
    
    
    #UNCOMMENT BELOW CODE TO DRAW VECTOR FIELD
    # noFill()
    # stroke(255) 
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         # print(grid[i][j])
    #         push()
    #         stroke(255)
    #         strokeWeight(0.51)
    #         translate(i*res,j*res)
    #         rotate(-grid[i][j])
    #         push()
    #         strokeWeight(1)
    #         point(0,0)
    #         pop()
    #         line(0,0,0,res)
    #         pop()

    print("setup done")

    
    
def colorChoosing(xCurr,yCurr):
    global xLeft,xRight,yTop,yBot
    anchors = [[xLeft,yTop],[xRight,yTop],[width/2,height/2],[xLeft,yBot],[xRight,yBot]]
    distances = []
    minD = 999999999999999
    maxD = -1
    for i in range(len(anchors)):
        d = dist(xCurr,yCurr,anchors[i][0],anchors[i][1])
        distances.append(d)
        if minD>d:
            minD=d
        if maxD<d:
            maxD=d
    adjDist = [x - minD for x in distances]
    distRange = maxD-minD
    wDist = [x / distRange for x in adjDist]
    sumDist = sum(wDist)
    nwDist = [x / sumDist for x in wDist]
    cumulationList=[]
    maxProb = 0
    cumulation=0
    # colorArr = [[217, 77, 100],[265, 76, 93],[334, 100, 100],[19, 97, 98],[44, 96, 100]]
    # colorArr = [[278, 33, 100],[274, 51, 100],[273, 65, 87],[272, 77, 75],[270, 84, 60]]
    # colorArr = [[18, 100, 100],[210, 74, 90],[85, 59, 83],[42, 100, 100],[334, 66, 100]]
    colorArr = [[239, 97, 37],[201, 100, 71],[190, 100, 85],[190, 19, 97],[189, 40, 94]]
    comboList = zip(nwDist,colorArr)
    comboList.sort(key = lambda x: x[0])
    for i in comboList:
        cumulation=cumulation+i[0]
        cumulationList.append(cumulation)
    r= random(0,1)
    index=-1
    for i in range(len(cumulationList)):
        if cumulationList[i]>r:
            index=i
            break
    return comboList[index][1]
    

def drawCircle(c,r,t,col):
    global borderXL,borderXR,borderYT,borderYB
    strokeWeight(0.9)
    lastR = r+t
    flag = False
    while r<= lastR:
        angle = 0
        while angle<=360:
            stroke(col[0],col[1],col[2])
            rareColor = int(random(0,4500))
            if rareColor == 4:
                numPoints = int(random(80,140))
                curr = 0
                flag=True
            if flag:
                # stroke(135,34,60)   #background colour
                stroke(backgroundCol[0],backgroundCol[1],backgroundCol[2])
                curr+=1
                if curr == numPoints:
                    flag = False
            x = c[0] + r*cos(radians(angle))
            y = c[1] + r*sin(radians(angle))
            if x>borderXL and x<borderXR and y >borderYT and y< borderYB:
                point(x,y)
            angle+=0.5
        r+=1
        
       
        
def checkProximity( xCurr, yCurr):
    # dsep = 0.5
    global spaceCellSize, spaceGrid,dsep
    ##calculate index of current point
    xIndex = int(xCurr // spaceCellSize)
    yIndex = int(yCurr // spaceCellSize)
    #search in this cell of the spaceGrid   (add code to seach neighbouring grids also)
    for points in spaceGrid[xIndex][yIndex]:
        if(dist(xCurr,yCurr, points[0],points[1])<dsep):
            return False
    if xIndex-1>0:
        for points in spaceGrid[xIndex-1][yIndex]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if yIndex-1>0:
        for points in spaceGrid[xIndex][yIndex-1]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if xIndex+1<len(spaceGrid):
        for points in spaceGrid[xIndex+1][yIndex]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if yIndex+1<len(spaceGrid[0]):
        for points in spaceGrid[xIndex][yIndex+1]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if yIndex+1<len(spaceGrid[0]) and xIndex+1<len(spaceGrid):
        for points in spaceGrid[xIndex+1][yIndex+1]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if yIndex+1<len(spaceGrid[0]) and xIndex-1>0:
        for points in spaceGrid[xIndex-1][yIndex+1]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if yIndex-1>0 and xIndex-1>0:
        for points in spaceGrid[xIndex-1][yIndex-1]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    if yIndex-1>0 and xIndex+1<len(spaceGrid):
        for points in spaceGrid[xIndex+1][yIndex-1]:
            if(dist(xCurr,yCurr, points[0],points[1])<dsep):
                return False
    
    
    
        
    spaceGrid[xIndex][yIndex].append([xCurr,yCurr])
    return True
        

count=0

def draw():
    # noLoop()
    global xLeft,xRight,yTop,yBot,res,numRows, numCols, grid, count, xPos, yPos, startingPoints,dsep
    flag = False
    if(len(startingPoints)%1000==0):
        print(len(startingPoints))
    # print(count)
    if len(startingPoints)==0:
        print("done")
        saveFrame("output.png")
        noLoop()
    
    
    stepLen = int(width*0.01)
    stepLen = 60
    # numSteps = int(random(10000,10000))
    numSteps = 3000

    index = int(random(0,len(startingPoints)))
    # index=0
    xStart = startingPoints[index][0]
    yStart = startingPoints[index][1]
    startingPoints.pop(index)
    colours = colorChoosing(xStart,yStart)
    ###COLOUR VARIATION
    # m1 = map(yStart,-10,width,80,120)
    # m2 = map(xStart,-10,height,80,120)
    # m=m1+m2
    # colour = int(random(m-25,m+25))
    # beginShape()
    # strokeWeight(5)
    # noStroke()
    # stroke(255,0,0)
    colorMode(HSB, 360, 100, 100,255)
    stroke(colours[0],colours[1],colours[2])
    fill(colours[0],colours[1],colours[2])
    # noFill()

    for i in range(numSteps):
        if checkProximity( xStart, yStart): 
            # flag=True
            # circle(xStart,yStart,5.5)
            ## FOR CIRCLE WITHIN CIRCLE UNCOMMENT THIS CODE
            startingR=3
            thickness=3
            center = [xStart,yStart]
            for i in range(5):
                drawCircle(center,startingR,thickness,colours)
                startingR = startingR + thickness + 3
            # print(startingR+thickness)
            
            xoff = xStart-xLeft
            yoff = yStart - yTop
            if xoff< xLeft or xoff > xRight or yoff > yBot or yoff < yTop:
                continue
            cIndex = int(xoff/res)
            rIndex = int(yoff/res)
            gridAngle = grid[cIndex][rIndex]
            xStep = stepLen*cos(gridAngle)
            yStep = stepLen*sin(gridAngle)
            xStart=xStart+xStep
            yStart=yStart+yStep
    # endShape()
    ##ONLY UNCOMMENT CODE BELOW IF CANVAS SIZE IS SMALL OR YOU HAVE A LOT OF DISK SPACE
    # if flag:
    #     count=count+1
    # if count==40:
    #     count=0
    #     saveFrame("C:/Users/User/Documents/Processing/improvedCurves/OUTPUTS/#######.tif")
                    
                                        
                            
