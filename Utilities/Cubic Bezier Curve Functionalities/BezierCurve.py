#!/usr/bin/python
# -*- coding: utf-8 -*-


class BezierCurve:

    def __init__(self, list_of_points):
        self.anchor1 = list_of_points[0]
        self.control1 = list_of_points[1]
        self.control2 = list_of_points[2]
        self.anchor2 = list_of_points[3]
        self.increment = 0.001
        self.dist_btwn_curves = 50
        self.inflection_points_list = []
        (self.bezier_point_vector_list,
         self.first_derivative_vector_list,
         self.second_derivative_vector_list) = \
            self.calculate_curve_details()

    def calculate_curve_details(self):
        bezier_point_vector_list = []
        first_derivative_vector_list = []
        second_derivative_vector_list = []
        t = 0
        while t <= 1:
            bezier_point_vector = \
                self.calculte_curve_points([self.anchor1,
                    self.control1, self.control2, self.anchor2], t)
            first_derivative_vector = \
                self.calculate_first_derivative([self.anchor1,
                    self.control1, self.control2, self.anchor2], t)
            second_derivative_vector = \
                self.calculate_second_derivative([self.anchor1,
                    self.control1, self.control2, self.anchor2], t)
            self.check_inflection_point(second_derivative_vector,
                    bezier_point_vector)
            bezier_point_vector_list.append(bezier_point_vector)
            first_derivative_vector_list.append(first_derivative_vector)
            second_derivative_vector_list.append(second_derivative_vector)
            t = t + self.increment
        return (bezier_point_vector_list, first_derivative_vector_list,
                second_derivative_vector_list)

    def calculte_curve_points(self, list_of_points, t):
        point_x = list_of_points[0][0] * (-1 * t ** 3 + 3 * t ** 2 - 3
                * t + 1) + list_of_points[1][0] * (3 * t ** 3 - 6 * t
                ** 2 + 3 * t) + list_of_points[2][0] * (-3 * t ** 3 + 3
                * t ** 2) + list_of_points[3][0] * t ** 3
        point_y = list_of_points[0][1] * (-1 * t ** 3 + 3 * t ** 2 - 3
                * t + 1) + list_of_points[1][1] * (3 * t ** 3 - 6 * t
                ** 2 + 3 * t) + list_of_points[2][1] * (-3 * t ** 3 + 3
                * t ** 2) + list_of_points[3][1] * t ** 3
        bezeir_point = PVector(point_x, point_y)
        return bezeir_point

    def calculate_first_derivative(self, list_of_points, t):
        point_x = list_of_points[0][0] * (-3 * t ** 2 + 6 * t - 3) \
            + list_of_points[1][0] * (9 * t ** 2 - 12 * t + 3) \
            + list_of_points[2][0] * (-9 * t ** 2 + 6 * t) \
            + list_of_points[3][0] * (3 * t ** 2)

        point_y = list_of_points[0][1] * (-3 * t ** 2 + 6 * t - 3) \
            + list_of_points[1][1] * (9 * t ** 2 - 12 * t + 3) \
            + list_of_points[2][1] * (-9 * t ** 2 + 6 * t) \
            + list_of_points[3][1] * (3 * t ** 2)
        tangent = PVector(point_x, point_y)
        return tangent

    def calculate_second_derivative(self, list_of_points, t):
        point_x = list_of_points[0][0] * (-6 * t + 6) \
            + list_of_points[1][0] * (18 * t - 12) \
            + list_of_points[2][0] * (-18 * t + 6) \
            + list_of_points[3][0] * (6 * t)

        point_y = list_of_points[0][1] * (-6 * t + 6) \
            + list_of_points[1][1] * (18 * t - 12) \
            + list_of_points[2][1] * (-18 * t + 6) \
            + list_of_points[3][1] * (6 * t)
        acceleration = PVector(point_x, point_y)
        return acceleration

    def draw_curve(self):
        for bezier_point in self.bezier_point_vector_list:
            point(bezier_point.x, bezier_point.y)

    def parallel_curves_in_both_directions(self):
        for index in range(len(self.first_derivative_vector_list)):
            dist_to_cover = self.dist_btwn_curves
            while dist_to_cover < width + 1000:
                normal_vector = \
                    self.first_derivative_vector_list[index].copy().normalize().rotate(HALF_PI).mult(dist_to_cover)
                point(self.bezier_point_vector_list[index].x
                      + normal_vector.x,
                      self.bezier_point_vector_list[index].y
                      + normal_vector.y)
                normal_vector = \
                    self.first_derivative_vector_list[index].copy().normalize().rotate(HALF_PI).mult(-1
                        * dist_to_cover)
                point(self.bezier_point_vector_list[index].x
                      + normal_vector.x,
                      self.bezier_point_vector_list[index].y
                      + normal_vector.y)
                dist_to_cover = dist_to_cover + self.dist_btwn_curves

    def check_if_tangents_at_all_points(self):
        if len(self.bezier_point_vector_list) \
            != len(self.first_derivative_vector_list):
            print True

    def check_inflection_point(self, second_derivative_vector,
                               bezier_point_vector):
        if second_derivative_vector.x * second_derivative_vector.y < 0:
            self.inflection_points_list.append(bezier_point_vector)

    def draw_inflection_point_bold(self):
        for inflection_point in self.inflection_points_list:
            stroke(0, 255, 255)
            strokeWeight(10)
            point(inflection_point.x, inflection_point.y)

    def calculate_osculating_circle(self, point_on_curve):
        index_point_on_curve = \
            self.bezier_point_vector_list.index(point_on_curve)
        curvature_direction = \
            PVector.cross(self.first_derivative_vector_list[index_point_on_curve],
                          self.second_derivative_vector_list[index_point_on_curve])
        curvature_magnitude = \
            self.first_derivative_vector_list[index_point_on_curve].mag() \
            ** 3
        curvature = curvature_direction.mag() / curvature_magnitude

        # Compute radius of osculating circle

        if curvature != 0:
            radius = 1 / curvature
        else:
            radius = float('inf')
        curvature_direction.normalize()
        normal_vector = \
            self.first_derivative_vector_list[index_point_on_curve].copy().normalize().rotate(HALF_PI).mult(radius)
        center = \
            PVector(self.bezier_point_vector_list[index_point_on_curve].x
                    + normal_vector.x,
                    self.bezier_point_vector_list[index_point_on_curve].y
                    + normal_vector.y)
        return (center, radius)

    def draw_osculating_circle_at_inflection(self):
        random_index = int(random(0, len(self.inflection_points_list)
                           - 1))
        (center, radius) = \
            self.calculate_osculating_circle(self.inflection_points_list[random_index])
        push()
        noFill()
        stroke(255, 0, 0)
        circle(center.x, center.y, radius * 2)
        pop()
