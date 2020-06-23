#include "huffman.h"

#include <algorithm>
#include "node.h"



void build_code_word(std::vector<WORD_T>& data, std::map<WORD_T, void*> code_word)
{
    // counter words in data
    std::map<WORD_T, uint32_t> counter;
    for (std::vector<WORD_T>::iterator it = data.begin(); it != data.end(); ++it) {
        if ( counter.find(*it) != counter.end() ) {
            ++counter[*it];
        }
        else {
            counter.insert(std::pair<WORD_T, uint32_t>(*it, 0));
        }
    }

    // build heap
    uint32_t n = data.size();
    std::vector<Node> heap;
    for (std::map<WORD_T, uint32_t>::iterator it = counter.begin(); it != counter.end(); it++) {
        Node node(it->second / n, it->first, nullptr, nullptr);
    }
    std::make_heap(heap.begin(), heap.end());

    // build tree
    while (heap.size() > 1) {
        std::pop_heap(heap.begin(), heap.end()); heap.pop_back();
        Node left = heap.front();
        std::pop_heap(heap.begin(), heap.end()); heap.pop_back();
        Node right = heap.front();
        Node c(left.key + right.key, 0, &left, &right);
        heap.push_back(c);
        std::push_heap(heap.begin(), heap.end());
    }
    std::pop_heap(heap.begin(), heap.end()); heap.pop_back();
    Node root = heap.front();

    // build code word
}
