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


def build_map_code(tree: Node, code=''):
    if not (tree.left and tree.right):
        return {
            tree.val: bitarray(code)
        }
    else:
        ret = {}
        if tree.left:
            ret.update(build_map_code(tree.left, code + '0'))
        if tree.right:
            ret.update(build_map_code(tree.right, code + '1'))
        return ret


def build_tree(data):
    counter = Counter(data)
    heap = []
    for value, f in counter.items():
        heap.append(Node(f, value, None, None))

    if len(data) == 1:
        return heap[0]
    else:
        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            c = Node(left.key + right.key, None, left=left, right=right)
            heapq.heappush(heap, c)
        tree = heapq.heappop(heap)
    return tree


def encode(data, map_code):
    out = bitarray()
    out.encode(map_code, data)
    return out


def decode(data, map_code):
    out = data.decode(map_code)
    return ''.join(out)
