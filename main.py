import Point
import Map
import breadth
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import visualization


# plt.figure(figsize=(5, 7))
map = Map.map()
# ax = plt.gca()
# ax.set_xlim([0, map.rows])
# ax.set_ylim([0, map.clos])

begin = Point.point(1, 1)
end = Point.point(1, 65)
A = breadth.breath(map, begin, end)
A.run_surrounding_point()
A.Back_line()
visualization.Visual(map, A.line, A.close_set, begin, end)

# for i in range(map.rows):
#     for j in range(map.clos):
#         p = Point.point(i, j)
#         if Map.map.is_obstacle(map, p):
#             rec = Rectangle((i, j), width=1, height=1, color='gray')
#             ax.add_patch(rec)
#         elif p in Backend:
#             rec = Rectangle((i, j), width=1, height=1, color='b')
#             ax.add_patch(rec)
#         else:
#             rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
#             ax.add_patch(rec)
# rec = Rectangle((1, 1), width=1, height=1, facecolor='b')
# ax.add_patch(rec)
#
# rec = Rectangle((45, 65), width=1, height=1, facecolor='r')
# ax.add_patch(rec)
# plt.axis('equal')
# plt.axis('off')
# plt.tight_layout()
# filename = './Line.png'
# plt.savefig(filename)
