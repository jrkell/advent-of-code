# %%
def openInput():
    with open('input.txt') as f:
        return f.read().splitlines()

# %%
def getMostCommon(arr, x):
    zero_count = 0
    one_count = 0
    for item in arr:
        if item[x] == '0':
            zero_count += 1
            # print('zero++')
        else:
            one_count += 1
            # print('one++')
    
    if zero_count > one_count:
        return {
            "max": 0,
            "min": 1
        }
        
    return {
        "max": 1,
        "min": 0
    }

lines = openInput()
gamma = ''
epsilon = ''

for x in range(0,12):
    result = getMostCommon(lines, x)
    gamma += str(result["max"])
    epsilon += str(result["min"])

print(f'{gamma=}')
print(f'{epsilon=}')

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)
product = gamma_int * epsilon_int
print(f'{gamma_int=}')
print(f'{epsilon_int=}')
print(f'{product=}')


# %%
