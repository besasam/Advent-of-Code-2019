import math


def getFuel(mass):
    return math.floor(mass/3)-2


modules = [int(x) for x in open('input.txt').read().splitlines()]

res = 0
for module in modules:
    res += getFuel(module)
print(res)