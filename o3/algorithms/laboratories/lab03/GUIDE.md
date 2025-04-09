# Linked Lists Laboratory

## Introduction

Welcome to the Linked Lists Laboratory! In this lab, you'll gain hands-on experience implementing and working with linked lists in Python. This step-by-step guide will help you understand the core concepts of linked lists and their operations.

## Learning Objectives

By the end of this lab, you should be able to:
1. Implement a singly linked list data structure
2. Understand the basic operations of linked lists
3. Analyze the time and space complexity of different operations
4. Apply linked lists to solve practical problems

## File Structure

Your `linked_list_lab.py` file will have the following structure:

```
linked_list_lab.py
├── class Node
│   ├── __init__()
│   ├── get_data()
│   ├── set_data()
│   ├── get_next()
│   └── set_next()
│
├── class LinkedList
│   ├── __init__()
│   ├── display()
│   ├── list_length()
│   ├── insert_at_beginning()
│   ├── insert_at_end()
│   ├── insert_at_position()
│   ├── delete_from_beginning()
│   ├── delete_from_end()
│   ├── delete_from_position()
│   ├── search()
│   ├── get_nth_from_end()
│   ├── clear()
│   ├── has_cycle()
│   ├── reverse()
│   ├── find_middle()
│   └── remove_duplicates()
│
├── merge_sorted_lists() (standalone function)
│
├── class Queue
│   ├── __init__()
│   ├── is_empty()
│   ├── enqueue()
│   ├── dequeue()
│   ├── peek()
│   ├── size()
│   └── display()
│
├── test_linked_list()
├── test_queue()
└── test_merge_sorted_lists()
```

## Part 1: The Node Class

Let's start by defining the basic building block of a linked list: the Node.

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

## Part 2: The LinkedList Class

Now, let's implement the LinkedList class that will use our Node class.

```python
class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.length = 0
```

## Part 3: Basic Operations

### Exercise 1: Displaying the List

Implement a method to display all elements in the list.

```python
def display(self):
    """Return a string representation of the linked list."""
    if self.head is None:
        return "Empty list"
    
    current = self.head
    result = ""
    
    while current is not None:
        result += str(current.get_data()) + " -> "
        current = current.get_next()
    
    return result + "None"
```

### Exercise 2: Counting Nodes

Implement a method to count the number of nodes in the linked list.

```python
def list_length(self):
    """Count and return the number of nodes in the list."""
    count = 0
    current = self.head
    
    while current is not None:
        count += 1
        current = current.get_next()
    
    return count
```

### Exercise 3: Insertion at the Beginning

Implement a method to insert a new node at the beginning of the list.

```python
def insert_at_beginning(self, data):
    """Insert a new node with data at the beginning of the list."""
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
    else:
        new_node.set_next(self.head)
        self.head = new_node
    
    self.length += 1
    return True
```

### Exercise 4: Insertion at the End

Implement a method to insert a new node at the end of the list.

```python
def insert_at_end(self, data):
    """Insert a new node with data at the end of the list."""
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
    else:
        current = self.head
        
        # Traverse to the last node
        while current.get_next() is not None:
            current = current.get_next()
        
        current.set_next(new_node)
    
    self.length += 1
    return True
```

### Exercise 5: Insertion at a Specific Position

Implement a method to insert a new node at a specific position in the list.

```python
def insert_at_position(self, position, data):
    """Insert a new node at the specified position (0-based)."""
    # Check if position is valid
    if position < 0 or position > self.length:
        return False
    
    # Insert at the beginning
    if position == 0:
        return self.insert_at_beginning(data)
    
    # Insert at the end
    if position == self.length:
        return self.insert_at_end(data)
    
    # Insert at the middle
    new_node = Node(data)
    current = self.head
    count = 0
    
    # Traverse to the node just before the insertion point
    while count < position - 1:
        current = current.get_next()
        count += 1
    
    new_node.set_next(current.get_next())
    current.set_next(new_node)
    
    self.length += 1
    return True
```

## Part 4: More Advanced Operations

### Exercise 6: Deletion from the Beginning

Implement a method to delete a node from the beginning of the list.

```python
def delete_from_beginning(self):
    """Delete and return the data from the first node."""
    if self.head is None:
        return None
    
    data = self.head.get_data()
    self.head = self.head.get_next()
    self.length -= 1
    
    return data
```

### Exercise 7: Deletion from the End

Implement a method to delete a node from the end of the list.

```python
def delete_from_end(self):
    """Delete and return the data from the last node."""
    if self.head is None:
        return None
    
    # If there's only one node
    if self.head.get_next() is None:
        data = self.head.get_data()
        self.head = None
        self.length -= 1
        return data
    
    current = self.head
    
    # Traverse to the second-to-last node
    while current.get_next().get_next() is not None:
        current = current.get_next()
    
    data = current.get_next().get_data()
    current.set_next(None)
    self.length -= 1
    
    return data
```

### Exercise 8: Deletion from a Specific Position

Implement a method to delete a node from a specific position in the list.

```python
def delete_from_position(self, position):
    """Delete and return data from node at the specified position."""
    # Check if position is valid
    if position < 0 or position >= self.length or self.head is None:
        return None
    
    # Delete from the beginning
    if position == 0:
        return self.delete_from_beginning()
    
    # Delete from the end
    if position == self.length - 1:
        return self.delete_from_end()
    
    # Delete from the middle
    current = self.head
    count = 0
    
    # Traverse to the node just before the deletion point
    while count < position - 1:
        current = current.get_next()
        count += 1
    
    node_to_delete = current.get_next()
    data = node_to_delete.get_data()
    
    current.set_next(node_to_delete.get_next())
    self.length -= 1
    
    return data
```

### Exercise 9: Searching

Implement a method to search for a value in the list and return its position.

```python
def search(self, data):
    """Find the position of data in the list, or return -1 if not found."""
    if self.head is None:
        return -1
    
    current = self.head
    position = 0
    
    while current is not None:
        if current.get_data() == data:
            return position
        current = current.get_next()
        position += 1
    
    return -1
```

### Exercise 10: Finding the Nth Node from the End

Implement a method to find the nth node from the end of the list.

```python
def get_nth_from_end(self, n):
    """Return the data of the nth node from the end (1-based indexing)."""
    if n <= 0 or n > self.length or self.head is None:
        return None
    
    # The nth node from the end is the (length-n+1)th node from the beginning
    position = self.length - n
    
    current = self.head
    count = 0
    
    while count < position:
        current = current.get_next()
        count += 1
    
    return current.get_data()
```

### Exercise 11: Clearing the List

Implement a method to clear all nodes from the list.

```python
def clear(self):
    """Remove all nodes from the list."""
    self.head = None
    self.length = 0
    return True
```

## Part 5: Testing Your Implementation

Let's test the basic operations we've implemented:

```python
def test_linked_list():
    """Test the LinkedList implementation with basic operations."""
    my_list = LinkedList()
    print("Created a new linked list")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")
    
    # Test insertions
    print("\nTesting insertions:")
    my_list.insert_at_beginning(5)
    print(f"After insert_at_beginning(5): {my_list.display()}")
    
    my_list.insert_at_beginning(10)
    print(f"After insert_at_beginning(10): {my_list.display()}")
    
    my_list.insert_at_end(20)
    print(f"After insert_at_end(20): {my_list.display()}")
    
    my_list.insert_at_position(1, 15)
    print(f"After insert_at_position(1, 15): {my_list.display()}")
    print(f"Current length: {my_list.list_length()}")
    
    # Test search
    print("\nTesting search:")
    print(f"Position of 15: {my_list.search(15)}")
    print(f"Position of 100: {my_list.search(100)}")
    
    # Test deletions
    print("\nTesting deletions:")
    deleted = my_list.delete_from_beginning()
    print(f"Deleted from beginning: {deleted}")
    print(f"After deletion: {my_list.display()}")
    
    deleted = my_list.delete_from_position(1)
    print(f"Deleted from position 1: {deleted}")
    print(f"After deletion: {my_list.display()}")
    
    deleted = my_list.delete_from_end()
    print(f"Deleted from end: {deleted}")
    print(f"After deletion: {my_list.display()}")
    
    # Clear the list
    print("\nTesting clear:")
    my_list.clear()
    print(f"After clear: {my_list.display()}")
    print(f"Length after clear: {my_list.list_length()}")

# Run the test
if __name__ == "__main__":
    test_linked_list()
```

## Part 6: Advanced Challenges (Optional)

Now that you've implemented and tested the basic linked list operations, here are some more advanced challenges to practice:

### Challenge 1: Cycle Detection

Implement a method to detect if a linked list has a cycle (a node points back to a previous node). For this, you can use Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm).

**Outline:**
- Use two pointers: one moving one step at a time (slow) and one moving two steps at a time (fast)
- If they ever meet, there's a cycle
- If fast reaches the end (null), there's no cycle

**Test case:**
```python
# Create a list with a cycle
cycle_list = LinkedList()
cycle_list.insert_at_end(1)
cycle_list.insert_at_end(2)
cycle_list.insert_at_end(3)
cycle_list.insert_at_end(4)

# Create a cycle by connecting the last node to the second node
last = cycle_list.head
while last.get_next() is not None:
    last = last.get_next()
second = cycle_list.head.get_next()
last.set_next(second)

# Test cycle detection
print(f"Has cycle: {cycle_list.has_cycle()}")
```

### Challenge 2: List Reversal

Implement a method to reverse the linked list in-place.

**Outline:**
- Use three pointers: previous, current, and next
- Iterate through the list, reversing each link
- Update the head to point to the new first node (previously the last)

**Test case:**
```python
# Create and reverse a list
reverse_list = LinkedList()
for i in range(1, 6):
    reverse_list.insert_at_end(i)
print(f"Original list: {reverse_list.display()}")

reverse_list.reverse()
print(f"Reversed list: {reverse_list.display()}")
```

### Challenge 3: Finding the Middle Node

Implement a method to find the middle node of the linked list using only one pass.

**Outline:**
- Use the "slow and fast pointer" technique
- Slow moves one step at a time, fast moves two steps
- When fast reaches the end, slow is at the middle

**Test case:**
```python
# Create a list and find the middle
middle_list = LinkedList()
for i in range(1, 8):
    middle_list.insert_at_end(i)
print(f"List: {middle_list.display()}")
print(f"Middle element: {middle_list.find_middle()}")
```

### Challenge 4: Removing Duplicates

Implement a method to remove duplicate values from a linked list.

**Outline:**
- Use a set to track values you've seen
- Traverse the list, removing nodes with duplicate values
- Keep track of the previous node to connect after removing a node

**Test case:**
```python
# Create a list with duplicates
dup_list = LinkedList()
for val in [1, 2, 3, 2, 4, 1, 5]:
    dup_list.insert_at_end(val)
print(f"List with duplicates: {dup_list.display()}")

dup_list.remove_duplicates()
print(f"List after removing duplicates: {dup_list.display()}")
```

### Challenge 5: Merging Sorted Lists

Implement a function to merge two sorted linked lists into a single sorted linked list.

**Outline:**
- Create a new result list
- Compare elements from both lists, adding the smaller to the result
- When one list is empty, add all remaining elements from the other list

**Test case:**
```python
# Create two sorted lists
list1 = LinkedList()
for val in [1, 3, 5, 7]:
    list1.insert_at_end(val)

list2 = LinkedList()
for val in [2, 4, 6, 8]:
    list2.insert_at_end(val)

print(f"List 1: {list1.display()}")
print(f"List 2: {list2.display()}")

merged = merge_sorted_lists(list1, list2)
print(f"Merged list: {merged.display()}")
```

## Part 7: Practical Linked List Exercises

Now that you've implemented the basic operations of a linked list, let's look at some practical exercises that use linked lists to solve real problems.

## Exercise 1: Implementing a Stack using a Linked List

A Stack is a Last-In-First-Out (LIFO) data structure. Implement a Stack using your LinkedList class:

```python
class Stack:
    """Stack implementation using a linked list (LIFO data structure)."""
    
    def __init__(self):
        self.linked_list = LinkedList()
    
    def is_empty(self):
        """Check if the stack is empty."""
        return self.linked_list.head is None
    
    def push(self, data):
        """Add an element to the top of the stack."""
        self.linked_list.insert_at_beginning(data)
    
    def pop(self):
        """Remove and return the element at the top of the stack."""
        return self.linked_list.delete_from_beginning()
    
    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()
    
    def size(self):
        """Return the number of elements in the stack."""
        return self.linked_list.length
    
    def display(self):
        """Display the elements in the stack."""
        return self.linked_list.display()
```

**Test your Stack implementation:**

```python
def test_stack():
    stack = Stack()
    print("Created a new stack")
    print(f"Stack: {stack.display()}")
    
    print("\nPushing elements:")
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}, Stack: {stack.display()}")
    
    print(f"\nTop element (peek): {stack.peek()}")
    print(f"Stack size: {stack.size()}")
    
    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}, Stack: {stack.display()}")
```

## Exercise 2: Implementing a Queue using a Linked List

A Queue is a First-In-First-Out (FIFO) data structure. Implement a Queue using your LinkedList class:

```python
class Queue:
    """Queue implementation using a linked list (FIFO data structure)."""
    
    def __init__(self):
        self.linked_list = LinkedList()
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.linked_list.head is None
    
    def enqueue(self, data):
        """Add an element to the end of the queue."""
        self.linked_list.insert_at_end(data)
    
    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        return self.linked_list.delete_from_beginning()
    
    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()
    
    def size(self):
        """Return the number of elements in the queue."""
        return self.linked_list.length
    
    def display(self):
        """Display the elements in the queue."""
        return self.linked_list.display()
```

**Test your Queue implementation:**

```python
def test_queue():
    queue = Queue()
    print("Created a new queue")
    print(f"Queue: {queue.display()}")
    
    print("\nEnqueuing elements:")
    for i in range(1, 6):
        queue.enqueue(i)
        print(f"Enqueued {i}, Queue: {queue.display()}")
    
    print(f"\nFront element (peek): {queue.peek()}")
    print(f"Queue size: {queue.size()}")
    
    print("\nDequeuing elements:")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}, Queue: {queue.display()}")
```

## Exercise 3: Polynomial Representation

Linked lists can be used to represent polynomials, where each node contains a coefficient and an exponent. Implement a PolynomialTerm class and a Polynomial class to represent polynomials:

```python
class PolynomialTerm:
    """A term in a polynomial with coefficient and exponent."""
    
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
    
    def __str__(self):
        if self.exponent == 0:
            return str(self.coefficient)
        elif self.exponent == 1:
            return f"{self.coefficient}x"
        else:
            return f"{self.coefficient}x^{self.exponent}"

class Polynomial:
    """A polynomial represented as a linked list of terms."""
    
    def __init__(self):
        self.terms = LinkedList()
    
    def add_term(self, coefficient, exponent):
        """Add a term to the polynomial."""
        # Skip terms with coefficient 0
        if coefficient == 0:
            return
            
        # Add term to the list
        term = PolynomialTerm(coefficient, exponent)
        current = self.terms.head
        prev = None
        
        # Find the right position based on exponent (descending order)
        while current is not None and current.get_data().exponent > exponent:
            prev = current
            current = current.get_next()
        
        # Check if we already have a term with this exponent
        if current is not None and current.get_data().exponent == exponent:
            # Add coefficients
            new_coef = current.get_data().coefficient + coefficient
            if new_coef != 0:
                current.get_data().coefficient = new_coef
            else:
                # If coefficient becomes 0, remove the term
                if prev is None:
                    self.terms.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                self.terms.length -= 1
        else:
            # Insert the new term at the right position
            new_node = Node(term)
            if prev is None:
                new_node.set_next(self.terms.head)
                self.terms.head = new_node
            else:
                new_node.set_next(current)
                prev.set_next(new_node)
            self.terms.length += 1
    
    def __str__(self):
        """Return string representation of the polynomial."""
        if self.terms.head is None:
            return "0"
            
        result = ""
        current = self.terms.head
        
        while current is not None:
            term = current.get_data()
            # Add + sign for positive terms (except the first one)
            if result and term.coefficient > 0:
                result += " + "
            # Add - sign for negative terms
            elif term.coefficient < 0:
                result += " - " if result else "-"
                
            # Add the term (without the sign if it's negative)
            coef = abs(term.coefficient)
            if term.exponent == 0:
                result += str(coef)
            elif term.exponent == 1:
                result += f"{coef}x"
            else:
                result += f"{coef}x^{term.exponent}"
                
            current = current.get_next()
            
        return result
```

**Test your Polynomial implementation:**

```python
def test_polynomial():
    poly = Polynomial()
    print("Created an empty polynomial")
    print(f"Polynomial: {poly}")
    
    print("\nAdding terms:")
    poly.add_term(3, 2)  # 3x^2
    print(f"After adding 3x^2: {poly}")
    
    poly.add_term(-2, 1)  # -2x
    print(f"After adding -2x: {poly}")
    
    poly.add_term(5, 0)  # 5
    print(f"After adding 5: {poly}")
    
    poly.add_term(1, 2)  # Add to existing term 3x^2 + 1x^2 = 4x^2
    print(f"After adding 1x^2: {poly}")
    
    poly.add_term(-5, 0)  # Cancel out constant term
    print(f"After adding -5: {poly}")
```

## Exercise 4: Sparse Matrix Representation

A sparse matrix is a matrix with mostly zero values. It can be efficiently represented using linked lists to store only non-zero elements. Each non-zero element is represented as a node containing the row index, column index, and value:

```python
class MatrixElement:
    """A non-zero element in a sparse matrix."""
    
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
    
    def __str__(self):
        return f"({self.row}, {self.col}, {self.value})"

class SparseMatrix:
    """A sparse matrix represented using linked lists."""
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = LinkedList()
    
    def set_element(self, row, col, value):
        """Set the value at position (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Position out of bounds")
            
        # If value is 0, remove the element if it exists
        if value == 0:
            self.remove_element(row, col)
            return
            
        # Check if element already exists
        current = self.elements.head
        prev = None
        
        while current is not None:
            elem = current.get_data()
            if elem.row == row and elem.col == col:
                # Update existing element
                elem.value = value
                return
            elif (elem.row > row) or (elem.row == row and elem.col > col):
                # Found position to insert (keep sorted by row, then column)
                break
            prev = current
            current = current.get_next()
        
        # Insert new element
        new_elem = MatrixElement(row, col, value)
        new_node = Node(new_elem)
        
        if prev is None:
            new_node.set_next(self.elements.head)
            self.elements.head = new_node
        else:
            new_node.set_next(current)
            prev.set_next(new_node)
        
        self.elements.length += 1
    
    def get_element(self, row, col):
        """Get the value at position (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Position out of bounds")
            
        current = self.elements.head
        
        while current is not None:
            elem = current.get_data()
            if elem.row == row and elem.col == col:
                return elem.value
            current = current.get_next()
            
        # If element not found, it's 0
        return 0
    
    def remove_element(self, row, col):
        """Remove the element at position (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Position out of bounds")
            
        current = self.elements.head
        prev = None
        
        while current is not None:
            elem = current.get_data()
            if elem.row == row and elem.col == col:
                # Remove the element
                if prev is None:
                    self.elements.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                self.elements.length -= 1
                return
            prev = current
            current = current.get_next()
    
    def display(self):
        """Display the matrix in a readable format."""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.get_element(i, j))
            result.append(row)
        return result
```

**Test your SparseMatrix implementation:**

```python
def test_sparse_matrix():
    matrix = SparseMatrix(4, 4)
    print("Created a 4x4 sparse matrix")
    
    # Set some elements
    matrix.set_element(0, 0, 1)
    matrix.set_element(1, 1, 2)
    matrix.set_element(2, 2, 3)
    matrix.set_element(3, 3, 4)
    matrix.set_element(0, 3, 5)
    
    print("\nMatrix after adding elements:")
    for row in matrix.display():
        print(row)
    
    # Update an element
    matrix.set_element(0, 0, 10)
    
    # Remove an element
    matrix.set_element(1, 1, 0)  # Setting to 0 removes the element
    
    print("\nMatrix after updates:")
    for row in matrix.display():
        print(row)
    
    # Print all non-zero elements
    print("\nNon-zero elements:")
    current = matrix.elements.head
    while current is not None:
        print(current.get_data())
        current = current.get_next()
```

## Part 8: Real-World Applications of Linked Lists

Linked lists are fundamental data structures used in many real-world applications:

1. **Implementation of other data structures**:
   - Stacks, queues, and hash tables (for collision handling)
   - Adjacency lists for graph representation
   - Symbol tables in compiler design

2. **Operating systems**:
   - Memory management (free lists)
   - Process scheduling queues
   - File system directories

3. **Applications**:
   - Undo functionality in text editors and applications
   - Browser's forward and backward navigation (doubly linked lists)
   - Music player playlists
   - Image galleries for navigating between images
   - Social media feeds for infinite scrolling
   - Text editors for efficient insertion/deletion

## Part 9: Time Complexity Analysis

Understanding the performance characteristics of linked lists is crucial for choosing the right data structure for your application:

| Operation                   | Linked List | Array | Dynamic Array  |
| --------------------------- | ----------- | ----- | -------------- |
| Access by index             | O(n)        | O(1)  | O(1)           |
| Insertion/deletion at start | O(1)        | O(n)  | O(n)           |
| Insertion/deletion at end   | O(n)*       | O(1)  | O(1) amortized |

## Conclusion

Linked lists are fundamental data structures that offer flexibility in dynamic memory allocation and efficient insertions/deletions at the beginning. While they have limitations in random access operations, they serve as building blocks for more complex data structures and algorithms.

The skills you've developed in this lab will help you understand not only linked lists but also the principles behind efficient data manipulation and algorithm design. Continue exploring and applying these concepts to enhance your programming toolkit!