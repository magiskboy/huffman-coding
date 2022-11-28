from pprint import pprint

import huffman
from view import viz_tree

data = b"Of course the values aren't going to be, because x means hexadecimal, and the decimal values 55, 33, 22 are the hexadecimal values 37, 21, 16. But if you had the hexadecimal values 55, 33, 22, you'd get exactly the output you want:"

tree = huffman.build_tree(data)
map_code = huffman.build_map_code(tree)

# encode
bin_data = huffman.encode(data, map_code)

print("Map code")
for k, v in map_code.items():
    print("{}: {}".format(chr(k), v.to01()))
print("Encoded data:", bin_data.to01())
viz_tree(tree)

# decode
print("After decode:", huffman.decode(bin_data.tobytes(), tree, bin_data.buffer_info()[3]))

# calculate performance
p = len(bin_data) / (len(data) * 8)
print("Reduce:", p)
