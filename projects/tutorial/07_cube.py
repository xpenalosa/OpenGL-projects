# Get Launcher as well as OpenGL imports
from projects.launcher import *

w, h = 500, 500
rot_x, rot_y, rot_z = 0.0, 0.0, 0.0

cube_vertices = [
    [[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0]],  # back
    [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],  # above
    [[0, 0, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1]],  # below
    [[1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0, 1]],  # right
    [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0]],  # left
    [[0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]   # front
]


def rotate_3d_object(size, rx=0.0, ry=0.0, rz=0.0):
    glTranslate(size[0] / 2, size[1] / 2, size[2] / 2)
    glRotate(rz, 0, 0, 1.0)
    glRotate(ry, 0, 1.0, 0)
    glRotate(rx, 1.0, 0, 0)
    glTranslate(-size[0] / 2, -size[1] / 2, -size[2] / 2)


def cube(size=(100, 100, 100)):
    global rot_x, rot_y, rot_z
    rot_x = rot_x + 0.01
    rot_y = rot_y + 0.01
    rot_z = rot_z + 0.01

    glTranslate(w // 2 - size[0] / 2, h // 2 - size[1] / 2, 0)
    rotate_3d_object(size, rot_x, rot_y, rot_z)

    glColor3f(0.25, 0.5, 0.75)
    glBegin(GL_QUADS)
    x = 0
    for face in cube_vertices:
        glColor(x, 0.0, 0.0)
        x += 1/6
        for vertex in face:
            glVertex(vertex[0] * size[0],
                     vertex[1] * size[1],
                     vertex[2] * size[2])
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


if __name__ == "__main__":
    Launcher(display_func, (w, h)).loop()
