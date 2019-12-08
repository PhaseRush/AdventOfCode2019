# 45 ms
import itertools as nya

start_state = list(map(int, open('input.txt', 'r').readline().split(',')))


def run_tape(inputs, idx, state):
    codes = state

    while idx < len(codes) and codes[idx] != 99:
        digits = [int(x) for x in str(codes[idx])]
        while len(digits) < 4:
            digits = [0] + digits

        opcode = digits[-1] + digits[-2] * 10
        digits = [0, 0] + digits[:-2]

        increment = 4  # default program counter increment is 4
        if opcode is 1:
            first, second, third = codes[idx + 1], codes[idx + 2], codes[idx + 3]
            codes[third] = (first if digits[3] == 1 else codes[first]) + (second if digits[2] == 1 else codes[second])
        elif opcode is 2:
            first, second, third = codes[idx + 1], codes[idx + 2], codes[idx + 3]
            codes[third] = (first if digits[3] == 1 else codes[first]) * (second if digits[2] == 1 else codes[second])
        elif opcode is 3:
            codes[codes[idx + 1]] = inputs.pop(0)
            increment = 2
        elif opcode is 4:
            return (codes[codes[idx + 1]]), idx + 2, codes
            # increment = 2
        elif opcode is 5:
            first, second = codes[idx + 1], codes[idx + 2]
            if (first if digits[3] == 1 else codes[first]) != 0:
                idx = (second if digits[2] == 1 else codes[second])
                increment = 0
            else:
                increment = 3
        elif opcode is 6:
            first, second = codes[idx + 1], codes[idx + 2]
            if (first if digits[3] == 1 else codes[first]) == 0:
                idx = second if digits[2] == 1 else codes[second]
                increment = 0
            else:
                increment = 3
        elif opcode is 7:
            first, second, third = codes[idx + 1], codes[idx + 2], codes[idx + 3]
            if (first if digits[3] == 1 else codes[first]) < (second if digits[2] == 1 else codes[second]):
                codes[third] = 1
            else:
                codes[third] = 0
        elif opcode is 8:
            first, second, third = codes[idx + 1], codes[idx + 2], codes[idx + 3]
            if (first if digits[3] == 1 else codes[first]) == (second if digits[2] == 1 else codes[second]):
                codes[third] = 1
            else:
                codes[third] = 0
        idx += increment

    return None, idx, None


def best_boost(permutation):
    max_out = -10000000000
    indexes = [0, 0, 0, 0, 0]  # starting indexes 0 for all amps
    outputs = [0, 0, 0, 0, 0]  # outputs 0 for all amps
    inputs = [[permutation[i]] for i in range(5)]  # init inputs are the phase themselves
    inputs[0].append(0)  # first amp starts with phase number, then 0
    states = [list(start_state) for _ in range(5)] # persist state, NOT NEEDED FOR THE BIG INPUT, CONFIRMED WITH MANY PPL, BUT NEED FOR EXAMPLE

    is_done = False
    while not is_done:
        for j in range(5):
            new_val, new_idx, new_state = run_tape(inputs[j], indexes[j], states[j])  # run it at the proper settings
            if new_val is None:
                return max(max_out, outputs[-1])
            states[j] = new_state
            indexes[j] = new_idx  # update idx
            outputs[j] = new_val  # update output
            inputs[(j + 1) % 5].append(new_val)  # (j+1) %5 because input to next amp


print(max(best_boost(permutation) for permutation in list(nya.permutations([5, 6, 7, 8, 9]))))
