from itertools import cycle
from math import gcd, tau

from PIL import Image, ImageDraw

from sp_math.colors import colors
from sp_math.draw_sp import calculate_n_gon_vertices, draw_star_polygon


def smoothing_function(n: int | float):
    return 3 * n ** 2 - 2 * n ** 3


def lerp(min, max, new_min, new_max, value):
    return (value - min) / (max - min) * (new_max - new_min) + new_min


def draw_exploding_polygon(
        n: int,
        m: int,
        size: tuple[int, int],
        t: float
):
    k = gcd(n, m)
    assert k > 1

    d = min(size) // 2 * .8
    start_r = min(size) // 2 * .8
    final_r = min(min(size) // 2 * .19, tau * d / k * .49)

    sub_n = n // k
    sub_m = m // k

    final_points = calculate_n_gon_vertices(k)

    positions = []
    for final_point in final_points:
        positions.append(
            (
                final_point[0] * smoothing_function(t),
                final_point[1] * smoothing_function(t)
            )
        )

    rotations = [tau / n * i for i in range(n)]

    current_radius = lerp(0, 1, start_r, final_r, t)

    image = Image.new('RGBA', size, (0, 0, 0, 0))

    for position, rotation, color in zip(positions, rotations, cycle(colors)):
        draw_star_polygon(
            image,
            sub_n,
            sub_m,
            current_radius,
            (
                position[0] * d + size[0] // 2,
                position[1] * d + size[1] // 2
            ),
            color,
            5,
            rotation
        )

    return image
