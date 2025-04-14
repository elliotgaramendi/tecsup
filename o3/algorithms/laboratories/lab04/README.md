# Stack - Complete Implementation

A didactic project that implements the Stack data structure with different approaches and practical applications.

## Table of Contents

- [Stack - Complete Implementation](#stack---complete-implementation)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Fundamental Concept](#fundamental-concept)
  - [Implementations](#implementations)
    - [1. Fixed Array](#1-fixed-array)
    - [2. Dynamic Array](#2-dynamic-array)
    - [3. Linked List](#3-linked-list)
  - [Complexity Analysis](#complexity-analysis)
  - [Practical Exercises](#practical-exercises)
    - [1. Reverse a String](#1-reverse-a-string)
    - [2. Evaluate Infix Expressions](#2-evaluate-infix-expressions)
    - [3. Stack with getMin() Function](#3-stack-with-getmin-function)
    - [4. History Feature Implementation](#4-history-feature-implementation)
    - [5. HTML Tags Checker](#5-html-tags-checker)
  - [Additional Practical Applications](#additional-practical-applications)
    - [1. Balanced Parentheses Checking](#1-balanced-parentheses-checking)
    - [2. Browser History](#2-browser-history)
  - [Unit Tests](#unit-tests)
  - [Demonstrations](#demonstrations)
  - [Implementation Comparison](#implementation-comparison)
  - [How to Use](#how-to-use)
  - [Next Steps](#next-steps)
  - [Conclusions](#conclusions)

## Description

This project implements the Stack data structure in Python using three different approaches: fixed array, dynamic array, and linked list. It also includes practical applications, unit tests, and usage demonstrations. 🔍

## Fundamental Concept

A **stack** is a data structure that follows the LIFO (Last-In, First-Out) principle, where the last element added is the first one to be removed. It works like a stack of books or plates, where you can only interact with the element at the top. 🧱

**Basic operations:**
- **push**: Add an element to the top ⬆️
- **pop**: Remove and return the element from the top ⬇️
- **peek/top**: View the top element without removing it 👀
- **isEmpty**: Check if the stack is empty 🔍
- **size**: Get the number of elements in the stack 📏

## Implementations

### 1. Fixed Array

Uses a fixed-size array to store elements. Simple and efficient, but with limited capacity. ⚙️

```python
stack = ArrayStack(5)  # Create stack with capacity for 5 elements
stack.push(10)         # Add element
value = stack.pop()    # Extract element (10)
```

### 2. Dynamic Array

Uses an array that automatically resizes when necessary, offering flexibility. 📊

```python
stack = DynamicArrayStack()  # Create stack with initial capacity
stack.push("data")           # Add element
stack.push("more data")      # Stack resizes if needed
```

### 3. Linked List

Uses linked nodes to store elements, allowing theoretically unlimited capacity. 📃

```python
stack = LinkedListStack()  # Create stack based on linked list
stack.push(42)             # Add element
element = stack.peek()     # View top element (42)
```

## Complexity Analysis

| Operation | Fixed Array | Dynamic Array   | Linked List |
| --------- | ----------- | --------------- | ----------- |
| push      | O(1)        | O(1)* amortized | O(1)        |
| pop       | O(1)        | O(1)* amortized | O(1)        |
| peek      | O(1)        | O(1)            | O(1)        |
| isEmpty   | O(1)        | O(1)            | O(1)        |
| size      | O(1)        | O(1)            | O(1)        |

*Amortized complexity is due to occasional resizing operations. ⏱️

**Space Complexity:**
- Fixed Array: O(n) where n is the capacity (not the current size)
- Dynamic Array: O(n) where n is the current capacity (may be greater than size)
- Linked List: O(n) where n is the number of elements, plus overhead for pointers

## Practical Exercises

The project includes the implementation of five practical exercises that demonstrate different stack applications:

### 1. Reverse a String

Uses a stack to reverse a string of text.

```python
reversed_text = reverse_string("Hello, World!")  # "!dlroW ,olleH"
```

**Complexity:**
- Time: O(n)
- Space: O(n)

### 2. Evaluate Infix Expressions

Converts and evaluates mathematical expressions in infix notation.

```python
result = evaluate_infix("(3 + 4) * 2")  # 14
postfix = infix_to_postfix("5 + ((1 + 2) * 4) - 3")  # "5 1 2 + 4 * + 3 -"
```

**Complexity:**
- Time: O(n)
- Space: O(n)

### 3. Stack with getMin() Function

Implements a special stack that can retrieve the minimum value in constant time.

```python
stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(4)
min_value = stack.get_min()  # 2 (in O(1) time)
```

**Complexity:**
- Time: O(1) for all operations
- Space: O(n)

### 4. History Feature Implementation

Text editor with undo functionality using stacks.

```python
editor = TextEditor()
editor.type("Hello")
editor.type(" World")
editor.delete(6)  # Deletes " World"
editor.undo()     # Restores to "Hello World"
```

**Complexity:**
- Time: O(1) for main operations
- Space: O(m) where m is the number of operations

### 5. HTML Tags Checker

Extends the balanced parentheses checker to validate HTML tags.

```python
check_html_tags("<div><p>Content</p></div>")  # True
check_html_tags("<div><p>Unbalanced</div>")   # False
```

**Complexity:**
- Time: O(n)
- Space: O(m) where m is the number of nested tags

## Additional Practical Applications

### 1. Balanced Parentheses Checking

Verifies if an expression has properly balanced parentheses, brackets, and braces.

```python
is_balanced("(a + b) * [c - d]")  # True
is_balanced("([)]")               # False
```

### 2. Browser History

Implements "Back" and "Forward" functionality like in a web browser.

```python
browser = BrowserHistory()
browser.visit("https://example.com")
browser.visit("https://example.com/page1")
browser.back()  # Returns to example.com
```

## Unit Tests

The project includes complete unit tests for all implementations and applications: 🧪

```python
# Run the tests
python -m unittest stack_implementations.py
```

## Demonstrations

The script includes interactive demonstrations for each concept: 🎮

```python
# Run all demonstrations
python stack_implementations.py
```

## Implementation Comparison

| Implementation | Advantages                                                                           | Disadvantages                                              | Optimal Use Cases                                                   |
| -------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| Fixed Array    | • Simple<br>• Excellent memory locality<br>• Predictable memory usage                | • Limited size<br>• Overflow risk                          | • When maximum size is known<br>• Performance-critical applications |
| Dynamic Array  | • Flexible size<br>• Good memory locality<br>• No overflow risk                      | • Occasional costly resizing<br>• Possible over-allocation | • General use<br>• When size varies significantly                   |
| Linked List    | • Unlimited size<br>• Constant insertion time<br>• Memory efficient for sparse usage | • Extra memory per node<br>• Poor cache locality           | • Memory-constrained systems<br>• Frequent large data variations    |

## How to Use

1. **Installation:** 🚀
   - Only requires Python 3.6+ with standard library.

2. **Import:**
   ```python
   from stack_implementations import ArrayStack, DynamicArrayStack, LinkedListStack
   # Or any other specific class or function
   ```

3. **Basic example:**
   ```python
   # Create a stack
   stack = DynamicArrayStack()
   
   # Add elements
   stack.push(10)
   stack.push(20)
   
   # View top element
   top_element = stack.peek()  # 20
   
   # Extract elements
   stack.pop()  # 20
   stack.pop()  # 10
   ```

## Next Steps

To expand this project, consider: 🛣️

1. **Advanced implementations:**
   - Thread-safe stack
   - Bounded circular stack
   - Persistent stack (that preserves versions)

2. **Integrations with other structures:**
   - Stack-based graph traversal
   - Expression tree construction
   - Custom memory allocator

3. **Algorithmic challenges:**
   - Next greater element problem
   - Largest rectangle in histogram
   - Stock span problem

## Conclusions

Stacks are one of the most fundamental and versatile data structures in computer science, used in numerous contexts from web browsers to compilers. Their conceptual simplicity contrasts with their incredible utility for solving complex problems. 🎓

By mastering stack implementation concepts and their applications, you gain a solid foundation for more advanced data structures and algorithms that use them as building blocks.