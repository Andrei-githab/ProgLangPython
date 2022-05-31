import math
import keyboard
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

file = open('input_08.txt')
s = []
for row in file:
    digit = row.split()
    s.append(digit)
print(s)


ax = plt.axes()
plt.autoscale(False)


def line(x1, y1, x2, y2):
    line_k = (y1 - y2) / (x1 - x2)
    line_b = y1 - line_k * x1
    x = np.linspace(-5, 5, 100)
    y = line_k * x + line_b
    plt.plot(x, y, color='red', alpha=1.00)
    plt.fill_between(x, y, np.max(y), color='blue', alpha=0.25)

    return


if s[0][0] == s[0][2]:
    print("Прямая параллельна оси Oy и пересекает ее в точке с координатами")
elif s[0][1] == s[0][3]:
    print("Прямая параллельна оси Oх и пересекает ее в точке с координатами")
else:
   line(float(s[0][0]), float(s[0][1]), float(s[0][2]), float(s[0][3]))


pramul_x1 = float(s[1][0])
pramul_y1 = float(s[1][1])
pramul_x2 = float(s[1][1])
pramul_y2 = float(s[1][1])
pramul_x3 = float(s[1][1])
pramul_y3 = float(s[1][1])
pramul_x4 = float(s[1][1])
pramul_y4 = float(s[1][1])

if pramul_x1 <= float(s[3][0]) <= pramul_x2 and pramul_y1 <= float(s[3][1]) <= pramul_y2 and pramul_x3 <= float(s[3][0]) <= pramul_x4 and pramul_y3 <= float(s[3][1]) <= pramul_y4:
    ax.add_patch(Rectangle((0.6, 0.2), 0.4, 0.3, color='blue', alpha=0.25))
else:
    ax.add_patch(Rectangle((0.6, 0.2), 0.4, 0.3, color='white', alpha=0.25))


ax.add_patch(Circle((0.2, 0.6), radius=0.1, color='white'))
ax.scatter(float(s[3][0]), float(s[3][1]), facecolor='green')

plt.show()
print(s)
