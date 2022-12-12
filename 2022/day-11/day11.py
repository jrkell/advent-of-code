import os
from typing import Callable


def openInput() -> list[str]:
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()


class Item:
    def __init__(self, worryLevel: int, part: int) -> None:
        self.worryLevel = worryLevel
        self.part = part

    def addRelief(self, modulo: int):
        if self.part == 1:
            self.worryLevel = int(self.worryLevel / 3)    
        else:
            self.worryLevel = int(self.worryLevel % modulo)

    def applyOperation(self, operation: Callable, operationNum: int):
        self.worryLevel = operation(self.worryLevel, operationNum)


class Monkey:
    def __init__(
        self,
        number: int,
        items: list[Item],
        operation: Callable,
        operationNum: int,
        divisibleBy: int,
        trueAction: int,
        falseAction: int
    ) -> None:
        self.number = number
        self.items = items
        self.operation = operation
        self.operationNum = operationNum
        self.divisibleBy = divisibleBy
        self.trueAction = trueAction
        self.falseAction = falseAction
        self.inspectCount = 0

    def go(self, monkeys: list, divisor: int):
        for item in self.items:
            self.inspectCount += 1
            item.applyOperation(self.operation, self.operationNum)
            item.addRelief(divisor)

            if isDivisibleBy(item.worryLevel, self.divisibleBy):
                passToMonkey = findMonkey(monkeys, self.trueAction)
            else:
                passToMonkey = findMonkey(monkeys, self.falseAction)
            passToMonkey.items.append(item)

        # empty items after processing
        self.items = []


def isDivisibleBy(number: int, divisor: int) -> bool:
    return number % divisor == 0

def getCommonModulo(divisors: int) -> int:
    """get a 'super modulo' we can use to reduce worry"""
    common = 1
    for divisor in divisors:
        common *= divisor
    return common

def findMonkey(monkeys: list[Monkey], monkeyNum: int) -> Monkey:
    return [monk for monk in monkeys if monk.number == monkeyNum][0]


def main():
    parts = [
        {
            "partNum": 1,
            "rounds": 20
        },
        {
            "partNum": 2,
            "rounds": 10000
        }
    ]

    data = openInput()

    for part in parts:
        monkeys = initialiseMonkeys(data, part['partNum'])
        goMonkeysGo(monkeys, part['rounds'])
        answer = getAnswer(monkeys)
        print(f'The answer to part {part["partNum"]} is {answer}')


def getAnswer(monkeys: list[Monkey]) -> int:
    top2Monkeys = [monkey.inspectCount for monkey in monkeys]
    top2Monkeys.sort(reverse=True)
    return top2Monkeys[0] * top2Monkeys[1]


def goMonkeysGo(monkeys: list[Monkey], rounds: int) -> None:
    divisor = getCommonModulo([monkey.divisibleBy for monkey in monkeys])
    for i in range(0, rounds):
        for monkey in monkeys:
            monkey.go(monkeys, divisor)


def initialiseMonkeys(data: list[str], part: int) -> list[Monkey]:
    """extract the info for each monkey and create Monkey object"""
    monkeys = []
    for lineNum in range(0, 55, 7):
        # probably some better regexy way to do all this...
        monkeyNum = int(data[lineNum][-3])
        startingItems = [Item(int(i), part)
                         for i in data[lineNum+1][18:].strip().split(', ')]
        operationType = data[lineNum+2][23]
        operationNum = data[lineNum+2].strip()[23:]
        if operationType == '*':
            if operationNum == 'old':
                def operation(x, y): return x * x
            else:
                def operation(x, y): return x * int(y)
        if operationType == '+':
            def operation(x, y): return x + int(y)

        divisibleBy = int(data[lineNum+3].strip()[19:])
        trueAction = int(data[lineNum+4].strip()[-1])
        falseAction = int(data[lineNum+5].strip()[-1])
        monkeys.append(Monkey(monkeyNum, startingItems, operation, operationNum,
                       divisibleBy, trueAction, falseAction))
    return monkeys


if __name__ == '__main__':
    main()
