#%%
import os


OPENERS = ['{','(','[','<']
CLOSERS = ['}','(',']','>']
BRACKETS = [
    {
        "open": "{",
        "close": "}"
    },
    {
        "open": "(",
        "close": ")"
    },
    {
        "open": "[",
        "close": "]"
    },
    {
        "open": "<",
        "close": ">"
    },
]

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

def isCorrupt(currently_open: str, line: str, index: int) -> bool:
    # if opener, recursively check the rest of the string
    checking = line[index]
    seeking = getClosingBracket(currently_open)

    print(f'{checking=}{seeking=}{line=}')

    if line[index] in OPENERS:
        return isCorrupt(line[index], line, index+1)

    # else it's a closer and check if it matches
    if checking != seeking:
        return True
    return False

def getClosingBracket(value: str) -> str:
    return next(bracket["close"] for bracket in BRACKETS if bracket["open"] == value)


test = '{([(<{}[<>[]}>{[]{[(<()>'

print(isCorrupt(test[0], test, 0))
# %%
