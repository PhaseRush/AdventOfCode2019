# 2694ms
from collections import defaultdict
from aoc.Intcode import Program

grid = defaultdict(int)


def determine_input():
    for (k, v) in grid.items():
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


Intcode = Program('0', 'input.txt', determine_input)
Intcode.P[0] = 2
score = 0
while not Intcode.halted:
    x = Intcode.run()
    y = Intcode.run()
    c = Intcode.run()
    if x == -1 and y == 0:
        score = c
    else:
        grid[(y, x)] = c

print(score)
