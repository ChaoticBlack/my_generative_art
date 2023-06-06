import Particles

scl = 5
rows=0
cols=0
z=0
objList = []
def setup():
    # randomSeed(42)
    global scl
    global rows
    global cols
    # fullScreen()
    # size(800,800)
    fullScreen()
    print(width,height)
    background(0)
    rows = floor(height/scl)
    cols=floor(width/scl)
    for i in range(width/2-100,width/2+100,30):
        for j in range(height/2-100,height/2+100,30):
            # print(i,j)
            objList.append(Particles.Particles(i,j))    


# objList.append(Particles.Particles(300,300))
# objList.append(Particles.Particles(300,350))

count=0
def draw():
    #noLoop()
    # background(0)
    global scl,rows,cols,z,objList,count
    count=count+1
    # saveFrame(str(count)+".png")
    # if count==2100000:
    #     noLoop()
    #     saveFrame("output.png")
    #     print("done")
    # yoff=0
    # inc=0.1
    # for y in range(0,rows):
    #     xoff=0
    #     for x in range(0,cols):
    #         n=noise(xoff,yoff,z)
    #         noStroke()
    #         fill(n*255)
    #         rect(x*scl,y*scl,scl,scl)
    #         xoff=xoff+inc
    #     yoff=yoff+inc
    # z=z+0.01
    for i in range(len(objList)):
        if objList[i].away==0:
            continue
        objList[i].forces(objList)
        objList[i].update()
        objList[i].edgeCheck()
        objList[i].displ()
        #objList[i].update()
        #objList[i].displ()
        
    # print(randomSeed())
    # saveFrame("C:/Users/User/Documents/Processing/virusOP/#####.tif")
