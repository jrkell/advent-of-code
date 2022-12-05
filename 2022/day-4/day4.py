import os


class Assignment:
    def __init__(self, text: str) -> None:
        splitText = text.split('-')
        self.lower = int(splitText[0])
        self.upper = int(splitText[1])


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def oneAssignmentContainsTheOther(assignmentPair: list[Assignment]) -> bool:
    a = assignmentPair[0]
    b = assignmentPair[1]
    aContainsB = a.lower <= b.lower and a.upper >= b.upper
    bContainsA = b.lower <= a.lower and b.upper >= a.upper
    return aContainsB or bContainsA


def assignmentsOverlap(assignmentPair: list[Assignment]) -> bool:
    a = assignmentPair[0]
    b = assignmentPair[1]
    aLowerInB = a.lower >= b.lower and a.lower <= b.upper
    aUpperInB = a.upper <= b.upper and a.upper >= b.lower
    bLowerInA = b.lower >= a.lower and b.lower <= a.upper
    bUpperInA = b.upper <= a.upper and b.upper >= a.lower
    return aLowerInB or aUpperInB or bLowerInA or bUpperInA


def main():
    data = openInput()
    pairs = []
    for line in data:
        split = line.split(',')
        pairs.append([Assignment(split[0]), Assignment(split[1])])

    # part 1
    containedPairs = list(filter(oneAssignmentContainsTheOther, pairs))
    print(f'The number of containing pairs is {len(containedPairs)}')

    # part 2
    overlappingPairs = list(filter(assignmentsOverlap, pairs))
    print(f'The number of overlapping pairs is {len(overlappingPairs)}')


if __name__ == '__main__':
    main()
