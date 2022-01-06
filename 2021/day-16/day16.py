import os

all_packets = []

hex = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def openInput():
    location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(location, 'input.txt')) as f:
        return f.read()


def hexToBinary(hex_string):
    return ''.join([hex[i] for i in hex_string])

# def removeTrailingZeroes(binary: str) -> str:
#     data = ''
#     for char in binary:
#         if char 

def createPacket(hex_string):
    binary = hexToBinary(hex_string)
    version = binary[0:3]
    type_id = binary[3:6]
    if type_id == '100':
        data = getType4Data(binary)
    else:
        data = getOtherTypesData(binary)
    return Packet(version, type_id, data)

def getOtherTypesData(bin_string: str) -> str:
    length_type_id, remaining_string = getFirstNDigits(1, bin_string)
    if length_type_id == '0':
        # next 15 bits represent the total length in bits
        packet_length, remaining_string = getFirstNDigits(15, remaining_string)
        packet_length = int(packet_length, 2)
        # TODO: need to get actual packets
        return getFirstNDigits(packet_length, remaining_string)
    else:
        # next 11 bits represent the number of sub-packets
        num_packets, remaining_string = getFirstNDigits(15, remaining_string)
        for _ in range(num_packets):
            new_data, remaining_string = getFirstPacket(remaining_string)
        return remaining_string

def getType4Data(bin_string: str):
    data = ''
    index = 0
    cont = True
    while cont:
        data += bin_string[index+1:index+5]
        if bin_string[index] == '0':
            cont = False
        index += 5
    return (data, bin_string[index:])

class Packet():
    def __init__(self, version, type_id, data) -> None:
        self.version = version
        self.type_id = type_id
        self.data = data

def getFirstNDigits(n: int, string):
    first_digits = ''
    for char in range(n):
        first_digits += string[char]
    return (first_digits, string[n:])

def removeLeadingZeroes(string: str) -> str:
    for index, char in enumerate(string):
        if char != '0':
            return string[index:]

# def getPackets(input_bin: str) -> list[Packet]:
#     packets = []
#     remaining_string = input_bin
    
#     while remaining_string != None:
#         version, remaining_string = getFirstNDigits(3)
#         type_id, remaining_string = getFirstNDigits(3)
#         if type_id == '100':
#             data, remaining_string = getType4Data(remaining_string)
#         else:
#             data, remaining_string = getOtherTypesData(remaining_string)

#         packets.append(Packet(version, type_id, data))
#         remaining_string = removeLeadingZeroes(remaining_string)

#     return packets

def getFirstPacket(input_bin: str):
    remaining_string = input_bin
   
    version, remaining_string = getFirstNDigits(3)
    type_id, remaining_string = getFirstNDigits(3)
    if type_id == '100':
        data, remaining_string = getType4Data(remaining_string)
    else:
        data, remaining_string = getOtherTypesData(remaining_string)
    
    remaining_string = removeLeadingZeroes(remaining_string)
    packet = Packet(version, type_id, data)
    all_packets.append(packet)
    return (packet, remaining_string)

def part1():
    input_hex = openInput()
    input_bin = hexToBinary(input_hex)
    packets = getPackets(input_bin)
    

if __name__ == '__main__':
    part1()