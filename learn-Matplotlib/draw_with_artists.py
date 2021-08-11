import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpathes

fig,ax = plt.subplots()
xy1 = np.array([0.2,0.2])
xy2 = np.array([0.2,0.8])
xy3 = np.array([0.8,0.2])
xy4 = np.array([2.8,1.5])
#圆形
circle = mpathes.Circle(xy1,0.05)
ax.add_patch(circle)
#长方形
rect = mpathes.Rectangle(xy2,0.2,0.1, fill='False', color='r')
ax.add_patch(rect)
#多边形
polygon = mpathes.RegularPolygon(xy3,5,0.1,color='g')
ax.add_patch(polygon)
#椭圆形
ellipse = mpathes.Ellipse(xy4,0.4,0.2,color='y')
ax.add_patch(ellipse)

#plt.axis('equal')  # 正方形作图，xy轴范围相同
plt.axis('square')  # xy刻度等长
#plt.grid()
plt.show()