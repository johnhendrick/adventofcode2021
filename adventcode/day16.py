from bitstring import BitArray
from adventcode.utils import read_file

file_path = './input/day16.txt'


def parse_file(file_content=read_file(file_path)):
    rows = file_content.split('\n')
    return rows

#  3 version
#  3 typeID : 4 or every other

# length typeID: 0 or 11


input_str = 'EE00D40C823060'
b = BitArray(hex=input_str)


print(b.bin)
