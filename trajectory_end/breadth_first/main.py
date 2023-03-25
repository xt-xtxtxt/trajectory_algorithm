import Point
import Map
import breadth
import visualization


map = Map.map()                                             # 创建地图
begin = Point.point(190, 65)                                # 设立起点
end = Point.point(1, 1)                                      # 设立终点
A = breadth.breath(map, begin, end)                         # 循迹初始化
A.run_surrounding_point()                                   # 循迹
A.Back_line()                                               # 导出结果路径
visualization.Visual(map, A.line, A.close_set, begin, end)  # 流程可视化

