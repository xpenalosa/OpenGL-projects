# Get Launcher as well as OpenGL imports
from projects.launcher import *

w, h = 500, 500
square_posx, square_posy = 0.0, 0.0
triangle_scale = 1.0


def square(size=(100, 100)):
    global square_posx, square_posy
    square_posx = (square_posx + 0.05) % w
    square_posy = (square_posy + 0.05) % h
    glTranslated(square_posx, square_posy, 0)

    glColor3f(0.25, 0.5, 0.75)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, size[1])
    glVertex2f(size[0], size[1])
    glVertex2f(size[0], 0)
    glEnd()
    glLoadIdentity()


def scale_2d_object_in_position(position=(50, 50), object_size=(1, 1),
                                scale=(1.0, 1.0)):
    pos_x = position[0] - (object_size[0] / 2 * scale[0])
    pos_y = position[1] - (object_size[1] / 2 * scale[1])
    # Multiple operations on matrix must be called in inverse order
    glTranslate(pos_x, pos_y, 0)
    glScale(scale[0], scale[1], 1.0)


def triangle(size=(100, 100)):
    global triangle_scale
    triangle_scale = (triangle_scale + 0.0005) % 1

    scale_2d_object_in_position((w//2, h//2), size, [triangle_scale]*2)

    glColor3f(0.8, 0, 0.25)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(size[0] // 2, size[1])
    glVertex2f(size[0], 0)
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
    square((50, 50))
    triangle((w // 3, h // 3))


if __name__ == "__main__":
    Launcher(display_func, (w, h)).loop()
