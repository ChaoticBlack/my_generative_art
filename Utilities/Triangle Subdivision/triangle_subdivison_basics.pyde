import Triangles
from collections import deque
triangleQueue = deque()

def setup():
    global triangleQueue
    size(900,900)
    background(255)
    t= Triangles.Triangle([0,0],[width,0],[width,height],[149,31,64])
    # t= Triangles.Triangle()
    triangleQueue.append(t)
    t= Triangles.Triangle([0,0],[0,height],[width,height],[15,48,54])
    triangleQueue.append(t)  

    
def subdivide():
    global triangleQueue
    # r=floor(random(0,len(obj.points)))
    lenQueue = len(triangleQueue)
    for i in range(lenQueue):
        obj = triangleQueue.popleft()
        pointToDivide1 = obj.points[0]
        pointToDivide2 = obj.points[2]
        oppositePoint = obj.points[1]
        newPoint = [0,0]
        newPoint[0] = (pointToDivide1[0] + pointToDivide2[0])//2
        newPoint[1] = (pointToDivide1[1] + pointToDivide2[1])//2
        colour1, colour2=colourPicking(obj.colour)
        newTriangle1 = Triangles.Triangle(oppositePoint,newPoint,pointToDivide1, colour1)
        newTriangle2 = Triangles.Triangle(oppositePoint,newPoint,pointToDivide2,colour2)
        triangleQueue.append(newTriangle1)
        triangleQueue.append(newTriangle2)
        
  
def colourPicking(colour):
    r1= random(1,1000)
    r2= random(1,1000) 
    if r1<5:
        colour1=[333,91,93]
    else:
        colour1 = [colour[0],colour[1],colour[2]]
    if r2<5:
        colour2=[333,91,93]
    else:
        colour2 = [colour[0],colour[1],colour[2]]
    return colour1,colour2
    

count =0
def draw():
    global triangleQueue,count
    count+=1
    if count==1:
        noLoop()
        print("DONE")
    for i in triangleQueue:
        i.drawTriangle()
    # t.drawTriangle()
    subdivide()
