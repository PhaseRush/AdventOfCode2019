# 54ms
import math


def slurp(f_in_chat):
    idx = f_in_chat.find(" ")
    return int(f_in_chat[:idx]), f_in_chat[idx + 1:]


recipes = {}


def parse(line):
    reactants, products = line.split(" => ")
    reactants = reactants.split(', ')
    reactants = [slurp(in_put) for in_put in reactants]
    products = slurp(products)
    recipes[products[1]] = (reactants, products)


file = [parse(line) for line in open("input.txt").read().strip().split('\n')]


def calc(required_amount):
    required = {'FUEL': required_amount}

    while any(required[k] > 0 and not k == 'ORE' for k in required):
        needs = [reactant for reactant in required if required[reactant] > 0 and reactant != "ORE"][0]
        product_quantities = recipes[needs][1][0]
        multiple = math.ceil(required[needs] / product_quantities)
        required[needs] -= product_quantities * multiple
        for reactant in recipes[needs][0]:
            if reactant[1] in required:
                required[reactant[1]] += reactant[0] * multiple
            else:
                required[reactant[1]] = reactant[0] * multiple

    return required['ORE']


print(calc(1))

low = 0
high = int(1e12)
while low < high:
    print(f'low = {low}, high = {high}')
    mid = (low + high + 1) // 2
    if calc(mid) <= int(1e12):
        low = mid
    else:
        high = mid - 1

print(low)
