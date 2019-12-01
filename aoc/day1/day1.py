accumulator = 0
cache = dict([(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])

def determinecost(mass):
    # if already calculated this
    if mass in cache:
        return cache[mass]
    # new input
    fuelmass = mass // 3 - 2
    finalmass = fuelmass + determinecost(fuelmass)
    cache[mass] = finalmass
    return finalmass


with open('day1/input1.txt', 'r') as file:
    for line in file:
        accumulator += determinecost(int(line))

print(accumulator)
print('dicts'.replace('t', 'k'))