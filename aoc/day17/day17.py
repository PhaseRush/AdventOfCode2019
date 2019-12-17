# 564 ms
from aoc.Intcode import Program


def next_input():
    return 0


computer = Program('0', 'input.txt', next_input)

char_list = []
while not computer.halted:
    char_out = computer.run()
    if char_out is None:
        break
    char_list.append(char_out)

string = ''.join(chr(i) for i in char_list)

print(string)

matrix = [list(line) for line in string.split('\n')]

accumulator = 0
for y in range(43):
    for x in range(len(matrix[3])):
        try:
            if matrix[y][x] == matrix[y - 1][x] == matrix[y + 1][x] == matrix[y][x - 1] == matrix[y][x + 1] == '#':
                accumulator += y * x
        except:
            pass
        # print(matrix[y][x], end='')

    # print(y, x)
print(accumulator)

prog = "A,B,A,B,A,C,B,C,A,C\n"
A = "L,6,R,12,L,6\n"
B = "R,12,L,10,L,4,L,6\n"
C = "L,10,L,10,L,4,L,6\n"
last = "n\n"

all_instr = prog + A + B + C + last
move_idx = 0


def next_move():
    global move_idx
    move_idx += 1
    return ord(all_instr[move_idx - 1])


computer = Program('0', 'input.txt', next_move)
outputs = []
while not computer.halted:
    outputs.append(computer.run())

print(list(reversed(outputs)))
