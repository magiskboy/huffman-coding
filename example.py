import sys
import json
from pprint import pprint
import huffman


help_str = '''
Usage: example.py <action> <file>
  Options:
    decode              Decode binary string present to origin text
    encode              Build code word and encode data from file
  Huffman coding implementation
'''


if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) < 2:
        print(help_str)
    else:
        if argv[0] == 'encode':
            map_code, enc = huffman.encode(argv[1])
            print('Map code')
            pprint(map_code, width=1)
            print('Encoded')
            print(enc)
        else:
            print(help_str)
