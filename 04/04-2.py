def sortNumber(num):
    return int(''.join(sorted(str(num))))


def checkIfSorted(num):
    return sortNumber(num) == num


def checkForGroups(num):
    for i in range(1,10):
        if str(num).count(str(i)) == 2:
            return True


def validate(num):
    return checkIfSorted(num) and checkForGroups(num)


res = [x for x in range(372037, 905158) if validate(x)]
print(len(res))