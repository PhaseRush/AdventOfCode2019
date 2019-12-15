# 97797 ms F in chat
from collections import defaultdict, deque

from aoc.Intcode import Program

maze = defaultdict(int)
paths = {}  # path from (0,0) to (r,c)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
y, x = 0, 0
curr_dist = 0
path = None
move = None
oxy = None

q = deque()
for i in range(4):  # to explore in all 4 directions
    q.append(((dy[i], dx[i]), (0, 0), i))

visited = set()
paths[(0, 0)] = []

flips = {0: 1, 1: 0, 2: 3, 3: 2}


def flip_direction(dir):
    return flips[dir]


def flip_path(path):
    return [flip_direction(d) for d in reversed(path)]


def get_input():
    global path, move, target, q
    if not path:
        while True:
            if not q:  # explored everything, start part 2
                depth = {}
                q = deque([(oxy, 0)])
                while len(q) > 0:
                    (this_y, this_x), this_depth = q.popleft()
                    if maze[(this_y, this_x)] == 1:
                        continue
                    if (this_y, this_x) in depth:
                        continue
                    depth[(this_y, this_x)] = this_depth
                    for dd in range(4):
                        rr, cc = this_y + dy[dd], this_x + dx[dd]
                        q.append(((rr, cc), this_depth + 1))
                print(f'part 2 = {max([d for _, d in depth.items()])}')
                exit(9001)
            target, parent, new = q.popleft()
            if target in visited:  # explored before, exit
                continue
            visited.add(target)
            path = paths[parent] + [new] + flip_path(paths[parent])
            path = deque(path)
            break
    move = path.popleft()
    return move + 1


P = Program('0', 'input.txt', get_input)
t = 0
part1 = False
while not P.halted:
    status = P.run()
    rr, cc = y + dy[move], x + dx[move]
    if status == 0:
        maze[(rr, cc)] = 1
    elif status in [1, 2]:
        if (rr, cc) not in paths:  # since havent been here before, record the path we took
            paths[(rr, cc)] = paths[(y, x)] + [move]
        y += dy[move]
        x += dx[move]
        if (y, x) == target:  # invalid place, undo move
            path.appendleft(flip_direction(move))
        maze[(y, x)] = 0
        for i in range(4):  # add 4 adjacent
            new_place = (y + dy[i], x + dx[i])
            if new_place not in visited:
                q.append((new_place, (y, x), i))
        if status == 2:
            if not part1:
                print(f'part 1 = {len(paths[(y, x)])}')
                part1 = True
            oxy = (y, x)
