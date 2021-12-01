#%%
def openInput():
    with open('input1.txt') as f:
        return [int(string) for string in f.read().splitlines()]

def getSlidingWindow(index):
    return lines[index:index+3]

lines = openInput()

# %%
increaseCount = 0

for (idx, line) in enumerate(lines):
    if idx == 0:
        continue
    if sum(getSlidingWindow(idx)) > sum(getSlidingWindow(idx-1)):
        increaseCount += 1

print(f'{increaseCount=}')
