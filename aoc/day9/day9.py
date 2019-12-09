# 1038ms

codes = [int(x) for x in open('input.txt').read().split(',')]
codes.extend([0] * 20000)
idx = 0
idx_offset = 0

num_ops = 0


def get_idx(i, modes):
    mode = (0 if i >= len(modes) else modes[i])
    val = codes[idx + 1 + i]
    if mode == 0:
        return val
    elif mode == 2:
        return val + idx_offset


def get_val(i, modes):
    mode = (0 if i >= len(modes) else modes[i])
    val = codes[idx + 1 + i]
    if mode == 0:
        val = codes[val]
    elif mode == 2:
        val = codes[val + idx_offset]
    return val


def run_tape():
    global idx_offset, idx, num_ops
    num_ops = 0

    while True:
        command = str(codes[idx])
        opcode = int(command[-2:])
        modes = list(reversed([int(x) for x in command[:-2]]))
        increment = 4
        if opcode is 1:
            i1, i2 = get_val(0, modes), get_val(1, modes)
            codes[get_idx(2, modes)] = i1 + i2
        elif opcode is 2:
            i1, i2 = get_val(0, modes), get_val(1, modes)
            codes[get_idx(2, modes)] = i1 * i2
        elif opcode is 3:
            codes[get_idx(0, modes)] = 2
            increment = 2
        elif opcode is 4:
            ans = get_val(0, modes)
            idx += 2
            return ans
        elif opcode is 5:
            if get_val(0, modes) != 0:
                idx = get_val(1, modes)
                increment = 0
            else:
                increment = 3
        elif opcode is 6:
            if get_val(0, modes) == 0:
                idx = get_val(1, modes)
                increment = 0
            else:
                increment = 3
        elif opcode is 7:
            codes[get_idx(2, modes)] = 1 if get_val(0, modes) < get_val(1, modes) else 0
        elif opcode is 8:
            codes[get_idx(2, modes)] = 1 if get_val(0, modes) == get_val(1, modes) else 0
        elif opcode is 9:
            idx_offset += get_val(0, modes)
            increment = 2
        else:  # 99
            return None

        idx += increment
        num_ops += 1


while True:
    val = run_tape()
    if val is None:
        break
    print(val)
    print(num_ops)
