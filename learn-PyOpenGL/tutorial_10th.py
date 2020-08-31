# -*- coding:utf-8 -*-
#!/usr/bin/env pythonw
# 本程序利用OpenGL绘制一个彩色三角形
# Reference： http://openglsamples.sourceforge.net/triangle_py.html

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

ESCAPE = '\033'

window = 0
rtri = 0.0

def InitGL(Width, Height):             
    glClearColor(0.0, 0.0, 0.0, 0.0)  
    glClearDepth(1.0)                 
    glDepthFunc(GL_LESS)              
    glEnable(GL_DEPTH_TEST)           
    glShadeModel(GL_SMOOTH)           
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                  
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:       
        Height = 1

    glViewport(0, 0, Width, Height)     
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global rtri, rquad

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
    glLoadIdentity()                   
    # 平移试图x，y，z
    glTranslatef(0.0,0.0,-6.0)            

    '''
    对于矩阵的操作都是对于矩阵栈的栈顶来操作的。当前矩阵即为矩阵栈的栈顶元素，
    而对当前矩阵进行平移、旋转等的变换操作也同样是对栈顶矩阵的修改。所以我们在变换之前调用giPushMatrix()的话，
    就会把当前状态压入第二层，不过此时栈顶的矩阵也与第二层的相同。
    当经过一系列的变换后，栈顶矩阵被修改，此时调用glPopMatrix()时，栈顶矩阵被弹出，且又会恢复为原来的状态。
    '''
    glPushMatrix()
    glBegin(GL_TRIANGLES)                 
    glColor3f(1.0,0.0,0.0)           
    glVertex3f(0.0, 0.0, 0.0)        
    glColor3f(0.0,0.0,1.0)           
    glVertex3f(1.0,0.0,0.0)        
    glColor3f(0.0,1.0,0.0)           
    glVertex3f(1.0,1.0, 0.0)        
    glEnd()
    glPopMatrix()

    # glutSwapBuffers函数是OpenGL中GLUT工具包中用于实现双缓冲技术的一个重要函数。该函数的功能是交换两个缓冲区指针。
    glutSwapBuffers()

def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Python OpenGL Triangle")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(640, 480)
    glutMainLoop()

# print "Hit ESC key to quit."
main()
