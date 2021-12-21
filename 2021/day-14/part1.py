
import os

class Instruction():
    def __init__(self, raw_string: str) -> None:
        self.pair, self.insert = raw_string.split(' -> ')

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

def getInstructions(lines):
    return [Instruction(line) for line in lines[2:]]

def applyInstructions(pair: str, instructions: list[Instruction]):
    for instruction in instructions:
        if pair == instruction.pair:
            return pair[0] + instruction.insert + pair[1]
    return pair

def findAnswer(master_string: str):
    maximum = 0
    minimum = 9999999

    for letter in set(master_string):
        count = master_string.count(letter)
        if count > maximum:
            maximum = count
        if count < minimum:
            minimum= count
    return maximum - minimum

TOTAL_STEPS = 10

lines = openInput()
master_string = lines[0]
instructions = getInstructions(lines)

for step in range(TOTAL_STEPS):
    new_string = ''
    for idx in range(len(master_string)-1):
        pair = master_string[idx:idx+2]
        updated_pair = applyInstructions(pair, instructions)
        new_string = new_string[:-1] + updated_pair
    master_string = new_string

answer = findAnswer(master_string)
print(f'{answer=}')
