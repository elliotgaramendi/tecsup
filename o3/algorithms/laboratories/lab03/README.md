# Linked Lists Laboratory

## Overview

This repository contains a comprehensive implementation of singly linked lists in Python, along with various applications and extensions. The project serves as both a learning resource and a reference implementation for linked list operations and applications.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Core Components](#core-components)
- [Basic Operations](#basic-operations)
- [Advanced Operations](#advanced-operations)
- [Applications](#applications)
- [Time Complexity Analysis](#time-complexity-analysis)
- [Implementation Notes](#implementation-notes)
- [Usage Examples](#usage-examples)
- [Running the Tests](#running-the-tests)

## Features

- Complete implementation of singly linked lists
- Basic operations (insertion, deletion, search)
- Advanced operations (cycle detection, reversal, finding middle node)
- Practical applications using linked lists:
  - Stack implementation (LIFO)
  - Queue implementation (FIFO)
  - Polynomial representation
  - Sparse matrix representation
- Comprehensive test suite for all components

## Core Components

### Node Class

The fundamental building block of a linked list:

```python
class Node:
    """Node in a linked list, stores data and reference to the next node."""
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node
```

### LinkedList Class

The main linked list implementation:

```python
class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.length = 0
```

## Basic Operations

### Display and Length

- **display()**: Returns a string representation of the linked list
- **list_length()**: Counts and returns the number of nodes in the list

### Insertion

- **insert_at_beginning(data)**: Inserts a new node at the beginning of the list
- **insert_at_end(data)**: Inserts a new node at the end of the list
- **insert_at_position(position, data)**: Inserts a new node at a specific position

### Deletion

- **delete_from_beginning()**: Deletes the first node from the list
- **delete_from_end()**: Deletes the last node from the list
- **delete_from_position(position)**: Deletes a node from a specific position
- **clear()**: Removes all nodes from the list

### Search

- **search(data)**: Finds the position of the first occurrence of a value
- **get_nth_from_end(n)**: Returns the data of the nth node from the end (1-based indexing)

## Advanced Operations

### Cycle Detection

```python
def has_cycle(self):
    """Check if the list has a cycle using Floyd's algorithm."""
    if self.head is None or self.head.get_next() is None:
        return False
    
    # Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
    slow = self.head  # Tortoise (moves one step at a time)
    fast = self.head  # Hare (moves two steps at a time)
    
    while fast is not None and fast.get_next() is not None:
        slow = slow.get_next()           # Move one step
        fast = fast.get_next().get_next() # Move two steps
        
        # If they meet, there's a cycle
        if slow == fast:
            return True
    
    # If we reach here, there's no cycle
    return False
```

Floyd's Cycle-Finding Algorithm (also known as "Tortoise and Hare") is an elegant approach to cycle detection. It uses two pointers moving at different speeds: if there's a cycle, the fast pointer will eventually catch up to the slow pointer.

### List Reversal

```python
def reverse(self):
    """Reverse the order of nodes in the list."""
    if self.head is None or self.head.get_next() is None:
        return True  # Empty list or single node (already reversed)
    
    previous = None
    current = self.head
    
    while current is not None:
        # Store the next node
        next_node = current.get_next()
        
        # Reverse the link
        current.set_next(previous)
        
        # Move to the next nodes
        previous = current
        current = next_node
    
    # Update the head to the new first node (previously the last)
    self.head = previous
    
    return True
```

Reversal is performed in-place by adjusting the pointers without creating a new list, making it memory-efficient.

### Finding the Middle Node

```python
def find_middle(self):
    """Find and return the data of the middle node."""
    if self.head is None:
        return None
    
    # Use the slow and fast pointer technique
    slow = self.head
    fast = self.head
    
    # When fast reaches the end, slow will be at the middle
    while fast is not None and fast.get_next() is not None:
        slow = slow.get_next()           # Move one step
        fast = fast.get_next().get_next() # Move two steps
    
    return slow.get_data()
```

This method also uses the "slow and fast pointer" technique to find the middle node in a single pass.

### Removing Duplicates

```python
def remove_duplicates(self):
    """Remove any duplicate values from the list."""
    if self.head is None or self.head.get_next() is None:
        return True  # Empty list or single node (no duplicates)
    
    # Set to keep track of values we've seen
    values_seen = set()
    
    current = self.head
    previous = None
    
    while current is not None:
        data = current.get_data()
        
        if data in values_seen:
            # Duplicate found, remove the node
            previous.set_next(current.get_next())
            self.length -= 1
        else:
            # New value, add to set
            values_seen.add(data)
            previous = current
        
        current = current.get_next()
    
    return True
```

This method uses a set to track values already seen, allowing for efficient duplicate removal in O(n) time.

### Merging Sorted Lists

```python
def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into a new sorted list."""
    # Create a new list for the result
    result = LinkedList()
    
    # Handle empty lists
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1
    
    # Pointers to the current nodes in each list
    curr1 = list1.head
    curr2 = list2.head
    
    # Merge the lists
    while curr1 is not None and curr2 is not None:
        if curr1.get_data() <= curr2.get_data():
            result.insert_at_end(curr1.get_data())
            curr1 = curr1.get_next()
        else:
            result.insert_at_end(curr2.get_data())
            curr2 = curr2.get_next()
    
    # Add any remaining nodes from list1
    while curr1 is not None:
        result.insert_at_end(curr1.get_data())
        curr1 = curr1.get_next()
    
    # Add any remaining nodes from list2
    while curr2 is not None:
        result.insert_at_end(curr2.get_data())
        curr2 = curr2.get_next()
    
    return result
```

This function merges two sorted linked lists into a single sorted list, similar to the merge part of merge sort.

## Applications

### Stack Implementation

A Stack is a Last-In-First-Out (LIFO) data structure. The implementation uses a linked list to store elements and provides the following operations:

- **push(data)**: Add an element to the top of the stack
- **pop()**: Remove and return the element at the top of the stack
- **peek()**: Return the top element without removing it
- **is_empty()**: Check if the stack is empty
- **size()**: Return the number of elements in the stack

```python
class Stack:
    """Stack implementation using a linked list (LIFO data structure)."""
    
    def __init__(self):
        self.linked_list = LinkedList()
    
    def push(self, data):
        """Add an element to the top of the stack."""
        self.linked_list.insert_at_beginning(data)
    
    def pop(self):
        """Remove and return the element at the top of the stack."""
        return self.linked_list.delete_from_beginning()
```

### Queue Implementation

A Queue is a First-In-First-Out (FIFO) data structure. The implementation uses a linked list to store elements and provides the following operations:

- **enqueue(data)**: Add an element to the end of the queue
- **dequeue()**: Remove and return the element at the front of the queue
- **peek()**: Return the front element without removing it
- **is_empty()**: Check if the queue is empty
- **size()**: Return the number of elements in the queue

```python
class Queue:
    """Queue implementation using a linked list (FIFO data structure)."""
    
    def __init__(self):
        self.linked_list = LinkedList()
    
    def enqueue(self, data):
        """Add an element to the end of the queue."""
        self.linked_list.insert_at_end(data)
    
    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        return self.linked_list.delete_from_beginning()
```

### Polynomial Representation

Linked lists can be used to represent polynomials, where each node contains a coefficient and an exponent:

```python
class PolynomialTerm:
    """A term in a polynomial with coefficient and exponent."""
    
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent

class Polynomial:
    """A polynomial represented as a linked list of terms."""
    
    def __init__(self):
        self.terms = LinkedList()
    
    def add_term(self, coefficient, exponent):
        """Add a term to the polynomial."""
        # Implementation details...
```

This representation allows for efficient polynomial operations like addition, subtraction, and evaluation.

### Sparse Matrix Representation

A sparse matrix (a matrix with mostly zero values) can be efficiently represented using a linked list to store only the non-zero elements:

```python
class MatrixElement:
    """A non-zero element in a sparse matrix."""
    
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

class SparseMatrix:
    """A sparse matrix represented using linked lists."""
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = LinkedList()
    
    def set_element(self, row, col, value):
        """Set the value at position (row, col)."""
        # Implementation details...
```

This approach can significantly reduce memory usage for matrices with many zero elements.

## Time Complexity Analysis

| Operation                    | Linked List | Array | Dynamic Array  |
| ---------------------------- | ----------- | ----- | -------------- |
| Access by index              | O(n)        | O(1)  | O(1)           |
| Insertion/deletion at start  | O(1)        | O(n)  | O(n)           |
| Insertion/deletion at end    | O(n)*       | O(1)  | O(1) amortized |
| Insertion/deletion in middle | O(n)        | O(n)  | O(n)           |

*Note: O(1) if we keep a tail pointer

### Memory Usage Comparison

- **Arrays**: Continuous block of memory, no overhead per element
- **Linked Lists**: Non-contiguous memory, additional memory per node for pointers (4-8 bytes per node)

## Implementation Notes

### Design Decisions

1. **Getter/Setter Methods**: The Node class uses getter and setter methods for data and next pointers to encapsulate the implementation details.

2. **Length Tracking**: The LinkedList class maintains a length attribute that's updated with each insertion and deletion, allowing for O(1) length queries.

3. **Error Handling**: The implementation includes checks for invalid positions and handles edge cases like empty lists.

4. **Auxiliary Data Structures**: Some operations use auxiliary data structures (like sets for removing duplicates) to optimize performance.

### Extension Possibilities

1. **Doubly Linked Lists**: Extend the implementation to include references to both next and previous nodes.

2. **Circular Linked Lists**: Modify the implementation so the last node points back to the first node.

3. **Skip Lists**: Implement a skip list, a probabilistic data structure based on linked lists with multiple layers.

## Usage Examples

### Basic Usage

```python
# Create a new linked list
my_list = LinkedList()

# Add elements
my_list.insert_at_beginning(10)
my_list.insert_at_end(20)
my_list.insert_at_position(1, 15)

# Display the list
print(my_list.display())  # Output: 10 -> 15 -> 20 -> None

# Search for an element
position = my_list.search(15)
print(f"Position of 15: {position}")  # Output: Position of 15: 1

# Remove elements
my_list.delete_from_beginning()
my_list.delete_from_end()
print(my_list.display())  # Output: 15 -> None
```

### Advanced Usage

```python
# Reverse a list
my_list = LinkedList()
for i in range(1, 6):
    my_list.insert_at_end(i)
print(f"Original: {my_list.display()}")  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

my_list.reverse()
print(f"Reversed: {my_list.display()}")  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

# Find the middle element
middle = my_list.find_middle()
print(f"Middle element: {middle}")  # Output: Middle element: 3
```

### Application Examples

```python
# Using a queue
queue = Queue()
queue.enqueue("Task 1")
queue.enqueue("Task 2")
print(queue.dequeue())  # Output: Task 1

# Using a polynomial
poly = Polynomial()
poly.add_term(3, 2)  # 3x^2
poly.add_term(-2, 1)  # -2x
poly.add_term(5, 0)  # 5
print(poly)  # Output: 3x^2 - 2x + 5
```

## Running the Tests

The repository includes comprehensive tests for all components. To run the tests:

```bash
python linked_list_lab.py
```

The tests will output the results of various operations and applications, allowing you to verify the correctness of the implementation.