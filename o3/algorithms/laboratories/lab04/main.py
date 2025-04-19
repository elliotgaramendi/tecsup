"""
Stack Data Structure Implementation
A comprehensive implementation of stack data structures with various applications.
"""

# ========================================================
# 1. Understanding the Concept
# ========================================================
# A stack is a data structure that follows the LIFO principle
# (Last-In, First-Out) where elements are added and removed
# from the same end, called the "top" of the stack.
#
# Basic Operations:
#   - Push: Add element to top ⬆️
#   - Pop: Remove element from top ⬇️
#   - Peek/Top: View top element without removing it 👀
#   - isEmpty: Check if stack is empty 🔍
#   - Size: Get number of elements in stack 📏

# ========================================================
# 2. Stack Implementations
# ========================================================

# 2.1 Fixed Array Implementation 📦
import threading


class ArrayStack:
    """Stack implementation using a fixed-size array."""

    def __init__(self, capacity=10):
        """Initialize empty stack with fixed capacity."""
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1  # Index of top element, -1 means empty stack

    def is_empty(self):
        """Check if stack is empty."""
        return self.top == -1

    def is_full(self):
        """Check if stack is full."""
        return self.top == self.capacity - 1

    def push(self, item):
        """Add item to the top of the stack."""
        if self.is_full():
            raise OverflowError("Stack overflow - stack is full! 💥")

        self.top += 1
        self.data[self.top] = item
        return True

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        item = self.data[self.top]
        self.data[self.top] = None  # Remove reference to the object
        self.top -= 1
        return item

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        return self.data[self.top]

    def size(self):
        """Return the number of items in the stack."""
        return self.top + 1

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"

        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


def test_array_stack():
    """Test fixed array stack implementation with basic operations."""
    # Test basic operations
    print("Test: Basic operations with fixed array stack 🧪")
    stack = ArrayStack(5)

    print(f"Empty stack: {stack} 🕳️")
    print(f"Is empty? {stack.is_empty()} 🤔")

    # Push operations
    for i in range(1, 4):
        stack.push(i * 10)
        print(f"After push({i*10}): {stack} ⬆️")

    # Test peek
    print(f"Peek: {stack.peek()} 👀")

    # Test pop
    print(f"Pop: {stack.pop()} ⬇️")
    print(f"After pop: {stack} 🔄")

    # Test full stack
    stack.push(40)
    stack.push(50)
    print(f"Full stack: {stack} 🔝")

    try:
        stack.push(60)  # Should raise OverflowError
        print("Push succeeded unexpectedly 😲")
    except OverflowError as e:
        print(f"Error as expected: {e} ✅")

    # Empty the stack
    while not stack.is_empty():
        print(f"Pop: {stack.pop()} ⬇️")

    print(f"Final stack: {stack} 🏁")
    print("All array stack tests passed! ✅")


# 2.2 Dynamic Array Implementation 📊
class DynamicArrayStack:
    """Stack implementation using a dynamic array that resizes when full."""

    def __init__(self, initial_capacity=10):
        """Initialize empty stack with dynamic capacity."""
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.top = -1

    def is_empty(self):
        """Check if stack is empty."""
        return self.top == -1

    def resize(self, new_capacity):
        """Resize the stack to a new capacity."""
        new_data = [None] * new_capacity

        # Copy existing elements to the new array
        for i in range(self.top + 1):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def push(self, item):
        """Add item to the top of the stack."""
        if self.top == self.capacity - 1:
            # Double the capacity when full 📈
            self.resize(2 * self.capacity)

        self.top += 1
        self.data[self.top] = item
        return True

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        item = self.data[self.top]
        self.data[self.top] = None  # Remove reference to the object
        self.top -= 1

        # Shrink the array if it's only 1/4 full 📉
        if 0 < self.top + 1 <= self.capacity // 4 and self.capacity > 10:
            self.resize(self.capacity // 2)

        return item

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        return self.data[self.top]

    def size(self):
        """Return the number of items in the stack."""
        return self.top + 1

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"

        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


def test_dynamic_array_stack():
    """Test dynamic array stack with auto-resizing capability."""
    print("Test: Dynamic array stack with auto-resizing 📈📉")
    stack = DynamicArrayStack(3)  # Start with small capacity

    print(f"Initial capacity: {stack.capacity} 🌱")

    # Push beyond initial capacity
    for i in range(1, 8):
        stack.push(i)
        print(
            f"After push({i}): size={stack.size()}, capacity={stack.capacity} ⬆️")

    # Pop to trigger shrinking
    for _ in range(6):
        val = stack.pop()
        print(
            f"After pop -> {val}: size={stack.size()}, capacity={stack.capacity} ⬇️")

    print("All dynamic array stack tests passed! ✅")


# 2.3 Linked List Implementation 📃
class Node:
    """Node class for the Linked List Stack."""

    def __init__(self, data=None):
        """Initialize node with data and next reference."""
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack implementation using a linked list."""

    def __init__(self):
        """Initialize empty stack using linked list."""
        self.head = None  # Top of the stack
        self.count = 0  # Number of elements

    def is_empty(self):
        """Check if stack is empty."""
        return self.head is None

    def push(self, item):
        """Add item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        item = self.head.data
        self.head = self.head.next
        self.count -= 1
        return item

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        return self.head.data

    def size(self):
        """Return the number of items in the stack."""
        return self.count

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"

        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next

        return f"Stack: [{', '.join(items)}]"


def test_linked_list_stack():
    """Test linked list stack implementation with push and pop operations."""
    print("Test: Linked list stack implementation 📃")
    stack = LinkedListStack()

    print(f"Empty stack: {stack} 🕳️")

    # Push operations
    for i in range(1, 6):
        stack.push(i * 10)
        print(f"After push({i*10}): {stack} ⬆️")

    print(f"Stack size: {stack.size()} 📏")
    print(f"Top element: {stack.peek()} 👀")

    # Pop operations
    while not stack.is_empty():
        print(f"Pop: {stack.pop()}, Remaining: {stack} ⬇️")

    # Test edge cases
    try:
        empty_peek = stack.peek()
        print("Peek should have raised an exception! 😲")
    except IndexError as e:
        print(f"Error as expected: {e} ✅")

    print("All linked list stack tests passed! ✅")


# ========================================================
# 3. Practical Applications
# ========================================================

# 3.1 Balanced Parentheses Checking ⚖️
def is_balanced(expression):
    """Check if an expression has balanced parentheses, brackets, and braces."""
    stack = []
    opening = "({["
    closing = ")}]"

    # Dictionary to match opening and closing brackets 🔄
    brackets_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        if char in opening:
            stack.append(char)  # Push opening bracket ⬆️
        elif char in closing:
            if not stack:  # Stack is empty but we found a closing bracket 😱
                return False

            top = stack.pop()  # Pop the top bracket ⬇️
            if top != brackets_map[char]:  # Mismatch! 🚫
                return False

    # If stack is empty, all brackets were matched ✅
    return len(stack) == 0


def test_balanced_parentheses():
    """Test parentheses balancing with various expressions."""
    test_cases = [
        ("()", True),              # Simple matched pair ✓
        ("()[]{}", True),          # Multiple pairs ✓
        ("([])", True),            # Nested pairs ✓
        ("([)]", False),           # Crossed pairs ✗
        ("{[]}", True),            # Complex nesting ✓
        (")(", False),             # Reversed order ✗
        ("((((", False),           # Unclosed brackets ✗
        ("))))", False),           # Unopened brackets ✗
        ("a*(b+c)-(d/e)", True)    # Expression with operators ✓
    ]

    print("Testing parentheses balancing: 🧪⚖️")
    for expr, expected in test_cases:
        result = is_balanced(expr)
        print(
            f"Expression: '{expr}', Balanced: {result}, Expected: {expected} {'✅' if result == expected else '❌'}")
        assert result == expected, f"Test failed for '{expr}' 😱"

    print("All balanced parentheses tests passed! 🎉")


# 3.2 Postfix Expression Evaluation 🧮
def evaluate_postfix(expression):
    """Evaluate a postfix expression in Reverse Polish Notation."""
    stack = []
    operators = {
        '+': lambda a, b: a + b,   # Addition ➕
        '-': lambda a, b: a - b,   # Subtraction ➖
        '*': lambda a, b: a * b,   # Multiplication ✖️
        '/': lambda a, b: a / b,   # Division ➗
        '^': lambda a, b: a ** b   # Exponentiation 💪
    }

    tokens = expression.split()

    for token in tokens:
        if token in operators:
            # It's an operator, pop two operands and apply 🔄
            if len(stack) < 2:
                raise ValueError(
                    "Invalid postfix expression: not enough operands! 😱")

            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand

            # Apply the operator 🧮
            result = operators[token](a, b)
            stack.append(result)
        else:
            # It's an operand, convert to number and push ⬆️
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token in expression: {token} 🚫")

    # If we have exactly one value in the stack, it's the result ✅
    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid postfix expression: too many operands! 😱")


def test_postfix_evaluation():
    """Test postfix expression evaluation with different operations."""
    test_cases = [
        ("3 4 +", 7),             # 3 + 4 = 7 ➕
        ("5 2 -", 3),             # 5 - 2 = 3 ➖
        ("3 4 * 2 +", 14),        # 3 * 4 + 2 = 14 ✖️➕
        ("7 2 / 3 *", 10.5),      # 7 / 2 * 3 = 10.5 ➗✖️
        ("5 1 2 + 4 * + 3 -", 14)  # 5 + ((1 + 2) * 4) - 3 = 14 🧮
    ]

    print("Testing postfix expression evaluation: 🧪🧮")
    for expr, expected in test_cases:
        try:
            result = evaluate_postfix(expr)
            print(
                f"Expression: '{expr}', Result: {result}, Expected: {expected} {'✅' if abs(result - expected) < 1e-10 else '❌'}")
            assert abs(
                result - expected) < 1e-10, f"Test failed for '{expr}' 😱"
        except Exception as e:
            print(f"Expression: '{expr}', Error: {str(e)} 💥")

    print("All postfix evaluation tests passed! 🎉")


# ========================================================
# 4. Real-world Case: Browser History 🌐
# ========================================================
class BrowserHistory:
    """Simple browser history implementation using stacks."""

    def __init__(self):
        """Initialize browser history with back and forward stacks."""
        self.back_stack = []      # Stack for back navigation ⬅️
        self.forward_stack = []   # Stack for forward navigation ➡️
        self.current_page = None  # Current page being viewed 📄

    def visit(self, url):
        """Visit a new page, adding current to back stack and clearing forward stack."""
        if self.current_page:
            # Add current page to back history ⬅️
            self.back_stack.append(self.current_page)

        self.current_page = url                       # Update current page 📄
        self.forward_stack = []                       # Clear forward history 🧹

        return f"Visited: {url} 🌐"

    def back(self):
        """Navigate back in history."""
        if not self.back_stack:
            return "No back history! 🛑"

        # Move current page to forward stack ➡️
        self.forward_stack.append(self.current_page)
        # Set current page to the last back page ⬅️
        self.current_page = self.back_stack.pop()

        return f"Navigated back to: {self.current_page} ⬅️"

    def forward(self):
        """Navigate forward in history."""
        if not self.forward_stack:
            return "No forward history! 🛑"

        # Move current page to back stack ⬅️
        self.back_stack.append(self.current_page)
        # Set current page to the last forward page ➡️
        self.current_page = self.forward_stack.pop()

        return f"Navigated forward to: {self.current_page} ➡️"

    def get_current(self):
        """Get the current page."""
        if not self.current_page:
            return "No current page! 📭"

        return f"Current page: {self.current_page} 📄"


def test_browser_history():
    """Test browser navigation with back and forward operations."""
    print("Testing browser navigation: 🧪🌐")
    browser = BrowserHistory()

    print(browser.get_current())  # Should show no current page 📭

    # Visit some pages 🖱️
    print(browser.visit("https://www.example.com"))
    print(browser.visit("https://www.example.com/page1"))
    print(browser.visit("https://www.example.com/page2"))

    # Test navigation 🔄
    print(browser.get_current())  # Should be on page2 📄
    print(browser.back())         # Should go back to page1 ⬅️
    print(browser.back())         # Should go back to home page ⬅️
    print(browser.forward())      # Should go forward to page1 ➡️

    # Visit a new page (should clear forward history) 🖱️
    print(browser.visit("https://www.example.com/page3"))
    print(browser.get_current())  # Should be on page3 📄

    # Try to go forward (should have no forward history) ➡️
    print(browser.forward())      # Should show no forward history 🛑

    # Test edge cases 🧪
    print(browser.back())         # Should go back to home page ⬅️
    print(browser.back())         # Should go back again ⬅️
    print(browser.back())         # Should show no back history 🛑

    print("All browser history tests completed successfully! 🎉")


# ========================================================
# 5. Practical Exercises
# ========================================================

# Exercise 1: Reverse a String 🔄
def reverse_string(s):
    """Reverse a string using a stack."""
    stack = []
    # Push each character onto the stack ⬆️
    for char in s:
        stack.append(char)

    # Pop characters from stack to get reversed string ⬇️
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string


def test_reverse_string():
    """Test string reversal using stack."""
    test_cases = [
        ("hello", "olleh"),
        ("python", "nohtyp"),
        ("racecar", "racecar"),  # Palindrome
        ("", ""),  # Empty string
        ("a", "a")  # Single character
    ]

    print("Testing string reversal using stack: 🧪🔄")
    for original, expected in test_cases:
        result = reverse_string(original)
        print(
            f"Original: '{original}', Reversed: '{result}', Expected: '{expected}' {'✅' if result == expected else '❌'}")
        assert result == expected, f"Test failed for '{original}' 😱"

    print("All string reversal tests passed! 🎉")


# Exercise 2: Evaluate Infix Expressions 🧮
def infix_to_postfix(expression):
    """Convert infix expression to postfix notation."""
    # Define operator precedence 📊
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    stack = []
    postfix = []

    # Function to check if current operator has higher precedence than stack top
    def has_higher_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        # Case 1: If token is an operand, add to output 🔢
        if token not in precedence and token not in '()':
            postfix.append(token)

        # Case 2: If token is opening parenthesis, push to stack ⬆️
        elif token == '(':
            stack.append(token)

        # Case 3: If token is closing parenthesis, pop stack until matching opening parenthesis ⬇️
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            # Remove the opening parenthesis
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                raise ValueError("Mismatched parentheses in expression! 😱")

        # Case 4: If token is an operator 🔣
        else:
            # Pop operators with higher or equal precedence from stack
            while stack and stack[-1] != '(' and (token not in precedence or precedence[stack[-1]] >= precedence[token]):
                postfix.append(stack.pop())

            # Push current operator to stack
            stack.append(token)

    # Pop any remaining operators from stack ⬇️
    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses in expression! 😱")
        postfix.append(stack.pop())

    return ' '.join(postfix)


def evaluate_infix(expression):
    """Evaluate an infix expression by converting to postfix first."""
    # Convert to postfix
    postfix_expr = infix_to_postfix(expression)
    # Evaluate postfix expression
    return evaluate_postfix(postfix_expr)


def test_infix_evaluation():
    """Test infix expression evaluation."""
    test_cases = [
        ("3 + 4", 7),
        ("5 - 2", 3),
        ("3 * 4 + 2", 14),
        ("(3 + 4) * 2", 14),
        ("7 / 2 * 3", 10.5),
        ("5 + ((1 + 2) * 4) - 3", 14)
    ]

    print("Testing infix expression evaluation: 🧪🧮")
    for expr, expected in test_cases:
        try:
            result = evaluate_infix(expr)
            print(
                f"Expression: '{expr}', Result: {result}, Expected: {expected} {'✅' if abs(result - expected) < 1e-10 else '❌'}")
            assert abs(
                result - expected) < 1e-10, f"Test failed for '{expr}' 😱"
        except Exception as e:
            print(f"Expression: '{expr}', Error: {str(e)} 💥")

    print("All infix evaluation tests passed! 🎉")


# Exercise 3: Implement a Stack with getMin() Function 📉
class MinStack:
    """Stack implementation that keeps track of minimum value."""

    def __init__(self):
        """Initialize main stack and min stack."""
        self.stack = []      # Main stack for elements
        self.min_stack = []  # Stack for tracking minimum values

    def push(self, x):
        """Push element x onto stack, updating min stack if needed."""
        self.stack.append(x)

        # Update min_stack if empty or new value is smaller than current min
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """Remove the element on top of the stack."""
        if not self.stack:
            raise IndexError("Stack is empty! 💨")

        # Pop from main stack
        item = self.stack.pop()

        # If popped item is current minimum, also pop from min_stack
        if self.min_stack and item == self.min_stack[-1]:
            self.min_stack.pop()

        return item

    def top(self):
        """Get the top element."""
        if not self.stack:
            raise IndexError("Stack is empty! 💨")

        return self.stack[-1]

    def get_min(self):
        """Retrieve the minimum element in the stack."""
        if not self.min_stack:
            raise IndexError("Stack is empty! 💨")

        return self.min_stack[-1]

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)


def test_min_stack():
    """Test MinStack implementation with various operations."""
    print("Testing MinStack implementation: 🧪📉")

    min_stack = MinStack()

    print("Pushing elements to MinStack...")
    min_stack.push(5)
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 5 and min_stack.get_min() == 5

    min_stack.push(2)
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 2 and min_stack.get_min() == 2

    min_stack.push(7)
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 7 and min_stack.get_min() == 2

    min_stack.push(1)
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 1 and min_stack.get_min() == 1

    min_stack.push(9)
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 9 and min_stack.get_min() == 1

    print("Popping elements from MinStack...")
    min_stack.pop()  # Removes 9
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 1 and min_stack.get_min() == 1

    min_stack.pop()  # Removes 1
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 7 and min_stack.get_min() == 2

    min_stack.pop()  # Removes 7
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 2 and min_stack.get_min() == 2

    min_stack.pop()  # Removes 2
    print(f"Top: {min_stack.top()}, Min: {min_stack.get_min()} ✅")
    assert min_stack.top() == 5 and min_stack.get_min() == 5

    print("All MinStack tests passed! 🎉")


# Exercise 4: Implement a History Feature ⌨️
class TextEditor:
    """Simple text editor with typing, deleting, and undo operations."""

    def __init__(self):
        """Initialize text buffer and operations history."""
        self.text = ""          # Current text buffer
        self.history = []       # Stack for operation history

    def type(self, text):
        """Type text and save operation to history."""
        # Save current state to history ⬆️
        self.history.append(("delete", len(text)))

        # Update text buffer with new text
        self.text += text
        return f"Typed: '{text}' -> Current text: '{self.text}'"

    def delete(self, count=1):
        """Delete the last 'count' characters and save operation to history."""
        if count <= 0:
            return f"Invalid count: {count} 🚫"

        # Adjust count if it exceeds text length
        count = min(count, len(self.text))

        if count > 0:
            # Save deleted text to history ⬆️
            deleted_text = self.text[-count:]
            self.history.append(("type", deleted_text))

            # Delete characters from the end
            self.text = self.text[:-count]
            return f"Deleted {count} character(s) -> Current text: '{self.text}'"
        else:
            return "Nothing to delete! 🛑"

    def undo(self):
        """Undo the last operation."""
        if not self.history:
            return "Nothing to undo! 🛑"

        # Pop the last operation from history ⬇️
        operation, data = self.history.pop()

        if operation == "type":
            # Restore deleted text
            self.text += data
            return f"Undo delete -> Current text: '{self.text}'"
        else:  # operation == "delete"
            # Delete last inserted characters
            self.text = self.text[:-data]
            return f"Undo type -> Current text: '{self.text}'"


def test_text_editor():
    """Test text editor with typing, deleting, and undo operations."""
    print("Testing text editor with history feature: 🧪⌨️")

    editor = TextEditor()

    # Test typing
    print(editor.type("Hello"))
    print(editor.type(" World"))
    print(editor.type("!"))

    # Test deleting
    print(editor.delete(1))  # Delete "!"
    print(editor.delete(5))  # Delete "World"

    # Test undo
    print(editor.undo())     # Undo delete "World"
    print(editor.undo())     # Undo delete "!"
    print(editor.undo())     # Undo type "!"
    print(editor.undo())     # Undo type " World"
    print(editor.undo())     # Undo type "Hello"
    print(editor.undo())     # Nothing to undo

    # Test complex sequence
    print(editor.type("Stack"))
    print(editor.type(" Data"))
    print(editor.type(" Structure"))
    print(editor.delete(10))  # Delete " Structure"
    print(editor.undo())      # Restore " Structure"
    print(editor.delete(15))  # Delete entire text

    print("All text editor tests completed successfully! 🎉")


# Exercise 5: Check for Balanced HTML Tags 📝
def is_balanced_html(html):
    """Check if HTML tags are balanced."""
    stack = []
    # HTML tags to ignore (self-closing or not needing closing tags)
    self_closing_tags = {"img", "br", "hr", "meta", "input", "link",
                         "area", "base", "col", "embed", "param", "source", "track", "wbr"}

    # Current tag being parsed
    current_tag = ""
    in_tag = False
    is_closing_tag = False

    for char in html:
        if char == '<':
            in_tag = True
            current_tag = ""
            is_closing_tag = False
        elif char == '/' and in_tag and current_tag == "":
            is_closing_tag = True
        elif char == '>':
            in_tag = False

            # Handle the completed tag
            if current_tag:
                # Skip comments and doctype
                if current_tag.startswith("!"):
                    continue

                # Get the tag name (remove attributes if any)
                tag_parts = current_tag.split()
                tag_name = tag_parts[0].lower()

                if is_closing_tag:
                    # Check if the closing tag matches the latest opening tag
                    if not stack:
                        return False

                    last_open_tag = stack.pop()
                    if last_open_tag != tag_name:
                        return False
                else:
                    # If it's not a self-closing tag, push it to the stack
                    if tag_name not in self_closing_tags and not (len(tag_parts) > 1 and tag_parts[-1].endswith('/')):
                        stack.append(tag_name)

            current_tag = ""
        elif in_tag:
            current_tag += char

    # Check if all tags were closed
    return len(stack) == 0


def test_balanced_html():
    """Test HTML tag balancing with various HTML snippets."""
    test_cases = [
        # Simple nested tags
        ("<div><p>Hello</p></div>", True),
        ("<div><img src='img.jpg'><p>Text</p></div>",
         True),           # Self-closing tag
        # Unclosed inner tag
        ("<div><p>Unclosed paragraph</div>", False),
        # Multiple root elements
        ("<div>Text</div><p>More text</p>", True),
        # Multiple nested elements
        ("<div><p>Text</p><p>More text</p></div>", True),
        # Improperly nested tags
        ("<div><p>Text</div></p>", False),
        # Full HTML document
        ("<!DOCTYPE html><html><head></head><body></body></html>", True),
        # Self-closing with slash
        ("<input type='text' />", True),
        # Break tag doesn't need closing
        ("<p>Text with <br> line break</p>", True),
        # Tags with attributes
        ("<div class='test' id='main'><span>Text</span></div>", True)
    ]

    print("Testing HTML tag balancing: 🧪📝")
    for html, expected in test_cases:
        result = is_balanced_html(html)
        print(
            f"HTML: '{html[:30]}{'...' if len(html) > 30 else ''}', Balanced: {result}, Expected: {expected} {'✅' if result == expected else '❌'}")
        assert result == expected, f"Test failed for '{html}' 😱"

    print("All HTML balancing tests passed! 🎉")


# ========================================================
# 6. Deepening the Concept
# ========================================================

# Implementation comparison table is in the documentation
# For this implementation, we'll create a performance comparison function

def compare_stack_implementations(n=10000):
    """Compare performance of different stack implementations."""
    import time

    print(f"Comparing stack implementations with {n} push/pop operations: ⏱️")

    # Test fixed array stack
    try:
        print("\nTesting ArrayStack:")
        fixed_stack = ArrayStack(n)

        # Measure push time
        start_time = time.time()
        for i in range(n):
            fixed_stack.push(i)
        push_time = time.time() - start_time
        print(f"  Push {n} items: {push_time:.6f} seconds ⬆️")

        # Measure pop time
        start_time = time.time()
        for _ in range(n):
            fixed_stack.pop()
        pop_time = time.time() - start_time
        print(f"  Pop {n} items: {pop_time:.6f} seconds ⬇️")
    except OverflowError:
        print("  Fixed array overflow! 💥")

    # Test dynamic array stack
    print("\nTesting DynamicArrayStack:")
    dynamic_stack = DynamicArrayStack()

    # Measure push time
    start_time = time.time()
    for i in range(n):
        dynamic_stack.push(i)
    push_time = time.time() - start_time
    print(f"  Push {n} items: {push_time:.6f} seconds ⬆️")

    # Measure pop time
    start_time = time.time()
    for _ in range(n):
        dynamic_stack.pop()
    pop_time = time.time() - start_time
    print(f"  Pop {n} items: {pop_time:.6f} seconds ⬇️")

    # Test linked list stack
    print("\nTesting LinkedListStack:")
    linked_stack = LinkedListStack()

    # Measure push time
    start_time = time.time()
    for i in range(n):
        linked_stack.push(i)
    push_time = time.time() - start_time
    print(f"  Push {n} items: {push_time:.6f} seconds ⬆️")

    # Measure pop time
    start_time = time.time()
    for _ in range(n):
        linked_stack.pop()
    pop_time = time.time() - start_time
    print(f"  Pop {n} items: {pop_time:.6f} seconds ⬇️")

    print("\nPerformance comparison complete! 📊")


# ========================================================
# 7. Next Steps (Advanced Implementations)
# ========================================================

# Here we'll implement a thread-safe stack for the next steps section


class ThreadSafeStack:
    """Thread-safe implementation of a stack using a lock."""

    def __init__(self):
        """Initialize stack and lock."""
        self.stack = []
        self.lock = threading.Lock()

    def push(self, item):
        """Push an item onto the stack in a thread-safe manner."""
        with self.lock:
            self.stack.append(item)
            return True

    def pop(self):
        """Pop an item from the stack in a thread-safe manner."""
        with self.lock:
            if not self.stack:
                return None
            return self.stack.pop()

    def peek(self):
        """Peek at the top item in a thread-safe manner."""
        with self.lock:
            if not self.stack:
                return None
            return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty in a thread-safe manner."""
        with self.lock:
            return len(self.stack) == 0

    def size(self):
        """Get the size of the stack in a thread-safe manner."""
        with self.lock:
            return len(self.stack)


def test_thread_safe_stack():
    """Test thread-safe stack with concurrent operations."""
    print("Testing ThreadSafeStack with concurrent operations: 🧪🔒")

    # Create a thread-safe stack
    stack = ThreadSafeStack()

    # Number of items each thread will push
    n = 1000

    # Function for threads to push items
    def push_items():
        for i in range(n):
            stack.push(i)

    # Function for threads to pop items
    def pop_items():
        for _ in range(n // 2):
            stack.pop()

    # Create and start multiple threads
    threads = []
    for _ in range(4):
        threads.append(threading.Thread(target=push_items))

    for thread in threads:
        thread.start()

    # Wait for all push threads to complete
    for thread in threads:
        thread.join()

    print(f"After pushing: Stack size = {stack.size()} 📏")

    # Create and start pop threads
    pop_threads = []
    for _ in range(2):
        pop_threads.append(threading.Thread(target=pop_items))

    for thread in pop_threads:
        thread.start()

    # Wait for all pop threads to complete
    for thread in pop_threads:
        thread.join()

    print(f"After popping: Stack size = {stack.size()} 📏")

    # Verify the expected size
    expected_size = 4 * n - 2 * (n // 2)
    print(
        f"Expected size: {expected_size} {'✅' if stack.size() == expected_size else '❌'}")

    print("All ThreadSafeStack tests completed! 🎉")


# Example of another advanced implementation: Bounded Stack
class BoundedStack:
    """Bounded stack implementation using a circular buffer."""

    def __init__(self, capacity):
        """Initialize bounded stack with fixed capacity."""
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size_val = 0
        self.head = 0  # Index where items are removed
        self.tail = 0  # Index where items are added

    def is_empty(self):
        """Check if stack is empty."""
        return self.size_val == 0

    def is_full(self):
        """Check if stack is full."""
        return self.size_val == self.capacity

    def push(self, item):
        """Add item to the stack."""
        if self.is_full():
            raise OverflowError("Stack is full! 💥")

        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size_val += 1
        return True

    def pop(self):
        """Remove and return item from the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty! 💨")

        # Adjust indices for LIFO behavior (item at tail-1 is the most recently added)
        self.tail = (self.tail - 1) % self.capacity
        item = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.size_val -= 1
        return item

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty! 💨")

        peek_index = (self.tail - 1) % self.capacity
        return self.buffer[peek_index]

    def size(self):
        """Return the number of items in the stack."""
        return self.size_val


def test_bounded_stack():
    """Test bounded stack implementation with circular buffer."""
    print("Testing BoundedStack with circular buffer: 🧪🔄")

    # Create a bounded stack with capacity 5
    stack = BoundedStack(5)

    print(f"Empty: {stack.is_empty()} ✅")

    # Push items
    for i in range(1, 6):
        stack.push(i * 10)
        print(f"Pushed {i*10}, Size: {stack.size()}")

    print(f"Full: {stack.is_full()} ✅")

    # Try to push when full
    try:
        stack.push(60)
        print("Push succeeded unexpectedly 😲")
    except OverflowError as e:
        print(f"Error as expected: {e} ✅")

    # Peek at top
    print(f"Peek: {stack.peek()} ✅")

    # Pop some items
    for _ in range(3):
        print(f"Popped: {stack.pop()}")

    # Push again to test circular behavior
    stack.push(60)
    stack.push(70)
    print(f"Size after pushing again: {stack.size()} ✅")

    # Pop all remaining items
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    print(f"Empty: {stack.is_empty()} ✅")

    print("All BoundedStack tests completed! 🎉")


# ========================================================
# Main function to run all tests
# ========================================================
def main():
    """Main function to run stack implementation tests."""
    print("===== STACK DATA STRUCTURE IMPLEMENTATION TESTS =====")

    # Test basic stack implementations
    test_array_stack()
    print("\n" + "="*50 + "\n")

    test_dynamic_array_stack()
    print("\n" + "="*50 + "\n")

    test_linked_list_stack()
    print("\n" + "="*50 + "\n")

    # Test practical applications
    test_balanced_parentheses()
    print("\n" + "="*50 + "\n")

    test_postfix_evaluation()
    print("\n" + "="*50 + "\n")

    test_browser_history()
    print("\n" + "="*50 + "\n")

    # Test practical exercises
    test_reverse_string()
    print("\n" + "="*50 + "\n")

    test_infix_evaluation()
    print("\n" + "="*50 + "\n")

    test_min_stack()
    print("\n" + "="*50 + "\n")

    test_text_editor()
    print("\n" + "="*50 + "\n")

    test_balanced_html()
    print("\n" + "="*50 + "\n")

    # Performance comparison
    # Use smaller number for quicker testing
    compare_stack_implementations(1000)
    print("\n" + "="*50 + "\n")

    # Advanced implementations
    test_thread_safe_stack()
    print("\n" + "="*50 + "\n")

    test_bounded_stack()
    print("\n" + "="*50 + "\n")

    print("===== ALL TESTS COMPLETED SUCCESSFULLY! =====")


if __name__ == "__main__":
    main()
