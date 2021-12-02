#%%
# "(" means he should go up one floor
# ")" means he should go down one floor

def openInput():
    with open('input.txt') as f:
        return f.read()

line = openInput()

floor = 0

for command in line:
    if command == '(':
        floor += 1
    if command == ')':
        floor -= 1

print(floor)
