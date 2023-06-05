import Boid
count=0
flock = []
flag=0
# frameNum=0
def setup():
    global flock
    fullScreen()
    # pixColor = get(width/2,height/2)
    # print(pixColor)
    # size(800,400)
    for i in range(275):   #reduce the number in range to reduce stuttering
        # print(":hi")
        flock.append(Boid.boids())
    
    
def draw():
    # noLoop()
    # print(width,height)
    global flock,count,flag
    #background(154,152,130,10)
    #if you want dynamic background uncomment the following code and comment background(51)
    # background(154,152,130)
    # # colors = [color(125, 255, 214),     
    # #           color(203, 255, 226),     
    # #           color(236, 255, 246),     
    # #           color(166, 250, 255)]    
    # colors = [color(242, 249, 255),     
    #           color(201, 232, 254),     
    #           color(169, 218, 255),     
    #           color(112, 193, 255),
    #           color(95, 186, 255),
    #           color(22, 155, 255),
    #           color(0, 135, 236),]      
    # if flag==0:
    #     count = count+0.01
    # if flag==1:
    #     count= count -0.01
    # if count>=len(colors)-1:
    #     flag=1
    # if count<=0:
    #     flag = 0
    
    # time_of_day = float(count) / len(colors)
    # num_colors = len(colors)
    # # time_of_day = time_of_day % (1.0 / num_colors)
    # index1 = int(time_of_day * num_colors)
    # index2 = (index1 + 1) % num_colors
    # background_color = lerpColor(colors[index1], colors[index2], time_of_day * num_colors - index1)
    # background(background_color)
    background(51)
    noStroke()
    # print("done")
    for i in flock:
        i.edges()
        i.update()
        i.show()
        i.culmination(flock)
        # C:\Users\User\Documents\Processing\tadpole\outputImages
    saveFrame("C:/Users/User/Documents/Processing/tadpole/outputImages/#####.tif")
