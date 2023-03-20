from breadth_first.Point import point
from breadth_first.Map import map
from breadth_first.visualization import Visual
from Dijkstra.Dijkstra import dijkstra as d
from Astar.Astar import Astar as a
from breadth_first.breadth import breath as b


map = map()                                             # 创建地图
begin = point(40, 65)                                # 设立起点
end = point(1, 1)                                      # 设立终点
A = b(map, begin, end)                         # 循迹初始化
A.run_surrounding_point()                                   # 循迹
A.Back_line()                                               # 导出结果路径
Visual(map, A.line, A.close_set, begin, end)  # 流程可视化