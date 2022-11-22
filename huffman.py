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


def freq_str(data):
    counter = Counter(data)
    return counter

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
    fr = freq_str(data)
    heap = []
    for value, f in fr.items():
        heap.append(Node(f, value, None, None))

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


def decode(data, tree, u_bit=None):
    _data = bitarray()
    _data.frombytes(data)
    if u_bit is not None: del _data[-u_bit:]
    
    out = ''
    p = tree
    for bit in _data:
        # leaf node
        if p.left == p.right == None:
            out = out + chr(p.val)
            if bit:
                p = tree.right
            else:
                p = tree.left
            continue

        if bit:
            p = p.right
        else:
            p = p.left

    out = out + chr(p.val)

    return out
