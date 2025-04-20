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

- **Modulo Arithmetic** (`%`): The "magic" that enables circular behavior by wrapping indices around the array when they reach the end
- **Front and Rear Pointers**: Track the queue boundaries without needing to shift elements
- **Dynamic Resizing**: Automatically grow the queue when it gets full while maintaining the circular property
- **Circular Linked Lists**: Implement a queue with just a single rear pointer by forming a circular connection

## 💻 Usage

```python
# Example: Using a circular queue for a process scheduler
from main import CircularQueue, Process

# Create a circular queue to hold processes
process_queue = CircularQueue(10)

# Add processes to the queue
process_queue.enqueue(Process(1, 10))
process_queue.enqueue(Process(2, 5))
process_queue.enqueue(Process(3, 8))

# Process queue in FIFO order
while not process_queue.is_empty():
    current_process = process_queue.dequeue()
    print(f"Processing: {current_process}")
    
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

| Implementation         | Enqueue        | Dequeue | Memory Usage           | Best Use Cases                                          |
| ---------------------- | -------------- | ------- | ---------------------- | ------------------------------------------------------- |
| Circular Array         | O(1) ⚡         | O(1) ⚡  | Fixed, may waste space | Fixed-size bounded queues, performance-critical systems |
| Dynamic Circular Array | O(1) average ⚡ | O(1) ⚡  | Grows as needed        | When size requirements vary but performance matters     |
| Circular Linked List   | O(1) ⚡         | O(1) ⚡  | Exact, no waste        | Memory-constrained environments, frequent size changes  |

### Key Advantages of Circular Queues

1. **Efficient Space Utilization**: Reuses array space that becomes available after dequeuing
2. **Constant-time Operations**: Both enqueue and dequeue are O(1) operations
3. **No Element Shifting**: Unlike simple array implementations, elements don't need to be shifted when dequeuing
4. **Memory Locality**: Array-based implementations benefit from better cache performance

## 📝 License

MIT License

---

Happy coding with circular queues! 🎉 Remember, when implemented correctly, circular data structures can significantly improve performance in many real-world applications.