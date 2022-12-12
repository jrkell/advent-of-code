import os


class Event:
    def __init__(self, cycleNum: int, xVal: int) -> None:
        self.cycleNum = cycleNum
        self.xVal = xVal


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main():
    data = openInput()
    events = runInstructions(data)

    # part 1
    part1Answer = 0
    for num in [20, 60, 100, 140, 180, 220]:
        part1Answer += [i.xVal for i in events if i.cycleNum == num][0] * num
    print(f'{part1Answer=}')

    # part 2
    print(f'part2Answer=')
    drawEvents(events)


def drawEvents(events: list[Event]) -> None:
    eventIndex = 0
    for _ in range(0, 6):
        for pixel in range(0, 40):
            # for each cycle compare the xval and pixel
            x = events[eventIndex].xVal
            spritePosition = [x-1, x, x+1]
            if pixel in spritePosition:
                print('#', end='')
            else:
                print('.', end='')
            eventIndex += 1
        print()


def runInstructions(data: list[str]) -> list[Event]:
    x = 1
    events = []
    cycle = 0
    for line in data:
        if line.strip() == 'noop':
            cycle += 1
            events.append(Event(cycle, x))
        if line[0:4] == 'addx':
            cycle += 1
            events.append(Event(cycle, x))
            cycle += 1
            events.append(Event(cycle, x))
            x += int(line[5:])

    return events


def noop():
    pass


if __name__ == '__main__':
    main()
