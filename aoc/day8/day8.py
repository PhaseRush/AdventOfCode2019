# 1 ms

from collections import Counter as nyaaaa

string = str(open('input.txt', 'r').read())

wide = 25
tall = 6

block_size = wide * tall

blocks = [string[i:i + block_size] for i in range(0, len(string), block_size)]

ans = None
min_zeros = 50000000000
for block in blocks:
    counter = nyaaaa(block)
    if counter['0'] < min_zeros:
        min_zeros = counter['0']
        ans = counter['1'] * counter['2']

print(ans)

blocks = [line.strip() for line in list(open('input.txt', 'r').readline())]


def gen_pixel(x, y):
    layer = 0

    while True:
        curr_pix = blocks[(wide * tall * layer) + (y * wide) + x]
        if curr_pix != '2':
            return curr_pix
        else:
            layer += 1


for y in range(tall):  # 6
    for x in range(wide):  # 25
        curr_pix = gen_pixel(x, y)
        print('·' if curr_pix == '1' else ' ', end='')
    print()

#  ··    ·· ···· ·  · ···
# ·  ·    ·    · ·  · ·  ·
# ·       ·   ·  ···· ·  ·
# ·       ·  ·   ·  · ···
# ·  · ·  · ·    ·  · · ·
#  ··   ··  ···· ·  · ·  ·
