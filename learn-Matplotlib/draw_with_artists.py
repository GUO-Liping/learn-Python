import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

xy1 = np.array([0.2, 0.2])
xy2 = np.array([0.2, 0.8])
xy3 = np.array([0.8, 0.2])
xy4 = np.array([2.8, 1.5])

circle = mpatches.Circle(xy1, 0.05)
ax.add_patch(circle)

rect = mpatches.Rectangle(xy2, 0.2, 0.1, fill=False, color='r')
ax.add_patch(rect)

polygon = mpatches.RegularPolygon(xy3, 5, radius=0.1, color='g')  # radius is a keyword argument here
ax.add_patch(polygon)

ellipse = mpatches.Ellipse(xy4, 0.4, 0.2, color='y')
ax.add_patch(ellipse)

ax.set_aspect('equal')
ax.set_xlim(0, 3.5)
ax.set_ylim(0, 2)

plt.show()
