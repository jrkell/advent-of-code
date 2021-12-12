
import os

class SignalPattern():
    def __init__(self, inputs, outputs) -> None:
        self.inputs     = inputs
        self.outputs    = outputs
        self.solved = ['' for i in range(0,10)]

    def countOutputsWithNChars(self, n: int) -> int:
        return sum([1 for output in self.outputs if len(output) == n])

    def solveEasyOnes(self):
        for inp in self.inputs:
            segment_len = len(inp)
            if segment_len == 2:
                self.solved[1] = inp
            elif segment_len == 4:
                self.solved[4] = inp
            elif segment_len == 3:
                self.solved[7] = inp
            elif segment_len == 7:
                self.solved[8] = inp

    def solveSixDigitOnes(self):
        for inp in self.inputs:
            segment_len = len(inp)
            
            # solve 6 digit ones
            if segment_len == 6:
                missing = getMissingChars(self.solved[8], inp)[0]
                missing_one_is_in_four = missing in self.solved[4]
                contains_seven = xContainsY(inp, self.solved[7])

                # zero
                if missing_one_is_in_four and contains_seven:
                    self.solved[0] = inp

                # nine
                elif not missing_one_is_in_four and contains_seven:
                    self.solved[9] = inp

                # six
                else:
                    self.solved[6] = inp

    def solveFiveDigitOnes(self):
        for inp in self.inputs:
            segment_len = len(inp)

            # solve 5 digit ones
            if segment_len == 5:
                contains_seven = xContainsY(inp, self.solved[7])
                can_fit_in_six = xContainsY(self.solved[6], inp)

                # three
                if contains_seven:
                    self.solved[3] = inp

                # five
                elif can_fit_in_six:
                    self.solved[5] = inp

                # two
                else:
                    self.solved[2] = inp

    def getOutput(self):
        result = []
        for out in self.outputs:
            for num in range(0,10):
                if isAnagramOf(self.solved[num], out):
                    result.append(num)
        # surely a better way to do this
        self.answer = result[0] * 1000 +result[1] * 100 + result[2] * 10 + result[3]

def xContainsY(x: str, y: str) -> bool:
    return not [char for char in y if char not in x]
    
def getMissingChars(haystack: str, needle: str) -> list[str]:
    return [char for char in haystack if char not in needle]

def isAnagramOf(x: str, y: str) -> bool:
    return sorted(x) == sorted(y)

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
    signal.solveEasyOnes()
    signal.solveSixDigitOnes()
    signal.solveFiveDigitOnes()
    signal.getOutput()
    total += signal.answer

print(f'{total=}')