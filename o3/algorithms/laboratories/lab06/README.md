# 🔄 Circular Queue Implementation Guide

A comprehensive Python implementation of circular queues with advanced applications and practical exercises.

## 🚀 Overview

This project explores circular queue data structures - an efficient implementation of the queue abstract data type that follows the First-In-First-Out (FIFO) principle. Circular queues optimize memory usage by reusing array space when items are dequeued, making them ideal for high-performance applications.

## ✨ Features

- Multiple circular queue implementations:
  - Fixed-size circular array queue 🔄
  - Dynamic circular array queue with auto-resizing 📏
  - Circular linked list queue with single pointer 🔗

- Real-world applications:
  - Print queue system simulation 🖨️
  - Breadth-first search for graph traversal 🔍
  - Bank service system with priority handling 🏦

- Advanced technical exercises:
  - Sliding window maximum algorithm 🪟
  - Array rotation using circular queues 🔄
  - Traffic light simulation 🚦
  - Round-robin task scheduling ⏱️
  - Circular buffer for streaming data 📊

## 🔍 Implementation Details

### Core Circular Queue Operations

All implementations support these fundamental operations:

1. `enqueue(item)`: Add an item to the rear of the queue ⬅️
2. `dequeue()`: Remove and return the item from the front ➡️
3. `peek()`: View the front item without removing it 👀
4. `is_empty()`: Check if the queue is empty 🔍
5. `is_full()`: Check if the queue has reached capacity 📏
6. `size()`: Get the number of elements in the queue 📊

### Key Implementation Techniques

- **Modulo Arithmetic** (`%`): The "magic" that enables circular behavior by wrapping indices around the array when they reach the end 🔄
- **Front and Rear Pointers**: Track the queue boundaries without needing to shift elements 📍
- **Dynamic Resizing**: Automatically grow the queue when it gets full while maintaining the circular property 📈
- **Circular Linked Lists**: Implement a queue with just a single rear pointer by forming a circular connection 🔁

## 💻 Usage Examples

### Basic Usage 🔰
```python
# Create a circular queue with capacity 5
queue = CircularQueue(5)

# Add elements 📥
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

# Remove elements 📤
first = queue.dequeue()  # Returns "A"
second = queue.dequeue()  # Returns "B"

# Check front element without removing 👀
front = queue.peek()  # Returns "C"
```

### Using for Process Scheduling ⏱️
```python
# Create a circular queue to hold processes
process_queue = CircularQueue(10)

# Add processes to the queue
process_queue.enqueue(Process(1, 10))
process_queue.enqueue(Process(2, 5))
process_queue.enqueue(Process(3, 8))

# Process queue in FIFO order with round-robin scheduling
while not process_queue.is_empty():
    current_process = process_queue.dequeue()
    
    # Execute process for a time slice
    executed_time = min(time_quantum, current_process.remaining_time)
    current_process.remaining_time -= executed_time
    
    # If not finished, re-queue for next round
    if current_process.remaining_time > 0:
        process_queue.enqueue(current_process)
```

## 🏃‍♂️ Running the Project

```bash
# Run all tests and examples
python main.py

# Expected output includes test results for all implementations and applications
```

## 📊 Performance Comparison

| Implementation | Enqueue | Dequeue | Memory Usage | Dynamic Resizing           |
| -------------- | ------- | ------- | ------------ | -------------------------- |
| Circular Array | O(1) ⚡  | O(1) ⚡  | O(n) 📦       | No ❌                       |
| Dynamic Array  | O(1)* ⚡ | O(1) ⚡  | O(n) 📦       | Yes ✅ (O(n) when resizing) |
| Linked List    | O(1) ⚡  | O(1) ⚡  | O(n) 📦       | Yes ✅ (always dynamic)     |

\* Amortized O(1), occasionally O(n) during resize operations

### 🧮 Memory Efficiency:
- **Circular Array**: 100% utilization after elements wrap around 🔄
- **Dynamic Array**: May have unused space after resizing 📏
- **Linked List**: Higher overhead per element due to pointers 🔗

### ⏱️ Operational Speed:
- **Circular Array**: Fastest for fixed-size applications 🚀
- **Dynamic Array**: Slight overhead during resize operations 📈
- **Linked List**: Slightly slower due to pointer traversal 🐢

## 🧩 Applications

Circular queues are excellent for:

- **Print Job Management** 🖨️: Managing pending print jobs in an efficient manner
- **Process Scheduling** ⏱️: Implementing round-robin CPU scheduling
- **Traffic Control** 🚦: Simulating traffic flow at intersections
- **Buffer Management** 📊: Implementing streaming data buffers
- **Breadth-First Search** 🔍: Efficient graph traversal algorithms
- **Banking Systems** 🏦: Customer service queue management

## 🔗 Related Resources
- [Queue Data Structure](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) 📚
- [Circular Buffer](https://en.wikipedia.org/wiki/Circular_buffer) 🔄
- [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) 🔍
- [Round-Robin Scheduling](https://en.wikipedia.org/wiki/Round-robin_scheduling) ⏱️

---
Created with ❤️ by a world-class data structures expert 🧠