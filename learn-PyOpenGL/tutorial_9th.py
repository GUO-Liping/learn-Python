# -*- coding:utf-8 -*-
# 本程序利用OpenGL绘制一个洋红色矩形
# Reference： https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500

# ---Section 1---
def square():
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(100, 100) # Coordinates for the bottom left point
    glVertex2f(200, 100) # Coordinates for the bottom right point
    glVertex2f(200, 200) # Coordinates for the top right point
    glVertex2f(100, 200) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

# This alone isn't enough to draw our square

# Add this function before Section 2 of the code above i.e. the showScreen function（保持正方形不消失）
def iterate():
    # glViewport(GLint x,GLint y,GLsizei width,GLsizei height)，x，y 以像素为单位，指定了视口的左下角位置。width，height 表示这个视口矩形的宽度和高度，根据窗口的实时变化重绘窗口
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho是创建一个正交平行的视景体，glOrtho(left, right, bottom, top, near, far)
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# ---Section 2---
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 0.5)  # Set the color to pink
    square()  # Draw a square using our function
    glutSwapBuffers()

#---Section 3---
glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop
