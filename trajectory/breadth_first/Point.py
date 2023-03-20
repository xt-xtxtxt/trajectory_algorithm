# Point.py
# 用于记录各点位信息


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent_x = -1        # 该点父节点 x
        self.parent_y = -1        # 该点父节点 y
        self.F = 0                # 该点代价
        self.H = 0                # 该点H预估代价
        self.G = 0                # 该点G已付出代价

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __lt__(self, other):
        if self.F <= other.F:
            return True
        return False
