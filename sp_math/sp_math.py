from math import tau, sin, pi, cos, degrees


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
