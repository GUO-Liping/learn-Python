# -*- coding:utf-8 -*-
#!/usr/bin/env pythonw
# 本程序利用OpenGL绘制绿色、红色螺旋线-二维
# Reference： http://www.siafoo.net/snippet/316

'''
Created on Jul 7, 2009

@author: Stou Sandalski (stou@icapsid.net)
@license:  Public Domain
'''

import math

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtOpenGL import *

class SpiralWidget(QGLWidget):
    '''
    Widget for drawing two spirals.
    '''
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent=None)
        self.setMinimumSize(500, 500)

    def paintGL(self):
        '''
        Drawing routine
        '''
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        '''
        glLoadIdentity()该函数的功能是重置当前指定的矩阵为单位矩阵.在语义上，其等同于用单位矩阵调用glLoadMatrix()。但是，在一些情况下，glLoadIdentity()更加效率。相当于恢复到原点（屏幕中心）
        '''
        glLoadIdentity()
        
        # Draw the spiral in 'immediate mode'
        # WARNING: You should not be doing the spiral calculation inside the loop
        # even if you are using glBegin/glEnd, sin/cos are fairly expensive functions
        # I've left it here as is to make the code simpler.
        radius = 1.0
        x = radius*math.sin(0)
        y = radius*math.cos(0)
        glColor(0.6, 0.1, 0.6)
        glBegin(GL_LINE_STRIP)
        for deg in range(990):
            glVertex(x, y, 0.0)
            rad = math.radians(deg)
            radius -= 0.001
            x = radius*math.sin(rad)
            y = radius*math.cos(rad)
        glEnd()

        '''
        OpenGL提供glEnableClientState()与glDisableClientState()函数启用/禁用6中不同类别的数组。此外，有6个函数用于指定数组的精确位置（地址），因此在你的应用程序中OpenGL可以访问这些数组。
        glVertexPointer()：指定顶点坐标数组指针
        glNormalPointer()：指定法线数组指针
        glColorPointer()：指定RGB颜色数组指针
        glIndexPointer()：指定索引颜色数组指针
        glTexCoordPointer()：指定纹理坐标数组指针
        glEdgeFlagPointer()：指定边标志数组指针
        '''

        '''
        下面的代码说明了顶点数组是如何使用的：
        glEnableClientState(GL_VERTEX_ARRAY);
        glVertexPointer(3, GL_FLOAT, 0, vertex_list);
        glDrawElements(GL_QUADS, 24, GL_UNSIGNED_INT, index_list);
        其中：
        glEnableClientState(GL_VERTEX_ARRAY); 表示启用顶点数组。
        glVertexPointer(3, GL_FLOAT, 0, vertex_list); 指定顶点数组的位置，3表示每个顶点由三个量构成（x, y, z），GL_FLOAT表示每个量都是一个GLfloat类型的值。第三个参数0，参见后面介绍“stride参数”。最后的vertex_list指明了数组实际的位置。
        glDrawElements(GL_QUADS, 24, GL_UNSIGNED_INT, index_list); 根据序号数组中的序号，查找到相应的顶点，并完成绘制。GL_QUADS表示绘制的是四边形，24表示总共有24个顶点，GL_UNSIGNED_INT表示序号数组内每个序号都是一个GLuint类型的值，index_list指明了序号数组实际的位置。
        上面三行代码代替了原来的循环。可以看到，原来的glBegin/glEnd不再需要了，也不需要调用glVertex*系列函数来指定顶点，因此可以明显的减少函数调用次数。另外，数组中的内容可以随时修改，比显示列表更加灵活。
        '''
        glEnableClientState(GL_VERTEX_ARRAY)
        
        spiral_array = []
        
        # Second Spiral using "array immediate mode" (i.e. Vertex Arrays)
        radius = 0.8
        x = radius*math.sin(0)
        y = radius*math.cos(0)
        glColor(0.0, 0.6, 0.6)
        for deg in range(810):
            spiral_array.append([x, y])
            rad = math.radians(deg)
            radius -= 0.001
            x = radius*math.sin(rad)
            y = radius*math.cos(rad)

        '''
        glVertexPointer(int size,int type,int stride,Buffer pointer)
        parameters：
        size:每个顶点有几个数指描述。必须是2，3  ，4 之一，初始值是4.
        type: 数组中每个顶点的坐标类型。取值：GL_BYTE, GL_SHORT , GL_FIXED , GL_FLOAT,   初始值 GL_FLOAT
        stride：数组中每个顶点间的间隔，步长（字节位移）。取值若为0，表示数组是连续的   初始值为0
        pointer: It's your array ,存储着每个顶点的坐标值。初始值为0
        '''
        glVertexPointerf(spiral_array)
        '''
        glDrawArrays(int mode,int first ,int count)
        参数：
        mode 指定你要绘制何种图元， opengl 中的图元就这几个: GL_POINTS, GL_LINE_STRIP, GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES.
        first 在已制定的数组中的开始位置(索引位置)
        count 点的绘制次数， 比如我们绘制一个三角形，就是绘制三个顶点，即此参数为 3。
        '''
        glDrawArrays(GL_LINE_STRIP, 0, len(spiral_array))
        '''
        glFlush()用于强制刷新缓冲，保证绘图命令将被执行，而不是存储在缓冲区中等待其他的OpenGL命令。
        '''
        glFlush()

    def resizeGL(self, w, h):
        '''
        Resize the GL window 
        '''
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.0, 1.0, 30.0)
    
    def initializeGL(self):
        '''
        Initialize GL
        '''
        
        # set viewing projection
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(40.0, 1.0, 1.0, 30.0)


# You don't need anything below this
class SpiralWidgetDemo(QtWidgets.QMainWindow):
    ''' Example class for using SpiralWidget'''
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        widget = SpiralWidget(self)    
        self.setCentralWidget(widget)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(['Spiral Widget Demo'])
    window = SpiralWidgetDemo()
    window.show()
    app.exec_()
