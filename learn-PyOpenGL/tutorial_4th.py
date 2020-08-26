import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtGui
from PyQt5.QtOpenGL import *
from PyQt5 import QtCore, QtWidgets, QtOpenGL


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        # super(Ui_MainWindow, self)含义是继承使Ui_MainWindow继承其父类的属性和函数，不然只能继承其父类的函数
        super(Ui_MainWindow, self).__init__()
        self.widget = glWidget()
        self.button = QtWidgets.QPushButton('Test', self)
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.widget)
        mainLayout.addWidget(self.button)
        self.setLayout(mainLayout)


class glWidget(QGLWidget):
    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(480, 360)

    def initializeGL(self):
        '''
        glClearDepth(取值范围0~1), 它给深度缓冲指定了一个初始值，缓冲中的每个像素的深度值都是这个， 比如1，这个时候你往里面画一个物体， 
        由于物体的每个像素的深度值都小于等于1， 所以整个物体都被显示了出来。 如果初始值指定为0， 物体的每个像素的深度值都大于等于0，
        所以整个物体都不可见。 如果初始值指定为0.5， 那么物体就只有深度小于0.5的那部分才是可见的
        '''
        glClearDepth(1.0)
        '''
        glDepthFunc（GLenum func）参数说明：
        func：指定“目标像素与当前像素在z方向上值大小比较”（即深度的比较）的函数，符合该函数关系的目标像素才进行绘制（渲染），否则对目标像素不予绘制，可以取下值：
        GL_NEVER:永不绘制
        GL_LESS:如果目标像素z值<当前像素z值，则绘制目标像素（深度小的时候才渲染）
        GL_EQUAL：如果目标像素z值=当前像素z值，则绘制目标像素
        GL_LEQUAL：如果目标像素<=当前像素z值，则绘制目标像素
        GL_GREATER:如果目标像素z值>当前像素z值，则绘制目标像素
        GL_NOTEQUAL：如果目标像素z值<>当前像素z值，则绘制目标像素
        GL_GEQUAL：如果目标像素z值>=当前像素z值，则绘制目标像素
        GL_ALWAYS：总是绘制
        '''              
        glDepthFunc(GL_LESS)
        # glEnable()启用(深度测试),根据坐标的远近自动隐藏被遮住的图形（材料）
        glEnable(GL_DEPTH_TEST)
        # glShadeModel函数用于控制opengl中绘制指定两点间其他点颜色的过渡模式,参数一般为GL_SMOOTH（默认）,GL_FLAT
        glShadeModel(GL_FLAT)
        '''
        glMatrixMode（GLenum mode）：
        mode 告诉计算机哪一个矩阵堆栈将是下面矩阵操作的目标,即将什么矩阵设置为当前矩阵，他的可选值有： GL_MODELVIEW、GL_PROJECTION、GL_TEXTURE.
        GL_MODELVIEW：应用这个参数后，表示接下来的矩阵操作都是针对模型视景矩阵堆栈,直到下一次调用这个函数并更改参数为止。   
        GL_PROJECTION：应用这个参数后，表示接下来的矩阵操作都是针对投影矩阵堆栈,直到下一次调用这个函数并更改参数为止。
        GL_TEXTURE ： 应用这个参数后，表示接下来的矩阵操作都是针对纹理矩阵堆栈,直到下一次调用这个函数并更改参数为止。
        '''
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        '''
        gluPerspective(GLdouble fovy,GLdouble aspect,GLdouble zNear,GLdouble zFar)
        fovy,眼睛睁开的角度,即,视角的大小,如果设置为0,相当你闭上眼睛了,所以什么也看不到,如果为180,那么可以认为你的视界很广阔,
        aspect,实际窗口的纵横比,即x/y
        zNear,表示近处,的裁面,
        zFar表示远处的裁面,
        '''                 
        gluPerspective(45.0,1.33,0.1, 100.0)
        # 模型和视图的变换(旋转、平移、缩放) 
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        '''
        官网解释：clear buffers to preset values，用预制的值来清空缓冲区
        参数：GL_COLOR_BUFFER_BIT,颜色缓冲
        GL_DEPTH_BUFFER_BIT,深度缓冲
        GL_STENCIL_BUFFER_BIT，模板缓冲
        '''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glLoadIdentity()该函数的功能是重置当前指定的矩阵为单位矩阵
        # 当调用glLoadIdentity()之后，实际上将当前点移到了屏幕中心：类似于一个复位操作
        glLoadIdentity()
        '''
        glTranslatef(GLfloat x,GLfloat y,GLfloat z);
        函数功能：沿X轴正方向平移x个单位(x是有符号数)
        沿Y轴正方向平移y个单位(y是有符号数)
        沿Z轴正方向平移z个单位(z是有符号数)
        '''
        glTranslatef(-2.5, 0.5, -5.0)
        # 在OpenGl中设置颜色，一般可以使用glColor3f(),(1,1,1)为白色
        glColor3f( 1.0, 0.5, 0.1 )
        '''
        glPolygonMode(GLenum face,GLenum mode);face这个参数确定显示模式将适用于物体的哪些部分，控制多边形的正面和背面的绘图模式：
        GL_FRONT：表示显示模式将适用于物体的前向面（也就是物体能看到的面）GL_BACK：表示显示模式将适用于物体的后向面（也就是物体上不能看到的面）
        GL_FRONT_AND_BACK：表示显示模式将适用于物体的所有面mode这个参数确定选中的物体的面以何种方式显示（显示模式）：GL_POINT：表示只显示顶点，多边形用顶点显示
        GL_LINE：表示显示线段，多边形用轮廓显示GL_FILL：表示显示面，多边形采用填充形式
        '''
        glPolygonMode(GL_FRONT, GL_FILL)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0.0,-2.0,0.0)
        glVertex3f(0.6,-1.0,0.0)
        glVertex3f(0.9,-2.0,0.0)
        glEnd()
        '''
        glFlush()清空缓冲区，将指令送往缓硬件立即执行，但是它是将命令传送完毕之后立即返回，不会等待指令执行完毕。这些指令会在有限时间内执行完毕
        '''
        glFlush()

if __name__ == '__main__':    
    app = QtWidgets.QApplication(sys.argv)    
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(Form)    
    ui.show()    
    sys.exit(app.exec_())