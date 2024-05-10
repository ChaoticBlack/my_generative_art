import Graph
import visuals
import Rectangles
from collections import deque
import random as rd
rectangleQueue = deque()
rectangleColours = [[0,0,17],[352,80,69],[217,59,41],[235,21,81], [51,75,94]]
numNodes=155  # Specify the number of nodes here
nodeList = []  #all the nodes will be in this list
cellSize = 230  #a node can only connect with nodes in a cell of this size (and neighbouring cells)
grid = {}      #spatial data structure
threshold=180   #this is as near as two nodes can come
def setup():
    global numNodes,nodeList,grid,rectangleQueue
    size(5400, 2400)
    # background(255)
    #background
    r = Rectangles.Rectangle([0,0],[width,0],[0,height],[width,height])
    rectangleQueue.append(r)
    numSubdivisions = 4
    while numSubdivisions:
        subdivide()
        numSubdivisions -=1
    for i in rectangleQueue:
        i.drawRect()
    for i in rectangleQueue:
        i.roughRect()
    
    create_and_connect_nodes(numNodes) 
        
def gridCoordinates(position):
    x, y = position
    grid_x = int(x / cellSize)
    grid_y = int(y / cellSize)
    return grid_x, grid_y

def create_and_connect_nodes(num_nodes):
    for i in range(num_nodes):
        node_id = i
        count=100
        while count:
            x = int(random(0, width))
            y = int(random(0, height))
            position = [x, y]
            
            is_far_enough = True
            for existing_node in nodeList:
                distance = dist(existing_node.position[0],existing_node.position[1], x,y)
                if distance < threshold:
                    is_far_enough = False
                    break
    
            if is_far_enough:
                break
            count=count-1

        if is_far_enough:
            node = Graph.Node(node_id, position)
            nodeList.append(node)

    # Update the grid with node positions
    for node in nodeList:
        x, y = node.position
        grid_x, grid_y = gridCoordinates([x, y])
        grid.setdefault((grid_x, grid_y), []).append(node)

    # Add connections between nodes in the same grid cell
    # numConnections=int(random(0,3))
    for i, node1 in enumerate(nodeList):
        # numConnections=int(random(3,5))
        numConnections=0
        r= random(0,1)
        if r>0.95:
            numConnections=1
        if r<=0.7:
            numConnections=1
        # if(r<0.5 and r>0.45):
        #     numConnections+=1
        for j in range(i + 1, len(nodeList)):
            if numConnections<=0:
                # numConnections=int(random(3,8))
                break
            node2 = nodeList[j]
            if are_nodes_in_same_cell(node1, node2):
                node1.add_connection(node2.id)
                # node2.add_connection(node1.id)
                numConnections-=1


def are_nodes_in_same_cell(node1, node2):
    x1, y1 = node1.position
    x2, y2 = node2.position
    grid_x1, grid_y1 = gridCoordinates([x1, y1])
    grid_x2, grid_y2 = gridCoordinates([x2, y2])
    # return grid_x1 == grid_x2 and grid_y1 == grid_y2
    if grid_x1 == grid_x2 and grid_y1 == grid_y2:
        return True

    # Check for neighboring cells
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (grid_x1 + dx == grid_x2) and (grid_y1 + dy == grid_y2):
                return True

    return False

def subdivide():
    global rectangleQueue
    lenQueue = len(rectangleQueue)
    for i in range(lenQueue):
        obj = rectangleQueue.popleft()  
        divide = int(random(0,2))
        # divide=1
        linesToDivide = obj.oppositeLines[divide]  #linesToDivide contains 2 lines

        midPoint1 = [0,0]
        midPoint2 = [0,0] 
        m= random(0.35,0.65)
        n=random(0.35,0.65)
        # m=0.5
        # n=0.5
        midPoint1[0]= (m*linesToDivide[0][0][0] + n*linesToDivide[0][1][0])//(m+n)
        midPoint1[1]= (m*linesToDivide[0][0][1] + n*linesToDivide[0][1][1])//(m+n)
        midPoint2[0]= (m*linesToDivide[1][0][0] + n*linesToDivide[1][1][0])//(m+n)
        midPoint2[1]= (m*linesToDivide[1][0][1] + n*linesToDivide[1][1][1])//(m+n)
        
        indices= uniqueRandomNumbers(0,len(rectangleColours),2) 
        colour1 = rectangleColours[indices[0]]
        colour2 = rectangleColours[indices[1]]
        if divide==0:
            newRect1 = Rectangles.Rectangle(obj.p1,midPoint1,obj.p3,midPoint2,colour1)
            newRect2 = Rectangles.Rectangle(midPoint1,obj.p2,midPoint2,obj.p4,colour2)
        if divide==1:
            newRect1 = Rectangles.Rectangle(obj.p1,obj.p2,midPoint1,midPoint2,colour1)
            newRect2 = Rectangles.Rectangle(midPoint1,midPoint2,obj.p3,obj.p4,colour2)
        rectangleQueue.append(newRect1)
        rectangleQueue.append(newRect2)

def uniqueRandomNumbers(low,high,num):
    return rd.sample(range(low,high),num)
   

def draw():
    global numNodes,nodeList
    noLoop()
    noFill()
    # background(255)
    for node in nodeList:
        stroke(255,0,0,100)
        x, y = node.position
        # fill(255,0,0)
        # ellipse(x, y, 40, 40)
        # radius=random(25,40)
        # numCircles=2
        # if radius < 25:
        #      numCircles=1

        # visuals.perlinNoiseCircle(x,y,radius,numCircles)
        stroke(0,100)
        noFill()
        for connected_id in node.connectedTo:
            connected_node = next((n for n in nodeList if n.id == connected_id), None)
            if connected_node:
                x2, y2 = connected_node.position
                drawDotted= random(0,1)
                if drawDotted < 0.3:
                    visuals.dashedLine([x,y],[x2,y2])
                else:
                    roughness=random(30,75)
                    visuals.drawRoughLine(x,y,x2,y2,roughness)
                # else:
                #     bezier(x, y, x + random(-50, 50), y + random(-50, 50),x2 + random(-50, 50), y2 + random(-50, 50), x2, y2)
                # line(x, y, x2, y2)
                
    for node in nodeList:
        stroke(255,0,0,100)
        x, y = node.position
        radius=random(30,65)
        numCircles=2
        if radius < 25:
             numCircles=1
        visuals.perlinNoiseCircle(x,y,radius,numCircles)
    #     # fill(255,0,0)
    #     # ellipse(x, y, 40, 40)
    #     radius=random(80,90)
    #     numCircles=int(random(1,4))
    #     visuals.perlinNoiseCircle(x,y,radius,numCircles)
    fileName = str(random(0,10000))
    saveFrame("/Outputs/"+fileName+".png")
    print(fileName)
    print("done")
