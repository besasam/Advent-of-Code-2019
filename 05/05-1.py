def parseInstruction(instruction):
    instruction = str(instruction)
    while len(instruction) < 5:
        instruction = '0' + instruction
    res = {'opcode': int(instruction[3:]), 'mode_first': int(instruction[2]), 'mode_second': int(instruction[1])}
    return res


def execute(inputlist, input, curpos = 0):
    instruction = parseInstruction(inputlist[curpos])
    opcode = instruction['opcode']
    mode_first = instruction['mode_first']
    mode_second = instruction['mode_second']
    if opcode == 99:
        return inputlist
    first = inputlist[curpos + 1]
    if opcode in range(1,3):
        second = inputlist[curpos + 2]
        result = inputlist[curpos + 3]
        if opcode == 1:
            inputlist[result] = (inputlist[first] if mode_first == 0 else first) + (inputlist[second] if mode_second == 0 else second)
        elif opcode == 2:
            inputlist[result] = (inputlist[first] if mode_first == 0 else first) * (inputlist[second] if mode_second == 0 else second)
        return execute(inputlist, input, curpos + 4)
    elif opcode in range(3,5):
        if opcode == 3:
            inputlist[first] = input
        elif opcode == 4:
            print(inputlist[first] if mode_first == 0 else first)
        return execute(inputlist, input, curpos + 2)
    else:
        print("Something went wrong")
        return


inputlist = [int(x) for x in open('input.txt').read().split(',')]
input = 1

execute(inputlist, input)