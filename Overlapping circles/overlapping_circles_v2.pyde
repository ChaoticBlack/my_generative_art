# res, numRows, numCols, grid = 0,0,0,0
import random as rd
borderXL,borderXR,borderYT,borderYB = 0,0,0,0
percent = 16
# backgroundCol = [135,34,60]    #mintish
# backgroundCol = [9,12,92]   #pinkish
# backgroundCol = [41,12,89] #dull yellow paper
# backgroundCol = [295,69,26]   #dark voilet
# backgroundCol = [34,7,91]   #paper
# backgroundCol = [0,0,0]
backgroundCol = [225,58,24] #voilet black
#1a2340
# colorArr = [[217, 77, 100],[265, 76, 93],[334, 100, 100],[19, 97, 98],[44, 96, 100]]    #colourful
# colorArr = [[278, 33, 100],[274, 51, 100],[273, 65, 87],[272, 77, 75],[270, 84, 60]]   #violet
# colorArr = [[18, 100, 100],[210, 74, 90],[85, 59, 83],[42, 100, 100],[334, 66, 100]]   #colourful but better
# colorArr = [[239, 97, 37],[201, 100, 71],[190, 100, 85],[190, 19, 97],[189, 40, 94]]    #blue
# colorArr = [[48, 59, 100],[47, 79, 93],[46, 81, 79],[43, 84, 64],[40, 88, 50]]   #gold
colorArr = [[41,59,98],[160,14,83],[200,36,75],[0,62,82],[170,73,64]]
rd.shuffle(colorArr)

def setup():
    
    # size(800,800)
    fullScreen()
    print(width,height)
    colorMode(HSB, 360, 100, 100,255)
    background(backgroundCol[0],backgroundCol[1],backgroundCol[2])
    
    global borderXL,borderXR,borderYT,borderYB
    
    ### Frame
    borderXL = int(width/percent)
    borderYT = int(height/percent)
    borderXR = width - int(width/percent)
    borderYB = height - int(height/percent)
    print(borderXL,borderXR,borderYT,borderYB)
    
    
    
    
def colorChoosing(xCurr,yCurr):
    xLeft,xRight,yTop,yBot=0,width,0,height
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
    return comboList[index][1], index
        
    
        
def checkProximity( xCurr, yCurr):
    # dsep = 0.5
    global circleStats
    
    nearestCircDist = 9999999
    nearestCircle=[]
    for circ in circleStats:
        distance = dist (circ[0],circ[1], xCurr,yCurr)
        if distance  < circ[2]:
            return False,[]
        if distance< nearestCircDist:
            # print("HI")
            nearestCircDist = distance
            nearestCircle = circ
            # print(nearestCircle)
    
    # print(nearestCircle)    
    return True, nearestCircle

   
def drawCircle(c,r,t, cols):
    global borderXL,borderXR,borderYT,borderYB
    colour = colorArr[cols]
    strokeWeight(1)
    stroke(255)
    lastR = r+t
    flag = False
    while r<= lastR:
        angle = 0
        while angle<=360:
            stroke(colour[0],colour[1],colour[2])
            rareColor = int(random(0,5000))
            # print(rareColor)
            if rareColor==4:
                numPoints = int(random(300,800))
                # print("\t", numPoints)
                curr = 0
                flag=True
            if flag:
                stroke(backgroundCol[0],backgroundCol[1],backgroundCol[2])
                curr+=1
                if curr == numPoints:
                    flag = False
            # print(angle)
            x = c[0] + r*cos(radians(angle))
            y = c[1] + r*sin(radians(angle))
            # print(x,y)
            prox , nearCircl = checkProximity(x,y)
            if prox and x>borderXL and x<borderXR and y >borderYT and y< borderYB:
                    # print("HI")
                point(x,y)
            angle+=0.1
        r+=1
    # return lastR
        
 
circleStats = []
globalCount=0
def draw():
    # noLoop()
    # print("hi")
    global circleStats, globalCount
    count=0
    globalCount+=1
    print(globalCount)
    # if (count%50==0):
    #     saveFrame(str(count)+".png")
        
    startingR = int(random(10,25))
    thickness = int(random(10,25))
    gap=int(random(3,12))
    numCircles = int(random(5,12))
    
    flag = True
    while flag:
        count=count+1
        centerX = random(0,width)
        centerY = random(0,height)
        if count==1000:
          saveFrame(str(globalCount)+".png")
          print("done")
          noLoop()  
          break
        prox,nearCircl = checkProximity(centerX,centerY)
        if prox:
            flag=False
    center = [centerX,centerY]
    # print(nearCircl)
    colours, colorIndex= colorChoosing(centerX,centerY)
    if len(nearCircl)!=0:
        while nearCircl[3]==colorIndex:
            # print("HI")
            colorIndex = int(random(0,len(colorArr)))
        
    # print(colorIndex)
    stroke(colours[0],colours[1],colours[2])
    for i in range(numCircles):
        thickness = (int(random(thickness - 5,thickness+5)))
        gap = (int(random(gap -2,gap+2)))
        drawCircle(center,startingR,thickness, colorIndex)
        startingR = startingR + thickness + gap
    circleStats.append([centerX,centerY,startingR-gap+2,colorIndex])

    # print("done")
    
    
