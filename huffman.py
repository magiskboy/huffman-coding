#encode=utf-8

import heapq
from collections import Counter
from bitarray import bitarray


class Node:
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, o):
        return self.key <= o.key


def build_map_code(tree: Node, code, map_code: dict):
    if not (tree.left and tree.right):
        map_code[tree.val] = bitarray(code)
    else:
        if tree.left:
            build_map_code(tree.left, code + '0', map_code)
        if tree.right:
            build_map_code(tree.right, code + '1', map_code)


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


def encode(data):
    counter = Counter(data)
    heap = []
    n = len(counter.keys())
    for value, f in counter.items():
        heap.append(Node(f / n, value, None, None))

    if n == 1:
        map_code = {heap[0].val: bitarray('0')}
    else:
        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            c = Node(left.key + right.key, None, left=left, right=right)
            heapq.heappush(heap, c)
        heap = heapq.heappop(heap)
        map_code = {}
        build_map_code(heap, '', map_code)
    print(map_code)

    enc = bitarray()
    enc.encode(map_code, data)

    return map_code, enc
