// ! Remove define before submitting !
#define local

#ifdef local
struct Node {  
  int value;  
  const Node* left = nullptr;  
  const Node* right = nullptr;
  Node(Node* left, Node* right, int value) : value(value), left(left), right(right) {}
};  
#endif

#ifndef local
#include "solution.h"
#endif
#include <cmath>
#include <iostream>
#include <cassert>

using namespace std;


Node* insert(Node* root, int key) {
    // Your code
    // “ヽ(´▽｀)ノ”
}

#ifdef local
void test() {
    Node node1({nullptr, nullptr, 7});
    Node node2({&node1, nullptr, 8});
    Node node3({nullptr, &node2, 7});
    Node* newHead = insert(&node3, 6);
    assert(newHead->left->value == 6);
    assert(newHead == &node3);
}

int main() {
  test();
}
#endif