import itertools

lastOutput = 0


def parseInstruction(instruction):
    instruction = str(instruction)
    while len(instruction) < 5:
        instruction = '0' + instruction
    res = {'opcode': int(instruction[3:]), 'mode_first': int(instruction[2]), 'mode_second': int(instruction[1])}
    return res


class Thruster(object):

    def __init__(self, intcode=None, pointer=0, phase=None, input=None):
        self.intcode = intcode
        self.pointer = pointer
        self.phase = phase
        self.input = input
        self.halt = False

    def execute(self):
        p = self.pointer
        instruction = parseInstruction(self.intcode[p])
        opcode = instruction['opcode']
        if opcode == 99:
            self.halt = True
            return
        mode_first = instruction['mode_first']
        mode_second = instruction['mode_second']
        first = self.intcode[p + 1]
        if opcode in range(1, 3) or opcode in range(7, 9):
            second = self.intcode[p + 2]
            result = self.intcode[p + 3]
            if opcode == 1:
                self.intcode[result] = (self.intcode[first] if mode_first == 0 else first) + (
                    self.intcode[second] if mode_second == 0 else second)
            elif opcode == 2:
                self.intcode[result] = (self.intcode[first] if mode_first == 0 else first) * (
                    self.intcode[second] if mode_second == 0 else second)
            elif (opcode == 7 and (self.intcode[first] if mode_first == 0 else first) < (
            self.intcode[second] if mode_second == 0 else second)) or (
                    opcode == 8 and (self.intcode[first] if mode_first == 0 else first) == (
                    self.intcode[second] if mode_second == 0 else second)):
                self.intcode[result] = 1
            else:
                self.intcode[result] = 0


def eexecute(inputlist, input, pointer=0, secondinput=None, useSecondInput=False):
    global lastOutput
    instruction = parseInstruction(inputlist[pointer])
    opcode = instruction['opcode']
    mode_first = instruction['mode_first']
    mode_second = instruction['mode_second']
    if opcode == 99:
        return inputlist
    first = inputlist[pointer + 1]
    if opcode in range(1, 3) or opcode in range(7, 9):
        second = inputlist[pointer + 2]
        result = inputlist[pointer + 3]
        if opcode == 1:
            inputlist[result] = (inputlist[first] if mode_first == 0 else first) + (
                inputlist[second] if mode_second == 0 else second)
        elif opcode == 2:
            inputlist[result] = (inputlist[first] if mode_first == 0 else first) * (
                inputlist[second] if mode_second == 0 else second)
        elif (opcode == 7 and (inputlist[first] if mode_first == 0 else first) < (
        inputlist[second] if mode_second == 0 else second)) or (
                opcode == 8 and (inputlist[first] if mode_first == 0 else first) == (
        inputlist[second] if mode_second == 0 else second)):
            inputlist[result] = 1
        else:
            inputlist[result] = 0
        return execute(inputlist, input, pointer + 4, secondinput, True)
    elif opcode in range(3, 5):
        if opcode == 3:
            inputlist[first] = input if not useSecondInput else secondinput
        elif opcode == 4:
            output = inputlist[first] if mode_first == 0 else first
            lastOutput = output
            # print(output)
        return execute(inputlist, input, pointer + 2, secondinput, True)
    elif opcode in range(5, 7):
        if (opcode == 5 and (inputlist[first] if mode_first == 0 else first) != 0) or (
                opcode == 6 and (inputlist[first] if mode_first == 0 else first) == 0):
            second = inputlist[pointer + 2]
            return execute(inputlist, input, (inputlist[second] if mode_second == 0 else second), secondinput, True)
        return execute(inputlist, input, pointer + 3, secondinput, True)
    else:
        print("Something went wrong")
        return


inputlist = [int(x) for x in open('input.txt').read().split(',')]
sequences = list(itertools.permutations([0, 1, 2, 3, 4]))
highestOutput = 0

for sequence in sequences:
    input = 0
    for i in range(0, 5):
        program = inputlist.copy()
        execute(program, sequence[i], 0, input)
        input = lastOutput
    if lastOutput > highestOutput:
        highestOutput = lastOutput

print(highestOutput)
