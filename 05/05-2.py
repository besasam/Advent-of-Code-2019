def parseInstruction(instruction):
    instruction = str(instruction)
    while len(instruction) < 5:
        instruction = '0' + instruction
    res = {'opcode': int(instruction[3:]), 'mode_first': int(instruction[2]), 'mode_second': int(instruction[1])}
    return res


def execute(inputlist, input, pointer = 0):
    instruction = parseInstruction(inputlist[pointer])
    opcode = instruction['opcode']
    mode_first = instruction['mode_first']
    mode_second = instruction['mode_second']
    if opcode == 99:
        return inputlist
    first = inputlist[pointer + 1]
    if opcode in range(1,3) or opcode in range(7,9):
        second = inputlist[pointer + 2]
        result = inputlist[pointer + 3]
        if opcode == 1:
            inputlist[result] = (inputlist[first] if mode_first == 0 else first) + (inputlist[second] if mode_second == 0 else second)
        elif opcode == 2:
            inputlist[result] = (inputlist[first] if mode_first == 0 else first) * (inputlist[second] if mode_second == 0 else second)
        elif (opcode == 7 and (inputlist[first] if mode_first == 0 else first) < (inputlist[second] if mode_second == 0 else second)) or (opcode == 8 and (inputlist[first] if mode_first == 0 else first) == (inputlist[second] if mode_second == 0 else second)):
            inputlist[result] = 1
        else:
            inputlist[result] = 0
        return execute(inputlist, input, pointer + 4)
    elif opcode in range(3,5):
        if opcode == 3:
            inputlist[first] = input
        elif opcode == 4:
            print(inputlist[first] if mode_first == 0 else first)
        return execute(inputlist, input, pointer + 2)
    elif opcode in range(5,7):
        if (opcode == 5 and (inputlist[first] if mode_first == 0 else first) != 0) or (opcode == 6 and (inputlist[first] if mode_first == 0 else first) == 0):
            second = inputlist[pointer + 2]
            return execute(inputlist, input, (inputlist[second] if mode_second == 0 else second))
        return execute(inputlist, input, pointer + 3)
    else:
        print("Something went wrong")
        return


inputlist = [int(x) for x in open('input.txt').read().split(',')]
input = 5

execute(inputlist, input)