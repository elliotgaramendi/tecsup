# 🌳 Binary Trees Implementation Guide

## Table of Contents

- [🌳 Binary Trees Implementation Guide](#-binary-trees-implementation-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Understanding the Fundamental Concept](#1-understanding-the-fundamental-concept)
    - [Tree Basics](#tree-basics)
    - [Binary Trees](#binary-trees)
    - [Tree Terminology](#tree-terminology)
    - [Types of Binary Trees](#types-of-binary-trees)
  - [2. Progressive Implementations](#2-progressive-implementations)
    - [2.1 Basic Binary Tree Node](#21-basic-binary-tree-node)
    - [2.2 Binary Tree with Traversals](#22-binary-tree-with-traversals)
    - [2.3 Binary Tree with Extended Operations](#23-binary-tree-with-extended-operations)
  - [3. Practical Applications](#3-practical-applications)
    - [3.1 Expression Tree Evaluator](#31-expression-tree-evaluator)
    - [3.2 Directory Structure Representation](#32-directory-structure-representation)
  - [4. Real-world Case Study: Compiler Syntax Tree](#4-real-world-case-study-compiler-syntax-tree)
  - [5. Technical Challenges](#5-technical-challenges)
    - [Challenge 1: Tree Height Calculation](#challenge-1-tree-height-calculation)
    - [Challenge 2: Count Leaf Nodes](#challenge-2-count-leaf-nodes)
    - [Challenge 3: Tree Mirroring](#challenge-3-tree-mirroring)
    - [Challenge 4: Level Order Traversal](#challenge-4-level-order-traversal)
    - [Challenge 5: Check if a Binary Tree is Balanced](#challenge-5-check-if-a-binary-tree-is-balanced)
  - [6. Comparative Analysis](#6-comparative-analysis)
  - [7. Next Learning Steps](#7-next-learning-steps)
  - [8. Key Conclusions](#8-key-conclusions)

## 1. Understanding the Fundamental Concept

### Tree Basics

A tree is a non-linear data structure that represents hierarchical relationships between elements 🌱. Unlike linear data structures like arrays and linked lists, trees allow for organizing data with multiple connections between elements.

Key characteristics:
- Trees have a hierarchical structure with a single root node 🌱
- Every node (except the root) has exactly one parent node
- A node can have zero or more child nodes
- Trees cannot contain cycles ⚠️

### Binary Trees

A binary tree is a specialized tree in which each node has at most two children, commonly referred to as the left child and right child 👨‍👧‍👦.

Visual representation of a binary tree:
```
      A
     / \
    B   C
   / \   \
  D   E   F
```

### Tree Terminology

Let's understand the important terms with this example tree:
```
      1
     / \
    2   3
   / \   \
  4   5   6
 /       / \
7       8   9
```

- **Root**: The topmost node (node 1)
- **Edge**: Connection between nodes (line between parent and child)
- **Leaf Node**: A node without children (nodes 4, 7, 5, 8, 9)
- **Internal Node**: A node with at least one child (nodes 1, 2, 3, 6)
- **Siblings**: Nodes that share the same parent (nodes 2 and 3 are siblings)
- **Depth of a Node**: Length of the path from root to the node
  - Depth of node 1 (root) is 0
  - Depth of nodes 2 and 3 is 1
  - Depth of nodes 4, 5, and 6 is 2
- **Height of a Node**: Length of the longest path from the node to a leaf
  - Height of leaf nodes is 0
  - Height of the tree is the height of the root (3 in this example)
- **Level**: Set of nodes at a given depth (root is level 0)

### Types of Binary Trees

1. **Full Binary Tree**: Every node has either 0 or 2 children 🌲
   ```
       A
      / \
     B   C
    / \   \
   D   E   F
      / \
     G   H
   ```

2. **Complete Binary Tree**: All levels are filled except possibly the last one, which is filled from left to right 📊
   ```
       A
      / \
     B   C
    / \ / \
   D  E F  G
   ```

3. **Perfect Binary Tree**: All internal nodes have two children and all leaves are at the same level 💯
   ```
       A
      / \
     B   C
    / \ / \
   D  E F  G
   ```

4. **Balanced Binary Tree**: The height difference between left and right subtrees for every node is not more than 1 ⚖️
   ```
       A
      / \
     B   C
    / \
   D   E
   ```

## 2. Progressive Implementations

Let's implement binary trees step by step, from basic to more advanced.

### 2.1 Basic Binary Tree Node

First, let's create a simple binary tree node class:

```python
class TreeNode:
    """Basic node in a binary tree."""
    
    def __init__(self, value):
        self.value = value       # 📊 Data stored in the node
        self.left = None         # 👈 Reference to left child
        self.right = None        # 👉 Reference to right child

def create_sample_tree():
    """Create a sample binary tree for testing."""
    # Create the root node
    root = TreeNode(1)           # 🌱 Root
    
    # Level 1 nodes
    root.left = TreeNode(2)      # 👈 Left child
    root.right = TreeNode(3)     # 👉 Right child
    
    # Level 2 nodes
    root.left.left = TreeNode(4) # 👈👈 Left-left child
    root.left.right = TreeNode(5) # 👈👉 Left-right child
    root.right.right = TreeNode(6) # 👉👉 Right-right child
    
    # Our tree looks like:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    
    return root

# Test creation of a simple binary tree
def test_tree_node():
    # Test 1: Create a node
    node = TreeNode(10)
    assert node.value == 10
    assert node.left is None
    assert node.right is None
    
    # Test 2: Create a simple tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert root.value == 1
    assert root.left.value == 2
    assert root.right.value == 3
    
    # Test 3: Create a more complex tree
    tree = create_sample_tree()
    assert tree.value == 1
    assert tree.left.value == 2
    assert tree.right.value == 3
    assert tree.left.left.value == 4
    assert tree.left.right.value == 5
    assert tree.right.right.value == 6
    
    # Test 4: Check invalid values
    empty_tree = None
    assert empty_tree is None
    
    # Test 5: Create a node with non-integer value
    string_node = TreeNode("hello")
    assert string_node.value == "hello"
    
    print("All basic tree node tests passed! ✅")

# Run the tests
test_tree_node()
```

### 2.2 Binary Tree with Traversals

Now, let's add the fundamental tree traversals:

```python
class BinaryTree:
    """Binary tree implementation with basic traversals."""
    
    def __init__(self, root=None):
        self.root = root    # 🌱 Reference to the root node
    
    def preorder_traversal(self, node, result=None):
        """DLR: Process Data, then Left, then Right subtree."""
        if result is None:
            result = []
        
        if node:
            # Visit the node first (D)
            result.append(node.value)
            # Traverse left subtree (L)
            self.preorder_traversal(node.left, result)
            # Traverse right subtree (R)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def inorder_traversal(self, node, result=None):
        """LDR: Process Left, then Data, then Right subtree."""
        if result is None:
            result = []
        
        if node:
            # Traverse left subtree (L)
            self.inorder_traversal(node.left, result)
            # Visit the node (D)
            result.append(node.value)
            # Traverse right subtree (R)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node, result=None):
        """LRD: Process Left, then Right, then Data."""
        if result is None:
            result = []
        
        if node:
            # Traverse left subtree (L)
            self.postorder_traversal(node.left, result)
            # Traverse right subtree (R)
            self.postorder_traversal(node.right, result)
            # Visit the node (D)
            result.append(node.value)
        
        return result
    
    def traverse(self, order="inorder"):
        """Traverse the tree in the specified order."""
        if order == "preorder":
            return self.preorder_traversal(self.root)
        elif order == "inorder":
            return self.inorder_traversal(self.root)
        elif order == "postorder":
            return self.postorder_traversal(self.root)
        else:
            raise ValueError("Invalid traversal order. Use 'preorder', 'inorder', or 'postorder'")

# Test the traversal methods
def test_tree_traversals():
    # Create our test tree:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    root = create_sample_tree()
    tree = BinaryTree(root)
    
    # Test 1: Test preorder traversal (DLR)
    preorder = tree.traverse("preorder")
    assert preorder == [1, 2, 4, 5, 3, 6], f"Expected [1, 2, 4, 5, 3, 6], got {preorder}"
    
    # Test 2: Test inorder traversal (LDR)
    inorder = tree.traverse("inorder")
    assert inorder == [4, 2, 5, 1, 3, 6], f"Expected [4, 2, 5, 1, 3, 6], got {inorder}"
    
    # Test 3: Test postorder traversal (LRD)
    postorder = tree.traverse("postorder")
    assert postorder == [4, 5, 2, 6, 3, 1], f"Expected [4, 5, 2, 6, 3, 1], got {postorder}"
    
    # Test 4: Test with empty tree
    empty_tree = BinaryTree()
    assert empty_tree.traverse("inorder") == [], "Empty tree should return empty list"
    
    # Test 5: Test with invalid traversal order
    try:
        tree.traverse("sideways")
        assert False, "Should raise ValueError for invalid traversal order"
    except ValueError:
        assert True, "Correctly raised ValueError"
    
    print("All tree traversal tests passed! ✅")

# Run the tests
test_tree_traversals()
```

The three traversal methods allow us to visit the nodes in different orders:

1. **Preorder (DLR)**: Visit the current node first, then recursively visit left and right subtrees. Useful for creating a copy of the tree or prefix expression.

2. **Inorder (LDR)**: Visit the left subtree, then the current node, then the right subtree. For binary search trees, this gives nodes in ascending order.

3. **Postorder (LRD)**: Visit the left subtree, then the right subtree, then the current node. Useful for deleting the tree or evaluating expressions.

Visual example:
```
      1
     / \
    2   3
   / \   \
  4   5   6

Preorder: 1, 2, 4, 5, 3, 6
Inorder: 4, 2, 5, 1, 3, 6
Postorder: 4, 5, 2, 6, 3, 1
```

### 2.3 Binary Tree with Extended Operations

Now let's add some more useful operations to our binary tree:

```python
class ExtendedBinaryTree(BinaryTree):
    """Binary tree with extended operations."""
    
    def height(self, node=None):
        """Calculate height of the tree (or subtree)."""
        if node is None:
            node = self.root
        
        if not node:
            return -1  # Empty tree has height -1
        
        # Recursively find the height of left and right subtrees
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        # Height is the maximum of left and right subtree heights, plus 1
        return max(left_height, right_height) + 1
    
    def size(self, node=None):
        """Count the number of nodes in the tree (or subtree)."""
        if node is None:
            node = self.root
        
        if not node:
            return 0  # Empty tree has size 0
        
        # Size is 1 (this node) plus sizes of left and right subtrees
        return 1 + self.size(node.left) + self.size(node.right)
    
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Print the tree structure for visualization."""
        if node is None:
            node = self.root
        
        if not node:
            print("Empty tree")
            return
        
        # Print the current node with indentation
        print(" " * (level * 4) + prefix + str(node.value))
        
        # Recursively print the children
        if node.left or node.right:
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
                
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Test the extended tree operations
def test_extended_tree():
    # Create our test tree:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    root = create_sample_tree()
    tree = ExtendedBinaryTree(root)
    
    # Test 1: Test height calculation
    assert tree.height() == 2, f"Expected height 2, got {tree.height()}"
    
    # Create a deeper tree for testing
    deep_root = TreeNode(1)
    deep_root.left = TreeNode(2)
    deep_root.left.left = TreeNode(3)
    deep_root.left.left.left = TreeNode(4)
    deep_tree = ExtendedBinaryTree(deep_root)
    
    # Test 2: Test height with deeper tree
    assert deep_tree.height() == 3, f"Expected height 3, got {deep_tree.height()}"
    
    # Test 3: Test size calculation
    assert tree.size() == 6, f"Expected size 6, got {tree.size()}"
    
    # Test 4: Test with empty tree
    empty_tree = ExtendedBinaryTree()
    assert empty_tree.height() == -1, "Empty tree should have height -1"
    assert empty_tree.size() == 0, "Empty tree should have size 0"
    
    # Test 5: Test with single node tree
    single_node_tree = ExtendedBinaryTree(TreeNode(42))
    assert single_node_tree.height() == 0, "Single node tree should have height 0"
    assert single_node_tree.size() == 1, "Single node tree should have size 1"
    
    print("All extended tree tests passed! ✅")
    
    # Demonstrate tree printing
    print("\nTree Visualization:")
    tree.print_tree()

# Run the tests
test_extended_tree()
```

Our extended tree implementation now includes:

1. **Height Calculation**: Finds the longest path from the root to any leaf (maximum depth)
2. **Size Calculation**: Counts the total number of nodes in the tree
3. **Tree Visualization**: Prints the tree structure for easier debugging

These operations are fundamental for more complex tree algorithms and applications.

## 3. Practical Applications

Let's explore some practical applications of binary trees.

### 3.1 Expression Tree Evaluator

Binary trees are perfect for representing and evaluating mathematical expressions. Operators are internal nodes, and operands are leaves.

```python
class ExpressionNode(TreeNode):
    """Node for an expression tree."""
    
    def is_operator(self):
        """Check if the node is an operator."""
        return self.value in "+-*/"

class ExpressionTree:
    """Binary tree for evaluating mathematical expressions."""
    
    def __init__(self):
        self.root = None
    
    def build_from_postfix(self, postfix_expr):
        """Build the expression tree from a postfix expression."""
        stack = []
        
        for token in postfix_expr:
            node = ExpressionNode(token)
            
            # If token is an operator, pop two operands from stack
            if token in "+-*/":
                # Right operand is popped first (stack is LIFO)
                node.right = stack.pop()
                node.left = stack.pop()
            
            # Push the node to the stack
            stack.append(node)
        
        # The final node on the stack is the root of the expression tree
        if stack:
            self.root = stack.pop()
    
    def evaluate(self, node=None):
        """Recursively evaluate the expression tree."""
        if node is None:
            node = self.root
            
        if not node:
            return 0
        
        # If node is an operand (leaf node)
        if not node.is_operator():
            return float(node.value)
        
        # Evaluate left and right subtrees
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        
        # Apply the operator
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            if right_val == 0:
                raise ZeroDivisionError("Division by zero")
            return left_val / right_val
    
    def print_infix(self, node=None):
        """Print the infix expression (with parentheses)."""
        if node is None:
            node = self.root
            
        if not node:
            return ""
        
        if node.is_operator():
            # Add parentheses around operations to preserve precedence
            left = self.print_infix(node.left)
            right = self.print_infix(node.right)
            return f"({left} {node.value} {right})"
        else:
            return node.value

# Test the expression tree
def test_expression_tree():
    expr_tree = ExpressionTree()
    
    # Test 1: Simple addition
    # Postfix: 3 4 +
    expr_tree.build_from_postfix(["3", "4", "+"])
    assert expr_tree.evaluate() == 7, f"Expected 3+4=7, got {expr_tree.evaluate()}"
    assert expr_tree.print_infix() == "(3 + 4)", f"Expected '(3 + 4)', got '{expr_tree.print_infix()}'"
    
    # Test 2: Complex expression
    # Postfix: 5 2 3 * +
    # Infix: 5 + (2 * 3)
    expr_tree = ExpressionTree()
    expr_tree.build_from_postfix(["5", "2", "3", "*", "+"])
    assert expr_tree.evaluate() == 11, f"Expected 5+(2*3)=11, got {expr_tree.evaluate()}"
    
    # Test 3: More complex expression
    # Postfix: 4 5 + 2 * 8 /
    # Infix: ((4 + 5) * 2) / 8
    expr_tree = ExpressionTree()
    expr_tree.build_from_postfix(["4", "5", "+", "2", "*", "8", "/"])
    assert expr_tree.evaluate() == 2.25, f"Expected ((4+5)*2)/8=2.25, got {expr_tree.evaluate()}"
    
    # Test 4: Empty expression
    expr_tree = ExpressionTree()
    assert expr_tree.evaluate() == 0, "Empty expression should evaluate to 0"
    
    # Test 5: Division by zero
    expr_tree = ExpressionTree()
    expr_tree.build_from_postfix(["5", "0", "/"])
    try:
        expr_tree.evaluate()
        assert False, "Should raise ZeroDivisionError"
    except ZeroDivisionError:
        assert True, "Correctly raised ZeroDivisionError"
    
    print("All expression tree tests passed! ✅")

# Run the tests
test_expression_tree()
```

For this example, let's consider the expression `(4 + 5) * 2`:

1. The postfix notation is: `4 5 + 2 *`
2. The expression tree will look like:
```
    *
   / \
  +   2
 / \
4   5
```

3. Evaluating this tree:
   - 4 + 5 = 9
   - 9 * 2 = 18

The tree helps maintain proper operator precedence and can be used for evaluating expressions, parsing, and more.

### 3.2 Directory Structure Representation

Binary trees (or more generally, trees) can be used to represent hierarchical structures like file systems:

```python
class FileNode:
    """Node representing a file or directory in a file system."""
    
    def __init__(self, name, is_directory=False):
        self.name = name               # 📄 File/directory name
        self.is_directory = is_directory  # 📁 Is this a directory?
        self.children = []             # 👨‍👩‍👧‍👦 Children nodes
        self.parent = None             # 👨 Parent node
    
    def add_child(self, child):
        """Add a child node."""
        child.parent = self
        self.children.append(child)
        return child
    
    def get_path(self):
        """Get the full path of this node."""
        if self.parent is None:
            return self.name
        return self.parent.get_path() + "/" + self.name

class FileSystem:
    """Simple file system representation."""
    
    def __init__(self, root_name="/"):
        """Initialize the file system with a root directory."""
        self.root = FileNode(root_name, True)
    
    def create_directory(self, path, directory_name):
        """Create a new directory at the given path."""
        parent = self._find_node(path)
        if not parent or not parent.is_directory:
            raise ValueError(f"Invalid path: {path}")
        
        # Check if directory already exists
        for child in parent.children:
            if child.name == directory_name and child.is_directory:
                return child
        
        new_dir = FileNode(directory_name, True)
        parent.add_child(new_dir)
        return new_dir
    
    def create_file(self, path, file_name):
        """Create a new file at the given path."""
        parent = self._find_node(path)
        if not parent or not parent.is_directory:
            raise ValueError(f"Invalid path: {path}")
        
        # Check if file already exists
        for child in parent.children:
            if child.name == file_name and not child.is_directory:
                return child
        
        new_file = FileNode(file_name)
        parent.add_child(new_file)
        return new_file
    
    def _find_node(self, path):
        """Find a node at the given path."""
        if not path or path == "/":
            return self.root
        
        parts = path.strip("/").split("/")
        current = self.root
        
        for part in parts:
            found = False
            for child in current.children:
                if child.name == part:
                    current = child
                    found = True
                    break
            if not found:
                return None
        
        return current
    
    def list_directory(self, path):
        """List all files and directories at the given path."""
        node = self._find_node(path)
        if not node or not node.is_directory:
            raise ValueError(f"Invalid directory path: {path}")
        
        return [child.name for child in node.children]
    
    def print_tree(self, node=None, level=0):
        """Print the file system tree."""
        if node is None:
            node = self.root
        
        # Print the current node with indentation
        prefix = "📁" if node.is_directory else "📄"
        print("  " * level + f"{prefix} {node.name}")
        
        # Recursively print children
        for child in node.children:
            self.print_tree(child, level + 1)

# Test the file system tree
def test_file_system():
    fs = FileSystem()
    
    # Test 1: Create directories
    home = fs.create_directory("/", "home")
    user = fs.create_directory("/home", "user")
    documents = fs.create_directory("/home/user", "documents")
    
    # Test directory paths
    assert home.get_path() == "/home", f"Expected '/home', got '{home.get_path()}'"
    assert user.get_path() == "/home/user", f"Expected '/home/user', got '{user.get_path()}'"
    
    # Test 2: Create files
    fs.create_file("/home/user", "notes.txt")
    fs.create_file("/home/user/documents", "report.pdf")
    
    # Test directory listing
    user_files = fs.list_directory("/home/user")
    assert "documents" in user_files, "Expected 'documents' in user directory"
    assert "notes.txt" in user_files, "Expected 'notes.txt' in user directory"
    
    # Test 3: Invalid paths
    try:
        fs.create_file("/nonexistent", "test.txt")
        assert False, "Should raise ValueError for invalid path"
    except ValueError:
        assert True, "Correctly raised ValueError"
    
    # Test 4: Create existing directory
    existing_dir = fs.create_directory("/home", "user")
    assert existing_dir == user, "Should return existing directory node"
    
    # Test 5: Create file in a file
    try:
        fs.create_file("/home/user/notes.txt", "invalid.txt")
        assert False, "Should raise ValueError for creating file inside a file"
    except ValueError:
        assert True, "Correctly raised ValueError"
    
    print("All file system tests passed! ✅")
    
    # Print the file system tree
    print("\nFile System Structure:")
    fs.print_tree()

# Run the tests
test_file_system()
```

This implementation creates a hierarchical tree structure to represent a file system:
- Each node can be a file or a directory
- Directories can have multiple children (making this a general tree, not a binary tree)
- The tree allows for path-based navigation

While this isn't strictly a binary tree (since directories can have more than two children), it demonstrates how tree structures can model hierarchical data.

## 4. Real-world Case Study: Compiler Syntax Tree

One of the most important applications of trees is in compilers and interpreters 🔄. Here's a simplified example of how a syntax tree might be used in a compiler:

```python
class SyntaxNode:
    """Node in a syntax tree."""
    
    def __init__(self, node_type, value=None):
        self.type = node_type    # 🏷️ Node type (e.g., 'variable', 'operator')
        self.value = value       # 📊 Node value (e.g., variable name, operator symbol)
        self.children = []       # 👨‍👩‍👧‍👦 Child nodes
    
    def add_child(self, child):
        """Add a child node."""
        self.children.append(child)
        return child

class SimpleCompiler:
    """A very simple compiler that builds and evaluates syntax trees."""
    
    def parse_expression(self, expression):
        """Parse a simple mathematical expression and build a syntax tree."""
        # This is a simplified parser for demonstration
        # It handles expressions like "x = 5 + 3 * 2"
        
        # Split the expression by space
        tokens = expression.split()
        
        # Check if it's an assignment
        if '=' in tokens:
            # Create the assignment node
            root = SyntaxNode('assignment')
            
            # Find the position of equals sign
            equals_pos = tokens.index('=')
            
            # Add variable name as first child
            var_node = SyntaxNode('variable', tokens[0])
            root.add_child(var_node)
            
            # Parse the right side of the assignment
            right_side = ' '.join(tokens[equals_pos + 1:])
            expr_node = self._parse_arithmetic(right_side)
            root.add_child(expr_node)
            
            return root
        else:
            # Just an arithmetic expression
            return self._parse_arithmetic(expression)
    
    def _parse_arithmetic(self, expr):
        """Parse an arithmetic expression (simplified)."""
        # This is a very simplified parser for demonstration
        # In a real compiler, this would use more sophisticated techniques
        
        tokens = expr.split()
        
        # Look for lowest precedence operator (+ or -)
        for i in range(len(tokens) - 1, 0, -1):
            if tokens[i] in ['+', '-']:
                # Create operator node
                op_node = SyntaxNode('operator', tokens[i])
                
                # Parse left and right expressions
                left_expr = ' '.join(tokens[:i])
                right_expr = ' '.join(tokens[i+1:])
                
                op_node.add_child(self._parse_arithmetic(left_expr) if left_expr else None)
                op_node.add_child(self._parse_arithmetic(right_expr) if right_expr else None)
                
                return op_node
        
        # If no operators, it must be a number or variable
        if len(tokens) == 1:
            # Try to convert to number
            try:
                return SyntaxNode('number', float(tokens[0]))
            except ValueError:
                return SyntaxNode('variable', tokens[0])
        
        # If we have parentheses, remove them and parse inside
        if tokens[0] == '(' and tokens[-1] == ')':
            inner_expr = ' '.join(tokens[1:-1])
            return self._parse_arithmetic(inner_expr)
        
        # Fallback (this is a simplification)
        return SyntaxNode('unknown', ' '.join(tokens))
    
    def print_syntax_tree(self, node, level=0):
        """Print the syntax tree for visualization."""
        if not node:
            return
        
        # Print the current node with indentation
        node_info = f"{node.type}"
        if node.value is not None:
            node_info += f": {node.value}"
        
        print("  " * level + node_info)
        
        # Recursively print children
        for child in node.children:
            self.print_syntax_tree(child, level + 1)
    
    def evaluate(self, node, variables=None):
        """Evaluate the syntax tree."""
        if variables is None:
            variables = {}
        
        if not node:
            return None
        
        # Handle different node types
        if node.type == 'number':
            return node.value
        
        elif node.type == 'variable':
            if node.value in variables:
                return variables[node.value]
            raise ValueError(f"Undefined variable: {node.value}")
        
        elif node.type == 'operator':
            # Evaluate operands
            left_val = self.evaluate(node.children[0], variables)
            right_val = self.evaluate(node.children[1], variables)
            
            # Apply operation
            if node.value == '+':
                return left_val + right_val
            elif node.value == '-':
                return left_val - right_val
            elif node.value == '*':
                return left_val * right_val
            elif node.value == '/':
                if right_val == 0:
                    raise ZeroDivisionError("Division by zero")
                return left_val / right_val
        
        elif node.type == 'assignment':
            # Evaluate right side
            var_name = node.children[0].value
            var_value = self.evaluate(node.children[1], variables)
            
            # Update variables dictionary
            variables[var_name] = var_value
            return var_value
        
        return None

# Test the simple compiler
def test_simple_compiler():
    compiler = SimpleCompiler()
    
    # Test 1: Simple arithmetic
    tree1 = compiler.parse_expression("5 + 3")
    result1 = compiler.evaluate(tree1)
    assert result1 == 8, f"Expected 5+3=8, got {result1}"
    
    # Test 2: Operator precedence
    tree2 = compiler.parse_expression("5 + 3 * 2")
    result2 = compiler.evaluate(tree2)
    assert result2 == 11, f"Expected 5+3*2=11, got {result2}"
    
    # Test 3: Variable assignment
    variables = {}
    tree3 = compiler.parse_expression("x = 10")
    result3 = compiler.evaluate(tree3, variables)
    assert result3 == 10, f"Expected x=10, got {result3}"
    assert variables['x'] == 10, f"Expected variables['x']=10, got {variables['x']}"
    
    # Test 4: Expression with variables
    tree4 = compiler.parse_expression("x + 5")
    result4 = compiler.evaluate(tree4, variables)
    assert result4 == 15, f"Expected x+5=15, got {result4}"
    
    # Test 5: More complex expression
    tree5 = compiler.parse_expression("y = x * 2 + 3")
    result5 = compiler.evaluate(tree5, variables)
    assert result5 == 23, f"Expected y=x*2+3=23, got {result5}"
    assert variables['y'] == 23, f"Expected variables['y']=23, got {variables['y']}"
    
    print("All compiler tests passed! ✅")
    
    # Visualize a syntax tree
    print("\nSyntax Tree for 'y = x * 2 + 3':")
    compiler.print_syntax_tree(tree5)

# Run the tests
test_simple_compiler()
```

This case study demonstrates how compilers use trees to represent the structure of a program:
1. **Parsing**: Converts the text code into a syntax tree
2. **Analysis**: Traverses the tree to verify semantics
3. **Evaluation/Code Generation**: Traverses the tree to execute or generate code

The syntax tree preserves the hierarchical structure of the code, maintaining the correct order of operations and nesting relationships.

For the expression `y = x * 2 + 3` (with x = 10), the syntax tree might look like:
```
assignment
  ├── variable: y
  └── operator: +
       ├── operator: *
       │    ├── variable: x
       │    └── number: 2.0
       └── number: 3.0
```

When evaluated, this gives the correct result of 23.

## 5. Technical Challenges

Here are five challenges to test your understanding of binary trees. Try to solve them on your own before looking at solutions! 🧩

### Challenge 1: Tree Height Calculation

**Problem**: Write a function to calculate the height of a binary tree. The height is the number of edges on the longest path from the root to a leaf.

**Example**:
```
      1
     / \
    2   3
   / \
  4   5
```
The height of this tree is 2.

**Tests**:

```python
def test_tree_height():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Test Case 2: Empty tree
    empty_tree = None
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    
    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)

    # TODO: Implement the tree_height function and run the tests
```

### Challenge 2: Count Leaf Nodes

**Problem**: Write a function to count the number of leaf nodes in a binary tree. A leaf node is a node that has no children.

**Example**:
```
      1
     / \
    2   3
   / \
  4   5
```
This tree has 3 leaf nodes: 4, 5, and 3.

**Tests**:

```python
def test_count_leaves():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Test Case 2: Empty tree
    empty_tree = None
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    
    # Test Case 4: No leaf nodes at first level
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    
    # Test Case 5: All nodes are leaves except root
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    
    # TODO: Implement the count_leaves function and run the tests
```

### Challenge 3: Tree Mirroring

**Problem**: Write a function to mirror a binary tree. Mirroring means swapping the left and right children of every node.

**Example**:
```
Before mirroring:
      1
     / \
    2   3
   / \
  4   5

After mirroring:
      1
     / \
    3   2
       / \
      5   4
```

**Tests**:

```python
def test_mirror_tree():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    # Test Case 2: Empty tree
    empty_tree = None
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    
    # Test Case 4: Tree with only left children
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    
    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    
    # TODO: Implement the mirror_tree function and run the tests
```

### Challenge 4: Level Order Traversal

**Problem**: Write a function to perform level order traversal of a binary tree. In level order traversal, nodes are visited level by level, from left to right.

**Example**:
```
      1
     / \
    2   3
   / \   \
  4   5   6

Level order traversal: [1, 2, 3, 4, 5, 6]
```

**Tests**:

```python
def test_level_order_traversal():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    # Test Case 2: Empty tree
    empty_tree = None
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    
    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    
    # Test Case 5: Right-skewed tree
    right_skewed = TreeNode(1)
    right_skewed.right = TreeNode(2)
    right_skewed.right.right = TreeNode(3)
    right_skewed.right.right.right = TreeNode(4)
    
    # TODO: Implement the level_order_traversal function and run the tests
```

### Challenge 5: Check if a Binary Tree is Balanced

**Problem**: Write a function to determine if a binary tree is balanced. A balanced tree is one where the height difference between left and right subtrees of any node is not more than 1.

**Example**:
```
Balanced tree:
      1
     / \
    2   3
   / \
  4   5

Unbalanced tree:
      1
     / 
    2   
   / 
  3  
 /
4
```

**Tests**:

```python
def test_is_balanced():
    # Test Case 1: Balanced tree
    balanced = TreeNode(1)
    balanced.left = TreeNode(2)
    balanced.right = TreeNode(3)
    balanced.left.left = TreeNode(4)
    balanced.left.right = TreeNode(5)
    
    # Test Case 2: Empty tree (trivially balanced)
    empty_tree = None
    
    # Test Case 3: Single node tree (trivially balanced)
    single_node = TreeNode(1)
    
    # Test Case 4: Unbalanced tree - left-heavy
    unbalanced_left = TreeNode(1)
    unbalanced_left.left = TreeNode(2)
    unbalanced_left.left.left = TreeNode(3)
    unbalanced_left.left.left.left = TreeNode(4)
    
    # Test Case 5: Just balanced on the edge case
    edge_balanced = TreeNode(1)
    edge_balanced.left = TreeNode(2)
    edge_balanced.right = TreeNode(3)
    edge_balanced.left.left = TreeNode(4)
    edge_balanced.left.right = TreeNode(5)
    edge_balanced.left.left.left = TreeNode(6)
    
    # TODO: Implement the is_balanced function and run the tests
```

## 6. Comparative Analysis

Let's compare different tree implementations and operations:

| **Aspect**                    | **Simple Binary Tree**                    | **Balanced Binary Tree**                                    | **Expression Tree**                 | **General Tree**                         |
| ----------------------------- | ----------------------------------------- | ----------------------------------------------------------- | ----------------------------------- | ---------------------------------------- |
| **Structure**                 | Each node has at most 2 children          | Each node has at most 2 children with height difference ≤ 1 | Special binary tree for expressions | Nodes can have any number of children    |
| **Height**                    | O(n) worst case                           | O(log n)                                                    | Depends on expression complexity    | Varies widely                            |
| **Search Efficiency**         | O(n) worst case                           | O(log n)                                                    | Not typically used for searching    | O(n)                                     |
| **Implementation Complexity** | Low 🟢                                     | Medium 🟡                                                    | Medium 🟡                            | Low 🟢                                    |
| **Memory Usage**              | 2 pointers per node                       | 2 pointers per node                                         | 2 pointers per node                 | Dynamic array or linked list of children |
| **Best Use Cases**            | Simple hierarchies, expression evaluation | Searching, sorting, balancing workloads                     | Mathematical expressions, compilers | File systems, organization charts        |
| **Common Operations**         | Traversals (pre/in/post order)            | Insert, delete, search                                      | Evaluation, conversion              | Path finding, hierarchy management       |

**Key Insights:**

1. **Standard Binary Trees** 🌳
   - Simple to implement
   - Useful for representing hierarchical relationships
   - Can degenerate to linear structures in worst case
   - Traversal operations are O(n)

2. **Balanced Binary Trees** ⚖️
   - More complex to maintain balance
   - Guarantee O(log n) operations
   - Require additional balancing logic (AVL, Red-Black, etc.)
   - Excellent for search-intensive applications

3. **Expression Trees** 🧮
   - Specialized for mathematical expressions
   - Support easy evaluation with proper precedence
   - Natural representation of formulas
   - Enable different notation conversions (infix, prefix, postfix)

4. **File System Trees** 📁
   - General trees (not binary)
   - Represent hierarchical relationships effectively
   - Support path-based navigation
   - Useful for modeling real-world hierarchies

5. **Syntax Trees** 🔠
   - Used in compilers and interpreters
   - Preserve semantic structure of code
   - Enable traversal-based operations (parsing, analysis, execution)
   - Form the basis for language processing

The choice of tree type depends on the specific requirements of your application, with trade-offs in terms of complexity, efficiency, and functionality.

## 7. Next Learning Steps

After mastering the basics of binary trees, consider exploring these advanced topics:

1. **Balanced Binary Search Trees** ⚖️
   - AVL Trees: Self-balancing with strict balance requirements
   - Red-Black Trees: Self-balancing with better insertion/deletion performance
   - B-Trees: Optimized for disk-based storage systems

2. **Specialized Tree Structures** 🌿
   - Tries: Efficient for string operations and prefix searches
   - Quad Trees: Used in spatial indexing and image processing
   - Heaps: Priority queues with efficient min/max operations
   - Segment Trees: Efficient for range queries

3. **Tree Algorithms** 🔍
   - Tree rotations for balancing
   - Lowest Common Ancestor (LCA) finding
   - Serialization and deserialization of trees
   - Path finding and graph traversals

4. **Real-world Applications** 🌐
   - Decision trees in machine learning
   - Game trees for AI (minimax, alpha-beta pruning)
   - Computational geometry with binary space partitioning
   - XML/HTML/DOM parsing and manipulation

5. **Advanced Compiler Theory** 💻
   - Abstract Syntax Trees (AST)
   - Parse trees and grammar analysis
   - Code optimization techniques
   - Static analysis algorithms

## 8. Key Conclusions

Binary trees are powerful data structures that form the foundation for many algorithms and applications:

1. **Hierarchical Representation** 📊 - Trees naturally model hierarchical relationships, making them perfect for file systems, organization charts, and nested structures.

2. **Efficient Operations** ⚡ - When balanced, binary trees provide O(log n) operations, significantly better than linear data structures for large datasets.

3. **Traversal Flexibility** 🔄 - Different traversal methods (preorder, inorder, postorder, level order) enable various processing approaches based on the application needs.

4. **Foundation for Advanced Structures** 🏗️ - Binary trees serve as building blocks for more sophisticated data structures like BST, AVL Trees, and Heaps.

5. **Compiler and Language Processing** 🔤 - Syntax trees are essential in compiler design, enabling the analysis, transformation, and execution of programming languages.

6. **Expression Evaluation** 🧮 - Binary trees elegantly handle mathematical expressions while preserving operator precedence and supporting efficient evaluation.

7. **Memory Efficiency** 💾 - Binary trees use minimal pointers per node (just two), making them memory-efficient compared to more complex structures.

In conclusion, binary trees strike an excellent balance between simplicity and power. Mastering tree operations and understanding when to use different tree variants will significantly enhance your problem-solving toolkit as a programmer. The hierarchical nature of trees makes them indispensable in countless algorithms and real-world applications. 🌳👨‍💻