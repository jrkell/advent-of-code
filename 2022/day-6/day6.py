import os


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read()


def main():
    data = openInput()

    # part 1
    part1Answer = findMarker(data, 4)
    print(f'{part1Answer=}')

    # part 2
    part1Answer = findMarker(data, 14)
    print(f'{part1Answer=}')


def findMarker(data: str, windowSize: int) -> int:
    for start in range(0, len(data)-windowSize):
        if not hasDuplicateChars(data[start:start+windowSize]):
            return start+windowSize


def hasDuplicateChars(string: str) -> bool:
    return len(set(string)) != len(string)


if __name__ == '__main__':
    main()
