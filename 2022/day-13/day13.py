import functools
import json
import os


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def main(part: int):
    data = openInput()

    if part == 1:
        pairs = getThePairs(data)
        # sum index for any pair that is correct
        return sum([index for index, pair in enumerate(pairs, 1) if compareThePair(pair)])

    if part == 2:
        data = [json.loads(line.strip()) for line in data if line != "\n"]
        data = insertSpecialOnes(data)

        # sort all data rows lowest to highest using comparator function
        sortedData = sorted(data, key=functools.cmp_to_key(comparator))

        # multiply indices of special rows
        total = 1
        for index, value in enumerate(sortedData, 1):
            if value == [[2]] or value == [[6]]:
                total *= index
        return total


def getThePairs(data: list[str]):
    # started parsing the strings myself but too hard.. json loads works
    return [(json.loads(data[lineNum]), json.loads(data[lineNum+1])) for lineNum in range(0, len(data), 3)]


def comparator(x, y) -> int:
    # if they are the same, return 0
    if x == y:
        return 0
    # if x should be before y, return -1
    if compareThePair((x, y)):
        return -1

    # else x should be after y, return 1
    return 1


def insertSpecialOnes(before: list[list]):
    before.append([[2]])
    before.append([[6]])
    return before


def compareThePair(pair: tuple) -> bool:
    left = pair[0]
    right = pair[1]

    # convert where one is int and one is list
    if (isinstance(left, int) and isinstance(right, list)):
        return compareThePair(([left], right))
    if (isinstance(left, list) and isinstance(right, int)):
        return compareThePair((left, [right]))

    # compare two ints
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        if left == right:
            return None

    # compare two lists
    if isinstance(left, list) and isinstance(right, list):
        for index in range(0, len(left)):
            # if right list runs out return false
            if index > len(right)-1:
                return False

            # else call this function again with each pair of args
            result = compareThePair((left[index], right[index]))
            if result != None:
                return result

        # no result yet if lists are the same legnth
        if len(left) == len(right):
            return None

        # else left side ran out - return True
        return True


if __name__ == '__main__':
    print("Part 1:", main(1))
    print("Part 2:", main(2))
