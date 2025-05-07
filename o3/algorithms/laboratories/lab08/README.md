# 🌳 Advanced Binary Trees Implementation

A comprehensive Python implementation of advanced binary trees with practical applications and algorithm challenges.

## 🚀 Overview

This project explores advanced binary tree implementations - extending beyond basic tree structures to specialized variants like binary search trees (BST), AVL trees, expression trees, and more. These advanced tree structures are fundamental in computer science for efficiently organizing and processing hierarchical data.

## ✨ Features

- **Multiple tree implementations** 🌿
  - Basic binary tree with traversal algorithms
  - Binary search tree (BST) with ordered operations
  - Self-balancing AVL tree with rotations
  
- **Practical applications** 🧰
  - Expression trees for mathematical evaluation
  - Huffman coding for data compression
  - File system modeling for directory structures
  
- **Advanced algorithms** 🧩
  - Tree balancing with rotations
  - Tree traversals (preorder, inorder, postorder, level-order)
  - Height, leaf counting, and balance analysis

- **Technical challenges** 💪
  - Tree height calculation
  - Counting leaf nodes
  - Tree mirroring
  - Level-order traversal
  - Balance checking

## 🔍 Implementation Details

### Tree Classes and Interfaces

The implementation provides multiple tree classes, each with specific operations:

1. **Basic Binary Tree** 🌱
   - Simple node structure with value, left and right pointers
   - Basic traversal operations (preorder, inorder, postorder)
   - Level-order traversal using queue-based approach

2. **Binary Search Tree** 🔍
   - Maintains BST property: left < node < right
   - Efficient search, insert, and delete operations
   - Handles special cases for deletion (leaf, one child, two children)

3. **AVL Tree** ⚖️
   - Self-balancing binary search tree
   - Maintains balance factor between -1 and 1
   - Implements tree rotations (left, right, left-right, right-left)

### Specialized Tree Applications

The implementation includes powerful applications of tree structures:

1. **Expression Tree** 🧮
   - Builds a tree from postfix mathematical expressions
   - Evaluates expressions while respecting operator precedence
   - Converts back to infix notation with proper parenthesization

2. **Huffman Coding** 📦
   - Creates a Huffman tree based on character frequencies
   - Generates variable-length codes for efficient data compression
   - Provides encoding and decoding functionality

3. **File System** 📂
   - Models hierarchical directory structure as a tree
   - Supports file and directory operations (mkdir, touch, ls, cd)
   - Implements path resolution and navigation

## 💻 Usage Examples

### Creating and Traversing a Binary Tree 🌱
```python
# Create a binary tree
tree = BinaryTree()
tree.build_tree_from_list([1, 2, 3, 4, 5, None, 6])

# The tree structure:
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6

# Traverse the tree
preorder = tree.traverse("preorder")   # [1, 2, 4, 5, 3, 6]
inorder = tree.traverse("inorder")     # [4, 2, 5, 1, 3, 6]
postorder = tree.traverse("postorder") # [4, 5, 2, 6, 3, 1]
level_order = tree.level_order_traversal()  # [1, 2, 3, 4, 5, 6]
```

### Working with Binary Search Trees 🔍
```python
# Create a BST
bst = BinarySearchTree()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(value)

# Search for values
found = bst.search(40)  # True
not_found = bst.search(55)  # False

# Delete values (handling different cases)
bst.delete(20)  # Delete leaf node
bst.delete(30)  # Delete node with one child
bst.delete(70)  # Delete node with two children
```

### Evaluating Expressions with Expression Trees 🧮
```python
expr_tree = ExpressionTree()
expr_tree.build_from_postfix(["3", "4", "+", "2", "*"])

# Convert to infix notation
infix = expr_tree.print_infix()  # "((3 + 4) * 2)"

# Evaluate the expression
result = expr_tree.evaluate()  # 14
```

### Compressing Data with Huffman Coding 📦
```python
text = "abracadabra"

huffman = HuffmanCoding()
huffman.build_huffman_tree(text)
codes = huffman.generate_codes()

# Encode the text
encoded = huffman.encode(text)

# Decode the encoded data
decoded = huffman.decode(encoded)  # "abracadabra"
```

## 🏃‍♂️ Running the Project

To run all the tests and examples:

```bash
python main.py
```

The output will include test results for all implementations and challenges, demonstrating the functionality of different tree structures.

## 📊 Comparative Analysis

| **Tree Type**          | **Search** | **Insert** | **Delete** | **Memory** | **Balance Guarantee** |
| ---------------------- | ---------- | ---------- | ---------- | ---------- | --------------------- |
| **Binary Tree**        | O(n)       | O(n)       | O(n)       | Low        | None                  |
| **Binary Search Tree** | O(log n)*  | O(log n)*  | O(log n)*  | Low        | None                  |
| **AVL Tree**           | O(log n)   | O(log n)   | O(log n)   | Medium     | Strict                |
| **Huffman Tree**       | N/A        | N/A        | N/A        | Medium     | None                  |

\* Average case for balanced trees, worst case O(n) for skewed trees

### Performance Characteristics

- **Binary Search Trees** excel at ordered data operations but can degrade to linear time if unbalanced
- **AVL Trees** guarantee logarithmic operations through self-balancing but require extra storage and balancing overhead
- **Expression Trees** optimize for operator precedence and evaluation, not for search performance
- **Huffman Trees** are specialized for compression based on frequency distribution, not for general-purpose searches

## 🧩 Applications

Advanced binary trees find applications across computer science and software development:

- **Database Indexing** 💾 - B-trees and variants optimize database lookups
- **Compiler Design** 🔠 - Abstract syntax trees represent and process code
- **File Systems** 📂 - Directory structures in operating systems
- **Game AI** 🎮 - Decision trees and minimax algorithms
- **Network Routing** 🌐 - Routing tables use tree-like structures
- **Machine Learning** 🤖 - Decision trees for classification and regression
- **Graphics Processing** 🖼️ - Spatial partitioning with binary space partition trees
- **Compression Algorithms** 📦 - Huffman coding for efficient data storage

## 🔗 Related Resources

- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms-third-edition) - Comprehensive coverage of tree algorithms
- [Data Structures and Algorithms in Python](https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275) - Python implementations of tree structures
- [Visualgo](https://visualgo.net/en/bst) - Visualizations of tree operations
- [GeeksforGeeks Tree Data Structure](https://www.geeksforgeeks.org/binary-tree-data-structure/) - Articles and tutorials on trees

---

Created with ❤️ for Elliot Garamendi