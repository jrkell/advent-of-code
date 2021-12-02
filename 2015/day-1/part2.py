#%%
# "(" means he should go up one floor
# ")" means he should go down one floor

def openInput():
    with open('input.txt') as f:
        return f.read()

line = openInput()

floor = 0

for (index, command) in enumerate(line):
    if command == '(':
        floor += 1
    if command == ')':
        floor -= 1
    if floor == -1:
        print(index+1)
