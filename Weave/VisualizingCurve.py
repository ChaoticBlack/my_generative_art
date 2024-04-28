from BezierCurve import BezierCurve
import random as rd


def points_for_cubic_curve():
    boundry = 100
    canvas_width = width
    canvas_height = height
    p0 = [random(-boundry, width + boundry), random(-boundry, boundry)]
    p1 = [random((width * 0.5) + boundry, width), random(boundry, height - boundry)]
    p2 = [random(0, (width * 0.5) - boundry), random(boundry, height - boundry)]
    p3 = [random(-boundry, width + boundry), random(height - boundry, height + boundry)]
    point_list = [p0, p1, p2, p3]
    return point_list


class CurveVisualizer:
    def __init__(self):
        list_of_points = points_for_cubic_curve()
        self.bezier_curve = BezierCurve(list_of_points)
        self.bezier_curve.parallel_curves_in_both_directions()
        self.sketch_details()
        background(
            self.sketch_values["Background"][0],
            self.sketch_values["Background"][1],
            self.sketch_values["Background"][2],
        )
        # self.draw_osculating_circle()

    def sketch_details(self):
        # self.sketch_values = {
        #     "Background": [214, 200, 180],
        #     "circle": {
        #         "strokeWeight": 1,
        #         "stroke": [217, 75, 28],
        #         "fill": [236, 227, 218],
        #     },
        #     "curve": {
        #         "color_variations": [
        #             [25, 48, 89],
        #             [45, 95, 141],
        #             [83, 60, 42],
        #             [125, 171, 192],
        #             [185, 218, 207],
        #             [231, 126, 46],
        #             [252, 189, 18],
        #             [210, 37, 43],
        #         ],
        #         "strokeWeight": 8,
        #     },
        # }
        self.sketch_values = {
            "Background": [22, 35, 46],
            "circle": {
                "strokeWeight": 1,
                "stroke": [247, 230, 168],
                "fill": [22, 35, 46],
            },
            "curve": {
                "color_variations": [
                    [215, 202, 209],
                    [97, 126, 192],
                    [59, 140, 195],
                    [41, 14, 65],
                    [27, 101, 128],
                    [252, 237, 206],
                    [0, 74, 119],
                    [49, 38, 80],
                    [14, 18, 126],
                ],
                "strokeWeight": 8,
            },
        }

    def draw_osculating_circle(self):
        self.draw_background_circle()
        push()
        strokeWeight(self.sketch_values["circle"]["strokeWeight"])
        fill(
            self.sketch_values["circle"]["fill"][0],
            self.sketch_values["circle"]["fill"][1],
            self.sketch_values["circle"]["fill"][2],
        )
        stroke(
            self.sketch_values["circle"]["stroke"][0],
            self.sketch_values["circle"]["stroke"][1],
            self.sketch_values["circle"]["stroke"][2],
        )
        # circle(self.bezier_curve.center.x, self.bezier_curve.center.y, self.bezier_curve.min_radius*2)
        self.draw_circle_by_point(self.bezier_curve.min_radius, 5)
        num_circles = rd.randint(
            int(self.bezier_curve.min_radius / 80),
            int(self.bezier_curve.min_radius / 80) + 2,
        )
        starting_radius = self.bezier_curve.min_radius * 0.2
        gap = self.bezier_curve.min_radius / (num_circles + 1)
        i = 0
        while i <= num_circles and starting_radius < self.bezier_curve.min_radius - 10:
            radius, thickess = self.calculate_inner_circle_parameters(starting_radius)
            self.draw_circle_by_point(radius, thickess)
            starting_radius = radius + thickess + gap
            i = i + 1
        # circle(self.bezier_curve.center.x, self.bezier_curve.center.y, self.bezier_curve.min_radius*2)
        pop()

    def draw_curve(self, points, stroke_color):
        # code to draw curve by drawing lines
        push()
        strokeWeight(self.sketch_values["curve"]["strokeWeight"])
        stroke(stroke_color[0], stroke_color[1], stroke_color[2])
        line(points[0].x, points[0].y, points[1].x, points[1].y)
        pop()

    def draw_all_curves(self, jump=1, gap=0):
        # if you want continuous curves, set jump =1, gap =0
        # draw main curve
        original_gap = gap
        stroke_color = rd.choice(self.sketch_values["curve"]["color_variations"])
        index = 0
        while index < len(self.bezier_curve.bezier_point_vector_list) - jump:
            self.draw_curve(
                [
                    self.bezier_curve.bezier_point_vector_list[index],
                    self.bezier_curve.bezier_point_vector_list[index + jump],
                ],
                stroke_color,
            )
            index = index + jump + gap
            gap = self.change_gap(gap, original_gap)

        for parallel_curve in self.bezier_curve.parallel_curves_left:
            index = 0
            stroke_color = rd.choice(self.sketch_values["curve"]["color_variations"])
            while index < len(parallel_curve) - jump:
                self.draw_curve(
                    [parallel_curve[index], parallel_curve[index + jump]], stroke_color
                )
                index = index + jump + gap
                gap = self.change_gap(gap, original_gap)

        stroke_color = rd.choice(self.sketch_values["curve"]["color_variations"])
        for parallel_curve in self.bezier_curve.parallel_curves_right:
            index = 0
            stroke_color = rd.choice(self.sketch_values["curve"]["color_variations"])
            while index < len(parallel_curve) - jump:
                self.draw_curve(
                    [parallel_curve[index], parallel_curve[index + jump]], stroke_color
                )
                index = index + jump + gap
                gap = self.change_gap(gap, original_gap)

    def change_gap(self, gap, original_gap):
        # determines how often to change gap
        if rd.randint(0, 100) < 3:
            return rd.randint(0, 15)
        return original_gap

    def calculate_inner_circle_parameters(self, starting_radius):
        radius = random(starting_radius, starting_radius + 10)
        thickess = random(20, 35)
        return radius, thickess

    def draw_circle_by_point(self, inner_radius, thickess):
        # set sketch properties
        outer_radius = inner_radius + thickess
        skip_flag = False
        while inner_radius <= outer_radius:
            angle = 0
            while angle <= 360:
                point_on_circle_x = self.bezier_curve.center.x + inner_radius * (
                    cos(radians(angle))
                )
                point_on_circle_y = self.bezier_curve.center.y + inner_radius * (
                    sin(radians(angle))
                )
                strokeWeight(self.sketch_values["circle"]["strokeWeight"])
                stroke(
                    self.sketch_values["circle"]["stroke"][0],
                    self.sketch_values["circle"]["stroke"][1],
                    self.sketch_values["circle"]["stroke"][2],
                )
                skip_points = rd.randint(0, 5000)
                if skip_points == 4:
                    num_points_to_skip = rd.randint(700, 1600)
                    points_skipped = 0
                    skip_flag = True
                if skip_flag:
                    stroke(
                        self.sketch_values["Background"][0],
                        self.sketch_values["Background"][1],
                        self.sketch_values["Background"][2],
                    )
                    points_skipped += 1
                    if points_skipped == num_points_to_skip:
                        skip_flag = False
                point(point_on_circle_x, point_on_circle_y)
                angle = angle + 0.1
            inner_radius = inner_radius + 1

    def draw_background_circle(self):
        stroke(
            self.sketch_values["Background"][0],
            self.sketch_values["Background"][1],
            self.sketch_values["Background"][2],
        )
        fill(
            self.sketch_values["Background"][0],
            self.sketch_values["Background"][1],
            self.sketch_values["Background"][2],
        )
        circle(
            self.bezier_curve.center.x,
            self.bezier_curve.center.y,
            self.bezier_curve.min_radius * 2,
        )
