from pprint import pprint
import huffman
from view import viz_tree


data = 'this is an example of a huffman tree'

tree = huffman.build_tree(data)
map_code = huffman.build_map_code(tree)


# encode
bin_data = huffman.encode(data, map_code)

print('Map code')
pprint(map_code, width=1)
print('Encoded data')
print(bin_data)
viz_tree(tree)

# decode
print('After decode')
print(huffman.decode(bin_data, map_code))


# calculate performance
p = (len(bin_data.tobytes()) * 8) / (len(data) * 8)
print(f'Reduce {p * 100}%')
