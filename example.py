from pprint import pprint

import huffman
from view import viz_tree
import utils


data = 'This is huffman coding'
data = utils.load_example()
tree = huffman.build_tree(data)
map_code = huffman.build_map_code(tree)

# encode
bin_data = huffman.encode(data, map_code)

# print("Map code")
# for k, v in map_code.items():
#     print("{}: {}".format(chr(k), v.to01()))
# print("Encoded data:", bin_data.to01())
# viz_tree(tree)

# # decode
# print("After decode:", huffman.decode(bin_data.tobytes(), tree, bin_data.buffer_info()[3]))

# calculate performance
p = len(bin_data.tobytes()) / len(data.encode('utf-8'))
print("Reduce:", p)
