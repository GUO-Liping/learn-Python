# 本程序用于OpenGL+PyQt5产生一个彩色正方体按照不同方向进行旋转的小程序
# https://nrotella.github.io/journal/first-steps-python-qt-opengl.html
from PyQt5 import QtCore      # core Qt functionality
from PyQt5 import QtGui       # extends QtCore with GUI functionality
from PyQt5 import QtWidgets
from PyQt5 import QtOpenGL    # provides QGLWidget, a special OpenGL QWidget

import OpenGL.GL as gl        # python wrapping of OpenGL
from OpenGL import GLU        # OpenGL Utility Library, extends OpenGL functionality
import sys                    # we'll need this later to run our Qt application

'''
VBO是一种组合数组，它把顶点坐标、颜色、法式、纹理等数据都集成在一起
如果用vbo对象 需导入这个库，不使用VBO时，我们每次绘制（ glDrawArrays ）
图形时都是从本地内存处获取顶点数据然后传输给OpenGL来绘制，这样就会频繁的操作CPU->GPU增大开销，从而降低效率。
使用VBO，我们就能把顶点数据缓存到GPU开辟的一段内存中，然后使用时不必再从本地获取，而是直接从显存中获取，这样就能提升绘制的效率
'''
from OpenGL.arrays import vbo  
import numpy as np


class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
            
    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(255, 255, 255))    # initialize the screen to white
        # glEnable 用于启用各种功能。功能由参数决定。与glDisable相对应。glDisable是用来关闭的。两个函数参数取值是一至的。
        # glEnable不能写在glBegin和glEnd两个函数中间。
        # gl.GL_DEPTH_TEST用于启用深度测试：根据坐标的远近自动隐藏被遮住的图形（材料）
        # enable depth testing
        gl.glEnable(gl.GL_DEPTH_TEST)                      

        self.initGeometry()

        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0
         
    def resizeGL(self, width, height):
        '''
        函数原型为：glViewport(GLint x,GLint y,GLsizei width,GLsizei height)
        x，y 以像素为单位，指定了视口的左下角位置。
        width，height 表示这个视口矩形的宽度和高度，根据窗口的实时变化重绘窗口。
        '''
        gl.glViewport(0, 0, width, height)
        '''
        OpenGL支持两种类型的投影变换，即透视投影和正投影。投影也是使用矩阵来实现的。
        如果需要操作投影矩阵，需要以GL_PROJECTION为参数调用glMatrixMode函数。
        '''
        gl.glMatrixMode(gl.GL_PROJECTION)
        
        # 把当前矩阵设置为单位矩阵
        gl.glLoadIdentity()
        aspect = width / float(height)
        '''
        GLU.gluPerspective(fovy,aspect,znear,zfar)fovy是眼睛上下睁开的幅度，角度值，值越小，视野范围越狭小（眯眼），值越大，视野范围越宽阔（睁开铜铃般的大眼）；
        aspect表示裁剪面的宽w高h比，这个影响到视野的截面有多大。
        zNear表示近裁剪面到眼睛的距离，zFar表示远裁剪面到眼睛的距离，注意zNear和zFar不能设置设置为负值（你怎么看到眼睛后面的东西）。
        '''
        GLU.gluPerspective(45.0, aspect, 1.0, 1000.0)
        # gl.GL_MODELVIEW说明接下来进行视景矩阵进行操作
        gl.glMatrixMode(gl.GL_MODELVIEW)
        '''GLU.gluLookAt函数定义一个视图矩阵，并与当前矩阵相乘。
        第一组eyex, eyey,eyez 相机在世界坐标的位置:就是脑袋的位置
        第二组centerx,centery,centerz 相机镜头对准的物体在世界坐标的位置:就是眼睛看的物体的位置
        第三组upx,upy,upz 相机向上的方向在世界坐标中的方向:就是头顶朝向的方向（因为你可以歪着头看同一个物体）
        '''
        GLU.gluLookAt(0,0,1, 0,0,0, 1,1,0)

    def paintGL(self):
        '''
        官网解释：clear buffers to preset values，用预制的值来清空缓冲区
        参数：GL_COLOR_BUFFER_BIT,颜色缓冲
        GL_DEPTH_BUFFER_BIT,深度缓冲
        GL_STENCIL_BUFFER_BIT，模板缓冲
        '''
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        '''
        当你做了一些移动或旋转等变换后，使用glPushMatrix();
        OpenGL 会把这个变换后的位置和角度保存起来。
        然后你再随便做第二次移动或旋转变换，再用glPopMatrix();
        OpenGL 就把刚刚保存的那个位置和角度恢复。

        比方：
        glLoadIdentity();
        glTranslatef(1,0,0);//向右移动(1,0,0)
        glPushMatrix();//保存当前位置
        glTranslatef(0,1,0);//如今是(1,1,0)了
        glPopMatrix();//这样，如今又回到(1,0,0)了
        '''
        gl.glPushMatrix()    # push the current matrix to the current stack

        '''
        glTranslatef(0.0f,-20.0f,-40.0f)表示bai将当前图形向dux轴平移0，向y轴平移-20，向z轴平移-40
        glScaled(10.0f,10.0f,10.0f)表示将当前图形沿x,y,z轴分别放大为原来的10倍
        glRotatef(-80.0f,1.0f,1.0f,0.0f)表示将当前图形沿方向向量(-1,1,0)顺时针旋转80度。
        '''
        gl.glTranslate(0.0, 0.0, -50.0)    # third, translate cube to specified depth
        gl.glScale(20.0, 20.0, 20.0)       # second, scale cube
        gl.glRotate(self.rotX, 1.0, 0.0, 0.0)
        gl.glRotate(self.rotY, 0.0, 1.0, 0.0)
        gl.glRotate(self.rotZ, 0.0, 0.0, 1.0)
        gl.glTranslate(-0.5, -0.5, -0.5)   # first, translate cube center to origin

        # 使用顶点数组时,必须先调用glEnableClientState开启顶点数组功能,在不用的时候调用glDisableClientState来禁用
        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)

        '''
        指定了需要启用的数组。array参数可以使用下面这些符号常量：
        顶点坐标GL_VERTEX_ARRAY、颜色数组GL_COLOR_ARRAY、RGBA颜色GL_SECONDARY_COLOR_ARRAY、GL_INDEX_ARRAY、表面法线GL_NORMAL_ARRAY、
        雾坐标GL_FOG_COORDINATE_ARRAY、纹理坐标GL_TEXTURE_COORD_ ARRAY和多边形的边界标志GL_EDGE_FLAG_ARRAY。
        '''

        # 指定三维物体的顶点坐标集合
        # 3维空间，顶点的坐标值为浮点数，且顶点是连续的集合
        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertVBO)
        gl.glColorPointer(3, gl.GL_FLOAT, 0, self.colorVBO)
        '''
        glDrawElements( GLenum mode, GLsizei count, GLenum type, const GLvoid *indices）；
        其中：
        mode指定绘制图元的类型，它应该是下列值之一，GL_POINTS, GL_LINE_STRIP, GL_LINE_LOOP, GL_LINES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_TRIANGLES, GL_QUAD_STRIP, GL_QUADS, and GL_POLYGON.
        count为绘制图元的数量乘上一个图元的顶点数。       
        type为索引值的类型，只能是下列值之一：GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT, or GL_UNSIGNED_INT。
        indices：指向索引存贮位置的指针。
        '''
        gl.glDrawElements(gl.GL_QUADS, len(self.cubeIdxArray), gl.GL_UNSIGNED_INT, self.cubeIdxArray)

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisableClientState(gl.GL_COLOR_ARRAY)

        gl.glPopMatrix()    # restore the previous modelview matrix
        
    def initGeometry(self):
        self.cubeVtxArray = np.array(
                [[0.0, 0.0, 0.0],
                 [1.0, 0.0, 0.0],
                 [1.0, 1.0, 0.0],
                 [0.0, 1.0, 0.0],
                 [0.0, 0.0, 0.0],
                 [1.0, 0.0, 0.0],
                 [1.0, 1.0, 0.0],
                 [0.0, 1.0, 0.0]])
        self.vertVBO = vbo.VBO(np.reshape(self.cubeVtxArray, (1, -1)).astype(np.float32))
        self.vertVBO.bind()
        
        self.cubeClrArray = np.array(
                [[0.0, 0.0, 0.0],
                 [1.0, 0.0, 0.0],
                 [1.0, 1.0, 0.0],
                 [0.0, 1.0, 0.0],
                 [0.0, 0.0, 1.0],
                 [1.0, 0.0, 1.0],
                 [1.0, 1.0, 1.0],
                 [0.0, 1.0, 1.0 ]])
        self.colorVBO = vbo.VBO(np.reshape(self.cubeClrArray, (1, -1)).astype(np.float32))
        self.colorVBO.bind()

        self.cubeIdxArray = np.array(
                [0, 1, 2, 3,
                 3, 2, 6, 7,
                 1, 0, 3, 3,
                 2, 1, 5, 6,
                 0, 3, 4, 4,
                 7, 6, 5, 4 ])

    def setRotX(self, val):
        self.rotX = np.pi * val

    def setRotY(self, val):
        self.rotY = np.pi * val

    def setRotZ(self, val):
        self.rotZ = np.pi * val

        
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)    # call the init for the parent class
        
        self.resize(300, 300)
        self.setWindowTitle('Hello OpenGL App')

        self.glWidget = GLWidget(self)
        self.initGUI()
        
        timer = QtCore.QTimer(self)
        timer.setInterval(20)   # period, in milliseconds
        timer.timeout.connect(self.glWidget.updateGL)
        timer.start()
        
    def initGUI(self):
        central_widget = QtWidgets.QWidget()
        gui_layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(gui_layout)

        self.setCentralWidget(central_widget)

        gui_layout.addWidget(self.glWidget)

        sliderX = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sliderX.valueChanged.connect(lambda val: self.glWidget.setRotX(val))

        sliderY = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sliderY.valueChanged.connect(lambda val: self.glWidget.setRotY(val))

        sliderZ = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sliderZ.valueChanged.connect(lambda val: self.glWidget.setRotZ(val))
        
        gui_layout.addWidget(sliderX)
        gui_layout.addWidget(sliderY)
        gui_layout.addWidget(sliderZ)

        
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    
    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
    
