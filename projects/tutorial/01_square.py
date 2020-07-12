# Get Launcher as well as OpenGL imports
from projects.launcher import *

w, h = 500, 500


def square():
    glBegin(GL_QUADS)
    glVertex2f(w / 2, w / 2)
    glVertex2f(w / 2, w / 3)
    glVertex2f(w / 3, w / 3)
    glVertex2f(w / 3, w / 2)
    glEnd()


def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display_func():
    glLoadIdentity()
    iterate()
    glColor3f(0.25, 0.5, 0.75)
    square()


if __name__ == "__main__":
    Launcher(display_func, (w, h)).loop()
