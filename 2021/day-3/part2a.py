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
            "min": 1,
            "tie": False
        }

    if zero_count == one_count:
        return {
            "tie": True
        }
    
    return {
        "max": 1,
        "min": 0,
        "tie": False
    }

def filterList(arr, x, keep):
    # return only items in arr that have bin in position x
    return [i for i in arr if i[x] == keep]


lines = openInput()
print(filterList(lines, 0, '1'))

filtered_list = lines

# oxygen generator rating
for x in range(0,12):
    result = getMostCommon(filtered_list, x)
    if result["tie"]:
        most_common = 1
    else:
        most_common = result["max"]
    filtered_list = filterList(filtered_list, x, str(most_common))

oxy_gen_rating = int(filtered_list[0],2)

filtered_list = lines
# CO2 scrubber rating
for x in range(0,12):
    if len(filtered_list) == 1:
        break
    result = getMostCommon(filtered_list, x)
    if result["tie"]:
        most_common = 0
    else:
        most_common = result["min"]
    filtered_list = filterList(filtered_list, x, str(most_common))

co2_scrubber_rating = int(filtered_list[0],2)

print(f'{oxy_gen_rating=}')
print(f'{co2_scrubber_rating=}')
print(f'{oxy_gen_rating*co2_scrubber_rating}')

# %%
