import random as rd
import math
# import circle
xLeft,xRight,yTop,yBot, res, numRows, numCols, grid =0,0,0,0,0,0,0,0
startingPoints = []
spaceGrid = []
dsep=0.6
spaceCellSize = dsep

def setup():
    size(1200,1200)
    background(16, 0, 43)
    # background(233,229,220)
    global xLeft,xRight,yTop,yBot,res,numRows, numCols, grid, startingPoints, spaceCellSize,spaceGrid
    #####INITIAL VALUES
    xLeft = int(width*-0.5)
    xRight = int(width*1.5)
    yTop = int(height*-0.5)
    yBot = int(height*1.5)
    res = int(width*0.005)
    # res = 150
    seedNo = int(random(3,10000))
    print("seed = ", seedNo)
    noiseSeed(9152)
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
    for i in range(xLeft,xRight,20):
        for j in range(yTop,yBot,20):
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
    anchors = [[0,0],[width,0],[width/2,height/2],[0,height],[width,height]]
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
    # print(distances)
    # minD = min(distances)
    # maxD = max(disances)
    # print(minD,maxD)
    adjDist = [x - minD for x in distances]
    distRange = maxD-minD
    wDist = [x / distRange for x in adjDist]
    sumDist = sum(wDist)
    nwDist = [x / sumDist for x in wDist]
    # print(nwDist)
    # print(nwDist)
    cumulationList=[]
    maxProb = 0
    cumulation=0
    colorArr = [[217, 77, 100],[265, 76, 93],[334, 100, 100],[19, 97, 98],[44, 96, 100]]
    # colorArr = [[278, 33, 100],[274, 51, 100],[273, 65, 87],[272, 77, 75],[270, 84, 60]]
    comboList = zip(nwDist,colorArr)
    comboList.sort(key = lambda x: x[0])
    # print(comboList)
    
    for i in comboList:
        # print(i[0])
        cumulation=cumulation+i[0]
        cumulationList.append(cumulation)
    # print(cumulationList)
    r= random(0,1)
    # print(r)
    # print(cumulationList)
    index=-1
    for i in range(len(cumulationList)):
        if cumulationList[i]>r:
            index=i
            break
    # print(comboList[index][1])
    return comboList[index][1]
    


    
def checkProximity( xCurr, yCurr):
    # dsep = 0.5
    global spaceCellSize, spaceGrid, dsep
    ##calculate index of current point
    xIndex = int(xCurr // spaceCellSize)
    yIndex = int(yCurr // spaceCellSize)
    #search in this cell of the spaceGrid   (add code to seach neighbouring grids also)
    for points in spaceGrid[xIndex][yIndex]:
        if(dist(xCurr,yCurr, points[0],points[1])<dsep):
            return False
        
    spaceGrid[xIndex][yIndex].append([xCurr,yCurr])
    return True
        

count=0

def draw():
    global xLeft,xRight,yTop,yBot,res,numRows, numCols, grid, count, xPos, yPos, startingPoints
    flag = False
    if(len(startingPoints)%1000==0):
        print(len(startingPoints))
    # print(count)
    if len(startingPoints)==0:
        print("done")
        saveFrame("output.png")
        noLoop()
    
    
    stepLen = int(width*0.01)
    # stepLen = 1
    # numSteps = int(random(10000,10000))
    numSteps = 100

    index = int(random(0,len(startingPoints)))
    # index=0
    xStart = startingPoints[index][0]
    yStart = startingPoints[index][1]
    startingPoints.pop(index)
    ###COLOUR VARIATION
    # m1 = map(yStart,-10,width,80,120)
    # m2 = map(xStart,-10,height,80,120)
    # m=m1+m2
    # colour = int(random(m-25,m+25))
    colours = colorChoosing(xStart,yStart)
    
    beginShape()
    strokeWeight(0.6)
    # noStroke()
    # stroke(255,0,0)
    colorMode(HSB, 360, 100, 100,255)
    stroke(colours[0],colours[1],colours[2])
    # stroke(colour,100,97)
    # fill(colour,100,97)
    noFill()

    for i in range(numSteps):
        if checkProximity( xStart, yStart): 
            flag=True
            curveVertex(xStart,yStart)
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
    endShape()
    ##ONLY UNCOMMENT CODE BELOW IF CANVAS SIZE IS SMALL OR YOU HAVE A LOT OF DISK SPACE
    # if flag:
    #     count=count+1
    # if count==40:
    #     count=0
    #     saveFrame("C:/Users/User/Documents/Processing/improvedCurves/OUTPUTS/#######.tif")
                    
                                        
                                        
# POSSIBLE VALUES
# size(400,400)
# dsep=0.5
# strokeWeight=0.3
# numStep= 3000

# size any
# dsep = 5
# strokeWeight 1
# numstep 50,80 or 3k to 5k
# fill same as stroke


# stepLen =1
# numStemps = 100
# dsep = 0.6
# strokeWeight = 0.6
