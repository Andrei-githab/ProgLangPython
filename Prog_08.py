"""
Лабораторная работа 8
Написать программу попадания точки в области (визуализированный вариант)
"""
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

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


line(2, 2, 3, 3)

ax.add_patch(Rectangle((0.6, 0.2), 0.4, 0.3))
ax.add_patch(Circle((0.2, 0.6), radius=0.1, color='white'))

plt.show()
