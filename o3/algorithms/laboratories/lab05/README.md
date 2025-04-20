# 🔄 Queue Data Structure

A Python implementation of queue data structures with practical applications and exercises.

## 🚀 Overview

This project implements the Queue data structure using multiple approaches with a focus on the First-In-First-Out (FIFO) principle. It includes basic implementations, practical applications, and algorithm exercises that leverage queues.

## ✨ Features

- Three queue implementations (list-based, circular array, linked list) 📋
- Real-world applications (print queue, customer service system) 🖨️
- Practical algorithm exercises 🧠
- Comprehensive test cases ✅

## 🔍 Implementation Details

### 📦 Queue Types

- **SimpleQueue**: Basic list-based implementation 📝
- **CircularQueue**: Fixed-size circular array implementation 🔄
- **LinkedQueue**: Dynamic linked list implementation 🔗
- **QueueWithTwoStacks**: Implementation using two stacks 🏗️

### 🌟 Key Applications

- Print queue simulation 🖨️
- Breadth-first search 🔍
- Customer service queuing system 🧑‍💼
- Hot potato game 🥔

## 💻 Usage

```python
# Example usage of LinkedQueue
from main import LinkedQueue

queue = LinkedQueue()
queue.enqueue("First")   # Add to rear ⬅️
queue.enqueue("Second")  # Add to rear ⬅️

while not queue.is_empty():
    print(queue.dequeue())  # Remove from front ➡️
```

## 🏃‍♂️ Running the Project

```bash
python main.py
```

## 📊 Performance Comparison

| Implementation | Enqueue | Dequeue | Best Use Cases                             |
| -------------- | ------- | ------- | ------------------------------------------ |
| List-based     | O(1) ⚡  | O(n) 🐢  | Small queues, simple applications 🔹        |
| Circular Array | O(1) ⚡  | O(1) ⚡  | Fixed-size, performance-critical systems ⚙️ |
| Linked List    | O(1) ⚡  | O(1) ⚡  | Dynamic size requirements 📈                |

## 📝 License

MIT License ⚖️

---

Happy coding! 🎉👨‍💻👩‍💻