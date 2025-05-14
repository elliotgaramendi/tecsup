# 🌿 Generic and Expression Trees Implementation

A comprehensive Python implementation of generic and expression trees with practical applications and algorithm challenges.

## 📝 Overview

This project implements generic and expression trees, fundamental data structures in computer science. Generic trees allow nodes to have any number of children, making them perfect for hierarchical data like file systems. Expression trees are specialized binary trees that represent mathematical expressions, enabling efficient evaluation and notation conversion.

## ✨ Features

- **Generic Tree Operations** 🌳
  - Support for unlimited children per node
  - Preorder, postorder, and level-order traversals
  - Node searching and tree printing
  - Height calculation and leaf finding

- **Expression Tree Capabilities** 🧮
  - Build from postfix and prefix notations
  - Convert between infix, prefix, and postfix
  - Evaluate mathematical expressions
  - Support for variables in expressions

- **Practical Applications** 🛠️
  - File system representation with directories and files
  - Calculator engine with expression evaluation
  - Decision tree implementation for AI/ML
  - Mathematical expression simplification

- **Advanced Algorithms** 🚀
  - Notation conversion algorithms
  - Tree serialization and traversal
  - Expression tree optimization
  - Generic tree manipulation

- **Technical Challenges** 🧩
  - Infix to postfix conversion
  - Build expression trees from infix
  - Generic tree height calculation
  - Find all leaf nodes
  - Expression tree simplification

## 🔍 Implementation Details

### Core Tree Structures

1. **Generic Tree Node** 🌱
   ```python
   class GenericTreeNode:
       def __init__(self, value):
           self.value = value  # 📊 Data stored in node
           self.children = []  # 👶 List of child nodes
   ```

2. **Expression Node** 🔢
   ```python
   class ExpressionNode:
       def __init__(self, value):
           self.value = value    # 📊 Operator or operand
           self.left = None      # 👈 Left operand
           self.right = None     # 👉 Right operand
   ```

### Key Classes

- `GenericTree`: Basic generic tree with root node management
- `GenericTreeTraversals`: Extended with traversal algorithms
- `GenericTreeOperations`: Tree operations including height calculation using standard convention (height = edge count)
- `ExpressionTree`: Binary tree for mathematical expressions
- `EvaluableExpressionTree`: Adds evaluation capabilities
- `Calculator`: Uses expression trees for calculations
- `FileSystem`: Models directories as generic trees
- `SimpleDecisionTree`: AI decision-making structure
- `CalculatorEngine`: Complete calculator with history
- `NotationConverter`: Converts between expression notations

### Algorithm Implementations

The project includes solutions for five technical challenges:
1. **Infix to Postfix Conversion** - Stack-based algorithm with operator precedence
2. **Build Expression Tree from Infix** - Two-step construction via postfix conversion
3. **Generic Tree Height** - Recursive depth calculation using standard convention (edges count)
4. **Find All Leaves** - Leaf node identification through recursive traversal
5. **Expression Tree Simplification** - Constant folding optimization

### Technical Details

#### Height Convention
This implementation uses the standard computer science convention for tree height:
- Empty tree: height = -1
- Single node (leaf): height = 0  
- Height represents the number of edges in the longest path from root to leaf

This convention is consistent with:
- Common algorithm textbooks (CLRS, Skiena)
- Tree balancing algorithms (AVL, Red-Black)
- Most academic and professional implementations

## 💻 Usage Examples

### Creating a Generic Tree 🌳
```python
# Create and populate a generic tree
tree = GenericTree()
root = tree.add_root("A")
b = tree.add_node(root, "B")
c = tree.add_node(root, "C")
d = tree.add_node(root, "D")

# Add more nodes
e = tree.add_node(b, "E")
f = tree.add_node(b, "F")
g = tree.add_node(d, "G")

# Traverse the tree
traversal = GenericTreeTraversals()
traversal.root = root
print(traversal.preorder_traversal())  # ['A', 'B', 'E', 'F', 'C', 'D', 'G']
print(traversal.level_order_traversal())  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Calculate tree height
operations = GenericTreeOperations(root)
print(operations.height())  # Returns 2 (longest path has 2 edges)
```

### Evaluating Mathematical Expressions 🧮
```python
# Create and evaluate an expression tree
expr_tree = EvaluableExpressionTree()
expr_tree.build_from_postfix(['3', '4', '+', '5', '*'])

# Convert to different notations
infix = expr_tree.infix_traversal()    # "((3 + 4) * 5)"
prefix = expr_tree.prefix_traversal()  # "* + 3 4 5"
result = expr_tree.evaluate()          # 35.0

# With variables
expr_tree.build_from_postfix(['x', 'y', '+', 'z', '*'])
variables = {'x': 3, 'y': 4, 'z': 5}
result = expr_tree.evaluate_with_variables(variables)  # 35.0
```

### Building a File System 📂
```python
# Create a file system structure
fs = FileSystem()
home = fs.add_directory(fs.root, "home")
user = fs.add_directory(home, "user")
docs = fs.add_directory(user, "documents")

# Add files
fs.add_file(docs, "report.txt", 1024)
fs.add_file(docs, "notes.md", 2048)

# Get total size
total_size = docs.get_total_size()  # 3072 bytes

# Print structure
fs.print_tree()
```

### Using the Calculator Engine 🖩
```python
# Create a calculator and evaluate expressions
calc = CalculatorEngine()

# Evaluate infix expressions
result1 = calc.calculate_infix("2 + 3 * 4")      # 14
result2 = calc.calculate_infix("(2 + 3) * 4")    # 20

# View calculation history
calc.show_history()

# Interactive calculator
interactive_calculator()  # Start interactive mode
```

### Making Decisions with Decision Trees 🤔
```python
# Create and use a decision tree
game = SimpleDecisionTree()
game.build_animal_guesser()

# Play the guessing game
game.play()  # Interactive animal guessing game
```

## 🚀 Running the Project

To run all tests and demonstrations:

```bash
python main.py
```

This will execute:
- Basic tree structure tests
- Expression tree evaluations
- File system operations
- Calculator functionality
- Decision tree demonstrations
- All technical challenge solutions

Expected output includes:
- Visual tree representations 🌳
- Calculation results 🧮
- Test confirmations ✅
- Performance demonstrations 📊

## 📊 Comparative Analysis

| **Feature**            | **Generic Tree**                               | **Expression Tree**              |
| ---------------------- | ---------------------------------------------- | -------------------------------- |
| **Structure**          | Variable children                              | Binary (2 children max)          |
| **Primary Use**        | Hierarchical data                              | Mathematical expressions         |
| **Node Types**         | Homogeneous                                    | Heterogeneous (operators/values) |
| **Traversals**         | Pre/Post/Level-order                           | Infix/Prefix/Postfix             |
| **Time Complexity**    | O(n) for traversals                            | O(n) for evaluation              |
| **Space Complexity**   | O(n) nodes                                     | O(n) nodes                       |
| **Flexibility**        | High (any structure)                           | Limited (binary only)            |
| **Special Operations** | Height calculation (edge count), leaf counting | Evaluation, simplification       |

### When to Use Each

**Generic Trees** are ideal for:
- File systems and directory structures 📁
- Organizational hierarchies 🏢
- Decision trees with multiple branches 🤔
- Game trees with variable moves 🎮
- Family trees and genealogy 👨‍👩‍👧‍👦

**Expression Trees** excel at:
- Mathematical expression evaluation 🧮
- Compiler design and parsing 💻
- Calculator implementations 🖩
- Expression optimization ⚡
- Notation conversion 🔄

## 🧩 Applications

### Real-World Use Cases

1. **File Systems** 💾
   - Operating system directory structures
   - Cloud storage organization
   - Version control systems (Git)
   - Package managers (npm, pip)

2. **Compilers and Interpreters** 🔧
   - Abstract syntax trees (AST)
   - Code optimization
   - Expression evaluation
   - Type checking

3. **Artificial Intelligence** 🤖
   - Decision trees for classification
   - Game tree search (minimax)
   - Expert systems
   - Machine learning models

4. **Data Compression** 📦
   - Huffman coding trees
   - Arithmetic coding
   - Dictionary-based compression

5. **Network Routing** 🌐
   - Routing tables
   - Multicast trees
   - Spanning trees
   - Network topology

6. **Database Systems** 💿
   - Query optimization
   - Index structures
   - Join algorithms
   - Execution plans

## 🔗 Related Resources

- [Data Structures and Algorithms in Python](https://www.wiley.com/en-us/Data+Structures+and+Algorithms+in+Python-p-9781118290279) - Comprehensive guide to tree structures
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) - Classic algorithms textbook
- [Tree Traversals Visualization](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) - Interactive tree visualization tools
- [Expression Parser Tutorial](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) - Shunting yard algorithm explanation
- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html) - Official Python documentation
- [GeeksforGeeks Trees Tutorial](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/) - Detailed tree traversal explanations
- [Visualgo Tree Animations](https://visualgo.net/en/bst) - Animated tree operations

---

Created with 💚 by Elliot Garamendi