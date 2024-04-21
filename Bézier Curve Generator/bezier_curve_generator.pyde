# the following code implements De Casteljau'sAlgorithm for Bezier Curve generation
# It just contains the barebones algorithm that can be used as part of a bigger project

def setup():
    size(2000,2000)
    background(0)
   
increment=0.005
power_of_curve =6
def bezierCurve(list_of_points,t=0):
    if len(list_of_points)==0:
        return
    if len(list_of_points)==1:
        #draw point
        stroke(255)
        strokeWeight(5)
        point(list_of_points[0][0],list_of_points[0][1])
        return
    while t<=1:
        new_list = []
        for index in range(len(list_of_points)-1):
            # if index+1 == len(list_of_points):
            #     break
            point_x = (1-t)*list_of_points[index][0] + t*list_of_points[index+1][0]
            point_y = (1-t)*list_of_points[index][1] + t*list_of_points[index+1][1]
            new_list.append([point_x,point_y])
            # stroke(255)
            # strokeWeight(5)
            # point(point_x,point_y)
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

def draw():
    background(0)
    list_of_points = randomPointsGenerator(power_of_curve)
    t=0
    while t<=1:
        bezierCurve(list_of_points,t)
        t=t+increment
    delay(1000)
    print("done")
