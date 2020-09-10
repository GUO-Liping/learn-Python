# -*- coding:utf-8 -*-
#!/usr/bin/env python

# 本程序利用OpenGL绘制可控制转动的QT-三维
# 采用list方式显示顶点
# Reference： http://nullege.com/codes/show/src%40p%40y%40pyqt5-HEAD%40examples%40opengl%40samplebuffers.py/51/PyQt5.QtOpenGL.QGLWidget/python
# Reference：（讲解pyqtSignal链接）https://www.cnblogs.com/archisama/p/5454200.html

import sys
import math
  
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMessageBox, QSlider, QWidget)
from PyQt5.QtOpenGL import QGLWidget
  
try:
	from OpenGL import GL
except ImportError:
	app = QApplication(sys.argv)
	QMessageBox.critical(None, "OpenGL hellogl",
			"PyOpenGL must be installed to run this example.")
	sys.exit(1)
  
  
class Window(QWidget):
	def __init__(self):
		super(Window, self).__init__()
  
		self.glWidget = GLWidget()
		mainLayout = QHBoxLayout()
		mainLayout.addWidget(self.glWidget)
		self.setLayout(mainLayout)
		self.setWindowTitle("Hello GL")
  
class GLWidget(QGLWidget):
  
	def __init__(self, parent=None):
		super(GLWidget, self).__init__(parent)
  
		self.object = 0
		self.xRot = 0
		self.yRot = 0
		self.zRot = 0
  
		self.lastPos = QPoint()

		# 设置QT图形颜色，静态函数fromRgb(), fromHsv(),fromCmyk()可以通过指定特定值返回需要的颜色
		# CYMK:青色Cyan、洋红色Magenta、黄色Yellow，黑色Black
		self.trolltechGreen = QColor.fromCmykF(0.50, 0.50, 0.1, 0.0)
		# 设置界面背景色
		self.trolltechPurple = QColor.fromCmykF(0.39, 0.39, 0.39, 0.0)
  
	def minimumSizeHint(self):
		# QSize 类代表一个矩形区域的大小，实现在 QtCore 共享库中。它可以认为是由一个整型的宽度和整型的高度组合
		return QSize(50, 50)
  
	def sizeHint(self):
		return QSize(400, 400)
	
	def normalizeAngle(self, angle):
		print('angle=',angle)
		if angle < 0:
			angle += 360 * 16
		elif angle >360 * 16:
			angle -= 360 * 16
		else:
			pass
		return angle
		  
	def setXRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.xRot:
			self.xRot = angle
			self.update()
			# 也可以是self.updateGL()
  
	def setYRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.yRot:
			self.yRot = angle
			self.update()
			# 也可以是self.updateGL()
  
	def setZRotation(self, angle):
		angle = self.normalizeAngle(angle)
		if angle != self.zRot:
			self.zRot = angle
			self.update()
			# 也可以是self.updateGL()
  
	# mousePressEvent鼠标键按下时调用
	def mousePressEvent(self, event):
		# pos() - 返回相对于控件空间的QPoint对象;
		self.lastPos = event.localPos()
		print('lastPos1.x = ',self.lastPos.x())
		print('lastPos1.y = ',self.lastPos.y())

	def mouseMoveEvent(self, event):
		# x() - 返回当前控件上鼠标的x坐标
		dx = -event.x() + self.lastPos.x()
		print('event.x=', event.x())
		dy = -event.y() + self.lastPos.y()
		print('event.y=', event.y())
		print('lastPos.x2 = ',self.lastPos.x())
		print('lastPos.y2 = ',self.lastPos.y())

		if event.buttons() == Qt.LeftButton:
			self.setXRotation(self.xRot + 8*dy)
			self.setYRotation(self.yRot + 8*dx)
		elif event.buttons() == Qt.RightButton:
			self.setXRotation(self.xRot + 8*dy)
			self.setZRotation(self.zRot + 8*dx)
 
		self.lastPos = event.pos()


	def initializeGL(self):
		self.qglClearColor(self.trolltechPurple.darker())
		self.object = self.makeObject()
		GL.glShadeModel(GL.GL_FLAT)
		GL.glEnable(GL.GL_DEPTH_TEST)
		GL.glEnable(GL.GL_CULL_FACE)
  
	def paintGL(self):
		'''
		clear buffers to preset values，用预制的值来清空缓冲区
		参数：
		GL_COLOR_BUFFER_BIT,颜色缓冲
		GL_DEPTH_BUFFER_BIT,深度缓冲
		GL_STENCIL_BUFFER_BIT，模板缓冲
		'''
		GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
		GL.glLoadIdentity()
		GL.glTranslated(0.0, 0.0, -6.0)

		# GL.glRotated函数功能：以点(0,0,0)到点(x,y,z)为轴，旋转angle角度；
		GL.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
		GL.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
		GL.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)
		GL.glCallList(self.object)
 
	def resizeGL(self, width, height):
		side = min(width, height)
		if side < 0:
			return
 		
		'''
		Viewport(GLint x,GLint y,GLsizei width,GLsizei height)
		x，y 以像素为单位，指定了视口的左下角位置
		width，height 表示这个视口矩形的宽度和高度，根据窗口的实时变化重绘窗口。
		# //为向下取整
		''' 

		GL.glViewport(0, 0, side, side)  
		GL.glMatrixMode(GL.GL_PROJECTION)
		GL.glLoadIdentity()
		# 正交投影glOrtho(left, right, bottom, top, near, far)
		# 透视投影glFrustum(left, right, bottom, top, near, far)
		# glFrustum()中near和far表示离视点的远近，它们总为正值(near/far 必须>0)
		GL.glFrustum(-0.5, +0.5, +0.5, -0.5, 5.0, 8.0)
		GL.glMatrixMode(GL.GL_MODELVIEW)
  
	def makeObject(self):
		# glGenLists()会生成一组连续的空的显示列表，参数range为空列表数量
		genList = GL.glGenLists(1)
		GL.glNewList(genList, GL.GL_COMPILE)
  
		GL.glBegin(GL.GL_QUADS)
		NumSectors = 20
  
		for i in range(NumSectors):
			angle1 = (i * 2 * math.pi) / NumSectors
			x1 = 0.20 * math.cos(angle1)
			y1 = 0.20 * math.sin(angle1)
			x2 = 0.30 * math.cos(angle1)
			y2 = 0.30 * math.sin(angle1)
  
			angle2 = ((i + 1) * 2 * math.pi) / NumSectors
			x3 = 0.30 * math.cos(angle2)
			y3 = 0.30 * math.sin(angle2)
			x4 = 0.20 * math.cos(angle2)
			y4 = 0.20 * math.sin(angle2)
  
			# 绘制上下表面
			self.quad(x1, y1, x2, y2, x3, y3, x4, y4)
			# 绘制侧面  
			self.extrude(x2, y2, x3, y3)
			self.extrude(x4, y4, x1, y1)
  
		GL.glEnd()
		GL.glEndList()
  
		return genList
  
	def quad(self, x1, y1, x2, y2, x3, y3, x4, y4):
		# self.qglColor(self.trolltechGreen)
		GL.glColor3f(112/255,112/255,235/255)
  
		GL.glVertex3d(x1, y1, -0.05)
		GL.glVertex3d(x2, y2, -0.05)
		GL.glVertex3d(x3, y3, -0.05)
		GL.glVertex3d(x4, y4, -0.05)
  
		GL.glVertex3d(x4, y4, +0.05)
		GL.glVertex3d(x3, y3, +0.05)
		GL.glVertex3d(x2, y2, +0.05)
		GL.glVertex3d(x1, y1, +0.05)
  
	def extrude(self, x1, y1, x2, y2):
		self.qglColor(self.trolltechGreen.darker(250 + int(100 * x1)))
  
		GL.glVertex3d(x1, y1, +0.05)
		GL.glVertex3d(x2, y2, +0.05)
		GL.glVertex3d(x2, y2, -0.05)
		GL.glVertex3d(x1, y1, -0.05)

if __name__ == '__main__':
  
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())