# Generic and Expression Trees: Fundamentals Guide

## Table of Contents

- [Generic and Expression Trees: Fundamentals Guide](#generic-and-expression-trees-fundamentals-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Understanding the Fundamental Concept](#1-understanding-the-fundamental-concept)
    - [What is a Generic Tree?](#what-is-a-generic-tree)
    - [What is an Expression Tree?](#what-is-an-expression-tree)
    - [Core Operations](#core-operations)
  - [2. Progressive Implementations](#2-progressive-implementations)
    - [Basic Generic Tree Implementation](#basic-generic-tree-implementation)
    - [Generic Tree Traversals](#generic-tree-traversals)
    - [Expression Tree Implementation](#expression-tree-implementation)
    - [Expression Tree Evaluation](#expression-tree-evaluation)
  - [3. Practical Applications](#3-practical-applications)
    - [File System Representation](#file-system-representation)
    - [Mathematical Expression Evaluation](#mathematical-expression-evaluation)
    - [Decision Trees](#decision-trees)
  - [4. Real-world Case Study: Calculator Engine](#4-real-world-case-study-calculator-engine)
  - [5. Technical Challenges](#5-technical-challenges)
    - [Challenge 1: Convert Infix to Postfix](#challenge-1-convert-infix-to-postfix)
    - [Challenge 2: Build Expression Tree from Infix](#challenge-2-build-expression-tree-from-infix)
    - [Challenge 3: Generic Tree Height](#challenge-3-generic-tree-height)
    - [Challenge 4: Find All Leaves](#challenge-4-find-all-leaves)
    - [Challenge 5: Expression Tree Simplification](#challenge-5-expression-tree-simplification)
  - [6. Comparative Analysis](#6-comparative-analysis)
    - [Key Differences](#key-differences)
    - [When to use which](#when-to-use-which)
  - [7. Next Learning Steps](#7-next-learning-steps)
  - [8. Key Conclusions](#8-key-conclusions)

## 1. Understanding the Fundamental Concept

### What is a Generic Tree?

A generic tree (also called n-ary tree) is a tree where each node can have any number of children. Unlike binary trees that limit nodes to two children, generic trees allow flexible hierarchies. 🌳

```
          A
        / | \
       B  C  D
      /|\    |
     E F G   H
```

Key characteristics:
- Each node can have zero or more children 👨‍👩‍👧‍👦
- No limit on the number of children per node 🔢
- Perfect for representing hierarchical data like file systems 📁
- More flexible than binary trees but potentially less efficient 📊

### What is an Expression Tree?

An expression tree is a binary tree used to represent mathematical expressions. Each internal node is an operator (+, -, *, /) and each leaf is an operand (number or variable). 🧮

```
Expression: (3 + 4) * 5

        *
       / \
      +   5
     / \
    3   4
```

Key characteristics:
- Binary tree structure (each operator needs exactly two operands) 🌲
- Leaves contain values, internal nodes contain operators 🔣
- Allows easy evaluation of complex expressions 📈
- Supports different notations: infix, prefix, and postfix 📝

### Core Operations

Both tree types support fundamental operations:

1. **Traversal**: Visiting all nodes in a specific order 🚶‍♂️
   - Generic trees: level-order, pre-order, post-order
   - Expression trees: infix, prefix, postfix

2. **Insertion**: Adding new nodes to the tree ➕

3. **Search**: Finding specific values in the tree 🔍

4. **Evaluation**: Computing results (specific to expression trees) 🧮

5. **Construction**: Building trees from various representations 🏗️

## 2. Progressive Implementations

Let's build these tree structures step by step, starting with the simplest implementations. 🛠️

### Basic Generic Tree Implementation

First, we'll create a simple generic tree where nodes can have multiple children:

```python
class GenericTreeNode:
    """Node for generic tree with multiple children."""
    
    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.children = []  # 👶 List of child nodes
    
    def add_child(self, child):
        """Add a child node."""
        self.children.append(child)  # ➕ Add to children list
        
    def remove_child(self, child):
        """Remove a child node."""
        self.children.remove(child)  # ➖ Remove from children list


class GenericTree:
    """Generic tree implementation with basic operations."""
    
    def __init__(self):
        self.root = None  # 🌱 Root of the tree
    
    def is_empty(self):
        """Check if tree is empty."""
        return self.root is None  # 🈳 True if no root
    
    def add_root(self, value):
        """Add root node to tree."""
        if self.root is not None:
            raise Exception("Root already exists! ❌")
        self.root = GenericTreeNode(value)  # 🌱 Create root
        return self.root
    
    def add_node(self, parent, value):
        """Add a child node to a parent."""
        if parent is None:
            raise Exception("Parent cannot be None! ❌")
        child = GenericTreeNode(value)  # 👶 Create child
        parent.add_child(child)  # ➕ Add to parent
        return child
    
    def print_tree(self, node=None, level=0):
        """Print tree structure."""
        if node is None:
            node = self.root
        
        if node is None:
            print("Empty tree 🈳")
            return
        
        # Print current node with indentation
        print("  " * level + str(node.value))  # 📊 Show value
        
        # Recursively print children
        for child in node.children:
            self.print_tree(child, level + 1)  # 🔄 Next level


# Example usage 🧪
def test_generic_tree():
    tree = GenericTree()
    
    # Create tree structure
    #      A
    #    / | \
    #   B  C  D
    #  / \    |
    # E   F   G
    
    root = tree.add_root("A")  # 🌱 Add root
    b = tree.add_node(root, "B")  # ➕ Add children
    c = tree.add_node(root, "C")
    d = tree.add_node(root, "D")
    
    e = tree.add_node(b, "E")  # ➕ Add grandchildren
    f = tree.add_node(b, "F")
    g = tree.add_node(d, "G")
    
    print("Generic Tree Structure: 🌳")
    tree.print_tree()

test_generic_tree()
```

### Generic Tree Traversals

Now let's implement different traversal methods for generic trees:

```python
class GenericTreeTraversals(GenericTree):
    """Generic tree with traversal operations."""
    
    def preorder_traversal(self, node=None, result=None):
        """Visit node first, then all children (DLR)."""
        if result is None:
            result = []
        
        if node is None:
            node = self.root
        
        if node is not None:
            result.append(node.value)  # 📌 Process current node
            for child in node.children:
                self.preorder_traversal(child, result)  # 🔄 Process children
        
        return result
    
    def postorder_traversal(self, node=None, result=None):
        """Visit all children first, then node (LRD)."""
        if result is None:
            result = []
        
        if node is None:
            node = self.root
        
        if node is not None:
            for child in node.children:
                self.postorder_traversal(child, result)  # 🔄 Process children
            result.append(node.value)  # 📌 Process current node
        
        return result
    
    def level_order_traversal(self):
        """Visit nodes level by level (BFS)."""
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]  # 📋 Queue for BFS
        
        while queue:
            node = queue.pop(0)  # ⏏️ Dequeue
            result.append(node.value)  # 📌 Process node
            
            # Add all children to queue
            for child in node.children:
                queue.append(child)  # ➕ Enqueue children
        
        return result
    
    def find_node(self, value, node=None):
        """Find a node with given value."""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        if node.value == value:
            return node  # 🎯 Found!
        
        # Search in children
        for child in node.children:
            found = self.find_node(value, child)
            if found:
                return found  # 🔍 Found in subtree
        
        return None  # ❌ Not found


# Example usage 🧪
def test_generic_traversals():
    tree = GenericTreeTraversals()
    
    # Build the same tree
    root = tree.add_root("A")
    b = tree.add_node(root, "B")
    c = tree.add_node(root, "C")
    d = tree.add_node(root, "D")
    e = tree.add_node(b, "E")
    f = tree.add_node(b, "F")
    g = tree.add_node(d, "G")
    
    print("Traversals: 🚶‍♂️")
    print(f"Preorder:  {tree.preorder_traversal()}")   # A B E F C D G
    print(f"Postorder: {tree.postorder_traversal()}")  # E F B C G D A
    print(f"Level:     {tree.level_order_traversal()}") # A B C D E F G
    
    # Test find
    node = tree.find_node("F")
    print(f"\nFound node 'F': {node.value if node else 'Not found'} 🔍")

test_generic_traversals()
```

### Expression Tree Implementation

Now let's implement expression trees for mathematical expressions:

```python
class ExpressionNode:
    """Node for expression tree."""
    
    def __init__(self, value):
        self.value = value    # 📊 Operator or operand
        self.left = None      # 👈 Left operand
        self.right = None     # 👉 Right operand
    
    def is_operator(self):
        """Check if node contains an operator."""
        return self.value in ['+', '-', '*', '/']  # 🔣 Check operators


class ExpressionTree:
    """Binary tree for mathematical expressions."""
    
    def __init__(self):
        self.root = None  # 🌱 Root of expression tree
    
    def build_from_postfix(self, postfix):
        """Build expression tree from postfix notation."""
        stack = []  # 📚 Stack for building tree
        
        for token in postfix:
            node = ExpressionNode(token)
            
            if node.is_operator():
                # Pop two operands (right first) 📤
                node.right = stack.pop()
                node.left = stack.pop()
            
            stack.append(node)  # 📥 Push to stack
        
        self.root = stack.pop()  # 🌱 Last item is root
    
    def build_from_prefix(self, prefix):
        """Build expression tree from prefix notation."""
        stack = []  # 📚 Stack for building tree
        
        # Process prefix in reverse order
        for token in reversed(prefix):
            node = ExpressionNode(token)
            
            if node.is_operator():
                # Pop two operands (left first) 📤
                node.left = stack.pop()
                node.right = stack.pop()
            
            stack.append(node)  # 📥 Push to stack
        
        self.root = stack.pop()  # 🌱 Last item is root
    
    def infix_traversal(self, node=None):
        """Get infix notation (with parentheses)."""
        if node is None:
            node = self.root
        
        if node is None:
            return ""
        
        if not node.is_operator():
            return str(node.value)  # 🔢 Return operand
        
        # Recursively build infix with parentheses
        left = self.infix_traversal(node.left)
        right = self.infix_traversal(node.right)
        return f"({left} {node.value} {right})"  # 🔄 Add parentheses
    
    def prefix_traversal(self, node=None):
        """Get prefix notation."""
        if node is None:
            node = self.root
        
        if node is None:
            return ""
        
        if not node.is_operator():
            return str(node.value)  # 🔢 Return operand
        
        # Recursively build prefix
        left = self.prefix_traversal(node.left)
        right = self.prefix_traversal(node.right)
        return f"{node.value} {left} {right}"  # 🔣 Operator first
    
    def postfix_traversal(self, node=None):
        """Get postfix notation."""
        if node is None:
            node = self.root
        
        if node is None:
            return ""
        
        if not node.is_operator():
            return str(node.value)  # 🔢 Return operand
        
        # Recursively build postfix
        left = self.postfix_traversal(node.left)
        right = self.postfix_traversal(node.right)
        return f"{left} {right} {node.value}"  # 🔣 Operator last
    
    def print_tree(self, node=None, prefix="", is_left=True):
        """Print tree structure."""
        if node is None:
            node = self.root
        
        if node is None:
            print("Empty tree 🈳")
            return
        
        # Print right subtree
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        
        # Print current node
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        
        # Print left subtree
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


# Example usage 🧪
def test_expression_tree():
    tree = ExpressionTree()
    
    # Build from postfix: 3 4 + 5 *
    # This represents: (3 + 4) * 5
    postfix = ['3', '4', '+', '5', '*']
    tree.build_from_postfix(postfix)
    
    print("Expression Tree Structure: 🌳")
    tree.print_tree()
    
    print("\nNotations: 📝")
    print(f"Infix:   {tree.infix_traversal()}")    # ((3 + 4) * 5)
    print(f"Prefix:  {tree.prefix_traversal()}")   # * + 3 4 5
    print(f"Postfix: {tree.postfix_traversal()}")  # 3 4 + 5 *

test_expression_tree()
```

### Expression Tree Evaluation

Now let's add evaluation capabilities to our expression tree:

```python
class EvaluableExpressionTree(ExpressionTree):
    """Expression tree that can be evaluated."""
    
    def evaluate(self, node=None):
        """Evaluate the expression tree."""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        # If leaf node, return the value
        if not node.is_operator():
            return float(node.value)  # 🔢 Convert to number
        
        # Recursively evaluate left and right
        left_val = self.evaluate(node.left)   # 👈 Evaluate left
        right_val = self.evaluate(node.right)  # 👉 Evaluate right
        
        # Apply operator
        if node.value == '+':
            return left_val + right_val  # ➕ Addition
        elif node.value == '-':
            return left_val - right_val  # ➖ Subtraction
        elif node.value == '*':
            return left_val * right_val  # ✖️ Multiplication
        elif node.value == '/':
            if right_val == 0:
                raise ValueError("Division by zero! ⚠️")
            return left_val / right_val  # ➗ Division
    
    def evaluate_with_variables(self, variables=None):
        """Evaluate expression with variables."""
        if variables is None:
            variables = {}
        
        return self._evaluate_with_vars(self.root, variables)
    
    def _evaluate_with_vars(self, node, variables):
        """Helper method for variable evaluation."""
        if node is None:
            return 0
        
        # If leaf node
        if not node.is_operator():
            # Check if it's a variable
            if node.value in variables:
                return variables[node.value]  # 📊 Use variable value
            else:
                try:
                    return float(node.value)  # 🔢 Convert to number
                except ValueError:
                    raise ValueError(f"Unknown variable: {node.value} ❓")
        
        # Recursively evaluate
        left_val = self._evaluate_with_vars(node.left, variables)
        right_val = self._evaluate_with_vars(node.right, variables)
        
        # Apply operator
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            if right_val == 0:
                raise ValueError("Division by zero! ⚠️")
            return left_val / right_val


# Example usage 🧪
def test_expression_evaluation():
    tree = EvaluableExpressionTree()
    
    # Test 1: Simple numeric expression
    # (3 + 4) * 5
    postfix1 = ['3', '4', '+', '5', '*']
    tree.build_from_postfix(postfix1)
    
    print("Expression 1: (3 + 4) * 5 🧮")
    print(f"Result: {tree.evaluate()}")  # Should be 35.0
    
    # Test 2: Complex expression
    # ((10 + 5) * 2) - (8 / 4)
    postfix2 = ['10', '5', '+', '2', '*', '8', '4', '/', '-']
    tree.build_from_postfix(postfix2)
    
    print("\nExpression 2: ((10 + 5) * 2) - (8 / 4) 🧮")
    print(f"Result: {tree.evaluate()}")  # Should be 28.0
    
    # Test 3: Expression with variables
    # (x + y) * z
    postfix3 = ['x', 'y', '+', 'z', '*']
    tree.build_from_postfix(postfix3)
    
    variables = {'x': 3, 'y': 4, 'z': 5}
    print("\nExpression 3: (x + y) * z with x=3, y=4, z=5 🔤")
    print(f"Result: {tree.evaluate_with_variables(variables)}")  # Should be 35.0

test_expression_evaluation()
```

## 3. Practical Applications

Let's explore real-world applications of generic and expression trees. 🌟

### File System Representation

Generic trees are perfect for representing file systems:

```python
class FileNode(GenericTreeNode):
    """Node representing a file or directory."""
    
    def __init__(self, name, is_directory=False, size=0):
        super().__init__(name)
        self.is_directory = is_directory  # 📁 Directory flag
        self.size = size  # 📊 File size in bytes
    
    def get_total_size(self):
        """Calculate total size including subdirectories."""
        if not self.is_directory:
            return self.size  # 📄 Return file size
        
        total = 0
        for child in self.children:
            total += child.get_total_size()  # 🔄 Add child sizes
        
        return total


class FileSystem:
    """Simple file system using generic tree."""
    
    def __init__(self):
        self.root = FileNode("/", True)  # 📁 Root directory
    
    def add_file(self, parent, name, size):
        """Add a file to the system."""
        if not parent.is_directory:
            raise ValueError("Parent must be a directory! ❌")
        
        file = FileNode(name, False, size)  # 📄 Create file
        parent.add_child(file)
        return file
    
    def add_directory(self, parent, name):
        """Add a directory to the system."""
        if not parent.is_directory:
            raise ValueError("Parent must be a directory! ❌")
        
        directory = FileNode(name, True)  # 📁 Create directory
        parent.add_child(directory)
        return directory
    
    def print_tree(self, node=None, indent=""):
        """Print file system tree."""
        if node is None:
            node = self.root
        
        # Print current node
        icon = "📁" if node.is_directory else "📄"
        size = f" ({node.size} bytes)" if not node.is_directory else ""
        print(f"{indent}{icon} {node.value}{size}")
        
        # Print children with increased indent
        for i, child in enumerate(node.children):
            is_last = i == len(node.children) - 1
            extension = "└── " if is_last else "├── "
            next_indent = indent + ("    " if is_last else "│   ")
            print(f"{indent}{extension}", end="")
            self.print_tree(child, next_indent)


# Example usage 🧪
def test_file_system():
    fs = FileSystem()
    
    # Create file system structure
    home = fs.add_directory(fs.root, "home")
    user = fs.add_directory(home, "user")
    docs = fs.add_directory(user, "documents")
    pics = fs.add_directory(user, "pictures")
    
    # Add files
    fs.add_file(docs, "report.txt", 1024)  # 📄 1KB
    fs.add_file(docs, "notes.md", 2048)    # 📄 2KB
    fs.add_file(pics, "photo1.jpg", 102400) # 📄 100KB
    fs.add_file(pics, "photo2.jpg", 204800) # 📄 200KB
    
    print("File System Structure: 💾")
    fs.print_tree()
    
    print(f"\nTotal size in pictures: {pics.get_total_size()} bytes 📊")
    print(f"Total size in documents: {docs.get_total_size()} bytes 📊")

test_file_system()
```

### Mathematical Expression Evaluation

Expression trees are essential for calculators and mathematical software:

```python
class Calculator:
    """Simple calculator using expression trees."""
    
    def __init__(self):
        self.expression_tree = EvaluableExpressionTree()
        self.variables = {}  # 📊 Store variables
    
    def set_variable(self, name, value):
        """Set a variable value."""
        self.variables[name] = value  # 📝 Store variable
    
    def evaluate_postfix(self, postfix):
        """Evaluate a postfix expression."""
        self.expression_tree.build_from_postfix(postfix)
        return self.expression_tree.evaluate_with_variables(self.variables)
    
    def evaluate_prefix(self, prefix):
        """Evaluate a prefix expression."""
        self.expression_tree.build_from_prefix(prefix)
        return self.expression_tree.evaluate_with_variables(self.variables)
    
    def show_expression_tree(self):
        """Display the current expression tree."""
        self.expression_tree.print_tree()


# Example usage 🧪
def test_calculator():
    calc = Calculator()
    
    # Example 1: Simple arithmetic
    print("Example 1: 2 * 3 + 4 - 1 🧮")
    postfix1 = ['2', '3', '*', '4', '+', '1', '-']
    result1 = calc.evaluate_postfix(postfix1)
    print(f"Result: {result1}")  # Should be 9.0
    
    # Example 2: With variables
    print("\nExample 2: (a + b) * c where a=5, b=3, c=2 🔤")
    calc.set_variable('a', 5)
    calc.set_variable('b', 3)
    calc.set_variable('c', 2)
    
    postfix2 = ['a', 'b', '+', 'c', '*']
    result2 = calc.evaluate_postfix(postfix2)
    print(f"Result: {result2}")  # Should be 16.0
    
    print("\nExpression Tree: 🌳")
    calc.show_expression_tree()

test_calculator()
```

### Decision Trees

Generic trees are used in machine learning for decision making:

```python
class DecisionNode(GenericTreeNode):
    """Node for decision tree."""
    
    def __init__(self, question=None, answer=None):
        super().__init__(question if question else answer)
        self.question = question  # ❓ Question to ask
        self.answer = answer      # 💡 Answer (for leaf nodes)
        self.is_leaf = answer is not None  # 🍃 Check if leaf
    
    def add_branch(self, condition, child):
        """Add a branch with condition."""
        self.children.append((condition, child))  # ➕ Add condition-child pair


class SimpleDecisionTree:
    """Simple decision tree for yes/no questions."""
    
    def __init__(self):
        self.root = None  # 🌱 Root of decision tree
    
    def build_animal_guesser(self):
        """Build a simple animal guessing game."""
        # Create decision tree
        self.root = DecisionNode(question="Does it live in water? 🌊")
        
        # Water animals branch
        water_branch = DecisionNode(question="Is it a mammal? 🐋")
        fish = DecisionNode(answer="It's a fish! 🐟")
        whale = DecisionNode(answer="It's a whale! 🐋")
        
        water_branch.add_branch("No", fish)
        water_branch.add_branch("Yes", whale)
        
        # Land animals branch
        land_branch = DecisionNode(question="Does it have wings? 🦅")
        bird = DecisionNode(answer="It's a bird! 🦅")
        mammal_branch = DecisionNode(question="Is it a pet? 🐕")
        dog = DecisionNode(answer="It's a dog! 🐕")
        lion = DecisionNode(answer="It's a lion! 🦁")
        
        mammal_branch.add_branch("Yes", dog)
        mammal_branch.add_branch("No", lion)
        
        land_branch.add_branch("Yes", bird)
        land_branch.add_branch("No", mammal_branch)
        
        # Connect to root
        self.root.add_branch("Yes", water_branch)
        self.root.add_branch("No", land_branch)
    
    def play(self):
        """Play the guessing game."""
        print("Think of an animal and I'll try to guess it! 🤔")
        current = self.root
        
        while not current.is_leaf:
            print(f"\n{current.question}")
            answer = input("Answer (Yes/No): ").strip().lower()
            
            # Find matching branch
            found = False
            for condition, child in current.children:
                if answer.startswith(condition.lower()[0]):
                    current = child
                    found = True
                    break
            
            if not found:
                print("Please answer Yes or No! ❌")
        
        print(f"\n{current.answer}")


# Example usage 🧪
def test_decision_tree():
    game = SimpleDecisionTree()
    game.build_animal_guesser()
    
    # Print tree structure
    print("Decision Tree Structure: 🌳")
    
    def print_tree(node, indent=""):
        if node.is_leaf:
            print(f"{indent}🍃 {node.answer}")
        else:
            print(f"{indent}❓ {node.question}")
            for condition, child in node.children:
                print(f"{indent}  └─ {condition}:")
                print_tree(child, indent + "    ")
    
    print_tree(game.root)
    
    # Uncomment to play the game
    # game.play()

test_decision_tree()
```

## 4. Real-world Case Study: Calculator Engine

Let's build a complete calculator engine that can convert between different notations and evaluate expressions: 🖩

```python
class NotationConverter:
    """Convert between different expression notations."""
    
    @staticmethod
    def infix_to_postfix(infix):
        """Convert infix to postfix notation."""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # 📊 Operator precedence
        stack = []  # 📚 Operator stack
        postfix = []  # 📝 Result
        
        for token in infix:
            if token not in precedence and token not in '()':
                # Operand - add to output
                postfix.append(token)  # 🔢 Add number
            elif token == '(':
                stack.append(token)  # 📥 Push (
            elif token == ')':
                # Pop until we find (
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())  # 📤 Pop operators
                stack.pop()  # Remove (
            else:
                # Operator - check precedence
                while (stack and stack[-1] != '(' and
                       stack[-1] in precedence and
                       precedence[stack[-1]] >= precedence[token]):
                    postfix.append(stack.pop())  # 📤 Pop higher precedence
                stack.append(token)  # 📥 Push operator
        
        # Pop remaining operators
        while stack:
            postfix.append(stack.pop())  # 📤 Pop remaining
        
        return postfix
    
    @staticmethod
    def postfix_to_infix(postfix):
        """Convert postfix to infix notation."""
        stack = []  # 📚 Expression stack
        
        for token in postfix:
            if token not in '+-*/':
                # Operand - push to stack
                stack.append(token)  # 📥 Push operand
            else:
                # Operator - pop two operands
                right = stack.pop()  # 👉 Right operand
                left = stack.pop()   # 👈 Left operand
                
                # Create infix expression with parentheses
                expr = f"({left} {token} {right})"
                stack.append(expr)  # 📥 Push expression
        
        return stack[0]  # 📤 Final expression


class CalculatorEngine:
    """Complete calculator engine with multiple features."""
    
    def __init__(self):
        self.tree = EvaluableExpressionTree()
        self.converter = NotationConverter()
        self.history = []  # 📜 Calculation history
    
    def calculate_infix(self, infix_expr):
        """Calculate result from infix expression."""
        # Convert string to token list
        tokens = self._tokenize(infix_expr)
        
        # Convert to postfix
        postfix = self.converter.infix_to_postfix(tokens)
        
        # Build tree and evaluate
        self.tree.build_from_postfix(postfix)
        result = self.tree.evaluate()
        
        # Save to history
        self.history.append({
            'expression': infix_expr,
            'result': result,
            'notation': 'infix'
        })
        
        return result
    
    def _tokenize(self, expression):
        """Convert expression string to token list."""
        tokens = []
        current_number = ""
        
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char  # 🔢 Build number
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                if char in '+-*/()':
                    tokens.append(char)  # 🔣 Add operator
        
        if current_number:
            tokens.append(current_number)
        
        return tokens
    
    def show_tree(self):
        """Display the current expression tree."""
        print("Expression Tree: 🌳")
        self.tree.print_tree()
    
    def show_history(self):
        """Display calculation history."""
        print("Calculation History: 📜")
        for i, entry in enumerate(self.history):
            print(f"{i+1}. {entry['expression']} = {entry['result']}")
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()  # 🗑️ Clear history
        print("History cleared! 🧹")


# Example usage 🧪
def test_calculator_engine():
    calc = CalculatorEngine()
    
    print("Calculator Engine Demo 🖩")
    print("========================")
    
    # Test various expressions
    expressions = [
        "2 + 3 * 4",          # 14 (precedence test)
        "(2 + 3) * 4",        # 20 (parentheses test)
        "10 / 2 + 3",         # 8 (mixed operations)
        "8 - 3 * 2 + 1",      # 3 (complex precedence)
        "(5 + 3) * (10 - 8)", # 16 (nested parentheses)
    ]
    
    for expr in expressions:
        result = calc.calculate_infix(expr)
        print(f"\n{expr} = {result} 🎯")
        calc.show_tree()
    
    print("\n" + "="*30)
    calc.show_history()


# Run the demo
test_calculator_engine()


# Additional helper functions for the calculator
def interactive_calculator():
    """Interactive calculator session."""
    calc = CalculatorEngine()
    
    print("Interactive Calculator 🖩")
    print("Type 'exit' to quit, 'history' to see history")
    print("Supported operations: +, -, *, /")
    print("="*40)
    
    while True:
        try:
            expr = input("\nEnter expression: ").strip()
            
            if expr.lower() == 'exit':
                print("Goodbye! 👋")
                break
            elif expr.lower() == 'history':
                calc.show_history()
            elif expr.lower() == 'clear':
                calc.clear_history()
            else:
                result = calc.calculate_infix(expr)
                print(f"Result: {result} 🎯")
                
        except Exception as e:
            print(f"Error: {e} ❌")


# Uncomment to run interactive mode
# interactive_calculator()
```

## 5. Technical Challenges

Master these fundamental tree operations through hands-on coding challenges! 🧩

### Challenge 1: Convert Infix to Postfix

**Problem**: Transform an infix expression to postfix notation, handling operator precedence and parentheses correctly. 📝

**Input**: A list of tokens representing an infix expression  
**Output**: A list of tokens representing the equivalent postfix expression

**Approach**:
1. Use a stack to hold operators temporarily 📚
2. Process tokens left to right, handling operands and operators differently 🔄
3. Respect operator precedence: `*,/` before `+,-` 📊
4. Handle parentheses for grouping operations 🔗

```python
def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    # Tu código aquí 🛠️
    pass

# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 📊 Precedence test

# Test 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🔗 Parentheses

# Test 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # 🧮 Complex

# Test 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # 🔤 Variables
```

---

### Challenge 2: Build Expression Tree from Infix

**Problem**: Create an expression tree directly from an infix expression. 🌳

**Input**: A list of tokens representing an infix expression  
**Output**: The root node of the corresponding expression tree

**Approach**:
1. Convert infix to postfix first 🔄
2. Build tree from postfix using stack method 📚
3. Return root of the constructed tree 🌱

```python
class ExpressionTree:
    """Expression tree implementation"""
    
    def __init__(self):
        self.root = None
    
    @classmethod
    def from_infix(cls, tokens):
        """Build expression tree from infix notation"""
        # Tu código aquí 🛠️
        pass

# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Tree:    +
#         / \
#        2   3
tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # 🌱 Simple tree

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')  # 📊 Precedence structure

# Test 3: Parentheses change structure
# Input: (2 + 3) * 4
# Tree:    *
#         / \
#        +   4
#       / \
#      2   3
tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')  # 🔗 Parentheses effect

# Test 4: Variables in expression
# Input: x + y * z
# Tree:    +
#         / \
#        x   *
#           / \
#          y   z
tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
print(tree4.root.value == '+' and tree4.root.right.value == '*')  # 🔤 Variable tree

# Test 5: Complex nested expression
# Input: (a + b) / (c - d)
# Tree:      /
#          /   \
#         +     -
#        / \   / \
#       a   b c   d
tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')  # 🧮 Complex tree
```

---

### Challenge 3: Generic Tree Height

**Problem**: Calculate the height (maximum depth) of a generic tree. 📏

**Input**: The root node of a generic tree  
**Output**: The height of the tree (integer)

**Approach**:
1. Base case: None → -1, leaf → 0 🌱
2. Recursively find height of all children 🔄
3. Return 1 + max(children heights) 📊

**Note**: Using standard convention where height = number of edges in the longest path from root to leaf.

```python
class GenericTree:
   """Generic tree implementation"""
   
   def __init__(self, root=None):
       self.root = root
   
   def height(self):
       """Calculate tree height"""
       # Tu código aquí 🛠️
       pass

# ✅ Test cases
# Test 1: Empty tree
# Tree: None
empty_tree = GenericTree(None)
print(empty_tree.height() == -1)  # 📭 Empty tree

# Test 2: Single node
# Tree: A
single = GenericTree(GenericTreeNode('A'))
print(single.height() == 0)  # 🌱 Single node

# Test 3: Linear tree
# Tree: A → B → C
#       A
#       |
#       B
#       |
#       C
linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.height() == 2)  # 📏 Linear path

# Test 4: Balanced tree
# Tree:     A
#         / | \
#        B  C  D
#       /|\    |
#      E F G   H
balanced_root = GenericTreeNode('A')
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')
balanced_root.children = [b, c, d]
b.children = [e, f, g]
d.children = [h]
balanced_tree = GenericTree(balanced_root)
print(balanced_tree.height() == 2)  # 🌳 Balanced tree

# Test 5: Unbalanced tree
# Tree:     A
#          /
#         B
#        /
#       C
#      /
#     D
unbalanced_root = GenericTreeNode('A')
ub_b = GenericTreeNode('B')
ub_c = GenericTreeNode('C')
ub_d = GenericTreeNode('D')
unbalanced_root.children = [ub_b]
ub_b.children = [ub_c]
ub_c.children = [ub_d]
unbalanced_tree = GenericTree(unbalanced_root)
print(unbalanced_tree.height() == 3)  # 📈 Deep path
```

---

### Challenge 4: Find All Leaves

**Problem**: Collect all leaf nodes (nodes with no children) in a generic tree. 🍃

**Input**: The root node of a generic tree  
**Output**: A list of values from all leaf nodes

**Approach**:
1. A node is a leaf if it has no children 🌿
2. Recursively traverse the tree 🔄
3. Collect nodes with empty children list 📋

```python
class GenericTree:
    """Generic tree implementation"""
    
    def __init__(self, root=None):
        self.root = root
    
    def find_leaves(self):
        """Find all leaf nodes in the tree"""
        # Tu código aquí 🛠️
        pass

# ✅ Test cases
# Test 1: Empty tree
# Tree: None
empty_tree = GenericTree(None)
print(empty_tree.find_leaves() == [])  # 📭 No leaves

# Test 2: Single node (root is leaf)
# Tree: X
single = GenericTree(GenericTreeNode('X'))
print(single.find_leaves() == ['X'])  # 🌱 Root is leaf

# Test 3: Linear tree
# Tree: A → B → C
#       A
#       |
#       B
#       |
#       C
linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.find_leaves() == ['C'])  # 🍃 End of chain

# Test 4: Multiple leaves
# Tree:     A
#         / | \
#        B  C  D
#       /|\    |
#      E F G   H
tree_root = GenericTreeNode('A')
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')
tree_root.children = [b, c, d]
b.children = [e, f, g]
d.children = [h]
tree = GenericTree(tree_root)
print(sorted(tree.find_leaves()) == ['C', 'E', 'F', 'G', 'H'])  # 🍂 All leaves

# Test 5: Wide tree (all children are leaves)
# Tree:     A
#      / | | | \
#     B  C D E  F
wide_root = GenericTreeNode('A')
wide_root.children = [GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D'), 
                      GenericTreeNode('E'), GenericTreeNode('F')]
wide_tree = GenericTree(wide_root)
print(sorted(wide_tree.find_leaves()) == ['B', 'C', 'D', 'E', 'F'])  # 🌿 Wide tree
```

---

### Challenge 5: Expression Tree Simplification

**Problem**: Simplify an expression tree by evaluating constant subexpressions. 🧮

**Input**: Root of an expression tree  
**Output**: Root of simplified expression tree

**Approach**:
1. Post-order traversal (children first) 🔄
2. If both children are constants, compute result 🔢
3. Replace subtree with computed value 📊
4. Preserve variables unchanged 🔤

```python
class ExpressionTree:
    """Expression tree implementation"""
    
    def __init__(self, root=None):
        self.root = root
    
    def simplify(self):
        """Simplify the expression tree by evaluating constants"""
        # Tu código aquí 🛠️
        pass

# ✅ Test cases
# Test 1: All constants
# Input: (2 + 3)
# Tree:    +        Result: 5
#         / \
#        2   3
const_tree = ExpressionTree()
const_tree.root = ExpressionNode('+')
const_tree.root.left = ExpressionNode('2')
const_tree.root.right = ExpressionNode('3')
const_tree.simplify()
print(const_tree.root.value == '5' and const_tree.root.left is None and const_tree.root.right is None)  # 🔢 Single node

# Test 2: Partial simplification
# Input: (2 + 3) * x
# Tree:    *         Result: *
#         / \               / \
#        +   x             5   x
#       / \
#      2   3
partial_tree = ExpressionTree()
partial_tree.root = ExpressionNode('*')
add = ExpressionNode('+')
add.left, add.right = ExpressionNode('2'), ExpressionNode('3')
partial_tree.root.left = add
partial_tree.root.right = ExpressionNode('x')
partial_tree.simplify()
print(partial_tree.root.value == '*' and partial_tree.root.left.value == '5' and partial_tree.root.right.value == 'x')  # ✨ Partial

# Test 3: No simplification possible
# Input: x + y
# Tree:    +         Result: + (unchanged)
#         / \               / \
#        x   y             x   y
no_simp_tree = ExpressionTree()
no_simp_tree.root = ExpressionNode('+')
no_simp_tree.root.left = ExpressionNode('x')
no_simp_tree.root.right = ExpressionNode('y')
no_simp_tree.simplify()
print(no_simp_tree.root.value == '+' and no_simp_tree.root.left.value == 'x' and no_simp_tree.root.right.value == 'y')  # 🔤 No change

# Test 4: Complex nested simplification
# Input: ((2 * 3) + (8 / 4))
# Tree:      +          Result: 8
#          /   \
#         *     /
#        / \   / \
#       2   3 8   4
complex_tree = ExpressionTree()
complex_tree.root = ExpressionNode('+')
mult = ExpressionNode('*')
div = ExpressionNode('/')
mult.left, mult.right = ExpressionNode('2'), ExpressionNode('3')
div.left, div.right = ExpressionNode('8'), ExpressionNode('4')
complex_tree.root.left, complex_tree.root.right = mult, div
complex_tree.simplify()
print(complex_tree.root.value == '8' and complex_tree.root.left is None)  # 🎯 Fully simplified

# Test 5: Mixed variables and constants
# Input: x * (6 / 2)
# Tree:    *         Result: *
#         / \               / \
#        x   /             x   3
#           / \
#          6   2
mixed_tree = ExpressionTree()
mixed_tree.root = ExpressionNode('*')
div = ExpressionNode('/')
div.left, div.right = ExpressionNode('6'), ExpressionNode('2')
mixed_tree.root.left = ExpressionNode('x')
mixed_tree.root.right = div
mixed_tree.simplify()
print(mixed_tree.root.value == '*' and mixed_tree.root.left.value == 'x' and mixed_tree.root.right.value == '3')  # 🔄 Right simplified
```

## 6. Comparative Analysis

Let's compare generic trees and expression trees to understand their strengths and use cases: 📊

| **Feature**             | **Generic Tree**               | **Expression Tree**                |
| ----------------------- | ------------------------------ | ---------------------------------- |
| **Structure**           | Variable children per node     | Binary (exactly 2 children)        |
| **Node Types**          | Homogeneous (all similar)      | Heterogeneous (operators/operands) |
| **Primary Use**         | Hierarchical data              | Mathematical expressions           |
| **Traversal Patterns**  | Pre, Post, Level-order         | Infix, Prefix, Postfix             |
| **Common Applications** | File systems, decision trees   | Calculators, compilers             |
| **Flexibility**         | High (any branching factor)    | Low (binary only)                  |
| **Memory Efficiency**   | Variable (depends on children) | Fixed (2 pointers per node)        |
| **Evaluation**          | Domain-specific                | Built-in mathematical evaluation   |

### Key Differences

1. **Structural Flexibility** 🌳
   - Generic trees: Can have any number of children (0 to n)
   - Expression trees: Always binary (for binary operators)

2. **Purpose and Semantics** 🎯
   - Generic trees: General hierarchical relationships
   - Expression trees: Specific to mathematical/logical expressions

3. **Node Information** 📊
   - Generic trees: Usually uniform data in all nodes
   - Expression trees: Different node types (operators vs operands)

4. **Traversal Meaning** 🚶‍♂️
   - Generic trees: Traversal for visiting/searching
   - Expression trees: Traversal produces different notations

5. **Operations** 🛠️
   - Generic trees: Add/remove nodes, search, traverse
   - Expression trees: Evaluate, convert notations, simplify

### When to use which

**Use Generic Trees when**:
- Representing hierarchical data with variable branching 📂
- Modeling organizational structures 🏢
- Building file systems or directory structures 💾
- Creating decision trees with multiple options 🤔
- Implementing game trees (like tic-tac-toe) 🎮

**Use Expression Trees when**:
- Parsing and evaluating mathematical expressions 🧮
- Building calculator applications 🖩
- Implementing programming language interpreters 💻
- Converting between different notations 🔄
- Optimizing expressions through simplification ⚡

## 7. Next Learning Steps

After mastering generic and expression trees, consider exploring these advanced topics: 🚀

1. **Advanced Tree Structures** 🌲
   - N-ary trees with fixed branching
   - Trie data structures for string processing
   - B-trees for database indexing
   - Red-black trees for balanced searching

2. **Tree Algorithms** 🧮
   - Tree serialization and deserialization
   - Lowest common ancestor algorithms
   - Tree isomorphism checking
   - Optimal tree construction

3. **Parsing Techniques** 📝
   - Recursive descent parsing
   - Shunting yard algorithm
   - Abstract syntax trees (AST)
   - Parse tree construction

4. **Optimization Methods** ⚡
   - Expression tree optimization
   - Common subexpression elimination
   - Constant folding techniques
   - Tree balancing algorithms

5. **Real-world Applications** 💡
   - Compiler design basics
   - Database query optimization
   - XML/HTML DOM trees
   - Machine learning decision trees

## 8. Key Conclusions

Through this guide, we've explored the fundamental concepts of generic and expression trees: 🎓

1. **Generic trees** provide flexible hierarchical structures perfect for representing real-world relationships like file systems and organizational charts. Their variable branching makes them adaptable to many scenarios. 🌳

2. **Expression trees** offer a specialized binary structure ideal for mathematical expressions, enabling efficient evaluation and notation conversion. They form the backbone of calculators and compilers. 🧮

3. **Tree traversals** are fundamental operations that serve different purposes - generic tree traversals help navigate hierarchies, while expression tree traversals produce different mathematical notations. 🚶‍♂️

4. **Practical applications** demonstrate how these structures solve real problems - from file system navigation to mathematical computation, trees are everywhere in computer science. 💻

5. **Implementation details** matter - understanding how to build, traverse, and manipulate these structures is crucial for effective use in larger applications. 🛠️

The journey from simple tree nodes to complex applications shows how fundamental data structures can be combined to create powerful solutions. As you continue learning, remember that trees are not just academic concepts but practical tools used in countless real-world applications. Keep practicing, keep building, and keep growing your tree knowledge! 🌱

Happy coding! 💻✨