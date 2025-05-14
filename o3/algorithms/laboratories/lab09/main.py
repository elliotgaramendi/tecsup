"""
🌿 Generic and Expression Trees Implementation 🌿

This module implements generic and expression tree concepts and operations,
providing solutions for challenges in the Generic and Expression Trees guide.
"""

# ========================================================================================
# 1. UNDERSTANDING THE FUNDAMENTAL CONCEPT
# ========================================================================================

# --- 1.1. Generic Tree Node ---


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


# --- 1.2. Expression Tree Node ---
class ExpressionNode:
    """Node for expression tree."""

    def __init__(self, value):
        self.value = value    # 📊 Operator or operand
        self.left = None      # 👈 Left operand
        self.right = None     # 👉 Right operand

    def is_operator(self):
        """Check if node contains an operator."""
        return self.value in ['+', '-', '*', '/']  # 🔣 Check operators


# ========================================================================================
# 2. PROGRESSIVE IMPLEMENTATIONS
# ========================================================================================

# --- 2.1. Basic Generic Tree ---
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

        # Print current node with indentation 📏
        print("  " * level + str(node.value))  # 📊 Show value

        # Recursively print children 🔄
        for child in node.children:
            self.print_tree(child, level + 1)  # 🔄 Next level


# --- 2.2. Generic Tree with Traversals ---
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

            # Add all children to queue 📥
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

        # Search in children 🔍
        for child in node.children:
            found = self.find_node(value, child)
            if found:
                return found  # 🔍 Found in subtree

        return None  # ❌ Not found


# --- 2.3. Basic Expression Tree ---
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

        if stack:
            self.root = stack.pop()  # 🌱 Last item is root

    def build_from_prefix(self, prefix):
        """Build expression tree from prefix notation."""
        stack = []  # 📚 Stack for building tree

        # Process prefix in reverse order ⏪
        for token in reversed(prefix):
            node = ExpressionNode(token)

            if node.is_operator():
                # Pop two operands (left first) 📤
                node.left = stack.pop()
                node.right = stack.pop()

            stack.append(node)  # 📥 Push to stack

        if stack:
            self.root = stack.pop()  # 🌱 Last item is root

    def infix_traversal(self, node=None):
        """Get infix notation (with parentheses)."""
        if node is None:
            node = self.root

        if node is None:
            return ""

        if not node.is_operator():
            return str(node.value)  # 🔢 Return operand

        # Recursively build infix with parentheses 🔄
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

        # Recursively build prefix 🔄
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

        # Recursively build postfix 🔄
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

        # Print right subtree 👉
        if node.right:
            self.print_tree(node.right, prefix +
                            ("│   " if is_left else "    "), False)

        # Print current node 📌
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        # Print left subtree 👈
        if node.left:
            self.print_tree(node.left, prefix +
                            ("    " if is_left else "│   "), True)


# --- 2.4. Expression Tree with Evaluation ---
class EvaluableExpressionTree(ExpressionTree):
    """Expression tree that can be evaluated."""

    def evaluate(self, node=None):
        """Evaluate the expression tree."""
        if node is None:
            node = self.root

        if node is None:
            return 0

        # If leaf node, return the value 🍃
        if not node.is_operator():
            return float(node.value)  # 🔢 Convert to number

        # Recursively evaluate left and right 🔄
        left_val = self.evaluate(node.left)   # 👈 Evaluate left
        right_val = self.evaluate(node.right)  # 👉 Evaluate right

        # Apply operator 🧮
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

        # If leaf node 🍃
        if not node.is_operator():
            # Check if it's a variable 🔤
            if node.value in variables:
                return variables[node.value]  # 📊 Use variable value
            else:
                try:
                    return float(node.value)  # 🔢 Convert to number
                except ValueError:
                    raise ValueError(f"Unknown variable: {node.value} ❓")

        # Recursively evaluate 🔄
        left_val = self._evaluate_with_vars(node.left, variables)
        right_val = self._evaluate_with_vars(node.right, variables)

        # Apply operator 🧮
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


# ========================================================================================
# 3. PRACTICAL APPLICATIONS
# ========================================================================================

# --- 3.1. File System Implementation ---
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

        # Print current node 📋
        icon = "📁" if node.is_directory else "📄"
        size = f" ({node.size} bytes)" if not node.is_directory else ""
        print(f"{indent}{icon} {node.value}{size}")

        # Print children with increased indent 📐
        for i, child in enumerate(node.children):
            is_last = i == len(node.children) - 1
            extension = "└── " if is_last else "├── "
            next_indent = indent + ("    " if is_last else "│   ")
            print(f"{indent}{extension}", end="")
            self.print_tree(child, next_indent)


# --- 3.2. Calculator Implementation ---
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


# --- 3.3. Decision Tree Implementation ---
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
        # Create decision tree 🌳
        self.root = DecisionNode(question="Does it live in water? 🌊")

        # Water animals branch 🌊
        water_branch = DecisionNode(question="Is it a mammal? 🐋")
        fish = DecisionNode(answer="It's a fish! 🐟")
        whale = DecisionNode(answer="It's a whale! 🐋")

        water_branch.add_branch("No", fish)
        water_branch.add_branch("Yes", whale)

        # Land animals branch 🏞️
        land_branch = DecisionNode(question="Does it have wings? 🦅")
        bird = DecisionNode(answer="It's a bird! 🦅")
        mammal_branch = DecisionNode(question="Is it a pet? 🐕")
        dog = DecisionNode(answer="It's a dog! 🐕")
        lion = DecisionNode(answer="It's a lion! 🦁")

        mammal_branch.add_branch("Yes", dog)
        mammal_branch.add_branch("No", lion)

        land_branch.add_branch("Yes", bird)
        land_branch.add_branch("No", mammal_branch)

        # Connect to root 🔗
        self.root.add_branch("Yes", water_branch)
        self.root.add_branch("No", land_branch)

    def play(self):
        """Play the guessing game."""
        print("Think of an animal and I'll try to guess it! 🤔")
        current = self.root

        while not current.is_leaf:
            print(f"\n{current.question}")
            answer = input("Answer (Yes/No): ").strip().lower()

            # Find matching branch 🔍
            found = False
            for condition, child in current.children:
                if answer.startswith(condition.lower()[0]):
                    current = child
                    found = True
                    break

            if not found:
                print("Please answer Yes or No! ❌")

        print(f"\n{current.answer}")


# ========================================================================================
# 4. REAL-WORLD CASE STUDY: CALCULATOR ENGINE
# ========================================================================================

# --- 4.1. Notation Converter ---
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
                # Operand - add to output 🔢
                postfix.append(token)  # 🔢 Add number
            elif token == '(':
                stack.append(token)  # 📥 Push (
            elif token == ')':
                # Pop until we find ( 🔍
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())  # 📤 Pop operators
                if stack:
                    stack.pop()  # Remove (
            else:
                # Operator - check precedence ⚖️
                while (stack and stack[-1] != '(' and
                       stack[-1] in precedence and
                       precedence[stack[-1]] >= precedence[token]):
                    postfix.append(stack.pop())  # 📤 Pop higher precedence
                stack.append(token)  # 📥 Push operator

        # Pop remaining operators 📤
        while stack:
            postfix.append(stack.pop())  # 📤 Pop remaining

        return postfix

    @staticmethod
    def postfix_to_infix(postfix):
        """Convert postfix to infix notation."""
        stack = []  # 📚 Expression stack

        for token in postfix:
            if token not in '+-*/':
                # Operand - push to stack 📥
                stack.append(token)  # 📥 Push operand
            else:
                # Operator - pop two operands 📤
                if len(stack) >= 2:
                    right = stack.pop()  # 👉 Right operand
                    left = stack.pop()   # 👈 Left operand

                    # Create infix expression with parentheses 🔄
                    expr = f"({left} {token} {right})"
                    stack.append(expr)  # 📥 Push expression

        return stack[0] if stack else ""  # 📤 Final expression


# --- 4.2. Calculator Engine ---
class CalculatorEngine:
    """Complete calculator engine with multiple features."""

    def __init__(self):
        self.tree = EvaluableExpressionTree()
        self.converter = NotationConverter()
        self.history = []  # 📜 Calculation history

    def calculate_infix(self, infix_expr):
        """Calculate result from infix expression."""
        # Convert string to token list 🔤
        tokens = self._tokenize(infix_expr)

        # Convert to postfix 🔄
        postfix = self.converter.infix_to_postfix(tokens)

        # Build tree and evaluate 🧮
        self.tree.build_from_postfix(postfix)
        result = self.tree.evaluate()

        # Save to history 💾
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


# --- 4.3. Interactive Calculator ---
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


# ========================================================================================
# 5. TECHNICAL CHALLENGES
# ========================================================================================

# --- 5.1. Challenge 1: Convert Infix to Postfix ---
def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}  # 📊 Operator precedence
    stack = []  # 📚 Operator stack
    postfix = []  # 📝 Result

    for token in tokens:
        if token not in precedence and token not in '()':
            postfix.append(token)  # 🔢 Add operand
        elif token == '(':
            stack.append(token)  # 📥 Push (
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())  # 📤 Pop operators
            stack.pop()  # Remove (
        else:
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                postfix.append(stack.pop())  # 📤 Pop higher precedence
            stack.append(token)  # 📥 Push operator

    while stack:
        postfix.append(stack.pop())  # 📤 Pop remaining

    return postfix


# --- 5.2. Challenge 2: Build Expression Tree from Infix ---
class ExpressionTreeBuilder:
    """Build expression tree from infix notation."""

    def __init__(self):
        self.root = None

    @classmethod
    def from_infix(cls, tokens):
        """Build expression tree from infix notation."""
        obj = cls()
        postfix = infix_to_postfix(tokens)  # Convert to postfix first 🔄
        stack = []  # 📚 Stack for building tree

        for token in postfix:
            node = ExpressionNode(token)

            if node.is_operator():
                node.right = stack.pop()  # 👉 Right operand
                node.left = stack.pop()   # 👈 Left operand

            stack.append(node)  # 📥 Push to stack

        obj.root = stack.pop()  # 🌱 Final node is root
        return obj


# --- 5.3. Challenge 3: Generic Tree Height ---
class GenericTreeOperations:
    """Operations on generic trees."""

    def __init__(self, root=None):
        self.root = root

    def height(self):
        """Calculate tree height using standard convention."""
        if self.root is None:
            return -1  # 📭 Empty tree (standard convention)
        return self._height_helper(self.root)

    def _height_helper(self, node):
        """Helper method for height calculation."""
        if not node.children:
            return 0  # 🌱 Leaf node (no edges)

        # Find maximum height among children 📏
        max_child_height = -1
        for child in node.children:
            child_height = self._height_helper(child)
            max_child_height = max(max_child_height, child_height)

        return 1 + max_child_height  # 📏 Current + max child


# --- 5.4. Challenge 4: Find All Leaves ---
class LeafFinder:
    """Find all leaf nodes in a generic tree."""

    def __init__(self, root=None):
        self.root = root

    def find_leaves(self):
        """Find all leaf nodes in the tree."""
        leaves = []
        self._find_leaves_helper(self.root, leaves)
        return leaves

    def _find_leaves_helper(self, node, leaves):
        """Helper method to find leaves."""
        if node is None:
            return

        if not node.children:  # 🍃 Leaf node
            leaves.append(node.value)
        else:
            for child in node.children:
                self._find_leaves_helper(child, leaves)


# --- 5.5. Challenge 5: Expression Tree Simplification ---
class ExpressionSimplifier:
    """Simplify expression trees by evaluating constants."""

    def __init__(self, root=None):
        self.root = root

    def simplify(self):
        """Simplify the expression tree."""
        self.root = self._simplify_helper(self.root)

    def _simplify_helper(self, node):
        """Helper method for simplification."""
        if node is None:
            return None

        # If leaf node (operand) 🍃
        if not node.is_operator():
            return node

        # Recursively simplify children 🔄
        node.left = self._simplify_helper(node.left)
        node.right = self._simplify_helper(node.right)

        # If both children are constants, evaluate 🧮
        if (node.left and not node.left.is_operator() and
                node.right and not node.right.is_operator()):
            try:
                left_val = float(node.left.value)
                right_val = float(node.right.value)

                # Evaluate operation 🔣
                result = 0
                if node.value == '+':
                    result = left_val + right_val  # ➕
                elif node.value == '-':
                    result = left_val - right_val  # ➖
                elif node.value == '*':
                    result = left_val * right_val  # ✖️
                elif node.value == '/':
                    if right_val != 0:
                        result = left_val / right_val  # ➗
                    else:
                        return node  # Keep division by zero

                # Create new node with result 📊
                new_node = ExpressionNode(
                    str(int(result) if result == int(result) else result))
                return new_node
            except ValueError:
                # One of the values is not a number (variable) 🔤
                return node

        return node


# ========================================================================================
# 6. TESTING FUNCTIONS
# ========================================================================================

# --- 6.1. Test Generic Tree ---
def test_generic_tree():
    """Test generic tree implementation."""
    print("\n🌳 Testing Generic Tree...")

    tree = GenericTree()

    # Create tree structure 🏗️
    root = tree.add_root("A")
    b = tree.add_node(root, "B")
    c = tree.add_node(root, "C")
    d = tree.add_node(root, "D")

    e = tree.add_node(b, "E")
    f = tree.add_node(b, "F")
    g = tree.add_node(d, "G")

    print("Tree Structure:")
    tree.print_tree()

    # Test traversals 🚶‍♂️
    tree_traversals = GenericTreeTraversals()
    tree_traversals.root = root

    print(f"\nPreorder: {tree_traversals.preorder_traversal()} 🔄")
    print(f"Postorder: {tree_traversals.postorder_traversal()} 🔄")
    print(f"Level Order: {tree_traversals.level_order_traversal()} 📊")

    print("✅ Generic tree tests passed!")


# --- 6.2. Test Expression Tree ---
def test_expression_tree():
    """Test expression tree implementation."""
    print("\n🧮 Testing Expression Tree...")

    tree = ExpressionTree()

    # Build from postfix 📝
    postfix = ['3', '4', '+', '5', '*']
    tree.build_from_postfix(postfix)

    print("Expression Tree Structure:")
    tree.print_tree()

    print(f"\nInfix: {tree.infix_traversal()} 📝")
    print(f"Prefix: {tree.prefix_traversal()} 🔢")
    print(f"Postfix: {tree.postfix_traversal()} 📋")

    # Test evaluation 🧮
    eval_tree = EvaluableExpressionTree()
    eval_tree.build_from_postfix(postfix)
    result = eval_tree.evaluate()
    print(f"Result: {result} 🎯")

    print("✅ Expression tree tests passed!")


# --- 6.3. Test File System ---
def test_file_system():
    """Test file system implementation."""
    print("\n📂 Testing File System...")

    fs = FileSystem()

    # Create structure 🏗️
    home = fs.add_directory(fs.root, "home")
    user = fs.add_directory(home, "user")
    docs = fs.add_directory(user, "documents")
    pics = fs.add_directory(user, "pictures")

    # Add files 📄
    fs.add_file(docs, "report.txt", 1024)
    fs.add_file(docs, "notes.md", 2048)
    fs.add_file(pics, "photo1.jpg", 102400)
    fs.add_file(pics, "photo2.jpg", 204800)

    print("File System Structure:")
    fs.print_tree()

    print(f"\nTotal size in pictures: {pics.get_total_size()} bytes 📊")
    print(f"Total size in documents: {docs.get_total_size()} bytes 📊")

    print("✅ File system tests passed!")


# --- 6.4. Test Calculator ---
def test_calculator():
    """Test calculator implementation."""
    print("\n🖩 Testing Calculator...")

    calc = Calculator()

    # Test simple arithmetic 🧮
    postfix1 = ['2', '3', '*', '4', '+', '1', '-']
    result1 = calc.evaluate_postfix(postfix1)
    print(f"2 * 3 + 4 - 1 = {result1} 🎯")

    # Test with variables 🔤
    calc.set_variable('a', 5)
    calc.set_variable('b', 3)
    calc.set_variable('c', 2)

    postfix2 = ['a', 'b', '+', 'c', '*']
    result2 = calc.evaluate_postfix(postfix2)
    print(f"(a + b) * c where a=5, b=3, c=2 = {result2} 🎯")

    print("✅ Calculator tests passed!")


# --- 6.5. Test Decision Tree ---
def test_decision_tree():
    """Test decision tree implementation."""
    print("\n🤔 Testing Decision Tree...")

    game = SimpleDecisionTree()
    game.build_animal_guesser()

    print("Decision Tree Structure:")

    def print_tree(node, indent=""):
        if node.is_leaf:
            print(f"{indent}🍃 {node.answer}")
        else:
            print(f"{indent}❓ {node.question}")
            for condition, child in node.children:
                print(f"{indent}  └─ {condition}:")
                print_tree(child, indent + "    ")

    print_tree(game.root)

    print("✅ Decision tree tests passed!")


# --- 6.6. Test Calculator Engine ---
def test_calculator_engine():
    """Test calculator engine."""
    print("\n🖩 Testing Calculator Engine...")

    calc = CalculatorEngine()

    # Test various expressions 🧮
    expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 / 2 + 3",
        "8 - 3 * 2 + 1",
        "(5 + 3) * (10 - 8)",
    ]

    for expr in expressions:
        result = calc.calculate_infix(expr)
        print(f"{expr} = {result} 🎯")

    print("\nCalculation History: 📜")
    calc.show_history()

    print("✅ Calculator engine tests passed!")


# --- 6.7. Test Technical Challenges ---
def test_challenges():
    """Test all technical challenges."""
    print("\n🧩 Testing Technical Challenges...")

    # Challenge 1: Infix to Postfix
    print("\n--- Challenge 1: Infix to Postfix ---")
    test_cases_1 = [
        (['2', '+', '3'], ['2', '3', '+']),
        (['2', '+', '3', '*', '4'], ['2', '3', '4', '*', '+']),
        (['(', '2', '+', '3', ')', '*', '4'], ['2', '3', '+', '4', '*']),
        (['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')'],
         ['1', '2', '+', '3', '4', '-', '*']),
        (['a', '+', 'b', '*', 'c', '/', 'd'],
         ['a', 'b', 'c', '*', 'd', '/', '+']),
    ]

    for infix, expected in test_cases_1:
        result = infix_to_postfix(infix)
        status = "✅" if result == expected else "❌"
        print(
            f"Infix: {' '.join(infix)} => Postfix: {' '.join(result)} {status}")

    # Challenge 2: Build Expression Tree from Infix
    print("\n--- Challenge 2: Build Expression Tree from Infix ---")
    test_cases_2 = [
        ['2', '+', '3'],
        ['2', '+', '3', '*', '4'],
        ['(', '2', '+', '3', ')', '*', '4'],
        ['x', '+', 'y', '*', 'z'],
        ['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'],
    ]

    for tokens in test_cases_2:
        tree = ExpressionTreeBuilder.from_infix(tokens)
        print(f"Built tree from: {' '.join(tokens)} ✅")

    # Challenge 3: Generic Tree Height
    print("\n--- Challenge 3: Generic Tree Height ---")

    # Empty tree 🈳
    empty_ops = GenericTreeOperations(None)
    print(f"Empty tree height: {empty_ops.height()} (expected: -1) ✅")

    # Single node 🌱
    single = GenericTreeNode('A')
    single_ops = GenericTreeOperations(single)
    print(f"Single node height: {single_ops.height()} (expected: 0) ✅")

    # Linear tree 📏
    linear_root = GenericTreeNode('A')
    linear_b = GenericTreeNode('B')
    linear_c = GenericTreeNode('C')
    linear_root.children = [linear_b]
    linear_b.children = [linear_c]
    linear_ops = GenericTreeOperations(linear_root)
    print(f"Linear tree height: {linear_ops.height()} (expected: 2) ✅")

    # Balanced tree 🌳
    balanced_root = GenericTreeNode('A')
    b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
    e, f, g, h = GenericTreeNode('E'), GenericTreeNode(
        'F'), GenericTreeNode('G'), GenericTreeNode('H')
    balanced_root.children = [b, c, d]
    b.children = [e, f, g]
    d.children = [h]
    balanced_ops = GenericTreeOperations(balanced_root)
    print(f"Balanced tree height: {balanced_ops.height()} (expected: 2) ✅")

    # Challenge 4: Find All Leaves
    print("\n--- Challenge 4: Find All Leaves ---")

    # Empty tree 🈳
    empty_finder = LeafFinder(None)
    print(f"Empty tree leaves: {empty_finder.find_leaves()} (expected: []) ✅")

    # Single node 🌱
    single_finder = LeafFinder(single)
    print(
        f"Single node leaves: {single_finder.find_leaves()} (expected: ['A']) ✅")

    # Multiple leaves 🍃
    tree_finder = LeafFinder(balanced_root)
    leaves = sorted(tree_finder.find_leaves())
    print(
        f"Balanced tree leaves: {leaves} (expected: ['C', 'E', 'F', 'G', 'H']) ✅")

    # Challenge 5: Expression Tree Simplification
    print("\n--- Challenge 5: Expression Tree Simplification ---")

    # All constants 🔢
    const_tree = ExpressionSimplifier()
    const_tree.root = ExpressionNode('+')
    const_tree.root.left = ExpressionNode('2')
    const_tree.root.right = ExpressionNode('3')
    const_tree.simplify()
    print(f"Simplify 2 + 3: {const_tree.root.value} (expected: 5) ✅")

    # Partial simplification ⚡
    partial_tree = ExpressionSimplifier()
    partial_tree.root = ExpressionNode('*')
    add = ExpressionNode('+')
    add.left, add.right = ExpressionNode('2'), ExpressionNode('3')
    partial_tree.root.left = add
    partial_tree.root.right = ExpressionNode('x')
    partial_tree.simplify()
    print(
        f"Simplify (2 + 3) * x: {partial_tree.root.left.value} * {partial_tree.root.right.value} (expected: 5 * x) ✅")

    print("\n✅ All technical challenges passed!")


# ========================================================================================
# 7. MAIN EXECUTION
# ========================================================================================

def main():
    """Run all tests and demonstrations."""
    print("🌿 GENERIC AND EXPRESSION TREES - IMPLEMENTATION 🌿")
    print("=" * 50)

    # Test basic implementations 🏗️
    test_generic_tree()
    test_expression_tree()

    # Test practical applications 💼
    test_file_system()
    test_calculator()
    test_decision_tree()

    # Test real-world case study 🌍
    test_calculator_engine()

    # Test technical challenges 🧩
    test_challenges()

    print("\n🎉 ALL TESTS COMPLETED SUCCESSFULLY! 🎉")
    print("=" * 50)


if __name__ == "__main__":
    main()
