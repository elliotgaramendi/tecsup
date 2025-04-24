# Circular Queue Implementation Guide

## Table of Contents

- [Circular Queue Implementation Guide](#circular-queue-implementation-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Understanding the Fundamental Concept](#1-understanding-the-fundamental-concept)
    - [Queue Basics](#queue-basics)
    - [The Circular Queue Solution](#the-circular-queue-solution)
    - [Core Operations](#core-operations)
  - [2. Progressive Implementations](#2-progressive-implementations)
    - [2.1 Circular Array Queue](#21-circular-array-queue)
    - [2.2 Dynamic Circular Array Queue](#22-dynamic-circular-array-queue)
    - [2.3 Circular Linked List Queue](#23-circular-linked-list-queue)
  - [3. Practical Applications](#3-practical-applications)
    - [3.1 Print Queue Simulation](#31-print-queue-simulation)
    - [3.2 Breadth-First Search](#32-breadth-first-search)
  - [4. Real-world Case Study](#4-real-world-case-study)
    - [Bank Service System](#bank-service-system)
  - [5. Technical Challenges](#5-technical-challenges)
    - [Challenge 1: Sliding Window Maximum](#challenge-1-sliding-window-maximum)
    - [Challenge 2: Rotating Array Elements](#challenge-2-rotating-array-elements)
    - [Challenge 3: Traffic Light Simulation](#challenge-3-traffic-light-simulation)
    - [Challenge 4: Task Scheduling System](#challenge-4-task-scheduling-system)
    - [Challenge 5: Circular Buffer for Streaming Data](#challenge-5-circular-buffer-for-streaming-data)
  - [6. Comparative Analysis](#6-comparative-analysis)
  - [7. Next Learning Steps](#7-next-learning-steps)
  - [8. Key Conclusions](#8-key-conclusions)

## 1. Understanding the Fundamental Concept

### Queue Basics

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle 🔄. Like a real-life queue:

- The first element added will be the first one removed 🥇
- Elements are added at the rear (enqueue) ⬅️
- Elements are removed from the front (dequeue) ➡️

When implemented with a simple array, dequeuing causes inefficiency as all elements must shift:

```
[A][B][C][D]  # Original queue
 ↑
 Dequeue

[B][C][D][ ]  # After dequeue - all elements shifted left
```

This shifting results in O(n) time complexity for the dequeue operation, making it inefficient for large queues 🐢.

### The Circular Queue Solution

A circular queue (or ring buffer) solves this problem by conceptually connecting the end of the array back to the beginning, creating a circular structure 🔄:

```
       front      rear
         ↓         ↓
Array: [A][B][C][D][_][_][_][_]

After some operations:
       rear      front
         ↓         ↓
Array: [I][J][_][_][E][F][G][H]
```

The circular approach provides constant-time O(1) operations for both enqueue and dequeue by:
- Using two pointers: `front` and `rear`
- Applying modulo arithmetic to "wrap around" the array

### Core Operations

Circular queues support these fundamental operations:

- **Enqueue**: Add an element to the rear of the queue ⬅️
  - If the queue is full, either report an overflow or resize
  - Otherwise, add the item at the rear position
  - Update the rear pointer using the modulo operation

- **Dequeue**: Remove and return the element from the front ➡️
  - If the queue is empty, report an underflow
  - Otherwise, retrieve the item at the front position
  - Update the front pointer using the modulo operation

- **IsEmpty/IsFull**: Check queue status 🔍
  - Various ways to implement, typically using size count or pointer positions

The key insight is using modulo arithmetic (%) to handle the "circular" behavior:
```
rear = (rear + 1) % capacity  // Move rear pointer forward with wrap-around
front = (front + 1) % capacity  // Move front pointer forward with wrap-around
```

## 2. Progressive Implementations

Let's explore three progressively more advanced implementations of circular queues.

### 2.1 Circular Array Queue

First, we'll implement a basic fixed-size circular queue using an array:

```python
class CircularQueue:
    """Queue implementation using a circular array."""
    
    def __init__(self, capacity=5):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size_count = 0
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise IndexError("Queue is full! 💥")
        
        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size_count += 1
    
    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference
        
        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity
        
        self.size_count -= 1
        return item
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]
    
    def size(self):
        """Return the number of items in the queue."""
        return self.size_count
    
    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"
        
        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity
        
        return f"Queue: [{', '.join(result)}]"
```

Let's visualize the circular behavior step by step:

```
Circular Queue with capacity 5:

Initial state:
[ ][ ][ ][ ][ ]
 F              F = Front, R = Rear (both -1 initially)
 R

After enqueue(A):
[A][ ][ ][ ][ ]
 F
 R

After enqueue(B):
[A][B][ ][ ][ ]
 F  R

After enqueue(C):
[A][B][C][ ][ ]
 F     R

After dequeue() (removes A):
[ ][B][C][ ][ ]
    F  R

After enqueue(D):
[ ][B][C][D][ ]
    F     R

After enqueue(E):
[ ][B][C][D][E]
    F        R

After dequeue() (removes B):
[ ][ ][C][D][E]
       F     R

After enqueue(F) - now we wrap around:
[F][ ][C][D][E]
 R     F
```

Testing our circular queue:

```python
def test_circular_queue():
    """Test the circular queue implementation."""
    queue = CircularQueue(5)
    
    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.is_full() == False, "New queue should not be full"
    
    # Test 2: Basic operations
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.size() == 2, "Queue should have 2 items"
    assert queue.peek() == "A", "Front item should be 'A'"
    
    # Test 3: Circular behavior
    queue.enqueue("C")
    queue.enqueue("D")
    queue.enqueue("E")
    assert queue.is_full() == True, "Queue should be full"
    
    # Test 4: Dequeuing and re-enqueueing (circular behavior)
    assert queue.dequeue() == "A", "Should dequeue 'A'"
    assert queue.dequeue() == "B", "Should dequeue 'B'"
    queue.enqueue("F")
    queue.enqueue("G")
    assert queue.is_full() == True, "Queue should be full again"
    
    # Test 5: Verify FIFO order after wraparound
    assert queue.dequeue() == "C", "Should dequeue 'C'"
    assert queue.dequeue() == "D", "Should dequeue 'D'"
    assert queue.dequeue() == "E", "Should dequeue 'E'"
    assert queue.dequeue() == "F", "Should dequeue 'F'"
    assert queue.dequeue() == "G", "Should dequeue 'G'"
    assert queue.is_empty() == True, "Queue should be empty after all dequeues"
    
    print("All circular queue tests passed! ✅")
```

### 2.2 Dynamic Circular Array Queue

Now let's implement a circular queue that can grow dynamically when it gets full:

```python
class DynamicCircularQueue:
    """Queue implementation with a dynamically resizing circular array."""
    
    def __init__(self, initial_capacity=5):
        """Initialize an empty queue with dynamic capacity."""
        self.capacity = initial_capacity
        self.queue = [None] * initial_capacity
        self.front = -1
        self.rear = -1
        self.size_count = 0
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        # If queue is full, resize it
        if self.is_full():
            self._resize()
        
        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size_count += 1
    
    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference
        
        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity
        
        self.size_count -= 1
        return item
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]
    
    def size(self):
        """Return the number of items in the queue."""
        return self.size_count
    
    def _resize(self):
        """Double the queue capacity."""
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        
        # Copy elements to the new array
        if not self.is_empty():
            i = 0
            index = self.front
            
            # Copy elements from front to rear
            while i < self.size_count:
                new_queue[i] = self.queue[index]
                index = (index + 1) % self.capacity
                i += 1
            
            # Update queue parameters
            self.queue = new_queue
            self.capacity = new_capacity
            self.front = 0
            self.rear = self.size_count - 1
```

The key improvement here is the `_resize()` method, which:
1. Creates a new array with double the capacity
2. Copies elements from the old array, reorganizing them to start from index 0
3. Updates the front and rear pointers

Visualizing the resize operation:

```
Before resize (capacity 5, full):
    front         rear
      ↓            ↓
    [C][D][E][A][B]

After resize (capacity 10, elements reorganized):
    front                     rear
      ↓                        ↓
    [A][B][C][D][E][_][_][_][_][_]
```

Testing our dynamic circular queue:

```python
def test_dynamic_circular_queue():
    """Test the dynamic circular queue implementation."""
    queue = DynamicCircularQueue(3)  # Start with smaller capacity
    
    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.capacity == 3, "Initial capacity should be 3"
    
    # Test 2: Filling to capacity
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.is_full() == True, "Queue should be full"
    
    # Test 3: Automatic resizing
    queue.enqueue("D")  # This should trigger resize
    assert queue.capacity == 6, "Capacity should double to 6"
    assert queue.is_full() == False, "Queue should not be full after resize"
    
    # Test 4: Verify elements after resize
    assert queue.peek() == "A", "Front element should still be 'A'"
    assert queue.size() == 4, "Queue should have 4 elements"
    
    # Test 5: Test circular behavior with resizing
    # Dequeue some items
    assert queue.dequeue() == "A", "Should dequeue 'A'"
    assert queue.dequeue() == "B", "Should dequeue 'B'"
    
    # Add more items to trigger another resize
    for item in ["E", "F", "G", "H", "I"]:
        queue.enqueue(item)
    
    # Queue should now contain: C,D,E,F,G,H,I
    assert queue.capacity == 12, "Capacity should be 12 after second resize"
    assert queue.size() == 7, "Queue should have 7 elements"
    
    # Verify all elements in FIFO order
    expected = ["C", "D", "E", "F", "G", "H", "I"]
    for expected_item in expected:
        assert queue.dequeue() == expected_item, f"Expected {expected_item}"
    
    assert queue.is_empty() == True, "Queue should be empty after all dequeues"
    
    print("All dynamic circular queue tests passed! ✅")
```

### 2.3 Circular Linked List Queue

Now, let's implement a circular queue using a circular linked list:

```python
class Node:
    """Node for a circular linked list queue."""
    
    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None


class CircularLinkedQueue:
    """Queue implementation using a circular linked list."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.rear = None  # We only need to track rear in circular linked list
        self.size_count = 0
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.rear is None
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)
        
        # If queue is empty
        if self.is_empty():
            # Point to itself to form a circle
            new_node.next = new_node
        else:
            # Insert after rear, connecting to front
            new_node.next = self.rear.next  # Connect to front
            self.rear.next = new_node       # Connect rear to new node
        
        # Update rear to the new node
        self.rear = new_node
        self.size_count += 1
    
    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        
        # If there's only one node
        if self.rear.next == self.rear:
            item = self.rear.data
            self.rear = None
        else:
            # Remove front node (next to rear)
            front = self.rear.next
            item = front.data
            self.rear.next = front.next
        
        self.size_count -= 1
        return item
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.rear.next.data  # Front is next to rear
    
    def size(self):
        """Return the number of items in the queue."""
        return self.size_count
    
    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"
        
        result = []
        current = self.rear.next  # Start from front
        
        # Traverse the circular list
        while True:
            result.append(str(current.data))
            current = current.next
            # Stop when we reach the front again
            if current == self.rear.next:
                break
        
        return f"Queue: [{', '.join(result)}]"
```

Visualizing the circular linked list:

```
Empty queue:
rear = None

After enqueue(A):
       ┌──────┐
       ↓      │
rear → [A]────┘

After enqueue(B):
       ┌───────────┐
       ↓           │
      [A] ← [B] ← rear
       │           ↑
       └───────────┘

After enqueue(C):
       ┌───────────────┐
       ↓               │
      [A] ← [B] ← [C] ← rear
       │               ↑
       └───────────────┘

After dequeue() (removes A):
       ┌───────────┐
       ↓           │
      [B] ← [C] ← rear
       │           ↑
       └───────────┘
```

Testing our circular linked list queue:

```python
def test_circular_linked_queue():
    """Test the circular linked list queue implementation."""
    queue = CircularLinkedQueue()
    
    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.size() == 0, "Queue size should be 0"
    
    # Test 2: Basic operations
    queue.enqueue(100)
    queue.enqueue(200)
    assert queue.size() == 2, "Queue should have 2 items"
    assert queue.peek() == 100, "Front item should be 100"
    
    # Test 3: FIFO behavior
    assert queue.dequeue() == 100, "Should dequeue 100"
    assert queue.dequeue() == 200, "Should dequeue 200"
    assert queue.is_empty() == True, "Queue should be empty"
    
    # Test 4: Error handling
    try:
        queue.dequeue()
        assert False, "Should raise error on empty queue"
    except IndexError:
        pass  # Expected behavior
    
    # Test 5: More complex operations
    for i in range(1, 6):
        queue.enqueue(i)
    
    assert queue.size() == 5, "Queue should have 5 items"
    
    # Check circular structure works correctly
    for i in range(1, 6):
        assert queue.dequeue() == i, f"Expected {i}"
    
    print("All circular linked queue tests passed! ✅")
```

## 3. Practical Applications

Let's explore practical applications of circular queues.

### 3.1 Print Queue Simulation

A printer queue is a perfect example of a circular queue in action:

```python
class PrintJob:
    """Represent a print job with name and pages."""
    
    def __init__(self, name, pages):
        """Initialize a print job."""
        self.name = name
        self.pages = pages
    
    def __str__(self):
        """Return a string representation."""
        return f"{self.name} ({self.pages} pages)"


class Printer:
    """Simulate a printer that processes jobs from a queue."""
    
    def __init__(self, pages_per_minute):
        """Initialize a printer with a processing rate."""
        self.page_rate = pages_per_minute
        self.current_job = None
        self.time_remaining = 0
        self.total_jobs = 0
        self.total_pages = 0
    
    def is_busy(self):
        """Check if the printer is currently busy."""
        return self.current_job is not None
    
    def start_next_job(self, job):
        """Start a new print job."""
        self.current_job = job
        # Calculate time to complete (in seconds)
        self.time_remaining = job.pages * 60 / self.page_rate
        print(f"Started printing: {job} 🖨️")
    
    def tick(self):
        """Simulate one second passing."""
        if self.is_busy():
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                print(f"Finished printing: {self.current_job} ✅")
                self.total_jobs += 1
                self.total_pages += self.current_job.pages
                self.current_job = None
                return True  # Job completed
        return False  # No job completed


def simulate_print_queue():
    """Simulate a printer processing jobs from a queue."""
    # Create print queue
    print_queue = CircularQueue(10)  # Using our circular queue
    
    # Create a printer (10 pages/minute)
    printer = Printer(10)
    
    # Create some print jobs
    jobs = [
        PrintJob("Research Paper", 8),
        PrintJob("Resume", 2),
        PrintJob("Presentation Slides", 15),
        PrintJob("Meeting Notes", 4),
        PrintJob("Financial Report", 12),
    ]
    
    print("Starting printer simulation... 🖨️")
    # Add jobs to the queue
    for job in jobs:
        print(f"Adding job to queue: {job}")
        print_queue.enqueue(job)
    
    # Simulate time passing (180 seconds = 3 minutes)
    for second in range(1, 181):
        # Check if printer is ready for next job
        if not printer.is_busy() and not print_queue.is_empty():
            next_job = print_queue.dequeue()
            printer.start_next_job(next_job)
        
        # Simulate one second of time
        printer.tick()
        
        # Check if all jobs are done
        if print_queue.is_empty() and not printer.is_busy():
            print(f"All jobs completed at second {second}! ✨")
            print(f"Total jobs printed: {printer.total_jobs}")
            print(f"Total pages printed: {printer.total_pages}")
            break
        
        # Print status every 30 seconds
        if second % 30 == 0:
            jobs_left = print_queue.size()
            print(f"Time: {second}s, Jobs in queue: {jobs_left}")
```

### 3.2 Breadth-First Search

Circular queues are essential for breadth-first search (BFS) algorithms:

```python
def breadth_first_search(graph, start_node):
    """Perform breadth-first search on a graph using a circular queue."""
    # Create a queue with sufficient capacity
    queue = CircularQueue(len(graph))
    visited = set()  # Track visited nodes
    
    # Start with the start node
    queue.enqueue(start_node)
    visited.add(start_node)
    
    result = []  # Store traversal order
    
    print(f"Starting BFS from node {start_node} 🔍")
    
    # Process nodes in breadth-first order
    while not queue.is_empty():
        # Get the next node to process
        current = queue.dequeue()
        result.append(current)
        print(f"Visiting: {current} 🚶")
        
        # Visit all unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                print(f"  Discovered: {neighbor} 👀")
                queue.enqueue(neighbor)
                visited.add(neighbor)
    
    return result


def demonstrate_bfs():
    """Demonstrate breadth-first search on a simple graph."""
    # Create a simple graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Graph structure:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {', '.join(neighbors)}")
    
    # Perform BFS starting from node 'A'
    traversal = breadth_first_search(graph, 'A')
    
    print("\nBFS traversal order:")
    print(" -> ".join(traversal))
```

Visual representation of the graph:

```
    A --- B --- D
    |     |
    |     |
    C --- F --- E
```

## 4. Real-world Case Study

### Bank Service System

Let's implement a bank service system with multiple queues:

```python
class Customer:
    """Represent a bank customer."""
    
    def __init__(self, id, service_type):
        """Initialize a customer with ID and service type."""
        self.id = id
        self.service_type = service_type  # 'deposit', 'withdrawal', 'info'
        self.arrival_time = 0
        self.priority = 2  # Default priority (1=high, 3=low)
        
        # Set priority based on service type
        if service_type == 'withdrawal':
            self.priority = 1  # Higher priority
        elif service_type == 'info':
            self.priority = 3  # Lower priority
    
    def __str__(self):
        """Return a string representation of the customer."""
        return f"Customer #{self.id} - {self.service_type} (Priority {self.priority})"


class BankServiceSystem:
    """Manage bank customer service using circular queues."""
    
    def __init__(self):
        """Initialize the bank service system."""
        # Separate queues for different services
        self.deposit_queue = CircularQueue(10)
        self.withdrawal_queue = CircularQueue(10)
        self.info_queue = CircularQueue(10)
        
        self.current_time = 0
        self.customers_served = 0
        self.average_wait_time = 0
        self.total_wait_time = 0
    
    def add_customer(self, customer):
        """Add a new customer to the appropriate queue."""
        # Set arrival time
        self.current_time += 1
        customer.arrival_time = self.current_time
        
        # Add to the appropriate queue based on service type
        if customer.service_type == 'deposit':
            self.deposit_queue.enqueue(customer)
            print(f"Customer added to deposit queue: {customer} 💰")
            
        elif customer.service_type == 'withdrawal':
            self.withdrawal_queue.enqueue(customer)
            print(f"Customer added to withdrawal queue: {customer} 💸")
            
        else:  # info
            self.info_queue.enqueue(customer)
            print(f"Customer added to information queue: {customer} ℹ️")
    
    def serve_next_customer(self):
        """Serve the next customer based on priority."""
        # First try to serve withdrawal (highest priority)
        if not self.withdrawal_queue.is_empty():
            return self._serve_from_queue(self.withdrawal_queue, "withdrawal")
        
        # Then try deposit
        elif not self.deposit_queue.is_empty():
            return self._serve_from_queue(self.deposit_queue, "deposit")
        
        # Finally try info
        elif not self.info_queue.is_empty():
            return self._serve_from_queue(self.info_queue, "info")
        
        else:
            print("No customers waiting! 🕒")
            return None
    
    def _serve_from_queue(self, queue, queue_name):
        """Serve a customer from the specified queue."""
        customer = queue.dequeue()
        self.customers_served += 1
        wait_time = self.current_time - customer.arrival_time
        
        # Update statistics
        self.total_wait_time += wait_time
        self.average_wait_time = self.total_wait_time / self.customers_served
        
        print(f"Serving {queue_name}: {customer} (waited {wait_time} time units) ✅")
        return customer
    
    def get_queue_status(self):
        """Return the current status of all service queues."""
        return {
            'deposit': self.deposit_queue.size(),
            'withdrawal': self.withdrawal_queue.size(),
            'info': self.info_queue.size(),
            'total_waiting': (self.deposit_queue.size() + 
                             self.withdrawal_queue.size() + 
                             self.info_queue.size()),
            'total_served': self.customers_served,
            'average_wait_time': round(self.average_wait_time, 2)
        }


def simulate_bank_service():
    """Simulate a bank's customer service operations."""
    # Create a bank service system
    bank = BankServiceSystem()
    
    # Create some customers
    customers = [
        Customer(101, 'deposit'),
        Customer(102, 'withdrawal'),
        Customer(103, 'info'),
        Customer(104, 'deposit'),
        Customer(105, 'info'),
        Customer(106, 'withdrawal'),
        Customer(107, 'deposit')
    ]
    
    # Add all customers to the system
    print("Customers arriving at the bank...")
    for customer in customers:
        bank.add_customer(customer)
    
    # Display queue status
    status = bank.get_queue_status()
    print("\nCurrent Queue Status:")
    print(f"Withdrawal Queue: {status['withdrawal']} customers 💸")
    print(f"Deposit Queue: {status['deposit']} customers 💰")
    print(f"Information Queue: {status['info']} customers ℹ️")
    print(f"Total Waiting: {status['total_waiting']} customers")
    
    # Simulate serving customers
    print("\nServing customers by priority...")
    
    # Serve customers until all queues are empty
    while status['total_waiting'] > 0:
        bank.serve_next_customer()
        status = bank.get_queue_status()
    
    # Final statistics
    print("\nFinal Queue Status:")
    print(f"Total Served: {status['total_served']} customers ✅")
    print(f"Average Wait Time: {status['average_wait_time']} time units ⏱️")
```

This bank service system demonstrates how circular queues can efficiently manage customers with different priorities, ensuring higher priority customers (like withdrawals) are served first. 🏦

## 5. Technical Challenges

Here are five unique challenges to test and expand your understanding of circular queues.

### Challenge 1: Sliding Window Maximum

**Problem**: Given an array of integers and a window size k, find the maximum element in each sliding window as it moves from left to right.

**Example**:
- Input: [1, 3, -1, -3, 5, 3, 6, 7], k=3
- Output: [3, 3, 5, 5, 6, 7]

**Approach**:
- Use a circular queue to maintain elements in the current window
- For each new element entering the window, remove elements smaller than it from the rear
- The front of the queue always contains the maximum for the current window
- Time complexity: O(n) where n is the array length

### Challenge 2: Rotating Array Elements

**Problem**: Rotate an array of n elements to the right by k steps. For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

**Approach**:
- Use a circular queue to efficiently handle the rotation
- First enqueue all elements into the circular queue
- Then dequeue and re-enqueue k times
- Finally, extract the elements in the new order
- Time complexity: O(n)

### Challenge 3: Traffic Light Simulation

**Problem**: Create a simulation of traffic flow through an intersection with traffic lights. Vehicles arrive at fixed intervals and must wait at red lights.

**Approach**:
- Use circular queues to represent each lane of traffic
- Implement a traffic light cycle that alternates between directions
- Track statistics like average wait time and maximum queue length
- Apply circular queue's FIFO behavior to ensure fairness in traffic flow

### Challenge 4: Task Scheduling System

**Problem**: Design a round-robin task scheduler that allocates CPU time slices to processes in a circular manner.

**Approach**:
- Use a circular queue to store processes waiting for CPU time
- Each process gets a fixed time quantum
- After execution, if a process needs more time, it goes back to the queue
- Continue until all processes complete
- Measure metrics like turnaround time and waiting time

### Challenge 5: Circular Buffer for Streaming Data

**Problem**: Implement a circular buffer for a data stream where you need to keep only the most recent N elements.

**Approach**:
- Create a fixed-size circular array
- When the buffer is full, new data overwrites the oldest data
- Implement methods to add data, get the latest N items, and calculate statistics
- Optimize for constant-time operations regardless of data volume

## 6. Comparative Analysis

Here's how different circular queue implementations compare:

| Implementation             | Time Complexity                     | Space Complexity | Advantages                                                               | Disadvantages                                               | Best Use Cases                                                              |
| -------------------------- | ----------------------------------- | ---------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Circular Array Queue**   | • Enqueue: O(1)<br>• Dequeue: O(1)  | O(n)             | • Fast operations ⚡<br>• Memory efficiency 📦<br>• Contiguous memory 🧩    | • Fixed capacity 📏<br>• Wasted space when partially full 🗑️  | • Fixed-size applications 📏<br>• Performance-critical systems ⚙️             |
| **Dynamic Circular Queue** | • Enqueue: O(1)*<br>• Dequeue: O(1) | O(n)             | • Fast operations ⚡<br>• Dynamic size ♾️<br>• No overflow issues 🔄        | • Resize operations occasionally O(n) ⏳<br>• More complex 🧩 | • Unknown size requirements 📏<br>• Balance of performance and flexibility 🔄 |
| **Circular Linked Queue**  | • Enqueue: O(1)<br>• Dequeue: O(1)  | O(n)             | • Simpler circular logic 🧩<br>• Dynamic size ♾️<br>• No resizing needed 📈 | • Extra memory per node 🧠<br>• Poorer cache locality 🐢      | • Frequent insertions/deletions 🔄<br>• Memory-constrained environments 💾    |

Key points to consider when choosing an implementation:

1. **Memory Usage**: Circular arrays use contiguous memory, which is more cache-friendly but can waste space. Linked lists use exactly the space needed but have overhead per node.

2. **Size Requirements**: If you know the maximum size in advance, circular arrays are more efficient. For unknown size, dynamic arrays or linked lists are better.

3. **Operation Patterns**: For balanced enqueue/dequeue patterns, all implementations perform well. For intermittent batches, consider how the data structure handles emptying and refilling.

4. **Implementation Complexity**: Circular arrays require careful index management with modulo arithmetic. Circular linked lists need only one pointer (rear) but require careful handling when inserting and removing.

The circular pattern provides consistent O(1) operations with any implementation, making circular queues excellent for performance-critical applications like buffers, schedulers, and real-time systems. 🎯

## 7. Next Learning Steps

After mastering circular queues, consider these advancement paths:

1. **Advanced Queue Variants** 🔄:
   - Priority Queue: Elements processed by priority, not FIFO order
   - Double-ended Queue (Deque): Add/remove from both ends
   - Blocking Queue: Thread-safe with blocking operations
   - Delay Queue: Elements available after delay expiration

2. **Real-time Applications** 🧠:
   - Stream Processing: Handling continuous data flows
   - Event Loops: Managing asynchronous events in systems
   - Bounded Buffer Problem: Producer-consumer patterns
   - Rate Limiting: Controlling request frequency

3. **Performance Optimization** ⚡:
   - Lock-free Circular Queues: For concurrent access
   - Memory-aligned Structures: For improved cache performance
   - Batched Operations: Amortizing costs across multiple elements
   - Custom Memory Allocators: For specialized queue implementations

4. **Related Data Structures** 📊:
   - Ring Buffers with Multiple Readers/Writers
   - Circular Arrays in Signal Processing
   - Cyclic Graphs and Their Algorithms
   - Circular Lists for Continuous Processing

## 8. Key Conclusions

Circular queues are a powerful optimization of the basic queue data structure, offering several important advantages:

1. **Efficient Space Utilization**: Circular queues reuse space that becomes available after dequeue operations, preventing the memory waste that occurs in linear queue implementations. 🔄

2. **Constant-time Operations**: Both enqueue and dequeue operations have O(1) time complexity, making circular queues ideal for performance-critical applications. ⚡

3. **Implementation Flexibility**: Whether implemented as arrays or linked lists, circular queues can be adapted to different requirements regarding size constraints, memory usage, and operation patterns. 🧩

4. **Real-world Applicability**: The circular queue pattern naturally models many real-world systems that involve cyclic processing, scheduling, or buffering. 🌐

5. **Fundamental Building Block**: Circular queues serve as the foundation for more complex data structures and algorithms, particularly in operating systems, networking, and embedded systems. 🏗️

Understanding circular queues thoroughly adds an essential tool to your programming toolkit that offers both theoretical elegance and practical efficiency. By mastering the circular structure pattern, you'll be better equipped to design systems that require continuous processing with minimal overhead. 🎓