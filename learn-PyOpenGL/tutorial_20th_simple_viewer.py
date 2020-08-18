# simple_viewer.py

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtOpenGL
import sys

class SimpleViewer(QtOpenGL.QGLWidget):

    initialize_cb    = QtCore.pyqtSignal()
    resize_cb        = QtCore.pyqtSignal(int,int)
    idle_cb          = QtCore.pyqtSignal()
    render_cb        = QtCore.pyqtSignal()

    mouse_move_cb    = QtCore.pyqtSignal( QtGui.QMouseEvent )
    mouse_press_cb   = QtCore.pyqtSignal( QtGui.QMouseEvent )
    mouse_release_cb = QtCore.pyqtSignal( QtGui.QMouseEvent )
    mouse_wheel_cb   = QtCore.pyqtSignal( QtGui.QWheelEvent )

    key_press_cb     = QtCore.pyqtSignal( QtGui.QKeyEvent )
    key_release_cb   = QtCore.pyqtSignal( QtGui.QKeyEvent )

    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent( self, evt ):
        self.mouse_move_cb.emit( evt )

    def mousePressEvent( self, evt ):
        self.mouse_press_cb.emit( evt )

    def mouseReleaseEvent( self, evt ):
        self.mouse_release_cb.emit( evt )

    def keyPressEvent( self, evt ):
        self.key_press_cb.emit(evt)

    def keyReleaseEvent( self, evt ):
        self.key_release_cb.emit(evt)

    def initializeGL(self):
        self.initialize_cb.emit()

    def resizeGL(self, width, height):
        if height == 0: height = 1
        self.resize_cb.emit(width,height)

    def paintGL(self):
        self.render_cb.emit()