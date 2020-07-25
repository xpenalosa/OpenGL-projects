# Get Launcher as well as OpenGL imports
from projects.launcher import *
from projects.tutorial.resources import resource_loader

w, h = 500, 500
rot_x, rot_y, rot_z = 0.0, 0.0, 0.0
cube_vertices, cube_surfaces = resource_loader.load_object("cube")
texture_coords = {
        0: (0, 0),
        1: (0, 1),
        2: (1, 1),
        3: (1, 0)
    }


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

    for surface in cube_surfaces:
        glBegin(GL_QUADS)
        tc = 0
        for index in surface:
            glVertex3f(*[v * s for v, s in zip(cube_vertices[index], size)])
            glTexCoord2f(*texture_coords[tc])
            tc += 1
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
    launcher = Launcher(display_func, (w, h))
    cube_texture = resource_loader.load_texture("simple100px")
    launcher.loop()
