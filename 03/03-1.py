def getDistance(pos):
    return abs(pos[0]) + abs(pos[1])


def tracePath(path):
    coords = set()
    curpos = [0, 0]
    for step in path:
        direction = step[0]
        distance = int(step[1:])
        while distance > 0:
            if direction == 'U':
                curpos[1] += 1
            elif direction == 'R':
                curpos[0] += 1
            elif direction == 'D':
                curpos[1] -= 1
            else:
                curpos[0] -= 1
            coords.add((curpos[0], curpos[1]))
            distance -= 1
    return coords


def findIntersections(path1, path2):
    return path1.intersection(path2)


def findClosestIntersection(path1, path2):
    tuples = findIntersections(path1, path2)
    closest = None
    for tuple in tuples:
        distance = getDistance([tuple[0], tuple[1]])
        if closest is not None:
            if distance < closest:
                closest = distance
        else:
            closest = distance
    return closest


input = [line.split(',') for line in open('input.txt').read().splitlines()]
wire1 = tracePath(input[0])
wire2 = tracePath(input[1])
print(findClosestIntersection(wire1, wire2))