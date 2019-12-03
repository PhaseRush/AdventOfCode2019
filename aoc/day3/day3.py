# 123 ms

(A, B) = map(lambda x: x.split(','), open('input.txt', 'r').read().split('\n'))

opX = {'U': 0, 'D': 0, 'R': +1, 'L': -1}
opY = {'U': +1, 'D': -1, 'R': 0, 'L': 0}


def get_points(commands):
    points = {}
    x = 0
    y = 0
    path_len = 0

    for cmd in commands:
        op = cmd[0]
        num = int(cmd[1:])

        for i in range(num):
            x += opX[op]
            y += opY[op]
            path_len += 1
            if (x, y) not in points:
                points[(x, y)] = path_len
    return points


p_a = get_points(A)
p_b = get_points(B)
inter_points = {k: p_a[k] + p_b[k] for k in p_a.keys() & p_b.keys()}
print(inter_points[min(inter_points, key=inter_points.get)])
