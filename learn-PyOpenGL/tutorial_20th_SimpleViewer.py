"""About the simplest PyQt OpenGL example with decent interaction"""
import sys
from PyQt5 import QtWidgets
from OpenGL.GL import *
from OpenGL.GLU import *

from tutorial_20th_simple_viewer import SimpleViewer

width = 800
height = 600
aspect = width/height

def resize( w, h ):
    width = w
    height = h
    aspect = w/h
    glViewport( 0, 0, width, height )

def initialize():
    glEnable(GL_DEPTH_TEST)
    glClearColor( 0.7, 0.7, 1.0, 0.0 )

def render():
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    gluPerspective( 45.0, aspect, 0.1, 10.0 )

    glMatrixMode( GL_MODELVIEW )
    glLoadIdentity()
    gluLookAt( 0.0, 2.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 )

    glPointSize(5.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(  1.0, 0.0, 0.0 )
    glVertex3f( 1.0, 0.0, 0.0 )
    glVertex3f( 0.0, 0.0, 0.0 )
    glColor3f(  0.0, 1.0, 0.0 )
    glVertex3f( 0.0, 1.0, 0.0 )
    glVertex3f( 0.0, 0.0, 0.0 )
    glColor3f(  0.0, 0.0, 1.0 )
    glVertex3f( 0.0, 0.0, 1.0 )
    glVertex3f( 0.0, 0.0, 0.0 )
    glEnd()

def mouse_move( evt ):
    print('Mouse move {}: [{},{}]'.format(evt.button(),evt.x(),evt.y()) )

def mouse_press( evt ):
    print('Mouse press {}: [{},{}]'.format(evt.button(),evt.x(),evt.y()) )

def mouse_release( evt ):
    print('Mouse release {}: [{},{}]'.format(evt.button(),evt.x(),evt.y()) )

def key_press( evt ):
    print('Key press {}'.format(evt.key()) )

def key_release( evt ):
    print('Key release {}'.format(evt.key()) )

# create the QApplication
app = QtWidgets.QApplication(sys.argv)

# set up the display
viewer = SimpleViewer()
viewer.resize_cb.connect( resize )
viewer.initialize_cb.connect( initialize )
viewer.render_cb.connect( render )

# keyboard & mouse interactions
viewer.key_press_cb.connect( key_press )
viewer.key_release_cb.connect( key_release )
viewer.mouse_press_cb.connect( mouse_press )
viewer.mouse_release_cb.connect( mouse_release )
viewer.mouse_move_cb.connect( mouse_move )

# resize the window
viewer.resize( width, height )
viewer.show()

# main loop
try:
    sys.exit(app.exec_())
except SystemExit:
    pass