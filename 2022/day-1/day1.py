import os


def openInput() -> list[str]:
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.readlines()

def main():
    caloriesList = openInput()

    # part 1
    totals = getTotals(caloriesList)
    print(f'Maximum calories is: {max(totals)}')

    # part 2
    top3 = getTop3(totals)
    print(f'Sum of top three is: {sum(top3)}')


def getTop3(totals: list[int]) -> list[int]:
    top3 = []
    for total in totals:
        if len(top3) < 3:
            top3.append(total)
            continue

        if total > min(top3):
            top3.pop(0)
            top3.append(total)
            top3.sort()

    return top3

    
def getTotals(caloriesList: list[str]) -> list[int]:
    totals = []
    subtotal = 0
    for calory in caloriesList:
        if calory == '\n':
            totals.append(subtotal)
            subtotal = 0
            continue
        
        subtotal += int(calory)

    return totals
        
if __name__ == '__main__':
    main()

