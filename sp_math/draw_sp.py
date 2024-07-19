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
    edges = []
    n = len(vertices)
    usedVertices = 0
    shift = 0
    while usedVertices < n:
        start_i = shift
        i1 = start_i
        i2 = start_i + m
        i2 %= n
        edge = (vertices[i1], vertices[i2])
        if edge not in edges:
            edges.append(edge)
        while i2 != start_i:
            i1 = i2
            i2 += m
            i2 %= n
            edge = (vertices[i1], vertices[i2])
            if edge not in edges:
                edges.append(edge)
            usedVertices += 1
        shift += 1

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

    return image


def side_length(n, m, r):
    alpha = tau / n * m
    return 2 * r * sin(alpha / 2)


def perimeter(n, m, r):
    return side_length(n, m, r) * n


def area(n, m, r):
    a = r * r * n / 2
    alpha = pi / n * (n - 2 * m)
    beta = tau / n
    b = (1 - cos(beta)) * sin(alpha + beta)
    c = (1 - cos(alpha + beta))
    return a * (sin(beta) - (b / c))

def oriented_area(n, m, r):
    total = 0
    for cur_m in range(m, 0, -1):
        if (m - cur_m) % 2 == 0:
            total += area(n, cur_m, r)
        else:
            total -= area(n, cur_m, r)

        alpha = (tau / 4 * (n - 2 * cur_m)) / n
        beta = tau / n / 2
        gamma = tau / 2 - alpha - beta

        r *= sin(alpha) / sin(gamma)
    return total


def vertex_angle(n, m):
    return degrees(pi / n * (n - 2 * m))


def central_angle(n):
    return degrees(tau / n)
