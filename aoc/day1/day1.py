# 0 ms for puzzle input
# 9306 ms for manual (dict) cache with benchmark_input.txt Ans:24999112324301, hits:10000000, misses:7506245

accumulator = 0
cache = dict([(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])

hits = 0
misses = 0

# Doesn't work, exit code error
# import functools, sys
#
# sys.setrecursionlimit(1000000)
#
#
# @functools.lru_cache(maxsize=None)
# def auto_cache(mass):
#     fuel_mass = mass // 3 - 2
#     final_mass = fuel_mass + auto_cache(fuel_mass)
#     return final_mass


def determine_cost(mass):
    global hits, misses
    # if already calculated this
    if mass in cache:
        hits += 1
        return cache[mass]
    # new input
    misses += 1
    fuel_mass = mass // 3 - 2
    final_mass = fuel_mass + determine_cost(fuel_mass)
    cache[mass] = final_mass
    return final_mass


ans = sum([determine_cost(int(line)) for line in open('day1/benchmark_input.txt', 'r')])
print(f'Ans:{ans}, hits:{hits}, misses:{misses}')

# import random
#
# with open('day1/benchmark_input.txt', 'w') as file:
#     file.write('\n'.join(map(str, [random.randrange(1, 100000000) for _ in range(10000000)])))
