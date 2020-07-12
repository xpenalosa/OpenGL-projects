# Get Launcher as well as OpenGL imports
from projects.launcher import *

w, h = 500, 500


def square(size=(100, 100), pos=(0, 0)):
    glColor3f(0.25, 0.5, 0.75)
    glBegin(GL_QUADS)
    glVertex2f(pos[0], pos[1])
    glVertex2f(pos[0] + size[0], pos[1])
    glVertex2f(pos[0] + size[0], pos[1] + size[1])
    glVertex2f(pos[0], pos[1] + size[1])
    glEnd()
    glLoadIdentity()


def triangle(size=(100, 100), pos=(0, 0)):
    glColor3f(0.8, 0, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(pos[0], pos[1])
    glVertex2f(pos[0] + size[0] // 2, pos[1] + size[1])
    glVertex2f(pos[0] + size[0], pos[1])
    glEnd()
    glLoadIdentity()


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
    square((50, 50), (100, 400))
    triangle((w // 3, h // 3), (w // 3, h // 3))


if __name__ == "__main__":
    Launcher(display_func, (w, h)).loop()
