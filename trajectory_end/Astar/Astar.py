# Astar.py
# Astar算法，加入启发函数，返回最短代价函数


from breadth_first.Point import point
from breadth_first.Map import map
from queue import PriorityQueue as pq
import math


class Astar:
    def __init__(self, map, begin, end):
        self.map = map
        self.begin = begin
        self.end = end
        self.open_set = pq()
        self.open_set.put((0, begin))
        self.close_set = {tuple([begin.x, begin.y]): begin}
        self.line = {}
        self.i = 0

    def Process_point(self, x, y, parent, f):
        point0 = point(x, y)
        if not map.isValid(self.map, point0):
            return
        if tuple([x, y]) in self.close_set:
            return
        else:
            point0.parent_x = parent.x
            point0.parent_y = parent.y
            self.G_x(point0)
            point0.G = parent.G + f
            # point0.H = parent.H + point0.H
            point0.F = point0.G + point0.H
            self.close_set[tuple([x, y])] = point0
            print(f"[{x},{y}],的parent[{point0.parent_x},{point0.parent_y}]")
            self.open_set.put((point0.F, point0))

    def surrounding_point(self, parent):
        self.Process_point(parent.x + 1, parent.y, parent, 1)  # right
        self.Process_point(parent.x + 1, parent.y + 1, parent, 1.41)
        self.Process_point(parent.x, parent.y + 1, parent, 1)
        self.Process_point(parent.x - 1, parent.y + 1, parent, 1.41)
        self.Process_point(parent.x - 1, parent.y, parent, 1)  # left
        self.Process_point(parent.x - 1, parent.y - 1, parent, 1.41)
        self.Process_point(parent.x, parent.y - 1, parent, 1)
        self.Process_point(parent.x + 1, parent.y - 1, parent, 1.41)

    def run_surrounding_point(self):
        while True:
            if self.open_set.qsize():
                print(self.open_set.qsize())
                parent = self.open_set.get()[-1]
                if parent == self.end:
                    break
                self.surrounding_point(parent)
            else:
                return

    def Back_line(self):  # 返回一条正确的路径坐标
        p = self.end
        z = tuple([p.x, p.y])
        while True:
            p = self.close_set[z]
            print(p.x, p.y)
            if p.x == self.begin.x and p.y == self.begin.y:
                print("已成功找到路径")
                break
            if p.parent_x == -1 and p.parent_y == -1:
                print("找不到合适路径")
                break
            self.line[tuple([p.x, p.y])] = p
            z = tuple([p.parent_x, p.parent_y])

    def G_x(self, point0):
        # point0.H = math.sqrt((point0.x - self.end.x)**2 + (point0.y - self.end.y)**2)  # 欧几里得距离
        H = abs(point0.x - self.end.x) + abs(point0.y - self.end.y)                      # 曼哈顿距离
        point0.H = (1.41 - 2) * (min(abs(point0.x - self.end.x), abs(point0.y - self.end.y))) + H   # 对角距离
        # point0.H = H
