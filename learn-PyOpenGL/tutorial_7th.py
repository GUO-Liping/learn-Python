# OpenGL显示白色背景散点抛物线
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-5.0,5.0,-5.0,5.0)

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.2,0.6)
    glPointSize(3.0)

    glBegin(GL_POINTS)
    for x in arange(-5.0,5.0,0.1):#from -5.0 to 5.0 plus 0.1 every time
        y=x*x
        glVertex2f(x,y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,100)
    glutInitWindowSize(400,400)
    glutCreateWindow("Function Plotter")
    glutDisplayFunc(plotfunc)

    init()
    glutMainLoop()
main()