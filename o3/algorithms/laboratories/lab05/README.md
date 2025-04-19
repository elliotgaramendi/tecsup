# Queue Data Structure Implementation

A comprehensive implementation of queue data structures with various applications and practical exercises.

## Table of Contents

- [Queue Data Structure Implementation](#queue-data-structure-implementation)
  - [Table of Contents](#table-of-contents)
  - [1. Understanding the Concept](#1-understanding-the-concept)
    - [Basic Operations](#basic-operations)
    - [Visual Representation](#visual-representation)
    - [Time Complexity](#time-complexity)
  - [2. Queue Implementations](#2-queue-implementations)
    - [2.1 Simple List-based Implementation](#21-simple-list-based-implementation)
    - [2.2 Circular Array Implementation](#22-circular-array-implementation)
    - [2.3 Linked List Implementation](#23-linked-list-implementation)
  - [3. Practical Applications](#3-practical-applications)
    - [3.1 Print Queue Simulation](#31-print-queue-simulation)
    - [3.2 Breadth-First Search](#32-breadth-first-search)
  - [4. Real-world Case: Customer Service System](#4-real-world-case-customer-service-system)
  - [5. Practical Exercises](#5-practical-exercises)
    - [Exercise 1: Queue with Two Stacks](#exercise-1-queue-with-two-stacks)
    - [Exercise 2: Level Order Traversal](#exercise-2-level-order-traversal)
    - [Exercise 3: Hot Potato Game](#exercise-3-hot-potato-game)
    - [Exercise 4: Sliding Window Maximum](#exercise-4-sliding-window-maximum)
    - [Exercise 5: Supermarket Checkout System](#exercise-5-supermarket-checkout-system)
  - [6. Implementation Comparison](#6-implementation-comparison)
  - [7. Next Steps](#7-next-steps)
  - [8. Usage](#8-usage)
  - [9. Testing](#9-testing)
  - [10. Contributing](#10-contributing)
  - [11. License](#11-license)

## 1. Understanding the Concept

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle 🔄, similar to a real-life queue or line of people waiting. In a queue:

- The first element added is the first one to be removed
- New elements are added at the rear (or end) of the queue 🔚
- Elements are removed from the front of the queue 🔝

### Basic Operations

- **Enqueue**: Add an element to the rear of the queue ⬅️
- **Dequeue**: Remove and return the element from the front of the queue ➡️
- **Peek/Front**: View the front element without removing it 👀
- **isEmpty**: Check if the queue is empty 🔍
- **size**: Get the number of elements in the queue 📏

### Visual Representation

```
     Dequeue ←—— Front [ A B C D ] Rear ←—— Enqueue
     (Remove)                            (Add)
```

### Time Complexity

For an efficient queue implementation:
- Enqueue: O(1) ⚡
- Dequeue: O(1) ⚡
- Peek: O(1) ⚡
- isEmpty: O(1) ⚡
- size: O(1) ⚡

## 2. Queue Implementations

This project includes three different queue implementations, each with its own advantages and trade-offs:

### 2.1 Simple List-based Implementation

The simplest approach using Python's built-in list data structure.

**Pros**:
- Easy to implement 🔧
- Flexible size 📏
- Uses built-in Python operations 🧰

**Cons**:
- O(n) time complexity for dequeue operations ⏱️
- Less efficient for large queues 📉

```python
class SimpleQueue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self.items.pop(0)  # O(n) operation
```

### 2.2 Circular Array Implementation

Using a fixed-size array with circular indexing to achieve better performance.

**Pros**:
- O(1) time complexity for all operations ⚡
- Better memory locality 📦
- Predictable performance 📊

**Cons**:
- Fixed capacity 📏
- More complex implementation 🧩
- Potentially wasted space if not full 🗑️

```python
class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size_count = 0
        
    def enqueue(self, item):
        # Implementation handles circular behavior
        # when rear reaches the end of array
```

### 2.3 Linked List Implementation

Using a linked list for dynamic sizing and consistent performance.

**Pros**:
- O(1) time complexity for all operations ⚡
- Dynamic size ♾️
- No wasted space 📊

**Cons**:
- Extra memory per node 🧠
- Poorer cache locality compared to arrays 🐢

```python
class LinkedQueue:
    def __init__(self):
        self.front = None  # For dequeue operations
        self.rear = None   # For enqueue operations
        self.size_count = 0
        
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
```

## 3. Practical Applications

### 3.1 Print Queue Simulation

A simulation of a printer processing print jobs in FIFO order.

```python
class PrintJob:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages
        
class Printer:
    def __init__(self, pages_per_minute):
        self.page_rate = pages_per_minute
        self.current_job = None
        self.time_remaining = 0
```

This simulation demonstrates:
- How print jobs are queued 📄
- How processing time is calculated ⏱️
- FIFO order of job processing 🔄

### 3.2 Breadth-First Search

Using a queue for level-by-level exploration of a graph.

```python
def breadth_first_search(graph, start_node):
    queue = LinkedQueue()
    visited = set()
    
    queue.enqueue(start_node)
    visited.add(start_node)
    
    while not queue.is_empty():
        current = queue.dequeue()
        # Process current node
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.enqueue(neighbor)
                visited.add(neighbor)
```

This demonstrates how queues enable level-by-level traversal in graphs 🕸️, essential for:
- Finding shortest paths
- Web crawling
- Network analysis

## 4. Real-world Case: Customer Service System

A comprehensive example of using multiple queues to handle different types of customer service requests.

```python
class CustomerServiceSystem:
    def __init__(self):
        # Separate queues for different types of issues
        self.technical_queue = LinkedQueue()
        self.billing_queue = LinkedQueue()
        self.general_queue = LinkedQueue()
```

This system demonstrates:
- Queue-based priority handling 🎯
- Multiple queue management 📋
- Wait time tracking ⏱️
- Service metrics collection 📊

## 5. Practical Exercises

### Exercise 1: Queue with Two Stacks

Implement a queue using two stacks to achieve O(1) amortized time complexity.

```python
class QueueWithTwoStacks:
    def __init__(self):
        self.stack_new = []  # For enqueue operations
        self.stack_old = []  # For dequeue operations
        
    def enqueue(self, item):
        self.stack_new.append(item)
        
    def dequeue(self):
        # If old stack is empty, shift all items from new stack
        if not self.stack_old:
            while self.stack_new:
                self.stack_old.append(self.stack_new.pop())
                
        if not self.stack_old:
            raise IndexError("Queue is empty")
            
        return self.stack_old.pop()
```

This exercise demonstrates:
- Creative data structure composition 🧩
- Stack-based FIFO implementation 🔄
- Amortized time complexity analysis ⏱️

### Exercise 2: Level Order Traversal

Using a queue to process a binary tree level by level.

```python
def level_order_traversal(root):
    if not root:
        return []
        
    result = []
    queue = LinkedQueue()
    queue.enqueue(root)
    
    while not queue.is_empty():
        node = queue.dequeue()
        result.append(node.value)
        
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
            
    return result
```

This exercise demonstrates the fundamental role queues play in tree traversal algorithms 🌳.

### Exercise 3: Hot Potato Game

A fun simulation of the Hot Potato game using a queue for players. The game simulates passing an object around a circle of players, and after a random number of passes, the player holding the object is eliminated.

```python
def hot_potato(names, max_passes):
    queue = LinkedQueue()
    
    # Add all players to the queue
    for name in names:
        queue.enqueue(name)
        
    # Continue until only one player remains
    while queue.size() > 1:
        # Simulate passing the potato
        for _ in range(random.randint(1, max_passes)):
            queue.enqueue(queue.dequeue())
            
        # Remove the player holding the potato
        eliminated = queue.dequeue()
        
    # Return the winner
    return queue.dequeue()
```

This exercise demonstrates:
- Queue rotation operations 🔄
- Simulation algorithms 🎮
- Game logic implementation using queues 🎯

### Exercise 4: Sliding Window Maximum

Finding maximum elements in fixed-size sliding windows of an array using a deque (double-ended queue).

```python
def sliding_window_maximum(nums, k):
    result = []
    deque = Deque()  # Using a double-ended queue
    
    # Process the first window
    for i in range(k):
        # Remove smaller elements from the back
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()
        
        deque.add_rear(i)
    
    # Process the rest of the array
    for i in range(k, len(nums)):
        # Add maximum of previous window to result
        result.append(nums[deque.peek_front()])
        
        # Remove elements outside the current window
        while not deque.is_empty() and deque.peek_front() <= i - k:
            deque.remove_front()
            
        # Remove smaller elements
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()
            
        deque.add_rear(i)
        
    # Add the maximum for the last window
    result.append(nums[deque.peek_front()])
    
    return result
```

This exercise demonstrates:
- Advanced queue variations (deque) 🔄
- Efficient algorithm design using queues 📊
- Window-based data processing techniques 🪟

### Exercise 5: Supermarket Checkout System

A simulation of a supermarket with multiple checkout lanes, allowing customers to choose the shortest queue.

```python
class Supermarket:
    def __init__(self):
        # Create multiple checkout lanes
        self.lanes = [
            CheckoutLane(1, 5),  # 5 items per time unit
            CheckoutLane(2, 3),  # 3 items per time unit
            CheckoutLane(3, 7)   # 7 items per time unit (express lane)
        ]
        
    def select_best_lane(self, customer):
        # Find lane with minimum estimated wait time
        best_lane = None
        min_wait_time = float('inf')
        
        for lane in self.lanes:
            # Calculate estimated wait time
            estimated_wait = lane.calculate_wait_time()
            
            if estimated_wait < min_wait_time:
                min_wait_time = estimated_wait
                best_lane = lane
                
        return best_lane
```

This exercise demonstrates:
- Multiple queue management 🗂️
- Queue selection algorithms 🔍
- Simulation of real-world systems 🏪
- Performance metrics and analysis 📊

## 6. Implementation Comparison

Understanding the strengths and weaknesses of different queue implementations helps choose the right one for specific use cases.

| Implementation            | Time Complexity                              | Space Complexity | Advantages                                                                       | Disadvantages                                                                    | Best Use Cases                                                                          |
| ------------------------- | -------------------------------------------- | ---------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **List-based Queue**      | • Enqueue: O(1)<br>• Dequeue: O(n)           | O(n)             | • Simple to code 🔧<br>• Flexible size 📏<br>• Built-in methods 🧰                  | • Slow dequeue ⏳<br>• Inefficient for large queues 📉                             | • Small queues 🔹<br>• Educational purposes 📚<br>• Quick prototyping 🔧                   |
| **Circular Array Queue**  | • Enqueue: O(1)<br>• Dequeue: O(1)           | O(n)             | • Fast operations ⚡<br>• Better memory locality 📦<br>• Predictable performance 📊 | • Fixed capacity 📏<br>• Complex implementation 🧩<br>• Wasted space if not full 🗑️ | • Fixed-size applications 📏<br>• Performance-critical systems ⚙️<br>• Embedded systems 🔌 |
| **Linked List Queue**     | • Enqueue: O(1)<br>• Dequeue: O(1)           | O(n)             | • Dynamic size ♾️<br>• No overflow issues 🔄<br>• No wasted space 📊                | • Extra memory per node 🧠<br>• Poorer cache locality 🐢                           | • Unknown size queues ❓<br>• Memory-tight environments 💾<br>• Frequent size changes 📈   |
| **Queue with Two Stacks** | • Enqueue: O(1)<br>• Dequeue: O(1) amortized | O(n)             | • Easy to implement with stacks 🧱<br>• Flexible size 📏                           | • Occasional O(n) dequeue ⏳<br>• Extra memory operations 🔄                       | • When stacks are available 📚<br>• Interview questions 💻<br>• Learning exercises 🧩      |

The performance comparison implemented in this project measures actual execution times of different queue implementations to provide empirical evidence of their performance characteristics.

## 7. Next Steps

After mastering the basics of queues, consider these advancement paths:

1. **Explore Queue Variations** 🔄:
   - Priority Queue: Elements processed by priority, not arrival order ⭐
   - Deque (Double-Ended Queue): Add/remove from both ends 🔄
   - Blocking Queue: Thread-safe with blocking operations 🔒
   - Delay Queue: Elements available after delay expiration ⏰

2. **Study Advanced Applications** 🧠:
   - Graph Algorithms: Implement Dijkstra's or A* pathfinding 🗺️
   - Message Brokers: Build communication systems between services 📨
   - Job Schedulers: Manage task execution in operating systems ⚙️
   - Cache Systems: Implement LRU caches with queues 💾

3. **Performance Optimization** ⚡:
   - Memory Optimization: Minimize memory footprint 🧩
   - Concurrent Queues: Thread-safe implementations 🧵
   - Lock-free Queues: Advanced concurrency techniques 🔓
   - Benchmarking: Measure and compare implementations 📊

## 8. Usage

To use the queue implementations in your own project:

```python
# Import the desired queue implementation
from main import SimpleQueue, CircularQueue, LinkedQueue

# Create a new queue
queue = LinkedQueue()

# Add elements
queue.enqueue("First element")
queue.enqueue("Second element")

# Process elements
while not queue.is_empty():
    element = queue.dequeue()
    print(f"Processing: {element}")
```

To run the example applications and tests:

```bash
python main.py
```

This will execute all the queue implementations, practical applications, and exercises with their respective tests.

## 9. Testing

Each queue implementation and application includes comprehensive tests that demonstrate their functionality. The tests cover:

- Basic operations (enqueue, dequeue, peek, isEmpty, size)
- Edge cases (empty queues, full queues)
- Performance measurements
- Practical application scenarios

Run the tests with:

```bash
python main.py
```

## 10. Contributing

Contributions to improve the implementations or add new queue variations are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Implement your changes
4. Add tests for your implementation
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 11. License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Created with ❤️ as an educational resource for data structures and algorithms learning.