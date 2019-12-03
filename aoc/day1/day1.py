# 0 ms

accumulator = 0
cache = dict([(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])


def determine_cost(mass):
    # if already calculated this
    if mass in cache:
        return cache[mass]
    # new input
    fuel_mass = mass // 3 - 2
    final_mass = fuel_mass + determine_cost(fuel_mass)
    cache[mass] = final_mass
    return final_mass


with open('day1/input.txt', 'r') as file:
    for line in file:
        accumulator += determine_cost(int(line))

print(accumulator)
