import os

class SignalPattern():
    def __init__(self, inputs, outputs) -> None:
        self.inputs = inputs
        self.outputs = outputs

    def countOutputsWithNChars(self, n: int) -> int:
        return sum([1 for output in self.outputs if len(output) == n])

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

lines = openInput()

total = 0
for line in lines:
    split = line.split(' | ')
    inputs = split[0].split(' ')
    outputs = split[1].split(' ')
    signal = SignalPattern(inputs, outputs)
    total += signal.countOutputsWithNChars(2) # 1
    total += signal.countOutputsWithNChars(4) # 4
    total += signal.countOutputsWithNChars(3) # 7
    total += signal.countOutputsWithNChars(7) # 8

print(f'{total=}')

