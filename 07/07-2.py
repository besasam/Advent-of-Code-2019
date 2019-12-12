import itertools

def parseInstruction(instruction):
    instruction = str(instruction)
    while len(instruction) < 5:
        instruction = '0' + instruction
    res = {'opcode': int(instruction[3:]), 'mode_first': int(instruction[2]), 'mode_second': int(instruction[1])}
    return res


class Amp(object):

    def __init__(self):
        self.intcode = None
        self.pointer = 0
        self.phase = None
        self.input = None
        self.output = None
        self.usedPhase = False
        self.didOutput = False
        self.halt = False
        self.isFirst = False
        self.isLast = False

    def execute(self):
        input = self.input if self.usedPhase else self.phase
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
            self.pointer += 4
        elif opcode in range(3, 5):
            if opcode == 3:
                self.intcode[first] = input
                if not self.usedPhase:
                    self.usedPhase = True
            elif opcode == 4:
                self.output = self.intcode[first] if mode_first == 0 else first
                self.didOutput = True
            self.pointer += 2
        elif opcode in range(5, 7):
            if (opcode == 5 and (self.intcode[first] if mode_first == 0 else first) != 0) or (
                    opcode == 6 and (self.intcode[first] if mode_first == 0 else first) == 0):
                second = self.intcode[p + 2]
                self.pointer = self.intcode[second] if mode_second == 0 else second
            else:
                self.pointer += 3
        return self.output

    def executeUntilOutput(self):
        while not self.didOutput and not self.halt:
            self.execute()
        self.didOutput = False
        return self.output


inputlist = [int(x) for x in open('input.txt').read().split(',')]
sequences = list(itertools.permutations([x for x in range(5,10)]))

amps = []
for i in range(0,5):
    amps.append(Amp())
amps[0].isFirst = True
amps[4].isLast = True


def initializeAmps(amps, intcode, phases):
    amps[0].input = 0
    for i in range(0,5):
        amps[i].intcode = intcode.copy()
        amps[i].phase = phases[i]
        amps[i].halt = False
        amps[i].pointer = 0
        amps[i].usedPhase = False


def runAmps(amps):
    output = None
    i = 0
    while not amps[4].halt:
        output = amps[i].executeUntilOutput()
        if i == 4:
            amps[0].input = output
            i = 0
        else:
            amps[i + 1].input = output
            i += 1
    return output


highestOutput = 0

for sequence in sequences:
    initializeAmps(amps, inputlist, sequence)
    output = runAmps(amps)
    if output > highestOutput:
        highestOutput = output

print(highestOutput)
