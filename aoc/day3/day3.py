# 204ms

(A, B) = map(lambda x: x.split(','), open('input.txt', 'r').read().split('\n'))

fx = {'U': lambda i: i, 'D': lambda i: i, 'R': lambda i: i + 1, 'L': lambda i: i - 1}
fy = {'U': lambda i: i + 1, 'D': lambda i: i - 1, 'R': lambda i: i, 'L': lambda i: i}


def get_points(commands):
    points = {}
    x = 0
    y = 0
    path_len = 0

    for cmd in commands:
        op = cmd[0]
        num = int(cmd[1:])

        for _ in range(num):
            x = fx[op](x)
            y = fy[op](y)
            path_len += 1
            if (x, y) not in points:
                points[(x, y)] = path_len
    return points


p_a = get_points(A)
p_b = get_points(B)
inter_points = {k: p_a[k] + p_b[k] for k in p_a.keys() & p_b.keys()}
print(inter_points[min(inter_points, key=inter_points.get)])
