# Map.py
# 用于生成地图，且带随机障碍物

import Point


class map:
    def __init__(self, rows=50, clos=70):
        self.rows = rows                    # 宽
        self.clos = clos                    # 长
        self.obstacle_point = []
        self.generate_obstacle()

    def generate_obstacle(self):
        begin = Point.point(12, 13)
        end = Point.point(20, 18)
        self.generate_linear_obstacle(begin, end)
        begin = Point.point(40, 13)
        end = Point.point(51, 18)
        self.generate_linear_obstacle(begin, end)
        begin = Point.point(20, 40)
        end = Point.point(51, 50)
        self.generate_linear_obstacle(begin, end)
        begin = Point.point(0, 20)
        end = Point.point(40, 30)
        self.generate_linear_obstacle(begin, end)
        begin = Point.point(0, 52)
        end = Point.point(40, 54)
        self.generate_linear_obstacle(begin, end)

    def generate_linear_obstacle(self, point1, point2):
        for i in range(point1.x, point2.x):
            for j in range(point1.y, point2.y):
                self.obstacle_point.append([i, j])

    def is_obstacle(self, x, y):
        if [x, y] in self.obstacle_point:
            return True
        return False

    def isout_size(self, point0):
        if point0.x > self.rows or point0.x < 0:
            return True
        if point0.y > self.clos or point0.y < 0:
            return True
        return False

    def isValid(self, point0):           # 该点合理性
        if self.is_obstacle(point0.x, point0.y) or self.isout_size(point0):
            return False
        return True
