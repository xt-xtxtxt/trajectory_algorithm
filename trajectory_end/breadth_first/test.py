import math
import re
import numpy as np

# PCorder = 'Linear,132.31231231,123.1231231'
# r = r'[0-9.0-9]+'
# loca = re.findall(r, PCorder)
# print(loca)
# y2 = -10
# x2 = 5
#
# y1 = 5
# x1 = 5
pi = math.pi
# arc = np.arctan2(y2-y1, x2-x1)*180/pi
# print(arc)
head = 0.0
y1 = -28.7
x1 = 192.2
Lineararc = np.arctan2(y1, x1)*180/pi
print(Lineararc)
if head >= 180:
    cursteer = head - 360
else:
    cursteer = head

# 判断与预计角度偏离是否超过30
if abs(cursteer - Lineararc) > 30:
    if 180 > cursteer - Lineararc > 0 or cursteer - Lineararc < -180:
        steer = 0.90
    else:
        steer = -0.90
    thr = 0.1
    brake = 0.0
else:
    steer = (cursteer - Lineararc) / 45

print(steer)
