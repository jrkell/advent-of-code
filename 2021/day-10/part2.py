#%% 
import os

OPENERS = ['{','(','[','<']
CLOSERS = ['}',')',']','>']
BRACKETS = [
    {
        "open": "(",
        "close": ")",
        "points": 1
    },
    {
        "open": "[",
        "close": "]",
        "points": 2
    },
    {
        "open": "{",
        "close": "}",
        "points": 3
    },
    {
        "open": "<",
        "close": ">",
        "points": 4
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

def getIncompletePoints(string: str):
    adj_string = removePairs(string)
    closer = containsCloser(adj_string)
    if closer == None:
        return getTotalPoints(adj_string[::-1])
    return 0

def getTotalPoints(string: str):
    total = 0
    for i in string:
        total *= 5
        total += getPoints(i)
    return total

def getPoints(opener: str):
    return next(bracket["points"] for bracket in BRACKETS if bracket["open"] == opener)

lines = openInput()

totals = []
for line in lines:
    result = getIncompletePoints(line)
    if result > 0:
        totals.append(result)

totals.sort()
midpoint = (len(totals)+1)/2
middle_score = totals[int(midpoint)-1]
print(f'{middle_score=}')
