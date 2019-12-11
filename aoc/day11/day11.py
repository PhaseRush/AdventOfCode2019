# 50ms
from aoc.Intcode import Program

R = 1000
C = 1000
picture = [[0 for _ in range(C)] for _ in range(R)]
picture[R // 2][C // 2] = 0
curr_dir = 0
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pos = (R // 2, C // 2)


def get_color():
    return picture[pos[0]][pos[1]]


instructions = 0
painted = set()
P = Program('0', 'input.txt', get_color)
while True:
    colour = P.run()
    turn = P.run()
    if colour is None or turn is None:
        break

    instructions += 2
    painted.add(pos)
    picture[pos[0]][pos[1]] = colour
    if turn == 0:
        curr_dir = (curr_dir + 3) % 4
    else:
        curr_dir = (curr_dir + 1) % 4
    pos = (pos[0] + DIR[curr_dir][0], pos[1] + DIR[curr_dir][1])

print(f'painted={len(painted)}')
for r in range(R):
    for c in range(C):
        print('X' if picture[r][c] == 1 else ' ', end='')
    print()

print(instructions)
