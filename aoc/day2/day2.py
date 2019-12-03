# 146 ms

start_state = list(map(int, open('input.txt', 'r').readline().split(',')))


def try_codes(noun, verb):
    opcodes = start_state[:]
    opcodes[1] = noun
    opcodes[2] = verb

    curr_idx = 0
    while curr_idx < len(opcodes) and opcodes[curr_idx] != 99:
        this_op = opcodes[curr_idx]
        first = opcodes[opcodes[curr_idx + 1]]
        second = opcodes[opcodes[curr_idx + 2]]
        third = opcodes[curr_idx + 3]
        if this_op is 1:
            opcodes[third] = first + second
        elif this_op is 2:
            opcodes[third] = first * second

        curr_idx += 4

    return opcodes[0]


for noun in range(100):
    for verb in range(100):
        if try_codes(noun, verb) == 19690720:
            print(noun * 100 + verb)
