# breath.py
# 广度优先算法，搜索各点，返回路径

import Point
import Map
import queue


class breath:
    def __init__(self, map0, begin, end):
        self.map = map0
        self.open_set = queue.Queue()
        self.begin = begin
        self.open_set.put(begin)
        self.close_set = {tuple([begin.x, begin.y]):begin} # 已遍历节点
        self.end = end
        self.line = {}      # 用字典来存储各点位对应信息
        self.i = 0

    def run_surrounding_point(self):
        while True:
            if self.open_set.qsize():
                print(self.open_set.qsize())
                parent = self.open_set.get()
                print(self.open_set.qsize(), parent.x, parent.y)
                if parent.x == self.end.x and parent.y == self.end.y:
                    break
                self.surrounding_point(parent)
            else:
                return
            # print(self.i)
            # self.i += 1

    def surrounding_point(self, parent):    # 检查该点前后左右四点合法性并加入open_set中
        self.check_point(parent.x + 1, parent.y, parent)  # 向右一步
        self.check_point(parent.x, parent.y + 1, parent)  # 向上一步
        self.check_point(parent.x - 1, parent.y, parent)  # 向左一步
        self.check_point(parent.x, parent.y - 1, parent)  # 向下一步

    def check_point(self, x1, y1, parent):  # 检查该点信息，若该点合法且第一次遍历，返回该点parent并加入open_set
        point = Point.point(x1, y1)
        if not Map.map.isValid(self.map, point):
            print('guojie')
            return
        elif tuple([x1, y1]) in self.close_set:
            print('chongfu')
            return
        else:
            point.parent_x = parent.x
            point.parent_y = parent.y
            self.close_set[tuple([x1, y1])] = point
            print(f"[{x1},{y1}],的parent[{point.parent_x},{point.parent_y}]")
            self.open_set.put(point)

    def Back_line(self):        # 返回一条正确的路径坐标
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

