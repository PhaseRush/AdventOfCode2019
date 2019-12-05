# 146 ms

start_state = list(map(int, open('input.txt', 'r').readline().split(',')))


def try_codes(noun, verb):
    codes = start_state[:]

    idx = 0
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
            codes[codes[idx + 1]] = noun
            increment = 2
        elif opcode is 4:
            print(codes[codes[idx + 1]])
            increment = 2
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

    return codes[0]


try_codes(5, 0)
