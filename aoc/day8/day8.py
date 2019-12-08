string = str(open('input.txt', 'r').read())

wide = 25
tall = 6

block_size = wide * tall

blocks = [string[i:i + block_size] for i in range(0, len(string), block_size)]

block_num = -1
min_zeros = 50000000000
for i in range(len(blocks)):
    block = blocks[i]
    this_zeros = 0
    for char in block:
        if char == '0':
            this_zeros += 1
    if this_zeros < min_zeros:
        min_zeros = this_zeros
        block_num = i
num_1 = 0
num_2 = 0
for char in blocks[block_num]:
    if char == '1':
        num_1 += 1
    elif char == '2':
        num_2 += 1

blocks = [line.strip() for line in list(open('input.txt', 'r').readline())]


def gen_pixel(x, y):
    layer = 0

    while True:
        curr_pix = blocks[(wide * tall * layer) + (y * wide) + x]
        if curr_pix != '2':
            return curr_pix
        else:
            layer += 1


final_pix = []
for y in range(tall):  # 6
    for x in range(wide):  # 25
        final_pix.append(gen_pixel(x, y))

counter = 0
for num in final_pix:
    if counter % wide == 0:
        print()
    else:
        print(num if num == '1' else '.', end='')

    counter += 1
