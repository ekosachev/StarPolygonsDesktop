from itertools import cycle
from math import tau, cos, sin, pi, degrees

from PIL import Image, ImageDraw

from sp_math.colors import colors


def calculate_n_gon_vertices(n: int, rotation: float = 0) -> list[tuple[float, float]]:
    return [
        (
            cos(tau * k / n + rotation),
            sin(tau * k / n + rotation)
        )
        for k in range(n)
    ]


def calculate_sp_edges(vertices: list[tuple[float, float]], m: int) \
        -> list[tuple[tuple[float, float], tuple[float, float]]]:

    edges = [
        (vertices[i], vertices[(i+m) % len(vertices)]) for i in range(len(vertices))
    ]

    return edges


def draw_star_polygon(
        image: Image,
        n: int,
        m: int,
        r: int,
        center: tuple[int, int],
        color: tuple[int, int, int, int],
        width: int,
        rotation: float = 0,
):
    points = calculate_n_gon_vertices(n, rotation)
    edges = calculate_sp_edges(points, m)

    imageDraw = ImageDraw.Draw(image)
    for edge in edges:
        imageDraw.line(
            (
                    (
                        edge[0][0] * r + center[0],
                        edge[0][1] * r + center[1]
                    ),
                    (
                        edge[1][0] * r + center[0],
                        edge[1][1] * r + center[1]
                    )
            ),
            fill=color,
            width=width
        )


def draw_sp(
        n: int,
        m: int,
        radius: float,
        draw_n_gon: bool,
        draw_inner_sp: bool,
        draw_vertex_coords: bool,
        draw_circumcircle: bool,
        size: tuple[int, int],
):
    image = Image.new('RGBA', size, (0, 0, 0, 0))
    imageDraw = ImageDraw.Draw(image)
    r = int(min(size[0] // 2, size[1] // 2) * .8)

    draw_star_polygon(
        image,
        n,
        m,
        r,
        (size[0] // 2, size[1] // 2),
        (0, 0, 0, 255),
        5
    )

    if draw_n_gon:
        draw_star_polygon(
            image,
            n,
            1,
            r,
            (size[0] // 2, size[1] // 2),
            (255, 0, 0, 255),
            3
        )

    if draw_inner_sp:
        alpha = (tau / 4 * (n - 2 * m)) / n
        beta = pi / n
        gamma = tau / 2 - alpha - beta
        theta = tau / n
        new_r = int(r * (sin(alpha) / sin(gamma)))
        for cur_m, color in zip(range(m - 1, 0, -1), cycle(colors)):
            rot = pi / n * ((m - cur_m) % 2)
            draw_star_polygon(
                image,
                n,
                cur_m,
                new_r,
                (size[0] // 2, size[1] // 2),
                color,
                5,
                rot,
            )

            alpha = (tau / 4 * (n - 2 * cur_m)) / n
            beta = theta / 2
            gamma = tau / 2 - alpha - beta

            new_r *= sin(alpha) / sin(gamma)

    if draw_vertex_coords:
        for point in calculate_n_gon_vertices(n):
            imageDraw.circle(
                (
                    point[0] * r + size[0] // 2,
                    point[1] * r + size[1] // 2
                ),
                fill=(255, 0, 255, 255),
                radius=5,
            )
            imageDraw.text(
                (
                    point[0] * r + size[0] // 2 + 10,
                    point[1] * r + size[1] // 2 - 10
                ),
                fill=(0, 255, 0, 255),
                font_size=20,
                text=f"({(point[0] * radius):.2f}, {(point[1] * (- radius)):.2f})"
            )

    if draw_circumcircle:
        imageDraw.ellipse(
            (
                size[0] // 2 - r,
                size[1] // 2 - r,
                size[0] // 2 + r,
                size[1] // 2 + r
            ),
            outline=(0, 0, 255, 255),
            width=5,
        )

    return image


