import huffman


with open('big.txt', 'rb') as fi:
    data = []
    for i in fi.
    map_code, enc = huffman.encode(data)

    with open('out.bin', 'wb') as fo:
        enc.tofile(fo)


# text = 'This is a example'
# map_code, enc = huffman.encode([1,2,1,2,3,4])
# print(map_code)
# print(enc)
