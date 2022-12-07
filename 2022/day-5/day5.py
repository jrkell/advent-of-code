import os


class Instruction:
    def __init__(self, amount: int, fromStack: int, toStack: int) -> None:
        self.amount = amount
        self.fromStack = fromStack
        self.toStack = toStack


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main():
    data = openInput()

    # part 1
    stacks = initStacks(data)
    instructions = getInstructions(data)
    applyInstructions(instructions, stacks)
    part1Answer = ''.join([stack[-1] for stack in stacks])
    print(f'{part1Answer=}')

    # part 2
    # restart stacks first
    stacks = initStacks(data)
    applyInstructions(instructions, stacks, True)
    part2Answer = ''.join([stack[-1] for stack in stacks])
    print(f'{part2Answer=}')


def getInstructions(data: list[str]) -> list[Instruction]:
    instructions = []
    for row in range(10, len(data)):
        splitRow = data[row].split()
        instructions.append(Instruction(
            int(splitRow[1]), int(splitRow[3]), int(splitRow[5])))
    return instructions


def initStacks(data: list[str]) -> list[list[str]]:
    stacks = [[] for _ in range(0, 9)]
    for row in range(0, 8):
        line = data[row]
        stackIndex = 0
        for col in range(1, len(line), 4):
            crate = line[col]
            if crate != ' ':
                stacks[stackIndex].insert(0, crate)
            stackIndex += 1
    return stacks


def applyInstructions(instructions: list[Instruction], stacks: list[list[str]], part2=False) -> None:
    for instruction in instructions:
        movingCrates = []
        for _ in range(0, instruction.amount):
            movingCrates.append(stacks[instruction.fromStack-1].pop())

        if (part2):
            movingCrates.reverse() # need to flip the order to simulate picking up multiple at once
        
        stacks[instruction.toStack-1] = stacks[instruction.toStack-1] + movingCrates


if __name__ == '__main__':
    main()
