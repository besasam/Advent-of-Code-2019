def execute(inputlist, curpos = 0):
    opcode = inputlist[curpos]
    if opcode == 99:
        return inputlist
    first = inputlist[curpos+1]
    second = inputlist[curpos+2]
    result = inputlist[curpos+3]
    if opcode == 1:
        res = inputlist[first] + inputlist[second]
    elif opcode == 2:
        res = inputlist[first] * inputlist[second]
    else:
        print("Something went wrong")
        return
    inputlist[result] = res
    return execute(inputlist, curpos+4)


def testNounVerb(inputlist, noun, verb, output):
    curlist = inputlist.copy()
    curlist[1] = noun
    curlist[2] = verb
    return execute(curlist)[0] == output


def findNounVerb(inputlist, output):
    for noun in range(100):
        for verb in range(100):
            if testNounVerb(inputlist, noun, verb, output):
                return 100 * noun + verb


inputlist = [int(x) for x in open('input.txt').read().split(',')]

print(findNounVerb(inputlist, 19690720))