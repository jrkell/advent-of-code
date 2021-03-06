import os

OPENERS = ['{','(','[','<']
CLOSERS = ['}',')',']','>']
BRACKETS = [
    {
        "open": "(",
        "close": ")",
        "points": 3
    },
    {
        "open": "[",
        "close": "]",
        "points": 57
    },
    {
        "open": "{",
        "close": "}",
        "points": 1197
    },
    {
        "open": "<",
        "close": ">",
        "points": 25137
    },
]

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

# recursively remove the pairs until there are none left
def removePairs(string: str):
    # print(string)
    if len(string) < 2:
        return string
    for i in range(0,len(string)-1):
        if string[i] in OPENERS:
            closer = getClosingBracket(string[i])
            if string[i+1] == closer:
                return removePairs(string[0:i] + string[i+2:])
    return string

# if it has a closing bracket still in there it is corrupt    
def containsCloser(string: str):
    for i in string:
        if i in CLOSERS:
            return i
    return None

def getClosingBracket(value: str) -> str:
    return next(bracket["close"] for bracket in BRACKETS if bracket["open"] == value)

def getCorruptPoints(string: str):
    adj_string = removePairs(string)
    closer = containsCloser(adj_string)
    if closer != None:
        return getPoints(closer)
    return 0

def getPoints(closer):
        return next(bracket["points"] for bracket in BRACKETS if bracket["close"] == closer)

lines = openInput()

total = 0
for line in lines:
    total += getCorruptPoints(line)
print(f'{total=}')