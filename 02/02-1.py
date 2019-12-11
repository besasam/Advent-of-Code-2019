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


inputlist = [int(x) for x in open('input.txt').read().split(',')]
inputlist[1] = 12
inputlist[2] = 2

print(execute(inputlist)[0])