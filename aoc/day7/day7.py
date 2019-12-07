# 45 ms
import itertools as nya

start_state = list(map(int, open('input.txt', 'r').readline().split(',')))


def get_args(P, ip, n, digits, output):
    while len(digits) < n:
        digits = [0] + digits
    ans = P[ip + 1:ip + n + 1]
    if output:
        assert digits[0] == 0
        digits[0] = 1
    ans = [x if digits[len(digits) - 1 - i] == 1 else P[x] for i, x in enumerate(ans)]
    return ans


def run_tape(inputs, idx=0):
    codes = start_state[:]

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
            return (codes[codes[idx + 1]]), idx + 2
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

    return None, idx


list_amps = [5, 6, 7, 8, 9]
max_out = -10000000000

for permutation in list(nya.permutations(list_amps)):
    new_val = 0
    indexes = [0, 0, 0, 0, 0]  # starting indexes 0 for all amps
    outputs = [0, 0, 0, 0, 0]  # outputs 0 for all amps
    inputs = [[permutation[i]] for i in range(5)]  # init inputs are the phase themselves
    inputs[0].append(0)  # first amp starts with phase number, then 0

    is_done = False
    while not is_done:
        for j in range(5):
            # print(type(inputs[j]), type(indexes[j]))
            new_val, new_idx = run_tape(inputs[j], indexes[j])  # run it at the proper settings
            if new_val is None:
                max_out = max(max_out, outputs[-1])
                is_done = True
                break
            indexes[j] = new_idx  # update idx
            outputs[j] = new_val  # update output
            inputs[(j + 1) % 5].append(new_val)  # (j+1) %5 because input to next amp

print(max_out)
