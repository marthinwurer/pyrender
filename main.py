from collections import namedtuple

import numpy as np
import matplotlib.pyplot as plt

Point = namedtuple("Point", ["x", "y"])


def pixels(array):
    shape = array.shape
    height = shape[0]
    width = shape[1]
    for y in range(height):
        for x in range(width):
            s = Point(y, x)
            # output needs to be in range (-1, 1)
            c_y = (-y * 2 + height) / height  # needs to be negative so 1 is at top of screen
            c_x = (x * 2 - width) / width
            c = Point(c_x, c_y)
            yield (s, c)


def edge_func(p, v0, v1):
    return ((p.x - v0.x) * (v1.y - v0.y)) - ((p.y - v0.y) * (v1.x - v0.x))


def inside(p, v0, v1, v2):
    e01 = edge_func(p, v0, v1)
    e12 = edge_func(p, v1, v2)
    e20 = edge_func(p, v2, v0)

    return e01 >= 0 and e12 >= 0 and e20 >= 0


def main():
    """
    render a triangle.
    :return:
    """
    # Only worry about 2d right now
    height = 256
    width = 256
    # from (-1 to 1) in each dimension
    # x, y coordinates
    top = Point(0, .5)
    right = Point(.5, -.5)
    left = Point(-.5, -.5)

    output = np.zeros((height, width))  # y, x

    # pixel is pixel, x and y are screen coordinates
    for (pixel, c) in pixels(output):
        tri_x = [top[0], left[0], right[0]]
        tri_y = [top[1], left[1], right[1]]

        nw_x = min(tri_x)
        nw_y = max(tri_y)
        se_x = max(tri_x)
        se_y = min(tri_y)

        if nw_x < c.x < se_x and nw_y > c.y > se_y and inside(c, top, right, left):
            print(pixel)
            output[pixel] = 1




    plt.imshow(output)
    plt.show()

if __name__ == "__main__":
    main()