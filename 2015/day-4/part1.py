#%%
import hashlib

def openInput():
    with open('input.txt') as f:
        return f.read()

line = openInput()


cont = True
num = 1
while cont:
    test = line + str(num)
    hashed = hashlib.md5(test.encode()).hexdigest()
    # print(f'{test} has the hash {hashed}')
    if hashed[0:5] == '00000':
        cont = False
        print(f'{test} has the hash {hashed}')
    num += 1
# %%
