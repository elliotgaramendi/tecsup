"""
🌳 Binary Trees Implementation with tests and examples 🌳

This file contains implementations for all concepts and challenges
in the Binary Trees guide, with a clear structure following the course outline.
"""

# ==========================================================================
# 1. UNDERSTANDING THE FUNDAMENTAL CONCEPT
# ==========================================================================


class TreeNode:
    """Basic node in a binary tree."""

    def __init__(self, value):
        self.value = value  # 📊 Data stored in node
        self.left = None    # 👈 Left child reference
        self.right = None   # 👉 Right child reference


def create_sample_tree():
    """Create a sample binary tree for testing."""
    # Create tree structure:
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

# ==========================================================================
# 2. PROGRESSIVE IMPLEMENTATIONS
# ==========================================================================

# 2.1 Basic Binary Tree with Traversals


class BinaryTree:
    """Binary tree implementation with basic traversals."""

    def __init__(self, root=None):
        self.root = root    # 🌱 Root node reference

    def preorder_traversal(self, node, result=None):
        """DLR: Process Data, then Left, then Right subtree."""
        if result is None:
            result = []

        if node:
            result.append(node.value)           # Visit node (D)
            self.preorder_traversal(node.left, result)   # Left subtree (L)
            self.preorder_traversal(node.right, result)  # Right subtree (R)

        return result

    def inorder_traversal(self, node, result=None):
        """LDR: Process Left, then Data, then Right subtree."""
        if result is None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)    # Left subtree (L)
            result.append(node.value)           # Visit node (D)
            self.inorder_traversal(node.right, result)   # Right subtree (R)

        return result

    def postorder_traversal(self, node, result=None):
        """LRD: Process Left, then Right, then Data."""
        if result is None:
            result = []

        if node:
            self.postorder_traversal(node.left, result)  # Left subtree (L)
            self.postorder_traversal(node.right, result)  # Right subtree (R)
            result.append(node.value)           # Visit node (D)

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
            raise ValueError(
                "Invalid traversal order. Use 'preorder', 'inorder', or 'postorder'")

# 2.2 Binary Tree with Extended Operations


class ExtendedBinaryTree(BinaryTree):
    """Binary tree with extended operations."""

    def height(self, node=None):
        """Calculate height of the tree (or subtree)."""
        if node is None:
            node = self.root

        if not node:
            return -1  # Empty tree has height -1

        # Height is maximum of left and right subtree heights, plus 1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
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

# ==========================================================================
# 3. PRACTICAL APPLICATIONS
# ==========================================================================

# 3.1 Expression Tree Evaluator


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
        """Convert to infix notation with parentheses."""
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

# 3.2 Directory Structure Representation


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

        parent_path = self.parent.get_path()
        # Avoid double slash when parent is root
        if parent_path == "/":
            return parent_path + self.name
        return parent_path + "/" + self.name


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

        # Create new directory
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

        # Create new file
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

# ==========================================================================
# 4. REAL-WORLD CASE STUDY: COMPILER SYNTAX TREE
# ==========================================================================


class SyntaxNode:
    """Node in a syntax tree."""

    def __init__(self, node_type, value=None):
        self.type = node_type    # 🏷️ Node type (e.g., 'variable', 'operator')
        # 📊 Node value (e.g., variable name, operator symbol)
        self.value = value
        self.children = []       # 👨‍👩‍👧‍👦 Child nodes

    def add_child(self, child):
        """Add a child node."""
        if child:  # Only add non-None children
            self.children.append(child)
        return self


class SimpleCompiler:
    """A very simple compiler that builds and evaluates syntax trees."""

    def parse_expression(self, expression):
        """Parse a simple mathematical expression and build a syntax tree."""
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
        tokens = expr.split()

        # Look for lowest precedence operator (+ or -)
        for i in range(len(tokens) - 1, 0, -1):
            if tokens[i] in ['+', '-']:
                # Create operator node
                op_node = SyntaxNode('operator', tokens[i])

                # Parse left and right expressions
                left_expr = ' '.join(tokens[:i])
                right_expr = ' '.join(tokens[i+1:])

                op_node.add_child(self._parse_arithmetic(
                    left_expr) if left_expr else None)
                op_node.add_child(self._parse_arithmetic(
                    right_expr) if right_expr else None)

                return op_node

        # Look for higher precedence operator (* or /)
        for i in range(len(tokens) - 1, 0, -1):
            if tokens[i] in ['*', '/']:
                # Create operator node
                op_node = SyntaxNode('operator', tokens[i])

                # Parse left and right expressions
                left_expr = ' '.join(tokens[:i])
                right_expr = ' '.join(tokens[i+1:])

                op_node.add_child(self._parse_arithmetic(
                    left_expr) if left_expr else None)
                op_node.add_child(self._parse_arithmetic(
                    right_expr) if right_expr else None)

                return op_node

        # Single token (number or variable)
        if len(tokens) == 1:
            # Try to convert to number
            try:
                return SyntaxNode('number', float(tokens[0]))
            except ValueError:
                return SyntaxNode('variable', tokens[0])

        # Fallback
        return SyntaxNode('unknown', ' '.join(tokens))

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
            left_val = self.evaluate(node.children[0], variables)
            right_val = self.evaluate(node.children[1], variables)

            if node.value == '+':
                return left_val + right_val
            if node.value == '-':
                return left_val - right_val
            if node.value == '*':
                return left_val * right_val
            if node.value == '/':
                if right_val == 0:
                    raise ZeroDivisionError("Division by zero")
                return left_val / right_val

        elif node.type == 'assignment':
            var_name = node.children[0].value
            var_value = self.evaluate(node.children[1], variables)
            variables[var_name] = var_value
            return var_value

        return None

# ==========================================================================
# 5. TECHNICAL CHALLENGES
# ==========================================================================

# 5.1 Challenge 1: Tree Height Calculation


def tree_height(root):
    """Calculate the height of a binary tree."""
    # Base case: empty tree has height -1
    if not root:
        return -1

    # Recursively find the height of left and right subtrees
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    # Height is the maximum of left and right subtree heights, plus 1
    return max(left_height, right_height) + 1

# 5.2 Challenge 2: Count Leaf Nodes


def count_leaves(root):
    """Count the number of leaf nodes in a binary tree."""
    # Base case: empty tree has 0 leaves
    if not root:
        return 0

    # If node is a leaf (no children), count as 1
    if not root.left and not root.right:
        return 1

    # Recursively count leaves in left and right subtrees
    return count_leaves(root.left) + count_leaves(root.right)

# 5.3 Challenge 3: Tree Mirroring


def mirror_tree(root):
    """Mirror a binary tree by swapping left and right children."""
    # Base case: empty tree or leaf node
    if not root:
        return

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively mirror the subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root

# 5.4 Challenge 4: Level Order Traversal


def level_order_traversal(root):
    """Perform level order traversal of a binary tree."""
    if not root:
        return []

    result = []
    queue = [root]  # Use a list as a queue

    while queue:
        # Get the next node
        current = queue.pop(0)
        result.append(current.value)

        # Add children to the queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# 5.5 Challenge 5: Check if a Binary Tree is Balanced


def is_balanced(root):
    """Check if a binary tree is balanced (height difference between subtrees ≤ 1)."""

    def check_height(node):
        """Helper function that returns (is_balanced, height)."""
        # Base case: empty subtree is balanced with height -1
        if not node:
            return True, -1

        # Check left subtree
        left_balanced, left_height = check_height(node.left)
        if not left_balanced:
            return False, 0

        # Check right subtree
        right_balanced, right_height = check_height(node.right)
        if not right_balanced:
            return False, 0

        # Check balance at current node
        is_balanced_here = abs(left_height - right_height) <= 1
        height_here = max(left_height, right_height) + 1

        return is_balanced_here, height_here

    # Call the helper function and return the balanced status
    balanced, _ = check_height(root)
    return balanced

# ==========================================================================
# 6. TESTING FUNCTIONS
# ==========================================================================


def test_tree_node():
    """Test basic tree node creation."""
    print("\n🌳 Testing basic tree node...")

    # Create a simple tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # Verify structure
    assert root.value == 1
    assert root.left.value == 2
    assert root.right.value == 3
    assert root.left.left is None

    # Test creating a sample tree
    tree = create_sample_tree()
    assert tree.value == 1
    assert tree.left.left.value == 4

    print("✅ Basic tree node tests passed!")


def test_traversals():
    """Test tree traversal algorithms."""
    print("\n🔄 Testing tree traversals...")

    # Create a test tree
    tree = BinaryTree(create_sample_tree())

    # Test traversals
    preorder = tree.traverse("preorder")
    inorder = tree.traverse("inorder")
    postorder = tree.traverse("postorder")

    assert preorder == [1, 2, 4, 5, 3, 6], f"Got {preorder}"
    assert inorder == [4, 2, 5, 1, 3, 6], f"Got {inorder}"
    assert postorder == [4, 5, 2, 6, 3, 1], f"Got {postorder}"

    print("✅ Tree traversals tests passed!")


def test_expression_tree():
    """Test expression tree evaluation."""
    print("\n🧮 Testing expression tree...")

    # Create and test expression tree
    expr_tree = ExpressionTree()
    expr_tree.build_from_postfix(["3", "4", "+", "2", "*"])

    assert expr_tree.print_infix() == "((3 + 4) * 2)"
    assert expr_tree.evaluate() == 14.0

    # Test more complex expression
    expr_tree = ExpressionTree()
    expr_tree.build_from_postfix(["5", "2", "3", "*", "+"])

    assert expr_tree.print_infix() == "(5 + (2 * 3))"
    assert expr_tree.evaluate() == 11.0

    print("✅ Expression tree tests passed!")


def test_file_system():
    """Test file system implementation."""
    print("\n📁 Testing file system...")

    # Create file system
    fs = FileSystem()

    # Create directories and files
    home = fs.create_directory("/", "home")
    user = fs.create_directory("/home", "user")
    fs.create_file("/home/user", "notes.txt")

    # Test paths
    assert home.get_path() == "/home"
    assert user.get_path() == "/home/user"

    # Test directory listing
    contents = fs.list_directory("/home")
    assert "user" in contents

    print("✅ File system tests passed!")


def test_compiler():
    """Test the simple compiler."""
    print("\n🔠 Testing simple compiler...")

    compiler = SimpleCompiler()
    variables = {}

    # Test arithmetic expressions
    tree = compiler.parse_expression("5 + 3")
    result = compiler.evaluate(tree, variables)
    assert result == 8

    # Test operator precedence
    tree = compiler.parse_expression("5 + 3 * 2")
    result = compiler.evaluate(tree, variables)
    assert result == 11

    # Test variable assignment
    tree = compiler.parse_expression("x = 10")
    compiler.evaluate(tree, variables)
    assert variables["x"] == 10

    # Test expression with variables
    tree = compiler.parse_expression("x + 5")
    result = compiler.evaluate(tree, variables)
    assert result == 15

    print("✅ Compiler tests passed!")


def test_challenges():
    """Test all the technical challenges."""
    print("\n🧩 Testing technical challenges...")

    # Create test trees
    normal_tree = create_sample_tree()
    empty_tree = None
    single_node = TreeNode(1)

    # Create an unbalanced tree
    unbalanced = TreeNode(1)
    unbalanced.left = TreeNode(2)
    unbalanced.left.left = TreeNode(3)
    unbalanced.left.left.left = TreeNode(4)

    # Test Challenge 1: Tree Height
    assert tree_height(normal_tree) == 2
    assert tree_height(empty_tree) == -1
    assert tree_height(single_node) == 0
    assert tree_height(unbalanced) == 3
    print("✅ Tree height challenge passed!")

    # Test Challenge 2: Count Leaves
    assert count_leaves(normal_tree) == 3
    assert count_leaves(empty_tree) == 0
    assert count_leaves(single_node) == 1
    assert count_leaves(unbalanced) == 1
    print("✅ Count leaves challenge passed!")

    # Test Challenge 3: Tree Mirroring
    # Create a copy for comparison
    normal_copy = create_sample_tree()
    inorder_before = inorder_traversal(normal_tree, [])
    mirror_tree(normal_tree)
    inorder_after = inorder_traversal(normal_tree, [])
    assert inorder_before != inorder_after
    # Mirror back
    mirror_tree(normal_tree)
    inorder_after_mirror_back = inorder_traversal(normal_tree, [])
    assert inorder_before == inorder_after_mirror_back
    print("✅ Tree mirroring challenge passed!")

    # Test Challenge 4: Level Order Traversal
    assert level_order_traversal(normal_tree) == [1, 2, 3, 4, 5, 6]
    assert level_order_traversal(empty_tree) == []
    assert level_order_traversal(single_node) == [1]
    print("✅ Level order traversal challenge passed!")

    # Test Challenge 5: Is Balanced
    assert is_balanced(normal_tree) == True
    assert is_balanced(empty_tree) == True
    assert is_balanced(single_node) == True
    assert is_balanced(unbalanced) == False
    print("✅ Is balanced challenge passed!")

    print("✨ All technical challenges passed!")


def inorder_traversal(root, result=None):
    """Standalone inorder traversal for testing."""
    if result is None:
        result = []

    if root:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)

    return result

# ==========================================================================
# 7. MAIN EXECUTION
# ==========================================================================


def run_all_tests():
    """Run all tests for the binary trees implementation."""
    print("🌳 BINARY TREES IMPLEMENTATION - TESTS 🌳")
    print("=======================================")

    # Test basic concepts
    test_tree_node()
    test_traversals()

    # Test practical applications
    test_expression_tree()
    test_file_system()
    test_compiler()

    # Test the challenges
    test_challenges()

    print("\n✨✨✨ ALL TESTS PASSED! ✨✨✨")


if __name__ == "__main__":
    run_all_tests()
