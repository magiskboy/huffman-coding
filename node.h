#ifndef NODE_H
#define NODE_H

#include "huffman.h"

class Node {
    public:
        float key;
        WORD_T value;
        Node* left;
        Node* right;

        Node(float key, WORD_T value, Node* left, Node* right) {
            this->key = key;
            this->value = value;
            this->left = left;
            this->right = right;
        }

        bool operator<=(const Node& o) {
            return this->key <= o.key;
        }
};

#endif
