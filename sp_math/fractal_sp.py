import random
from math import cos, tau, sin, sqrt, pi

from PIL import Image

from sp_math.colors import colors
from sp_math.draw_sp import draw_star_polygon


def fractal_distance(n, m, r):
    theta = pi / n
    return r * sin(pi - 2 * theta) / sin(theta)


def inverse_fractal_distance(n, m, d):
    theta = pi / n
    return d * sin(theta) / sin(pi - 2 * theta)


def some_fucking_magical_calculation(n, m, r):
    theta = pi / n
    fumo = 1 + sin(pi - 2 * theta) / sin(theta)
    return fractal_distance(n, m, inverse_fractal_distance(n, m, r) / fumo)


def draw_fractal_sp(
        image: Image,  # Image to draw on
        n: int,  # Number of vertices
        m: int,  # Step
        r: float,  # distance between to adjacent stars / fractal segments
        center: tuple[int, int],  # center of the star / fractal segment
        maxdepth: int,  # maximum depth
        depth: int | None = None,  # current depth
        rotation: float = 0,  # rotation
):

    if depth == 0:
        draw_star_polygon(
            image,
            n,
            m,
            int(r),
            center,
            (0, 0, 0, 255),
            1,
            rotation
        )
        return

    points = [center]
    tweak = tau / n / 2
    rotations = [0.0]
    rotations += [tau / n * i + tweak for i in range(n)]
    for angle in [tau / n * i + tweak for i in range(n)]:
        points.append(
            (
                center[0] + r * cos(angle),
                center[1] + r * sin(angle)
            )
        )
    if depth is None:
        depth = maxdepth - 1
    else:
        depth -= 1
    for point, tweak in zip(points, rotations):
        draw_fractal_sp(
            image,
            n,
            m,
            inverse_fractal_distance(n, m, r),
            point,
            maxdepth,
            depth,
            tweak
        )
