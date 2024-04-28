from BezierCurve import BezierCurve
from VisualizingCurve import CurveVisualizer



def setup():
    size(6000,6000)
    background(0)
    
def draw():
    stroke(255)
    # noLoop()
    background(0)
    curve_obj = CurveVisualizer()
    curve_obj.draw_all_curves()
    curve_obj.draw_osculating_circle()
    file_name = str(random(0,500000))
    saveFrame('outputs/'+'without_circle_night_colors'+file_name+'.png')
    print(file_name)
    delay(1000)
