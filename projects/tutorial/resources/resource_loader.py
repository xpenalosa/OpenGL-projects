import numpy
from OpenGL.GL import *
from PIL import Image


def load_object(resource):
    with open(f"resources/objects/{resource}.csv", "r") as f:
        vertices, surfaces = [], []
        for line in f.readlines():
            if line and not line.startswith("#"):
                t, *values = line.split(",")
                if t == "v":
                    vertices.append([int(v) for v in values])
                if t == "s":
                    surfaces.append([int(v) for v in values])
        return vertices, surfaces


def load_texture(resource):
    img = Image.open(f"resources/textures/{resource}.png")
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB,
                 GL_UNSIGNED_BYTE, img_data)
    return texture_id
