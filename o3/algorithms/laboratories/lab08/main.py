"""
🌳 Advanced Binary Trees Implementation 🌳

This module implements advanced binary tree concepts and operations,
providing examples and solutions for challenges in the Advanced Binary Trees guide.
"""

# ========================================================================================
# 1. Understanding the Fundamental Concept
# ========================================================================================

from collections import Counter
import heapq


class TreeNode:
    """Basic node for binary tree structures."""

    def __init__(self, value):
        self.value = value    # 📊 Node's data
        self.left = None      # 👈 Left child reference
        self.right = None     # 👉 Right child reference


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


# ========================================================================================
# 2. Progressive Implementations
# ========================================================================================

# Basic Binary Tree with Traversals
class BinaryTree:
    """Binary tree implementation with basic traversals."""

    def __init__(self, root=None):
        self.root = root    # 🌱 Root node reference

    def preorder_traversal(self, node, result=None):
        """DLR: Process Data, then Left, then Right subtree."""
        if result is None:
            result = []

        if node:
            result.append(node.value)           # 📌 Process current node
            self.preorder_traversal(node.left, result)   # 👈 Process left
            self.preorder_traversal(node.right, result)  # 👉 Process right

        return result

    def inorder_traversal(self, node, result=None):
        """LDR: Process Left, then Data, then Right subtree."""
        if result is None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)    # 👈 Process left
            result.append(node.value)           # 📌 Process current node
            self.inorder_traversal(node.right, result)   # 👉 Process right

        return result

    def postorder_traversal(self, node, result=None):
        """LRD: Process Left, then Right, then Data."""
        if result is None:
            result = []

        if node:
            self.postorder_traversal(node.left, result)  # 👈 Process left
            self.postorder_traversal(node.right, result)  # 👉 Process right
            result.append(node.value)           # 📌 Process current node

        return result

    def level_order_traversal(self):
        """Visit nodes level by level from top to bottom."""
        if not self.root:
            return []

        result = []
        queue = [self.root]  # 📋 Use queue for level-order traversal

        while queue:
            current = queue.pop(0)  # ⏏️ Dequeue front node
            result.append(current.value)

            if current.left:
                queue.append(current.left)  # ➕ Enqueue left child
            if current.right:
                queue.append(current.right)  # ➕ Enqueue right child

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

    def build_tree_from_list(self, values):
        """Build a binary tree from a list of values in level order."""
        if not values:
            return

        self.root = TreeNode(values[0])
        queue = [self.root]
        i = 1

        while queue and i < len(values):
            current = queue.pop(0)

            # Add left child
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            # Add right child
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

    def print_tree(self, node=None, prefix="", is_left=True):
        """Print the tree structure in a visual format."""
        if node is None:
            node = self.root

        if node is None:
            print("Empty tree 🈳")
            return

        if node.right:
            self.print_tree(node.right, prefix +
                            ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.left:
            self.print_tree(node.left, prefix +
                            ("    " if is_left else "│   "), True)

# Binary Search Tree (BST)


class BinarySearchTree:
    """Binary Search Tree implementation with ordered operations."""

    def __init__(self):
        self.root = None  # 🌱 Root node reference

    def insert(self, value):
        """Insert a value maintaining the BST property."""
        if not self.root:
            self.root = TreeNode(value)
            return

        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Helper method for insert."""
        if value < node.value:
            # Go left 👈
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            # Go right 👉
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method for search."""
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            # Search left subtree 👈
            return self._search_recursive(node.left, value)
        else:
            # Search right subtree 👉
            return self._search_recursive(node.right, value)

    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        """Helper method for delete."""
        if node is None:
            return None

        if value < node.value:
            # Delete from left subtree 👈
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            # Delete from right subtree 👉
            node.right = self._delete_recursive(node.right, value)
        else:
            # Found the node to delete 🎯

            # Case 1: Node with no children 🍃
            if node.left is None and node.right is None:
                return None

            # Case 2: Node with one child 👨‍👦
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Node with two children 👨‍👧‍👦
            # Find inorder successor (smallest in right subtree)
            successor_value = self._find_min_value(node.right)
            node.value = successor_value
            node.right = self._delete_recursive(node.right, successor_value)

        return node

    def _find_min_value(self, node):
        """Find the minimum value in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current.value

    def inorder_traversal(self):
        """Return values in sorted order (inorder traversal)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def print_tree(self):
        """Print the tree structure in a visual format."""
        self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self, node, prefix, is_left):
        """Helper method for print_tree."""
        if node is None:
            return

        if node.right:
            self._print_tree_recursive(
                node.right, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.left:
            self._print_tree_recursive(
                node.left, prefix + ("    " if is_left else "│   "), True)

# AVL Tree: Self-Balancing BST


class AVLNode(TreeNode):
    """Node for AVL Tree with height information."""

    def __init__(self, value):
        super().__init__(value)
        self.height = 1  # 📏 Height of the node (leaf nodes have height 1)


class AVLTree:
    """Self-balancing AVL tree implementation."""

    def __init__(self):
        self.root = None  # 🌱 Root node reference

    def height(self, node):
        """Get the height of a node."""
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        """Calculate balance factor of a node."""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        """Update the height of a node based on its children's heights."""
        if node is None:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, y):
        """Perform right rotation on node y.

             y                x
            / \              / \
           x   T3   -->     T1  y
          / \                  / \
         T1  T2               T2  T3
        """
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self.update_height(y)
        self.update_height(x)

        # Return new root
        return x

    def left_rotate(self, x):
        """Perform left rotation on node x.

            x                 y
           / \               / \
          T1  y     -->     x   T3
             / \           / \
            T2  T3        T1  T2
        """
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self.update_height(x)
        self.update_height(y)

        # Return new root
        return y

    def insert(self, value):
        """Insert a value into the AVL tree."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Helper method for insert."""
        # 1. Perform standard BST insert
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        # 2. Update height of current node
        self.update_height(node)

        # 3. Get the balance factor
        balance = self.balance_factor(node)

        # 4. If node is unbalanced, there are 4 cases

        # Left Left Case ⬅️⬅️
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Right Right Case ➡️➡️
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Left Right Case ⬅️➡️
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case ➡️⬅️
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the unchanged node pointer
        return node

    def inorder_traversal(self):
        """Return values in sorted order (inorder traversal)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def print_tree(self):
        """Print the tree structure in a visual format."""
        self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self, node, prefix, is_left):
        """Helper method for print_tree."""
        if node is None:
            return

        if node.right:
            self._print_tree_recursive(
                node.right, prefix + ("│   " if is_left else "    "), False)

        balance = self.balance_factor(node)
        print(prefix + ("└── " if is_left else "┌── ") +
              f"{node.value} [h={node.height}, b={balance}]")

        if node.left:
            self._print_tree_recursive(
                node.left, prefix + ("    " if is_left else "│   "), True)


# ========================================================================================
# 3. Practical Applications
# ========================================================================================

# Expression Tree Evaluator
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
                raise ZeroDivisionError("Division by zero ⚠️")
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


# Huffman Coding


class HuffmanNode:
    """Node for Huffman encoding tree."""

    def __init__(self, char, freq):
        self.char = char        # 📝 Character (None for internal nodes)
        self.freq = freq        # 📊 Frequency of the character
        self.left = None        # 👈 Left child
        self.right = None       # � Right child

    # Allow nodes to be compared based on frequency (for the heap)
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    """Implements Huffman coding for data compression."""

    def __init__(self):
        self.root = None       # 🌱 Root of the Huffman tree
        self.codes = {}        # 📖 Dictionary to store character codes

    def build_huffman_tree(self, text):
        """Build Huffman tree from input text."""
        # Count frequency of each character
        frequency = Counter(text)

        # Create a priority queue (min heap)
        priority_queue = [HuffmanNode(char, freq)
                          for char, freq in frequency.items()]
        heapq.heapify(priority_queue)

        # Build the Huffman tree
        while len(priority_queue) > 1:
            # Extract two nodes with lowest frequencies
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            # Create a new internal node with frequency = sum of the two nodes
            internal = HuffmanNode(None, left.freq + right.freq)
            internal.left = left
            internal.right = right

            # Add the internal node back to the priority queue
            heapq.heappush(priority_queue, internal)

        # The remaining node is the root of the Huffman tree
        if priority_queue:
            self.root = heapq.heappop(priority_queue)

    def generate_codes(self):
        """Generate codes for each character."""
        self.codes = {}
        self._generate_codes_recursive(self.root, "")
        return self.codes

    def _generate_codes_recursive(self, node, code):
        """Recursively generate codes for the Huffman tree."""
        if node is None:
            return

        # If node is a leaf (has a character), assign code
        if node.char is not None:
            self.codes[node.char] = code
            return

        # Traverse left (add '0' to code)
        self._generate_codes_recursive(node.left, code + "0")

        # Traverse right (add '1' to code)
        self._generate_codes_recursive(node.right, code + "1")

    def encode(self, text):
        """Encode input text using Huffman codes."""
        # Make sure codes are generated
        if not self.codes:
            self.generate_codes()

        # Encode text
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]

        return encoded_text

    def decode(self, encoded_text):
        """Decode Huffman-encoded text."""
        if not self.root:
            return ""

        decoded_text = ""
        current_node = self.root

        for bit in encoded_text:
            # Navigate the tree based on the bit
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            # If we reach a leaf node, add character and reset to root
            if current_node.char is not None:
                decoded_text += current_node.char
                current_node = self.root

        return decoded_text

    def print_tree(self):
        """Print the Huffman tree."""
        self._print_tree_recursive(self.root, "", True)

    def _print_tree_recursive(self, node, prefix, is_left):
        """Helper method for print_tree."""
        if node is None:
            return

        if node.right:
            self._print_tree_recursive(
                node.right, prefix + ("│   " if is_left else "    "), False)

        # Show character (or frequency for internal nodes)
        display = f"'{node.char}'" if node.char is not None else "*"
        print(prefix + ("└── " if is_left else "┌── ") +
              f"{display} ({node.freq})")

        if node.left:
            self._print_tree_recursive(
                node.left, prefix + ("    " if is_left else "│   "), True)


# ========================================================================================
# 4. Real-world Case Study: File System Navigation
# ========================================================================================

class FileSystemNode:
    """Node representing a file or directory."""

    def __init__(self, name, is_directory=False):
        self.name = name                # 📛 Name of file/directory
        self.is_directory = is_directory  # 📁 Is it a directory?
        self.children = {}              # 👨‍👩‍👧‍👦 Child nodes (if directory)
        self.content = ""               # 📄 File content (if file)

    def add_child(self, name, is_directory=False):
        """Add a child node (file or directory)."""
        if not self.is_directory:
            raise ValueError("Cannot add child to a file")

        # Check if child already exists
        if name in self.children:
            return self.children[name]

        # Create new child and add to children dictionary
        child = FileSystemNode(name, is_directory)
        self.children[name] = child
        return child


class FileSystem:
    """Simple file system implementation using trees."""

    def __init__(self):
        self.root = FileSystemNode("/", True)  # 🌱 Root directory
        self.current_path = "/"                # 🧭 Current working directory

    def get_node(self, path):
        """Get the node at the specified path."""
        if not path or path == "/":
            return self.root

        # Split path into components
        if path.startswith("/"):
            path = path[1:]  # Remove leading slash

        if path.endswith("/"):
            path = path[:-1]  # Remove trailing slash

        components = path.split("/")

        # Start at root and follow path
        current = self.root
        for component in components:
            if not current.is_directory or component not in current.children:
                return None
            current = current.children[component]

        return current

    def mkdir(self, path):
        """Create a directory at the specified path."""
        # If absolute path, start from root
        if path.startswith("/"):
            parent_path = "/".join(path.split("/")[:-1])
            if not parent_path:
                parent_path = "/"
        else:
            # Relative path, start from current directory
            parent_path = self.current_path
            if not parent_path.endswith("/"):
                parent_path += "/"
            parent_path += "/".join(path.split("/")[:-1])

        dir_name = path.split("/")[-1]

        # Get parent directory
        parent = self.get_node(parent_path)
        if not parent or not parent.is_directory:
            raise ValueError(f"Invalid parent directory: {parent_path}")

        # Create directory
        return parent.add_child(dir_name, is_directory=True)

    def touch(self, path, content=""):
        """Create a file at the specified path."""
        # If absolute path, start from root
        if path.startswith("/"):
            parent_path = "/".join(path.split("/")[:-1])
            if not parent_path:
                parent_path = "/"
        else:
            # Relative path, start from current directory
            parent_path = self.current_path
            if not parent_path.endswith("/"):
                parent_path += "/"
            parent_path += "/".join(path.split("/")[:-1])

        file_name = path.split("/")[-1]

        # Get parent directory
        parent = self.get_node(parent_path)
        if not parent or not parent.is_directory:
            raise ValueError(f"Invalid parent directory: {parent_path}")

        # Create file
        file = parent.add_child(file_name)
        file.content = content
        return file

    def ls(self, path=None):
        """List contents of a directory."""
        if path is None:
            path = self.current_path

        node = self.get_node(path)
        if not node:
            raise ValueError(f"Path not found: {path}")

        if not node.is_directory:
            # If path is a file, just return the file name
            return [node.name]

        # Return sorted list of children
        return sorted(node.children.keys())

    def cd(self, path):
        """Change current directory."""
        # Handle special paths
        if path == "..":
            # Go up one directory
            if self.current_path == "/":
                return  # Already at root

            self.current_path = "/".join(self.current_path.split("/")[:-1])
            if not self.current_path:
                self.current_path = "/"
            return

        # Resolve path
        if not path.startswith("/"):
            # Relative path
            if not self.current_path.endswith("/"):
                absolute_path = self.current_path + "/" + path
            else:
                absolute_path = self.current_path + path
        else:
            # Absolute path
            absolute_path = path

        # Check if path exists and is a directory
        node = self.get_node(absolute_path)
        if not node:
            raise ValueError(f"Path not found: {absolute_path}")

        if not node.is_directory:
            raise ValueError(f"Not a directory: {absolute_path}")

        # Update current path
        self.current_path = absolute_path

    def cat(self, path):
        """Display the contents of a file."""
        node = self.get_node(path)
        if not node:
            raise ValueError(f"File not found: {path}")

        if node.is_directory:
            raise ValueError(f"Not a file: {path}")

        return node.content

    def print_tree(self, path="/", indent=0):
        """Print the directory structure as a tree."""
        node = self.get_node(path)
        if not node:
            print("Path not found")
            return

        # Print the current node
        prefix = "   " * indent
        type_icon = "📁" if node.is_directory else "📄"
        print(f"{prefix}{type_icon} {node.name}")

        # Recursively print children if directory
        if node.is_directory:
            for child_name in sorted(node.children.keys()):
                child_path = f"{path}/{child_name}" if path != "/" else f"/{child_name}"
                self.print_tree(child_path, indent + 1)


# ========================================================================================
# 5. Technical Challenges
# ========================================================================================

# Challenge 1: Tree Height Calculation
def tree_height(root):
    """Calculate the height of a binary tree."""
    if not root:
        return -1  # Empty tree has height -1

    # Height is the maximum of left and right subtree heights, plus 1
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return max(left_height, right_height) + 1

# Challenge 2: Count Leaf Nodes


def count_leaves(root):
    """Count the number of leaf nodes in a binary tree."""
    if not root:
        return 0  # Empty tree has 0 leaves

    # If node is a leaf (no children), return 1
    if not root.left and not root.right:
        return 1

    # Recursively count leaves in left and right subtrees
    return count_leaves(root.left) + count_leaves(root.right)

# Challenge 3: Tree Mirroring


def mirror_tree(root):
    """Mirror a binary tree by swapping left and right children."""
    if not root:
        return  # Base case: empty tree

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Recursively mirror the subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)

    return root

# Challenge 4: Level Order Traversal


def level_order_traversal(root):
    """Perform level order traversal of a binary tree."""
    if not root:
        return []

    result = []
    queue = [root]  # Use a list as a queue

    while queue:
        current = queue.pop(0)  # Dequeue front node
        result.append(current.value)

        # Add children to queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Challenge 5: Check if a Binary Tree is Balanced


def is_balanced(root):
    """Check if a binary tree is balanced (height difference between subtrees ≤ 1)."""

    def check_height(node):
        """Helper function that returns (is_balanced, height)."""
        # Base case: empty subtree is balanced with height -1
        if not node:
            return True, -1

        # Check left and right subtrees
        left_balanced, left_height = check_height(node.left)
        if not left_balanced:
            return False, 0  # Short-circuit if left subtree is unbalanced

        right_balanced, right_height = check_height(node.right)
        if not right_balanced:
            return False, 0  # Short-circuit if right subtree is unbalanced

        # Check if current node is balanced
        is_balanced_here = abs(left_height - right_height) <= 1
        height_here = max(left_height, right_height) + 1

        return is_balanced_here, height_here

    # Call helper function and return balanced status
    balanced, _ = check_height(root)
    return balanced


# ========================================================================================
# 6. Testing Functions
# ========================================================================================

def test_basic_binary_tree():
    """Test basic binary tree functionality."""
    print("\n🌱 Testing basic binary tree structure and traversals...")

    # Create a test tree
    tree = BinaryTree()
    tree.build_tree_from_list([1, 2, 3, 4, 5, None, 6])

    print("Tree structure:")
    tree.print_tree()

    # Test traversals
    preorder = tree.preorder_traversal(tree.root)
    inorder = tree.inorder_traversal(tree.root)
    postorder = tree.postorder_traversal(tree.root)
    level_order = tree.level_order_traversal()

    print(f"Preorder traversal: {preorder}")  # Expected: [1, 2, 4, 5, 3, 6]
    print(f"Inorder traversal: {inorder}")    # Expected: [4, 2, 5, 1, 3, 6]
    print(f"Postorder traversal: {postorder}")  # Expected: [4, 5, 2, 6, 3, 1]
    # Expected: [1, 2, 3, 4, 5, 6]
    print(f"Level order traversal: {level_order}")

    # Validate traversals
    assert preorder == [1, 2, 4, 5, 3, 6], "Preorder traversal error"
    assert inorder == [4, 2, 5, 1, 3, 6], "Inorder traversal error"
    assert postorder == [4, 5, 2, 6, 3, 1], "Postorder traversal error"
    assert level_order == [1, 2, 3, 4, 5, 6], "Level order traversal error"

    print("✅ All basic binary tree tests passed!")


def test_binary_search_tree():
    """Test binary search tree functionality."""
    print("\n🔍 Testing binary search tree...")

    # Create BST and insert values
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)

    print("BST structure:")
    bst.print_tree()

    # Test search
    assert bst.search(50) == True, "BST search error for root"
    assert bst.search(20) == True, "BST search error for leaf"
    assert bst.search(55) == False, "BST search error for non-existent value"

    # Test inorder traversal (should be sorted)
    inorder = bst.inorder_traversal()
    assert inorder == sorted(
        values), f"BST inorder traversal error: {inorder} vs {sorted(values)}"

    # Test deletion
    # Delete leaf node
    bst.delete(20)
    assert bst.search(20) == False, "BST delete leaf node error"

    # Delete node with one child
    bst.delete(30)
    assert bst.search(30) == False, "BST delete one-child node error"
    assert bst.search(40) == True, "BST structure corrupted after deletion"

    # Delete node with two children
    bst.delete(70)
    assert bst.search(70) == False, "BST delete two-children node error"
    assert bst.search(60) == True and bst.search(
        80) == True, "BST structure corrupted after deletion"

    print("✅ All binary search tree tests passed!")


def test_avl_tree():
    """Test AVL tree functionality."""
    print("\n⚖️ Testing AVL tree...")

    # Create AVL tree
    avl = AVLTree()

    # Insert values that would cause imbalance in regular BST
    print("Inserting values: 10, 20, 30, 40, 50, 25")

    # Regular BST would become right-skewed
    for value in [10, 20, 30, 40, 50, 25]:
        avl.insert(value)
        balance_factor = avl.balance_factor(avl.root)
        print(
            f"After inserting {value}, root balance factor: {balance_factor}")

        # Verify balance factor is maintained
        assert abs(
            balance_factor) <= 1, f"AVL tree unbalanced after inserting {value}"

    print("AVL tree structure:")
    avl.print_tree()

    # Verify tree is balanced
    def is_avl_balanced(node):
        if not node:
            return True

        balance = avl.balance_factor(node)
        if abs(balance) > 1:
            return False

        return is_avl_balanced(node.left) and is_avl_balanced(node.right)

    assert is_avl_balanced(avl.root), "AVL tree not balanced"

    # Verify inorder traversal is sorted
    inorder = avl.inorder_traversal()
    assert inorder == sorted(inorder), "AVL tree inorder traversal not sorted"

    print("✅ All AVL tree tests passed!")


def test_expression_tree():
    """Test expression tree evaluation."""
    print("\n🧮 Testing expression tree...")

    # Test case 1: Simple addition and multiplication
    expr_tree = ExpressionTree()
    expr_tree.build_from_postfix(["3", "4", "+", "2", "*"])

    infix = expr_tree.print_infix()
    result = expr_tree.evaluate()

    print(f"Postfix: 3 4 + 2 *")
    print(f"Infix: {infix}")
    print(f"Result: {result}")

    assert infix == "((3 + 4) * 2)", f"Expected ((3 + 4) * 2), got {infix}"
    assert result == 14.0, f"Expected 14, got {result}"

    # Test case 2: More complex expression
    expr_tree2 = ExpressionTree()
    expr_tree2.build_from_postfix(["5", "2", "3", "*", "+", "4", "/"])

    infix2 = expr_tree2.print_infix()
    result2 = expr_tree2.evaluate()

    print(f"Postfix: 5 2 3 * + 4 /")
    print(f"Infix: {infix2}")
    print(f"Result: {result2}")

    assert infix2 == "((5 + (2 * 3)) / 4)", f"Expected ((5 + (2 * 3)) / 4), got {infix2}"
    assert result2 == 2.75, f"Expected 2.75, got {result2}"

    print("✅ All expression tree tests passed!")


def test_huffman_coding():
    """Test Huffman coding compression."""
    print("\n📦 Testing Huffman coding...")

    # Test with a simple string
    text = "abracadabra"

    huffman = HuffmanCoding()
    huffman.build_huffman_tree(text)

    # Generate Huffman codes
    codes = huffman.generate_codes()
    print("Huffman Codes:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")

    # Test encoding
    encoded = huffman.encode(text)
    print(f"Original text: {text}")
    print(f"Encoded text: {encoded}")

    # Calculate compression ratio
    original_size = len(text) * 8  # Assuming 8 bits per character in ASCII
    compressed_size = len(encoded)
    print(f"Original size: {original_size} bits")
    print(f"Compressed size: {compressed_size} bits")
    print(
        f"Compression ratio: {(original_size - compressed_size) / original_size * 100:.2f}%")

    # Test decoding
    decoded = huffman.decode(encoded)
    print(f"Decoded text: {decoded}")

    assert decoded == text, f"Expected {text}, got {decoded}"
    assert len(encoded) < original_size, "Compression failed"

    print("✅ All Huffman coding tests passed!")


def test_file_system():
    """Test file system implementation."""
    print("\n📂 Testing file system...")

    fs = FileSystem()

    # Create directories
    fs.mkdir("/home")
    fs.mkdir("/home/user")
    fs.mkdir("/home/user/documents")
    fs.mkdir("/home/user/pictures")

    # Create files
    fs.touch("/home/user/documents/report.txt", "This is my report content")
    fs.touch("/home/user/documents/notes.txt", "Important notes here")
    fs.touch("/home/user/pictures/vacation.jpg", "<binary image data>")

    # Print directory structure
    print("File system structure:")
    fs.print_tree()

    # List directory contents
    home_user_contents = fs.ls("/home/user")
    print(f"Contents of /home/user: {home_user_contents}")
    assert "documents" in home_user_contents, "Missing directory"
    assert "pictures" in home_user_contents, "Missing directory"

    # Check file content
    report_content = fs.cat("/home/user/documents/report.txt")
    print(f"Content of report.txt: {report_content}")
    assert report_content == "This is my report content", "File content mismatch"

    # Test navigation
    fs.cd("/home/user/documents")
    assert fs.current_path == "/home/user/documents", "CD command failed"

    # List current directory
    doc_contents = fs.ls()
    print(f"Contents of current directory: {doc_contents}")
    assert "report.txt" in doc_contents and "notes.txt" in doc_contents, "File listing incorrect"

    # Navigate up
    fs.cd("..")
    assert fs.current_path == "/home/user", "CD .. command failed"

    print("✅ All file system tests passed!")


def test_tree_challenges():
    """Test the tree challenge solutions."""
    print("\n🧩 Testing tree challenges...")

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
    print("Testing tree height...")
    assert tree_height(
        normal_tree) == 2, f"Expected height 2, got {tree_height(normal_tree)}"
    assert tree_height(empty_tree) == - \
        1, f"Expected height -1, got {tree_height(empty_tree)}"
    assert tree_height(
        single_node) == 0, f"Expected height 0, got {tree_height(single_node)}"
    assert tree_height(
        unbalanced) == 3, f"Expected height 3, got {tree_height(unbalanced)}"

    # Test Challenge 2: Count Leaves
    print("Testing leaf count...")
    assert count_leaves(
        normal_tree) == 3, f"Expected 3 leaves, got {count_leaves(normal_tree)}"
    assert count_leaves(
        empty_tree) == 0, f"Expected 0 leaves, got {count_leaves(empty_tree)}"
    assert count_leaves(
        single_node) == 1, f"Expected 1 leaf, got {count_leaves(single_node)}"
    assert count_leaves(
        unbalanced) == 1, f"Expected 1 leaf, got {count_leaves(unbalanced)}"

    # Test Challenge 3: Tree Mirroring
    print("Testing tree mirroring...")
    normal_copy = create_sample_tree()
    normal_inorder_before = BinaryTree(
        normal_copy).inorder_traversal(normal_copy)

    mirrored = mirror_tree(normal_copy)
    normal_inorder_after = BinaryTree(mirrored).inorder_traversal(mirrored)

    # Inorder traversal of mirrored tree should be reverse of original
    assert normal_inorder_after == list(
        reversed(normal_inorder_before)), "Mirror function failed"

    # Test Challenge 4: Level Order Traversal
    print("Testing level order traversal...")
    assert level_order_traversal(normal_tree) == [
        1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], got {level_order_traversal(normal_tree)}"
    assert level_order_traversal(
        empty_tree) == [], f"Expected [], got {level_order_traversal(empty_tree)}"
    assert level_order_traversal(single_node) == [
        1], f"Expected [1], got {level_order_traversal(single_node)}"

    # Test Challenge 5: Is Balanced
    print("Testing balance check...")
    assert is_balanced(normal_tree) == True, "Normal tree should be balanced"
    assert is_balanced(empty_tree) == True, "Empty tree should be balanced"
    assert is_balanced(
        single_node) == True, "Single node tree should be balanced"
    assert is_balanced(
        unbalanced) == False, "Unbalanced tree should be unbalanced"

    print("✅ All tree challenges tests passed!")


# ========================================================================================
# 7. Main Execution
# ========================================================================================

def run_all_tests():
    """Run all tests for the advanced binary trees implementation."""
    print("🌳 ADVANCED BINARY TREES - TEST SUITE 🌳")
    print("=======================================")

    # Test basic tree implementation
    test_basic_binary_tree()

    # Test specialized tree implementations
    test_binary_search_tree()
    test_avl_tree()

    # Test practical applications
    test_expression_tree()
    test_huffman_coding()
    test_file_system()

    # Test tree challenges
    test_tree_challenges()

    print("\n🎉 ALL TESTS COMPLETED SUCCESSFULLY! 🎉")


if __name__ == "__main__":
    run_all_tests()
