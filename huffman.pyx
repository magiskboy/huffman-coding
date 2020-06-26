#encode=utf-8

import heapq
from collections import Counter
from bitarray import bitarray
from libcpp.map cimport map as cpp_map
from cython.operator cimport dereference
from cython.operator cimport preincrement
cdef extern from "<algorithm>" namespace "std":
    Iter find[Iter](Iter first, Iter last)
from queue import LifoQueue


cdef class Node:
    cdef int key
    cdef bytes val
    cdef Node left
    cdef Node right

    def __init__(self, int key, bytes val, Node left, Node right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, Node o):
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


def counter(data):
    cdef cpp_map[char*, int] c;
    cdef char* ch
    for ch in data:
        preincrement(c[ch])
    return c


def build_tree(cpp_map[char*, int] freq):
    heap = []
    cdef cpp_map[char*, int].iterator it = freq.begin()
    while (it != freq.end()):
        heap.append(Node(dereference(it).second, dereference(it).first, None, None))
        preincrement(it)

    heapq.heapify(heap)
    cdef Node left, right, c
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


def decode(data, map_code, u_bit=None):
    _data = bitarray()
    _data.frombytes(data)
    if u_bit is not None: del _data[-u_bit:]
    out = _data.decode(map_code)
    try:
        return bytes(out)
    except:
        return b''.join(out)
