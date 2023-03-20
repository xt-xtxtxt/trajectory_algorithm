# visualization.py
# 该文件用于对产生的结果路径进行可视化操作并输出图片

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from breadth_first import Point
from breadth_first import Map


def Visual(map, line, wide, begin, end):        # 传入地图、路径、已搜索地址、起点、终点
    plt.figure(figsize=(map.rows/10, map.clos/10))      # 生成图片大小
    ax = plt.gca()
    ax.set_xlim([0, map.rows])
    ax.set_ylim([0, map.clos])
    for i in range(map.rows+1):
        for j in range(map.clos+1):
            p = Point.point(i, j)
            if Map.map.is_obstacle(map, p.x, p.y):
                rec = Rectangle((i, j), width=1, height=1, color='gray')        # 绘制障碍物
                ax.add_patch(rec)
            elif tuple([i, j]) in line:
                rec = Rectangle((i, j), width=1, height=1, color='b')           # 绘制路径
                ax.add_patch(rec)
            elif tuple([i, j]) in wide:
                rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='y')     # 绘制被搜索区域
                ax.add_patch(rec)
            else:
                rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')     # 绘制空白地图
                ax.add_patch(rec)
    # for p in wide.values():
    #     rec = Rectangle((p.x, p.y), width=1, height=1, edgecolor='gray', facecolor='y')  # 绘制被搜索区域
    #     ax.add_patch(rec)
    # for p in line.values():
    #     rec = Rectangle((p.x, p.y), width=1, height=1, color='b')  # 绘制路径
    #     ax.add_patch(rec)
    rec = Rectangle((begin.x, begin.y), width=1, height=1, facecolor='b')       # 绘制起点终点
    ax.add_patch(rec)
    rec = Rectangle((end.x, end.y), width=1, height=1, facecolor='r')
    ax.add_patch(rec)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    filename = './Line.png'
    plt.savefig(filename)
