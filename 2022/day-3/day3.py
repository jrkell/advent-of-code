import os


class Rucksack():
    def __init__(self, items: str) -> None:
        halfLength = int(len(items)/2)
        self.compartment1 = items[0:halfLength]
        self.compartment2 = items[halfLength:]

    def findDuplicate(self):
        return [item for item in self.compartment1 if item in self.compartment2][0]


class ThreeElfRucksack():
    def __init__(self, lines: list[str]) -> None:
        self.rucksack1 = lines[0]
        self.rucksack2 = lines[1]
        self.rucksack3 = lines[2]

    def getCommonLetter(self):
        return [item for item in self.rucksack1 if item in self.rucksack2 and item in self.rucksack3][0]


letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


def getPriority(letter: str) -> int:
    return letters.find(letter) + 1


def main():
    data = openInput()

    # part 1
    # create Rucksack for each line, get the duplicates, convert to score and sum
    rucksackList = [Rucksack(line) for line in data]
    duplicates = [rucksack.findDuplicate() for rucksack in rucksackList]
    total = sum([getPriority(duplicate) for duplicate in duplicates])
    print(f'Sum of the duplicates is {total}')

    # part 2
    priorities = []
    # iterate up in groups of 3, get the duplicates, convert to score and sum
    for index in range(0, len(data), 3):
        rucksack = ThreeElfRucksack(data[index:index+3])
        priorities.append(getPriority(rucksack.getCommonLetter()))
    total = sum(priorities)
    print(f'Sum of the duplicates is {total}')


if __name__ == '__main__':
    main()
