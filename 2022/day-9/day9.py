import os
import enum


class Marker:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.path = [(0, 0)]
        self.inFront: Marker = None

    def move(self, direction: str) -> None:
        # L left, R right, U up, D down
        # diagonals = UL UR DL DR
        if 'L' in direction:
            self.x -= 1
        if 'R' in direction:
            self.x += 1
        if 'U' in direction:
            self.y -= 1
        if 'D' in direction:
            self.y += 1
        self.path.append((self.x, self.y))


class Head(Marker):
    pass


class Tail(Marker):
    def follow(self) -> None:
        xDistance = self.inFront.x - self.x
        yDistance = self.inFront.y - self.y

        # do nothing if in the same position or adjacent
        if abs(xDistance) <= 1 and abs(yDistance) <= 1:
            return

        direction = getFollowDirection(xDistance, yDistance)
        self.move(direction)


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def getFollowDirection(xDistance: int, yDistance: int) -> str:
    if xDistance < 0 and yDistance == 0:
        return 'L'

    if xDistance > 0 and yDistance == 0:
        return 'R'

    if yDistance < 0 and xDistance == 0:
        return 'U'

    if yDistance > 0 and xDistance == 0:
        return 'D'

    if yDistance > 0 and xDistance > 0:
        return 'DR'

    if yDistance > 0 and xDistance < 0:
        return 'DL'

    if yDistance < 0 and xDistance > 0:
        return 'UR'

    if yDistance < 0 and xDistance < 0:
        return 'UL'


def getInstructions(data: list[str]) -> list[tuple]:
    instructions = []
    for row in data:
        splitRow = row.split()
        direction = splitRow[0]
        quantity = int(splitRow[1])
        instructions.append((direction, quantity))
    return instructions


def runInstructions(instructions: list[tuple], numTails: int) -> Tail:
    # init markers
    head = Head()

    # for each tail, link previous head/tail
    previous = head
    tails = []
    for i in range(0, numTails):
        tail = Tail()
        tail.inFront = previous
        previous = tail
        tails.append(tail)

    # for each instruction move the head then all the tails follow the one in front
    for instruction in instructions:
        for _ in range(0, instruction[1]):
            head.move(instruction[0])
            for tail in tails:
                tail.follow()

    # return last tail
    return tails[-1]


def main():
    data = openInput()
    instructions = getInstructions(data)

    # part 1
    tail = runInstructions(instructions, 1)
    part1Answer = len(set(tail.path))
    print(f'{part1Answer=}')

    # part 2
    tail = runInstructions(instructions, 9)
    part2Answer = len(set(tail.path))
    print(f'{part2Answer=}')


if __name__ == '__main__':
    main()
