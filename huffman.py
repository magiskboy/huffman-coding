#encode=utf-8

import heapq
from collections import Counter
import json
import sys


help_str = '''
Usage: huffman.py <action> <file>
  Options:
    decode              Decode binary string present to origin text
    encode              Build code word and encode data from file
  Huffman coding implementation
'''


class Node:
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, o):
        return self.key <= o.key


def build_map_code(tree, trace_path, map_code):
    if not (tree.left and tree.right):
        map_code[tree.val] = trace_path
    else:
        if tree.left:
            build_map_code(tree.left, trace_path + '0', map_code)
        if tree.right:
            build_map_code(tree.right, trace_path + '1', map_code)


def decode(map_code, data):
    out = []
    token = ''
    inv_map = {v: k for k, v in map_code.items()}
    for char in data:
        token += char
        if token in inv_map:
            out.append(inv_map[token])
            token = ''
    return ''.join(out)


def huffman(text):
    counter = Counter(text)
    heap = []
    n = len(counter.keys())
    for value, f in counter.items():
        heap.append(Node(f / n, value, None, None))
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        c = Node(left.key + right.key, None, left=left, right=right)
        heapq.heappush(heap, c)
    heap = heapq.heappop(heap)
    map_code = {}
    build_map_code(heap, '', map_code)

    enc = ''
    for char in text:
        enc += map_code[char]

    return map_code, enc


if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) < 2:
        print(help_str)
    else:
        if argv[0] == 'encode':
            with open(argv[1]) as fi:
                data = list(fi.readlines())
                data = '\n'.join(data)
            map_code, enc = huffman(data)
            with open(f'{argv[1].split(".")[0]}.encode.json', 'w') as fo:
                json.dump({
                    'map': map_code,
                    'data': enc,
                }, fo)
        elif argv[0] == 'decode':
            with open(argv[1]) as fi:
                j = json.load(fi)
                out = decode(j['map'], j['data'])
            with open(argv[1].split('.')[0] + '.txt', 'w') as fo:
                fo.write(out)
        else:
            print(help_str)
