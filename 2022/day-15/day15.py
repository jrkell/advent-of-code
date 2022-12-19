import os


class Sensor:
    def __init__(self, coords, nearestBeaconCoords) -> None:
        self.coords = coords
        self.nearestBeaconCoords = nearestBeaconCoords
        self.range = getManhattanDistance(
            self.coords, self.nearestBeaconCoords)

    def getKnownPointsForY(self, y: int) -> list[tuple[int, int]]:
        known = []
        # only need to consider X's within one "range" of the sensor
        for x in range(self.coords[0]-self.range, self.coords[0]+self.range+1):
            if getManhattanDistance(self.coords, (x, y)) <= self.range and (x, y) != self.nearestBeaconCoords:
                known.append((x, y))
        return known

    def getKnownRangeForY(self, y: int) -> list[int, int]:
        """returns (startX, endX) if there are some known or None if none known"""
        if y > self.coords[1]+self.range or y < self.coords[1]-self.range:
            return None

        # reduces by 1 on each side for every row away from Sensor
        # creates diamond shape without needing to calculate manhattan distances
        reduction = abs(self.coords[1]-y)
        return [self.coords[0]-self.range+reduction, self.coords[0]+self.range-reduction]


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def getManhattanDistance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])


def parseInput(data: list[str]) -> list[Sensor]:
    sensors = []
    for line in data:
        sensor = extractCoords(line[line.find('x='):line.find(':')])
        beacon = extractCoords(line[line.find('beacon')+13:].strip())
        sensors.append(Sensor(sensor, beacon))
    return sensors


def extractCoords(coords: str) -> tuple[int, int]:
    ints = [i[2:] for i in coords.split(', ')]
    return (int(ints[0]), int(ints[1]))


def mergeAllRanges(ranges: list[list]) -> list[list]:
    ranges.sort()
    stack = []
    stack.append(ranges[0])

    for r in ranges[1:]:
        # Check for overlapping range
        if stack[-1][0] <= r[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], r[-1])
        else:
            stack.append(r)

    return stack


def getAllKnownRangesForRow(sensors: list[Sensor], y: int) -> list[list]:
    ranges = []

    # get all known ranges for row y
    for sensor in sensors:
        knownRange = sensor.getKnownRangeForY(y)
        if knownRange != None:
            ranges.append(knownRange)

    return ranges


def main(part: int):
    data = openInput()
    sensors = parseInput(data)

    if part == 1:
        knownCoords = []
        for sensor in sensors:
            knownCoords += sensor.getKnownPointsForY(2000000)
        return len(set(knownCoords))

    if part == 2:
        found = False
        for y in range(0, 4000000):
            ranges = getAllKnownRangesForRow(sensors, y)
            merged = mergeAllRanges(ranges)

            if len(merged) > 1:
                for i in range(len(merged)-1):
                    if merged[i][1] < merged[i+1][0] - 1:
                        # found it!!
                        x, y = merged[i][1]+1, y
                        print(f'yey found it at {(x, y)}')
                        found = True
                        break
            if found:
                break
        return (x*4000000)+y


if __name__ == '__main__':
    print("Part 1:", main(1))
    print("Part 2:", main(2))
