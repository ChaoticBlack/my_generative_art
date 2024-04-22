# the following code implements De Casteljau'sAlgorithm for Bezier Curve generation
# It just contains the barebones algorithm that can be used as part of a bigger project

def setup():
    size(2000,2000)
    background(0)
   
increment=0.005
power_of_curve =8

# def draw_control_lines(x1,y1,x2,y2):
#     mid_x = (x1+x2)2
#     mid_y = (y1+y2)/2

def bezierCurve(list_of_points,t):
    if len(list_of_points)==0:
        return
    if len(list_of_points)==1:
        #draw point
        stroke(255)
        strokeWeight(5)
        point(list_of_points[0][0],list_of_points[0][1])
        return
    # draw midpoint line
    while t<=1:
        new_list = []
        for index in range(len(list_of_points)-1):
            # if index+1 == len(list_of_points):
            #     break
            point_x = (1-t)*list_of_points[index][0] + t*list_of_points[index+1][0]
            point_y = (1-t)*list_of_points[index][1] + t*list_of_points[index+1][1]
            new_list.append([point_x,point_y])
            # draw_control_line(list_of_points[index][0],list_of_points[index][1],list_of_points[index+1][0],list_of_points[index+1][1])
            # stroke(255)
            # strokeWeight(5)
            # point(point_x,point_y)
        # print(t)
        bezierCurve(new_list,t)
        t=t+increment
        list_of_points=new_list
    
def randomPointsGenerator(n):
    point_list = []
    boundry=100
    for i in range(n+1):
        random_point= [random(-boundry,width+boundry), random(-boundry,height+boundry)]
        point_list.append(random_point)
    return point_list    

def drawLines(list_of_points):
    if len(list_of_points)<2:
        return
    new_list =[]
    for index in range(len(list_of_points)-1):
        stroke(0,255,255)
        strokeWeight(5)
        point(list_of_points[index][0],list_of_points[index][1])
        point(list_of_points[index+1][0],list_of_points[index+1][1])
        stroke(255,0,255)
        strokeWeight(1)
        line(list_of_points[index][0],list_of_points[index][1],list_of_points[index+1][0],list_of_points[index+1][1])
        mid_point = [ (list_of_points[index][0] + list_of_points[index+1][0])/2 ,(list_of_points[index][1] + list_of_points[index+1][1])/2 ]
        new_list.append(mid_point)
    drawLines(new_list)

def draw():
    background(0)
    # noLoop()
    list_of_points = randomPointsGenerator(power_of_curve)
    # for index in range(len(list_of_points)-2):
    #     stroke(255,0,0)
    #     line((list_of_points[index][0] + list_of_points[index+1][0])/2 ,(list_of_points[index][1] + list_of_points[index+1][1])/2,\
    #      (list_of_points[index+1][0] +list_of_points[index+2][0])/2, (list_of_points[index+1][1] + list_of_points[index+2][1])/2)
        
    # for index in range(len(list_of_points)):
    #     print(index)
    #     stroke(255,0,255)
    #     strokeWeight(10)
    #     point(list_of_points[index][0],list_of_points[index][1])
    drawLines(list_of_points)
    t=0
    while t<=1:
        bezierCurve(list_of_points,t)
        t=t+increment
    delay(1000)
    file_name = str(random(-100000,100000))
    # saveFrame('outputs/'+file_name+'.png')
    print("done")
