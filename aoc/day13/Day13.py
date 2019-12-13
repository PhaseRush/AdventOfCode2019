# 2694ms
from collections import defaultdict
from aoc.Intcode import Program

Grid = defaultdict(int)


def determine_input():
    # xs = sorted([x for (x, _) in Grid])
    # ys = sorted([y for (_, y) in Grid])
    for (k, v) in Grid.items():
        if v == 3:
            paddle = k
        elif v == 4:
            ball = k
    if ball[1] < paddle[1]:
        return -1
    elif ball[1] > paddle[1]:
        return 1
    else:
        return 0


P = Program('0', 'input.txt', determine_input)
P.P[0] = 2
score = 0
while not P.halted:
    x = P.run()
    y = P.run()
    c = P.run()
    if x == -1 and y == 0:
        score = c
    else:
        Grid[(y, x)] = c
print(score)
