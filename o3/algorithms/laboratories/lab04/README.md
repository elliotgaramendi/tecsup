# Stack Data Structure Implementation

## 📚 Overview

This project provides a comprehensive implementation of the stack data structure in Python, including various implementations, applications, and practical exercises. A stack is a fundamental data structure that follows the Last-In-First-Out (LIFO) principle, where elements can only be added or removed from one end, typically called the "top" of the stack.

## 🧩 Features

### Stack Implementations

- **Fixed Array Stack**: Simple implementation with a predefined capacity.
- **Dynamic Array Stack**: Resizable implementation that grows and shrinks as needed.
- **Linked List Stack**: Implementation using linked nodes with no capacity limit.
- **Advanced Implementations**: Thread-safe stack and bounded circular stack.

### Stack Operations

All implementations support these fundamental operations:

- **push(item)**: Add an item to the top of the stack.
- **pop()**: Remove and return the item from the top of the stack.
- **peek()**: View the top item without removing it.
- **is_empty()**: Check if the stack is empty.
- **size()**: Get the number of items in the stack.

### Special Implementations

- **MinStack**: A stack that efficiently tracks the minimum value.
- **ThreadSafeStack**: A stack that safely handles concurrent operations.
- **BoundedStack**: A circular buffer implementation with a fixed capacity.

## 🧪 Applications and Examples

### Basic Applications

1. **Balanced Parentheses Checking**: Validate if brackets in an expression are balanced.
2. **Expression Evaluation**: 
   - Postfix (Reverse Polish Notation) evaluation
   - Infix to postfix conversion and evaluation

### Real-world Applications

1. **Browser History Simulation**: Implementation of back/forward navigation.
2. **Text Editor with Undo**: Simple text editor supporting typing, deletion, and undo.
3. **HTML Tag Validation**: Check if HTML tags are properly nested and balanced.

### String Manipulation

- String reversal using a stack.

## 📊 Performance Analysis

The project includes a performance comparison function that measures the time taken by different stack implementations to perform push and pop operations. Key findings:

- **Fixed Array Stack**: Fastest for a known and limited number of elements.
- **Dynamic Array Stack**: Good overall performance with occasional resizing overhead.
- **Linked List Stack**: Consistent performance but with higher memory overhead per element.

## 🛠️ Implementation Details

### Fixed Array Stack

```python
class ArrayStack:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1
```

- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) where n is the capacity
- **Advantages**: Simple, memory-efficient, predictable
- **Limitations**: Fixed size, potential for overflow

### Dynamic Array Stack

```python
class DynamicArrayStack:
    def __init__(self, initial_capacity=10):
        self.data = [None] * initial_capacity
        self.capacity = initial_capacity
        self.top = -1
```

- **Time Complexity**: 
  - Average: O(1) for all operations
  - Worst-case: O(n) for push/pop when resizing is needed
- **Space Complexity**: O(n) where n is the current capacity
- **Advantages**: No size limit, efficient memory usage
- **Limitations**: Occasional resizing overhead

### Linked List Stack

```python
class LinkedListStack:
    def __init__(self):
        self.head = None  # Top of the stack
        self.count = 0
```

- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) plus overhead for node pointers
- **Advantages**: No size limit, consistent operation time
- **Limitations**: Higher memory overhead per element

## 🔍 Usage Examples

### Basic Stack Operations

```python
# Create a stack
stack = ArrayStack(5)

# Push elements
stack.push(10)
stack.push(20)
stack.push(30)

# Peek at top element
top_element = stack.peek()  # Returns 30

# Pop elements
popped = stack.pop()  # Returns 30

# Check if empty
is_empty = stack.is_empty()  # Returns False

# Get size
size = stack.size()  # Returns 2
```

### Balancing Parentheses

```python
def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if (char == ")" and stack[-1] != "(") or \
               (char == "}" and stack[-1] != "{") or \
               (char == "]" and stack[-1] != "["):
                return False
            stack.pop()
    return len(stack) == 0
```

### Evaluating Expressions

```python
# Evaluate a postfix expression
result = evaluate_postfix("3 4 + 2 *")  # Returns 14

# Convert and evaluate an infix expression
result = evaluate_infix("(3 + 4) * 2")  # Returns 14
```

## 🚀 Advanced Topics

### Optimizing Memory Usage

The `BoundedStack` uses a circular buffer to maximize space efficiency:

```python
class BoundedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size_val = 0
        self.head = 0  # Index where items are removed
        self.tail = 0  # Index where items are added
```

### Thread Safety

The `ThreadSafeStack` ensures safe concurrent access:

```python
class ThreadSafeStack:
    def __init__(self):
        self.stack = []
        self.lock = threading.Lock()
        
    def push(self, item):
        with self.lock:
            self.stack.append(item)
```

## 🔄 Running the Tests

Execute the main script to run all tests:

```bash
python stack_implementation.py
```

This will run tests for all stack implementations, applications, and exercises.

## 📝 Conclusion

Stacks are versatile data structures with applications in many areas of computing, including:

- **Program Execution**: Call stacks for function calls
- **Memory Management**: Resource allocation and tracking
- **Browser History**: Navigation history in web browsers
- **Syntax Parsing**: Compilers and interpreters
- **Undo/Redo Functionality**: Text editors and design software
- **Backtracking Algorithms**: Depth-first search and state management

This implementation provides a solid foundation for understanding and utilizing stacks in various programming scenarios.

## 🔮 Next Steps

- Implement a persistent stack that preserves previous versions
- Create a stack-based memory allocator
- Apply stacks to solve more complex algorithmic problems
- Explore hybrid data structures that combine stacks with other collections