# Get Launcher as well as OpenGL imports
from projects.launcher import *

w, h = 500, 500
cube_vertices = [
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1)
]
cube_surfaces = [
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
]


def rotate_3d_object(size, rx=0.0, ry=0.0, rz=0.0):
    glTranslate(size[0] / 2, size[1] / 2, size[2] / 2)
    glRotate(rz, 0, 0, 1.0)
    glRotate(ry, 0, 1.0, 0)
    glRotate(rx, 1.0, 0, 0)
    glTranslate(-size[0] / 2, -size[1] / 2, -size[2] / 2)


def cube(size=(100, 100, 100)):
    glTranslate(w // 2 - size[0] / 2, h // 2 - size[1] / 2, 0)
    rotate_3d_object(size, 30, 0, 0)
    rotate_3d_object(size, 0, -45, 0)

    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        for index in surface:
            glVertex3f(*[v * s for v, s in zip(cube_vertices[index], size)])
    glEnd()
    glLoadIdentity()


def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, -200.0, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display_func():
    glLoadIdentity()
    iterate()
    cube((100, 100, 100))


def enable_lighting(light_pos):
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glLightfv(GL_LIGHT0, GL_POSITION, [*light_pos, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1])
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.001)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.005)
    glEnable(GL_LIGHT0)


if __name__ == "__main__":
    launcher = Launcher(display_func, (w, h))
    enable_lighting(light_pos=[w/4, h*3/5, 0])
    launcher.loop()
