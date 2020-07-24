from OpenGL.GL import *
from OpenGL.GLUT import *


class Launcher:

    def __init__(self, display_function, win_size=(500, 500)):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(*win_size)
        glutInitWindowPosition(0, 0)
        glutCreateWindow("OpenGL Coding Practice")
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        self.func = display_function

    def display_func(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.func()
        glutSwapBuffers()

    def loop(self):
        glutIdleFunc(self.display_func)
        glutDisplayFunc(self.display_func)
        glutMainLoop()


if __name__ == "__main__":
    Launcher(lambda: None).loop()
