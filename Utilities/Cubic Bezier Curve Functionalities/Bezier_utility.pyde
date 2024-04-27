from BezierCurve import BezierCurve

def points_for_cubic_curve():
    boundry = 100
    canvas_width = width
    canvas_height = height
    p0 = [random(-boundry, width + boundry), random(-boundry, boundry)]
    p1 = [random((width * 0.5) + boundry, width), random(boundry, height - boundry)]
    p2 = [random(0, (width * 0.5) - boundry), random(boundry, height - boundry)]
    p3 = [random(-boundry, width + boundry), random(height - boundry, height + boundry)]
    
    #uncoomment for more uniform anchor points
    # p0 = (random(-canvas_width, 0), random(0, canvas_height))
    # p1 = (random(0, canvas_width), random(0, canvas_height))
    # p2 = (random(0, canvas_width), random(0, canvas_height))
    # p3 = (random(canvas_width, 2 * canvas_width), random(0, canvas_height))

    point_list = [p0, p1, p2, p3]
    return point_list



def setup():
    size(5000,2000)
    background(0)
    
def draw():
    stroke(255)
    # noLoop()
    background(0)
    list_of_points = points_for_cubic_curve()
    bezier_curve = BezierCurve(list_of_points)
    bezier_curve.draw_curve()
    bezier_curve.draw_osculating_circle_at_inflection()
    bezier_curve.parallel_curves_in_both_directions()
    file_name = str(random(-100000,100000))
    saveFrame('outputs/'+file_name+'.png')
    delay(1000)
