# coding=utf-8

import sys
import pickle
from bitarray import bitarray
import huffman


help_str = '''
Usage: compress.py <action> <filein> <fileout>
  Options:
    decode              Decode binary string present to origin text
    encode              Build code word and encode data from file
  Huffman coding implementation
'''


def read_each(fi, n=1):
    chunk = 1
    while chunk:
        chunk = fi.read(n)
        yield chunk


def encode(filename_in, filename_out):
    with open(filename_in, 'rb') as fi:
        freq = huffman.freq_str(read_each(fi))
        tree = huffman.build_tree(freq)
        map_code = huffman.build_map_code(tree)
        fi.seek(0)
        out = huffman.encode(read_each(fi), map_code)
        u = out.buffer_info()[3]            # unused bits of last byte
        header = pickle.dumps(freq, pickle.HIGHEST_PROTOCOL)
        n_header = len(header)

        with open(filename_out,'wb') as fo:
            fo.write(n_header.to_bytes(8, 'big') + u.to_bytes(1, 'big') + header + out.tobytes())


def decode(filename_in, filename_out):
    with open(filename_in, 'rb') as fi:
        n_header = int.from_bytes(fi.read(8), 'big')
        u = int.from_bytes(fi.read(1), 'big')
        header = fi.read(n_header)
        data = fi.read()
        freq = pickle.loads(header)
        tree = huffman.build_tree(freq)
        out = huffman.decode(data, tree, u)
        with open(filename_out, 'wb') as fo:
            fo.write(out)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(help_str)
        exit(1)

    _, action, filename_in, filename_out = sys.argv
    if action == 'encode':
        encode(filename_in, filename_out)
    elif action == 'decode':
        decode(filename_in, filename_out)
    else:
        print(help_str)
