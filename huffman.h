#ifndef HUFFMAN_H
#define HUFFMAN_H

#include <iostream>
#include <vector>
#include <map>
#include <bitset>


#define WORD_T unsigned char

void build_code_word(std::vector<WORD_T>&, std::map<WORD_T, std::bitset<3>>);


#endif
