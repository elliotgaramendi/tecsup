"""
Stack Data Structure - Complete Implementation
==============================================
This file contains implementations of the Stack data structure
using different approaches, along with practical applications.

Author: Elliot Garamendi
Date: April 7, 2025
"""

import unittest
from typing import Any, List, Dict, Callable, Optional, TypeVar, Generic
import re

T = TypeVar('T')

# ======================================================
# 1. STACK IMPLEMENTATIONS
# ======================================================


class ArrayStack:
    """Stack implementation using a fixed-size array. 📦"""

    def __init__(self, capacity: int = 10) -> None:
        """Initialize empty stack with fixed capacity. 🏗️"""
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1  # Index of top element, -1 means empty stack

    def is_empty(self) -> bool:
        """Check if stack is empty. 🕳️"""
        return self.top == -1

    def is_full(self) -> bool:
        """Check if stack is full. 🔝"""
        return self.top == self.capacity - 1

    def push(self, item: Any) -> bool:
        """Add item to the top of the stack. ⬆️"""
        if self.is_full():
            raise OverflowError("Stack overflow - stack is full! 💥")

        self.top += 1
        self.data[self.top] = item
        return True

    def pop(self) -> Any:
        """Remove and return the top item from the stack. ⬇️"""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        item = self.data[self.top]
        self.data[self.top] = None  # Remove reference to the object
        self.top -= 1
        return item

    def peek(self) -> Any:
        """Return the top item without removing it. 👀"""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        return self.data[self.top]

    def size(self) -> int:
        """Return the number of items in the stack. 📏"""
        return self.top + 1

    def __str__(self) -> str:
        """Return a string representation of the stack. 📝"""
        if self.is_empty():
            return "Stack: []"

        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


class DynamicArrayStack(Generic[T]):
    """Stack implementation using a dynamic array that resizes when full. 📊"""

    def __init__(self, initial_capacity: int = 10) -> None:
        """Initialize empty stack with dynamic capacity. 🌱"""
        self.data: List[Optional[T]] = [None] * initial_capacity
        self.capacity = initial_capacity
        self.top = -1

    def is_empty(self) -> bool:
        """Check if stack is empty. 🕳️"""
        return self.top == -1

    def resize(self, new_capacity: int) -> None:
        """Resize the stack to a new capacity. 📏↔️📐"""
        new_data: List[Optional[T]] = [None] * new_capacity

        # Copy existing elements to the new array
        for i in range(self.top + 1):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def push(self, item: T) -> bool:
        """Add item to the top of the stack. ⬆️"""
        if self.top == self.capacity - 1:
            # Double the capacity when full 📈
            self.resize(2 * self.capacity)

        self.top += 1
        self.data[self.top] = item
        return True

    def pop(self) -> T:
        """Remove and return the top item from the stack. ⬇️"""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        item = self.data[self.top]
        self.data[self.top] = None  # Remove reference to the object
        self.top -= 1

        # Shrink the array if it's only 1/4 full 📉
        if 0 < self.top + 1 <= self.capacity // 4 and self.capacity > 10:
            self.resize(self.capacity // 2)

        return item  # type: ignore

    def peek(self) -> T:
        """Return the top item without removing it. 👀"""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        return self.data[self.top]  # type: ignore

    def size(self) -> int:
        """Return the number of items in the stack. 📏"""
        return self.top + 1

    def __str__(self) -> str:
        """Return a string representation of the stack. 📝"""
        if self.is_empty():
            return "Stack: []"

        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


class Node(Generic[T]):
    """Node class for the Linked List Stack. 🧩"""

    def __init__(self, data: Optional[T] = None) -> None:
        """Initialize node with data and next reference. 🏗️"""
        self.data = data
        self.next: Optional['Node[T]'] = None


class LinkedListStack(Generic[T]):
    """Stack implementation using a linked list. 📃"""

    def __init__(self) -> None:
        """Initialize empty stack using linked list. 🌱"""
        self.head: Optional[Node[T]] = None  # Top of the stack
        self.count = 0  # Number of elements

    def is_empty(self) -> bool:
        """Check if stack is empty. 🕳️"""
        return self.head is None

    def push(self, item: T) -> bool:
        """Add item to the top of the stack. ⬆️"""
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True

    def pop(self) -> T:
        """Remove and return the top item from the stack. ⬇️"""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        item = self.head.data
        self.head = self.head.next
        self.count -= 1
        return item  # type: ignore

    def peek(self) -> T:
        """Return the top item without removing it. 👀"""
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty! 💨")

        return self.head.data  # type: ignore

    def size(self) -> int:
        """Return the number of items in the stack. 📏"""
        return self.count

    def __str__(self) -> str:
        """Return a string representation of the stack. 📝"""
        if self.is_empty():
            return "Stack: []"

        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next

        return f"Stack: [{', '.join(items)}]"


# ======================================================
# 2. PRACTICAL APPLICATIONS
# ======================================================

def is_balanced(expression: str) -> bool:
    """Check if an expression has balanced parentheses, brackets, and braces. ⚖️"""
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


def evaluate_postfix(expression: str) -> float:
    """Evaluate a postfix expression in Reverse Polish Notation. 🧮"""
    stack: List[float] = []
    operators: Dict[str, Callable[[float, float], float]] = {
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


def infix_to_postfix(expression: str) -> str:
    """Convert infix expression to postfix notation. 🔄"""
    # Remove spaces and split expression into tokens
    expression = expression.replace(" ", "")
    tokens = []

    # Parse the expression into tokens
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Extract the full number
            num = ""
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(expression[i])
            i += 1

    # Operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    stack = []
    postfix = []

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            # It's a number, add to output
            postfix.append(token)
        elif token == '(':
            # Opening parenthesis, push to stack
            stack.append(token)
        elif token == ')':
            # Closing parenthesis, pop until matching opening parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            if stack and stack[-1] == '(':
                stack.pop()  # Remove the opening parenthesis
            else:
                raise ValueError("Mismatched parentheses in expression! 🚫")
        elif token in precedence:
            # It's an operator
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                postfix.append(stack.pop())

            stack.append(token)
        else:
            raise ValueError(f"Invalid token in expression: {token} 🚫")

    # Pop any remaining operators from the stack
    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses in expression! 🚫")
        postfix.append(stack.pop())

    return ' '.join(postfix)


def evaluate_infix(expression: str) -> float:
    """Evaluate an infix expression by converting to postfix first. 🧮"""
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)


class BrowserHistory:
    """Simple browser history implementation using stacks. 🌐"""

    def __init__(self) -> None:
        """Initialize browser history with back and forward stacks. 🏗️"""
        self.back_stack: List[str] = []      # Stack for back navigation ⬅️
        self.forward_stack: List[str] = []   # Stack for forward navigation ➡️
        self.current_page: Optional[str] = None  # Current page being viewed 📄

    def visit(self, url: str) -> str:
        """Visit a new page, adding current to back stack and clearing forward stack. 🖱️"""
        if self.current_page:
            # Add current page to back history ⬅️
            self.back_stack.append(self.current_page)

        self.current_page = url                       # Update current page 📄
        self.forward_stack = []                       # Clear forward history 🧹

        return f"Visited: {url} 🌐"

    def back(self) -> str:
        """Navigate back in history. ⬅️"""
        if not self.back_stack:
            return "No back history! 🛑"

        # Move current page to forward stack ➡️
        if self.current_page:
            self.forward_stack.append(self.current_page)
        # Set current page to the last back page ⬅️
        self.current_page = self.back_stack.pop()

        return f"Navigated back to: {self.current_page} ⬅️"

    def forward(self) -> str:
        """Navigate forward in history. ➡️"""
        if not self.forward_stack:
            return "No forward history! 🛑"

        # Move current page to back stack ⬅️
        if self.current_page:
            self.back_stack.append(self.current_page)
        # Set current page to the last forward page ➡️
        self.current_page = self.forward_stack.pop()

        return f"Navigated forward to: {self.current_page} ➡️"

    def get_current(self) -> str:
        """Get the current page. 📄"""
        if not self.current_page:
            return "No current page! 📭"

        return f"Current page: {self.current_page} 📄"


# ======================================================
# 3. PRACTICAL EXERCISES
# ======================================================

# -------------------------------------------------------
# Exercise 1: Reverse a String
# -------------------------------------------------------
# Time: O(n) where n is the length of the string
# Space: O(n) to store the string in the stack
# -------------------------------------------------------

def reverse_string(s: str) -> str:
    """
    Exercise 1: Use a stack to reverse a string.

    Approach:
    1. Iterate through each character of the original string and push it onto a stack
    2. Pop characters from the stack to form the reversed string

    Complexity:
    - Time: O(n) where n is the length of the string
    - Space: O(n) for storing the stack

    Args:
        s: String to reverse

    Returns:
        The reversed string 🔄📝
    """
    stack = []

    # Push each character onto the stack
    for char in s:
        stack.append(char)

    # Pop characters to get the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()

    return reversed_str


# -------------------------------------------------------
# Exercise 2: Evaluate Infix Expressions
# -------------------------------------------------------
# Included in section 2 (Practical Applications) as:
# - infix_to_postfix()
# - evaluate_infix()
#
# Time: O(n) where n is the length of the expression
# Space: O(n) for the stacks used in conversion
# -------------------------------------------------------


# -------------------------------------------------------
# Exercise 3: Implement a Stack with getMin() Function
# -------------------------------------------------------
# Time: O(1) for all operations
# Space: O(n) where n is the number of elements
# -------------------------------------------------------

class MinStack(Generic[T]):
    """
    Exercise 3: Stack with O(1) getMin() operation.

    Approach:
    - Uses two internal stacks: a main one for elements and
      an auxiliary one to track minimum values.
    - When an element less than or equal to the current minimum is added,
      it's also added to the min stack.
    - When an element that matches the current minimum is removed,
      it's also removed from the min stack.

    Complexity:
    - Time: O(1) for all operations (push, pop, top, getMin)
    - Space: O(n) where n is the number of elements in the stack

    Operations:
    - push(x): Push element x onto stack ⬆️
    - pop(): Remove and return the element on top of the stack ⬇️
    - top(): Get the top element 👀
    - getMin(): Retrieve the minimum element in the stack 📉
    """

    def __init__(self) -> None:
        """Initialize stack with min tracking. 🏗️"""
        self.stack: List[T] = []               # Main stack for elements
        # Auxiliary stack to track minimums
        self.min_stack: List[T] = []

    def push(self, val: T) -> None:
        """Push element onto stack and update minimums. ⬆️"""
        self.stack.append(val)

        # Update min_stack - add to min stack if empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:  # type: ignore
            self.min_stack.append(val)

    def pop(self) -> T:
        """Pop and return top element, updating minimums if needed. ⬇️"""
        if not self.stack:
            raise IndexError("Cannot pop from empty stack! 💨")

        val = self.stack.pop()

        # Update min_stack if we're removing a minimum
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

        return val

    def top(self) -> T:
        """Return top element without removing it. 👀"""
        if not self.stack:
            raise IndexError("Stack is empty! 💨")

        return self.stack[-1]

    def get_min(self) -> T:
        """Get minimum element in O(1) time. 📉"""
        if not self.min_stack:
            raise IndexError("Stack is empty! 💨")

        return self.min_stack[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty. 🕳️"""
        return len(self.stack) == 0

    def size(self) -> int:
        """Return the number of elements in the stack. 📏"""
        return len(self.stack)


# -------------------------------------------------------
# Exercise 4: Implement a History Feature
# -------------------------------------------------------
# Time: O(1) for type, delete and undo
# Space: O(m) where m is the number of operations
# -------------------------------------------------------

class TextEditor:
    """
    Exercise 4: Simple text editor with undo functionality using stacks.

    Approach:
    - Maintains the current text content as a string.
    - Uses a stack to store operation history.
    - Each operation (type, delete) is saved on the stack with
      information needed to undo it.
    - The undo operation retrieves and reverses the last operation.

    Complexity:
    - Time: O(1) for all main operations
    - Space: O(m) where m is the number of operations performed

    Operations:
    - type(text): Add text to the current content ⌨️
    - delete(count): Delete the last 'count' characters ❌
    - undo(): Undo the last operation 🔄
    - get_content(): Get the current content 📄
    """

    def __init__(self) -> None:
        """Initialize text editor with empty content and history. 🏗️"""
        self.content = ""
        self.history: List[Dict[str, Any]] = []  # Stack for operations history

    def type(self, text: str) -> str:
        """Add text to the content and record the operation. ⌨️"""
        operation = {
            'action': 'type',
            'text': text,
            'position': len(self.content)
        }
        self.history.append(operation)
        self.content += text
        return f"Typed: '{text}' ⌨️"

    def delete(self, count: int = 1) -> str:
        """Delete last 'count' characters and record the operation. ❌"""
        if count <= 0:
            return "Invalid count for delete operation! 🚫"

        # Limit count to available characters
        count = min(count, len(self.content))

        if count > 0:
            deleted_text = self.content[-count:]
            operation = {
                'action': 'delete',
                'text': deleted_text,
                'position': len(self.content) - count
            }
            self.history.append(operation)
            self.content = self.content[:-count]
            return f"Deleted: '{deleted_text}' ❌"
        else:
            return "Nothing to delete! 🚫"

    def undo(self) -> str:
        """Undo last operation using the history stack. 🔄"""
        if not self.history:
            return "Nothing to undo! 🚫"

        operation = self.history.pop()

        if operation['action'] == 'type':
            # Undo a type operation by removing the typed text
            text_length = len(operation['text'])
            self.content = self.content[:-text_length]
            return f"Undid typing of '{operation['text']}' 🔄"
        elif operation['action'] == 'delete':
            # Undo a delete operation by restoring the deleted text
            position = operation['position']
            self.content = self.content[:position] + \
                operation['text'] + self.content[position:]
            return f"Undid deletion of '{operation['text']}' 🔄"

        return "Unknown operation in history! 🚫"

    def get_content(self) -> str:
        """Get the current text content. 📄"""
        return self.content


# -------------------------------------------------------
# Exercise 5: Check for Balanced HTML Tags
# -------------------------------------------------------
# Time: O(n) where n is the length of the HTML
# Space: O(m) where m is the number of opening tags
# -------------------------------------------------------

def check_html_tags(html: str) -> bool:
    """
    Exercise 5: Check if HTML tags are properly balanced in a string.

    Approach:
    - Uses regular expressions to identify HTML tags.
    - Uses a stack to track opening tags.
    - When a closing tag is found, verifies it matches the last opening tag.
    - Ignores self-closing tags like <br>, <hr>, etc.

    Complexity:
    - Time: O(n) where n is the length of the HTML string
    - Space: O(m) where m is the number of opening tags

    Args:
        html: String with HTML content to check

    Returns:
        True if all tags are balanced, False otherwise 🔍
    """
    stack = []

    # Regular expression to find HTML tags (opening or closing)
    tag_pattern = re.compile(r'<\s*([/]?\s*[a-zA-Z0-9]+)[^>]*>')

    # Find all tags in the HTML string
    tags = tag_pattern.finditer(html)

    for match in tags:
        tag = match.group(1).strip()

        if tag.startswith('/'):
            # It's a closing tag
            # Remove the '/' and standardize case
            closing_tag = tag[1:].lower()

            if not stack:
                # No opening tag to match
                return False

            opening_tag = stack.pop().lower()
            if opening_tag != closing_tag:
                # Mismatch between opening and closing tags
                return False
        else:
            # It's an opening tag
            # Skip self-closing tags like <br>, <hr>, <img>
            if tag.lower() not in ['br', 'hr', 'img', 'input', 'meta', 'link']:
                stack.append(tag)

    # If stack is empty, all tags were matched correctly
    return len(stack) == 0

# ======================================================
# 4. UNIT TESTS
# ======================================================


class TestStackImplementations(unittest.TestCase):
    """Unit tests for all stack implementations. 🧪"""

    def test_array_stack(self) -> None:
        """Test fixed array stack implementation. 🧪"""
        stack = ArrayStack(5)
        self.assertTrue(stack.is_empty())

        # Push and size
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.size(), 3)

        # Peek
        self.assertEqual(stack.peek(), 30)
        self.assertEqual(stack.size(), 3)  # Size shouldn't change after peek

        # Pop
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.size(), 1)

        # Push to capacity and test overflow
        stack.push(40)
        stack.push(50)
        with self.assertRaises(OverflowError):
            stack.push(60)

        # Empty the stack and test underflow
        stack.pop()
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_dynamic_array_stack(self) -> None:
        """Test dynamic array stack with resizing. 🧪"""
        stack = DynamicArrayStack(3)  # Start with small capacity
        initial_capacity = stack.capacity

        # Push beyond initial capacity to test resizing
        for i in range(10):
            stack.push(i)

        # Capacity should have increased
        self.assertTrue(stack.capacity > initial_capacity)
        self.assertEqual(stack.size(), 10)

        # Test peek and pop
        self.assertEqual(stack.peek(), 9)
        self.assertEqual(stack.pop(), 9)

        # Pop many elements to test shrinking
        for _ in range(7):
            stack.pop()

        # Capacity should have decreased
        self.assertTrue(stack.capacity < 2 * initial_capacity)

        # Empty the stack
        while not stack.is_empty():
            stack.pop()

        # Test empty stack behavior
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()

    def test_linked_list_stack(self) -> None:
        """Test linked list stack implementation. 🧪"""
        stack = LinkedListStack()
        self.assertTrue(stack.is_empty())

        # Push and size
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.size(), 3)

        # Peek
        self.assertEqual(stack.peek(), 30)
        self.assertEqual(stack.size(), 3)  # Size shouldn't change after peek

        # Pop
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.size(), 1)

        # Empty the stack and test underflow
        stack.pop()
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()


class TestStackApplications(unittest.TestCase):
    """Unit tests for stack applications. 🧪"""

    def test_balanced_parentheses(self) -> None:
        """Test parentheses balancing function. 🧪"""
        test_cases = [
            ("()", True),
            ("()[]{}", True),
            ("([])", True),
            ("([)]", False),
            ("{[]}", True),
            (")(", False),
            ("((((", False),
            ("))))", False),
            ("a*(b+c)-(d/e)", True)
        ]

        for expr, expected in test_cases:
            with self.subTest(expr=expr):
                self.assertEqual(is_balanced(expr), expected)

    def test_postfix_evaluation(self) -> None:
        """Test postfix expression evaluation. 🧪"""
        test_cases = [
            ("3 4 +", 7),
            ("5 2 -", 3),
            ("3 4 * 2 +", 14),
            ("7 2 / 3 *", 10.5),
            ("5 1 2 + 4 * + 3 -", 14)
        ]

        for expr, expected in test_cases:
            with self.subTest(expr=expr):
                self.assertAlmostEqual(evaluate_postfix(expr), expected)

    def test_infix_to_postfix(self) -> None:
        """Test conversion from infix to postfix notation. 🧪"""
        test_cases = [
            ("3+4", "3 4 +"),
            ("5-2", "5 2 -"),
            ("3*4+2", "3 4 * 2 +"),
            ("(3+4)*2", "3 4 + 2 *"),
            ("5+((1+2)*4)-3", "5 1 2 + 4 * + 3 -"),
            ("a+b*c", "a b c * +")
        ]

        for infix, expected in test_cases:
            with self.subTest(infix=infix):
                self.assertEqual(infix_to_postfix(infix.replace("a", "1").replace("b", "2").replace("c", "3")),
                                 expected.replace("a", "1").replace("b", "2").replace("c", "3"))

    def test_infix_evaluation(self) -> None:
        """Test infix expression evaluation. 🧪"""
        test_cases = [
            ("3+4", 7),
            ("5-2", 3),
            ("3*4+2", 14),
            ("(3+4)*2", 14),
            ("5+((1+2)*4)-3", 14),
            ("10/2+3", 8)
        ]

        for expr, expected in test_cases:
            with self.subTest(expr=expr):
                self.assertAlmostEqual(evaluate_infix(expr), expected)

    def test_browser_history(self) -> None:
        """Test browser history navigation. 🧪"""
        browser = BrowserHistory()

        # Test initial state
        self.assertEqual(browser.get_current(), "No current page! 📭")
        self.assertEqual(browser.back(), "No back history! 🛑")
        self.assertEqual(browser.forward(), "No forward history! 🛑")

        # Visit pages and test navigation
        browser.visit("https://www.example.com")
        browser.visit("https://www.example.com/page1")
        browser.visit("https://www.example.com/page2")

        self.assertEqual(browser.get_current(),
                         "Current page: https://www.example.com/page2 📄")

        # Test back navigation
        self.assertEqual(
            browser.back(), "Navigated back to: https://www.example.com/page1 ⬅️")
        self.assertEqual(
            browser.back(), "Navigated back to: https://www.example.com ⬅️")
        self.assertEqual(browser.back(), "No back history! 🛑")

        # Test forward navigation
        self.assertEqual(
            browser.forward(), "Navigated forward to: https://www.example.com/page1 ➡️")

        # Visit a new page and test clearing of forward history
        browser.visit("https://www.example.com/page3")
        self.assertEqual(browser.forward(), "No forward history! 🛑")


class TestPracticalExercises(unittest.TestCase):
    """Unit tests for the practical exercises. 🧪"""

    def test_reverse_string(self) -> None:
        """Test string reversal using a stack. 🧪"""
        test_cases = [
            ("hello", "olleh"),
            ("python", "nohtyp"),
            ("", ""),
            ("a", "a"),
            ("12345", "54321")
        ]

        for original, expected in test_cases:
            with self.subTest(original=original):
                self.assertEqual(reverse_string(original), expected)

    def test_min_stack(self) -> None:
        """Test stack with min function. 🧪"""
        stack = MinStack()

        # Test empty stack
        self.assertTrue(stack.is_empty())
        with self.assertRaises(IndexError):
            stack.get_min()

        # Push elements and test min
        stack.push(5)
        self.assertEqual(stack.get_min(), 5)

        stack.push(2)
        self.assertEqual(stack.get_min(), 2)

        stack.push(4)
        self.assertEqual(stack.get_min(), 2)

        stack.push(1)
        self.assertEqual(stack.get_min(), 1)

        # Test min after pops
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.get_min(), 2)

        stack.pop()  # pop the 4
        self.assertEqual(stack.get_min(), 2)

        stack.pop()  # pop the 2
        self.assertEqual(stack.get_min(), 5)

        stack.pop()  # pop the 5
        self.assertTrue(stack.is_empty())

    def test_text_editor(self) -> None:
        """Test text editor with undo functionality. 🧪"""
        editor = TextEditor()

        # Test initial state
        self.assertEqual(editor.get_content(), "")

        # Type text
        editor.type("Hello")
        self.assertEqual(editor.get_content(), "Hello")

        editor.type(" World")
        self.assertEqual(editor.get_content(), "Hello World")

        # Delete characters
        editor.delete(6)  # Delete " World"
        self.assertEqual(editor.get_content(), "Hello")

        # Undo operations
        editor.undo()  # Undo the delete
        self.assertEqual(editor.get_content(), "Hello World")

        editor.undo()  # Undo typing " World"
        self.assertEqual(editor.get_content(), "Hello")

        editor.undo()  # Undo typing "Hello"
        self.assertEqual(editor.get_content(), "")

        # Test undo on empty history
        result = editor.undo()
        self.assertEqual(result, "Nothing to undo! 🚫")

    def test_html_tags_checker(self) -> None:
        """Test HTML tags balancing function. 🧪"""
        test_cases = [
            ("<div></div>", True),
            ("<p>Hello <strong>World</strong></p>", True),
            ("<div><p>Nested</p></div>", True),
            ("<div><p>Unbalanced</div>", False),
            ("<p>Missing closing tag", False),
            ("</p>Missing opening tag", False),
            ("<br><hr><img>", True),  # Self-closing tags
            ("<div><br><p>Mixed</p></div>", True),
            ("<div><p>Wrong order</div></p>", False)
        ]

        for html, expected in test_cases:
            with self.subTest(html=html):
                self.assertEqual(check_html_tags(html), expected)


# ======================================================
# 5. VISUALIZATIONS AND USAGE EXAMPLES
# ======================================================

def demo_stack_operations() -> None:
    """Demonstrate basic stack operations with different implementations. 🎮"""
    print("\n" + "="*50)
    print("DEMO: BASIC STACK OPERATIONS 🎮")
    print("="*50)

    # Create instances of each stack implementation
    array_stack = ArrayStack(5)
    dynamic_stack = DynamicArrayStack(5)
    linked_stack = LinkedListStack()

    stacks = [
        ("Fixed Array Stack 📦", array_stack),
        ("Dynamic Array Stack 📊", dynamic_stack),
        ("Linked List Stack 📃", linked_stack)
    ]

    # Push operations
    print("\n--- Pushing elements to each stack ---")
    for name, stack in stacks:
        print(f"\n{name}:")
        for i in range(1, 4):
            value = i * 10
            stack.push(value)
            print(f"  Push {value} ⬆️ -> {stack}")

    # Peek operation
    print("\n--- Peeking at top element ---")
    for name, stack in stacks:
        print(f"{name}: Peek 👀 -> {stack.peek()}")

    # Pop operation
    print("\n--- Popping elements from each stack ---")
    for name, stack in stacks:
        print(f"\n{name}:")
        while not stack.is_empty():
            value = stack.pop()
            print(f"  Pop ⬇️ -> {value}, Remaining: {stack}")


def demo_balanced_parentheses() -> None:
    """Demonstrate parentheses balancing application. 🎮"""
    print("\n" + "="*50)
    print("DEMO: BALANCED PARENTHESES CHECKING 🎮⚖️")
    print("="*50)

    expressions = [
        "()",                # Simple matched pair
        "()[]{}<>",          # Multiple pairs
        "([]{})<>",          # Nested pairs
        "([)]",              # Crossed pairs
        "{[()]}",            # Complex nesting
        ")(",                # Reversed order
        "((a + b) * (c - d))",  # Expression with operators
        "if (a > b) { return a; } else { return b; }"  # Code-like expression
    ]

    for expr in expressions:
        balanced = is_balanced(expr)
        status = "✅ Balanced" if balanced else "❌ Unbalanced"
        print(f"Expression: '{expr}' is {status}")


def demo_expression_evaluation() -> None:
    """Demonstrate expression evaluation using stacks. 🎮"""
    print("\n" + "="*50)
    print("DEMO: EXPRESSION EVALUATION 🎮🧮")
    print("="*50)

    infix_expressions = [
        "3+4",
        "2*3+5",
        "(2+3)*4",
        "5+((1+2)*4)-3",
        "10/2+3*4"
    ]

    print("\n--- Converting Infix to Postfix ---")
    for expr in infix_expressions:
        try:
            postfix = infix_to_postfix(expr)
            print(f"Infix: '{expr}' -> Postfix: '{postfix}'")
        except ValueError as e:
            print(f"Error with '{expr}': {str(e)}")

    print("\n--- Evaluating Expressions ---")
    for expr in infix_expressions:
        try:
            result = evaluate_infix(expr)
            print(f"Infix: '{expr}' -> Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error with '{expr}': {str(e)}")


def demo_browser_history() -> None:
    """Demonstrate browser history navigation. 🎮"""
    print("\n" + "="*50)
    print("DEMO: BROWSER HISTORY NAVIGATION 🎮🌐")
    print("="*50)

    browser = BrowserHistory()

    # Initial state
    print(browser.get_current())

    # Visit some pages
    pages = [
        "https://www.example.com",
        "https://www.example.com/products",
        "https://www.example.com/products/item1",
        "https://www.example.com/products/item1/details"
    ]

    print("\n--- Visiting pages ---")
    for page in pages:
        print(browser.visit(page))

    # Navigate back
    print("\n--- Navigating back ---")
    for _ in range(3):
        print(browser.back())

    # Navigate forward
    print("\n--- Navigating forward ---")
    for _ in range(2):
        print(browser.forward())

    # Visit a new page (clears forward history)
    print("\n--- Visiting a new page ---")
    print(browser.visit("https://www.example.com/contact"))

    # Try to go forward (should have no forward history)
    print("\n--- Trying to go forward ---")
    print(browser.forward())


def demo_min_stack() -> None:
    """Demonstrate a stack with min operation. 🎮"""
    print("\n" + "="*50)
    print("DEMO: MIN STACK OPERATIONS 🎮📉")
    print("="*50)

    stack = MinStack()

    operations = [
        ("push", 5),
        ("push", 9),
        ("push", 1),
        ("push", 3),
        ("push", 2)
    ]

    print("\n--- Pushing elements ---")
    for op, val in operations:
        stack.push(val)
        print(f"Push {val} ⬆️ -> Current min: {stack.get_min()} 📉")

    print("\n--- Popping elements ---")
    while not stack.is_empty():
        val = stack.pop()
        print(f"Pop {val} ⬇️ -> ", end="")

        if stack.is_empty():
            print("Stack is empty")
        else:
            print(f"Current min: {stack.get_min()} 📉")


def demo_text_editor() -> None:
    """Demonstrate text editor with undo functionality. 🎮"""
    print("\n" + "="*50)
    print("DEMO: TEXT EDITOR WITH UNDO 🎮⌨️")
    print("="*50)

    editor = TextEditor()

    # Initial state
    print(f"Initial content: '{editor.get_content()}'")

    # Type text
    print("\n--- Typing text ---")
    print(editor.type("Hello"))
    print(f"Content: '{editor.get_content()}'")

    print(editor.type(" World!"))
    print(f"Content: '{editor.get_content()}'")

    # Delete text
    print("\n--- Deleting text ---")
    print(editor.delete(1))  # Delete "!"
    print(f"Content: '{editor.get_content()}'")

    print(editor.delete(6))  # Delete " World"
    print(f"Content: '{editor.get_content()}'")

    # Undo operations
    print("\n--- Undoing operations ---")
    print(editor.undo())  # Undo delete " World"
    print(f"Content: '{editor.get_content()}'")

    print(editor.undo())  # Undo delete "!"
    print(f"Content: '{editor.get_content()}'")

    print(editor.undo())  # Undo type " World!"
    print(f"Content: '{editor.get_content()}'")


# ======================================================
# 6. MAIN FUNCTION
# ======================================================

def main() -> None:
    """Run demos and tests for stack implementations and applications. 🚀"""
    print("\n" + "="*50)
    print("STACK DATA STRUCTURE - DEMONSTRATION 🚀")
    print("="*50)

    # Run demos
    demo_stack_operations()
    demo_balanced_parentheses()
    demo_expression_evaluation()
    demo_browser_history()
    demo_min_stack()
    demo_text_editor()

    # Run tests
    print("\n" + "="*50)
    print("RUNNING UNIT TESTS 🧪")
    print("="*50)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


if __name__ == "__main__":
    main()
