# Point.py
# 用于记录各点位信息

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent_x = -1        # 该点父节点 x
        self.parent_y = -1        # 该点父节点 y
        self.saw = 0            # 该点是否被遍历，若被遍历则取1，未被遍历默认为0

    def __eq__(self, other):
        self.x = other.x
        self.y = other.y
