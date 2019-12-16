# 30474 ms

input_list = [int(x) for x in str(open('input.txt').read().strip())]
base_pattern = [0, 1, 0, -1]


def gen_pattern(index):
    pattern = []
    cycle = 0
    while len(pattern) < len(input_list) + 1:
        curr_num = base_pattern[cycle % 4]
        for j in range(index + 1):
            pattern.append(curr_num)
        cycle += 1

    return pattern[1:]


def phase_pass(pass_list):
    phase_out = []
    for idx in range(len(pass_list)):
        pattern = gen_pattern(idx)
        # print(f'idx = {idx} pattern = {pattern}, list = {pass_list}')
        digit_acc = 0
        for digit in range(len(pass_list)):
            digit_acc += pass_list[digit] * pattern[digit]
        phase_out.append(abs(digit_acc) % 10)
    return phase_out


def fft(num_passes):
    operating_list = input_list[:]
    for _ in range(num_passes):
        operating_list = phase_pass(operating_list)

    return operating_list


print(f'part 1 = {fft(100)}')

offset = int("".join(map(str, input_list[:7])))
assert offset > len(input_list) * 10000 / 2  # or else 1 block assumption broken
input_2 = input_list * 10000
offset = int(''.join([str(input_2[i]) for i in range(7)]))
shorter = input_2[offset:]  # everything before 0 anyways


def phase2(op_list):
    suffix_sum = sum(op_list)
    to_out = []
    for i in range(len(op_list)):
        to_out.append(abs(suffix_sum) % 10)
        suffix_sum -= op_list[i]
    return to_out


for phase in range(100):
    shorter = phase2(shorter)

print(f"part 2 = {''.join([str(input_2[i]) for i in range(8)])}")
