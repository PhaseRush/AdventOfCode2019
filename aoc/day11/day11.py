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


history = list()
instructions = 0
painted = set()
P = Program('0', 'input.txt', get_color)
while True:
    colour = P.run()
    turn = P.run()
    if colour is None or turn is None:
        break

    history.append((instructions, pos, turn, curr_dir))
    instructions += 2
    painted.add(pos)
    picture[pos[0]][pos[1]] = colour
    if turn == 0:
        curr_dir = (curr_dir + 3) % 4
    else:
        curr_dir = (curr_dir + 1) % 4
    pos = (pos[0] + DIR[curr_dir][0], pos[1] + DIR[curr_dir][1])

dir_map = {0: 'UP', 1: 'LEFT', 2: 'DOWN', 3: 'RIGHT'}

def pretty(item):
    return f'instr: {item[0]} x: {item[1][0]} y: {item[1][1]} turn: {item[2]} curr_dir: {dir_map[item[3]]}'


history = map(pretty, history)

with open('panda.cute', 'w') as file:
    for item in history:
        file.write("{}\n".format(item))

for r in range(R):
    for c in range(C):
        print('X' if picture[r][c] == 1 else ' ', end='')
    print()

print(f'painted = {len(painted)} instructions = {instructions}')
