def tracePath(path):
    coords = {}
    curpos = [0, 0]
    steps = 0
    for step in path:
        direction = step[0]
        distance = int(step[1:])
        while distance > 0:
            steps += 1
            if direction == 'U':
                curpos[1] += 1
            elif direction == 'R':
                curpos[0] += 1
            elif direction == 'D':
                curpos[1] -= 1
            else:
                curpos[0] -= 1
            coords[steps] = (curpos[0], curpos[1])
            distance -= 1
    return coords


def findIntersections(path1, path2):
    set1 = set(path1.values())
    set2 = set(path2.values())
    return set1.intersection(set2)


def getSteps(path, pos):
    for steps, coordinates in path.items():
        if coordinates == pos:
            return steps


def findQuickestIntersection(path1, path2):
    intersections = findIntersections(path1, path2)
    quickest = None
    for intersection in intersections:
        steps1 = getSteps(path1, intersection)
        steps2 = getSteps(path2, intersection)
        steps = steps1 + steps2
        if quickest is not None:
            if steps < quickest:
                quickest = steps
        else:
            quickest = steps
    return quickest


input = [line.split(',') for line in open('input.txt').read().splitlines()]
wire1 = tracePath(input[0])
wire2 = tracePath(input[1])
print(findQuickestIntersection(wire1, wire2))