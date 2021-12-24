import os

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read().splitlines()

def getPairDict(lines):
    key_dict = {}
    length = len(lines[2:])
    for (index, instruction) in enumerate(lines[2:]):
        split = instruction.split(' -> ')
        key_dict[split[0]] = {
            'returns' : [split[0][0] + split[1], split[1] + split[0][1]],
            'count' : 0,
            'last' : False
        }
    return key_dict

def findAnswer(pair_dict: dict) -> int:
    maximum = None
    minimum = None
    letters = {}

    for key in pair_dict.keys():
        count = pair_dict[key]['count']
        isLast = pair_dict[key]['last']
        letter = key[0]
        if letter in letters.keys():
            letters[letter] += count
        else:
            letters[letter] = count
        
        if isLast:
            letter = key[1]
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1

    for letter in letters:
        count = letters[letter]
        if maximum == None:
            maximum = count
        elif count > maximum:
            maximum = count
        
        if minimum == None:
            minimum = count
        elif count < minimum:
            minimum = count

    return maximum - minimum

def initPairs(string: str, pair_dict: dict):
    string_len = len(string)
    for idx in range(string_len-1):
            pair = string[idx:idx+2]
            if pair in pair_dict.keys():
                pair_dict[pair]["count"] += 1    
            else:
                pair_dict[pair]["count"] = 1
            if idx == string_len-2:
                pair_dict[pair]['last'] = True

def applyInsertions(pair_dict: dict, lines):
    new_dict = getPairDict(lines)
    for key in pair_dict.keys():
        pair = pair_dict[key]
        count = pair['count']
        isLast = pair['last']
        if pair['count'] == 0:
            continue
        return1, return2 = pair['returns']
        new_dict[return1]['count'] += count
        new_dict[return2]['count'] += count
        if isLast:
            new_dict[return2]['last'] = True
        
    return new_dict

def solve(total_steps: int) -> int:
    lines = openInput()
    master_string = lines[0]
    pairs = getPairDict(lines)
    initPairs(master_string, pairs)
    
    for _ in range(total_steps):
        pairs = applyInsertions(pairs, lines)
    return findAnswer(pairs)

print(f'Part 1 = {solve(10)}')
print(f'Part 2 = {solve(40)}')