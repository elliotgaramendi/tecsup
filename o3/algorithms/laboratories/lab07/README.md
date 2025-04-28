# 🌳 Binary Trees Implementation Guide

A comprehensive Python implementation of binary trees with powerful applications and practical exercises.

## 🚀 Overview

This project explores binary tree data structures - a fundamental non-linear data structure that represents hierarchical relationships between elements. Binary trees are essential in countless algorithms and applications from compilers to file systems.

## ✨ Features

- Multiple binary tree implementations:
  - Basic tree nodes with left and right children 🌱
  - Full binary tree traversal algorithms (preorder, inorder, postorder, level-order) 🔍
  - Extended tree operations (height, size, balance checking) 📏

- Real-world applications:
  - Expression tree evaluator for mathematical expressions 🧮
  - File system representation for hierarchical data 📁
  - Simple compiler with syntax tree parsing and evaluation 🔠

- Technical challenges with solutions:
  - Tree height calculation ⬆️
  - Leaf node counting 🍃
  - Tree mirroring 🪞
  - Level order traversal 📊
  - Balance checking ⚖️

## 🔍 Implementation Details

### Core Tree Operations

All implementations support these fundamental operations:

1. **Creation**: Build trees with nodes connecting parent-child relationships 🏗️
2. **Traversal**: Visit all nodes in specific orders (preorder, inorder, postorder, level-order) 🔄
3. **Analysis**: Calculate properties like height, size, and balance ⚙️
4. **Manipulation**: Mirror, balance, or restructure trees 🔧

### Key Implementation Techniques

- **Recursive Algorithms**: Elegant solutions for tree operations through recursion 🔄
- **Node-based Structure**: Simple node class with value and left/right pointers 📊
- **Specialized Tree Types**: Different tree variants for specific applications 🌿
- **Traversal Patterns**: Various ways to visit all nodes in meaningful orders 🧭

## 💻 Usage Examples

### Basic Usage 🔰
```python
# Create a basic binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create a tree instance
tree = BinaryTree(root)

# Traverse the tree
inorder = tree.traverse("inorder")  # Returns [2, 1, 3]
preorder = tree.traverse("preorder")  # Returns [1, 2, 3]
postorder = tree.traverse("postorder")  # Returns [2, 3, 1]

# Get tree properties
height = tree.height()  # Returns 1
size = tree.size()  # Returns 3
```

### Expression Evaluation 🧮
```python
# Create an expression tree
expr_tree = ExpressionTree()

# Build from postfix notation
expr_tree.build_from_postfix(["3", "4", "+", "2", "*"])

# Convert to infix notation
infix = expr_tree.print_infix()  # Returns "((3 + 4) * 2)"

# Evaluate the expression
result = expr_tree.evaluate()  # Returns 14
```

## 🏃‍♂️ Running the Project

```bash
# Run all tests and examples
python main.py

# Expected output includes test results for all implementations and challenges
```

## 📊 Comparative Analysis

| **Tree Type**      | **Time Complexity**  | **Space Complexity** | **Best Use Cases**                      |
| ------------------ | -------------------- | -------------------- | --------------------------------------- |
| Simple Binary Tree | O(n) traversal       | O(n)                 | Hierarchical relationships, expressions |
| Balanced Tree      | O(log n) operations  | O(n)                 | Efficient searching and sorting         |
| Expression Tree    | O(n) evaluation      | O(n)                 | Mathematical expression evaluation      |
| File System Tree   | O(depth) path lookup | O(n)                 | Directory structures, hierarchical data |

### 🧮 Operational Efficiency:
- **Traversal**: All methods visit each node exactly once → O(n) time complexity
- **Height/Size Calculation**: Requires visiting all nodes → O(n) time complexity
- **Building Trees**: Each node must be created and linked → O(n) time/space complexity

## 🧩 Applications

Binary trees are excellent for:

- **Compiler Design** 🔠: Syntax trees for language parsing and code generation
- **Expression Evaluation** 🧮: Maintaining operator precedence in calculations
- **File Systems** 📁: Representing hierarchical directory structures
- **Decision Trees** 🔍: Classification algorithms in machine learning
- **Huffman Coding** 📊: Data compression algorithms
- **Game AI** 🎮: Game state evaluation with minimax algorithm

## 🔗 Related Resources
- [Binary Tree Data Structure](https://en.wikipedia.org/wiki/Binary_tree) 📚
- [Tree Traversal](https://en.wikipedia.org/wiki/Tree_traversal) 🔍
- [Expression Trees](https://en.wikipedia.org/wiki/Binary_expression_tree) 🧮
- [Abstract Syntax Trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree) 🔠

---
Created with ❤️ by a world-class data structures expert 🧠