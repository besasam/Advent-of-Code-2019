import math


def getFuel(mass):
    return math.floor(mass/3)-2


def getFuelRec(mass):
    cur = getFuel(mass)
    nex = getFuel(cur)
    if nex <= 0:
        return cur
    return cur + getFuelRec(cur)


modules = [int(x) for x in open('input.txt').read().splitlines()]

res = 0
for module in modules:
    res += getFuelRec(module)
print(res)