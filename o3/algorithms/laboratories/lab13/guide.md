# 🚀🧩💡 Technical Challenges: Heap Skills in Action! 🎯🔢🌱

🌟 This section presents five progressive, hands-on challenges to help students master heap operations in Python—from basic setup to real-world applications. 🌟

## 🎯 Objectives

* 🔨 **Build and manage MinHeap and MaxHeap** using standard methods and best coding practices.
* 🌟 **Apply heap operations** to solve real-world and interview-style challenges.

---

## Technical Challenges

### 1️⃣ Challenge 1: Implementing a Basic MinHeap Class

#### ❓ Problem

🎯 Design a class `MinHeap` to represent a min-heap using a Python list. Implement the methods to create the heap and check if it is empty.

#### 📜 Description

* 📦 Use a list `self.heap` to store values.
* 🚀 `__init__()` initializes an empty heap.
* 🔍 `is_empty(self)` returns `True` if no elements, else `False`.
* 🛑 **Stop here**: do **not** implement insert/delete/heapify yet!

#### 🧩 Base Code

```python
class MinHeap:
    # 📦 MinHeap data structure using list
    def __init__(self):
        # Initialize empty list for heap
        pass

    def is_empty(self):
        # Return True if heap is empty
        pass

# 🧪 Test cases
def test_min_heap_init_and_empty():
    h = MinHeap()
    print("🌱 Test 1:", h.is_empty() == True)
    h.heap.append(1)
    print("🌱 Test 2:", h.is_empty() == False)
    h.heap.clear()
    print("🌱 Test 3:", h.is_empty() == True)
    h.heap.extend([2,3,4])
    print("🌱 Test 4:", h.is_empty() == False)
    h.heap.pop(); h.heap.pop(); h.heap.pop()
    print("🌱 Test 5:", h.is_empty() == True)

test_min_heap_init_and_empty()
```

#### 💡 Tips

* 📝 Ensure `self.heap` exists before any method call.
* Keep implementations minimal.

#### 🧠 Motivation

🔑 Master heap foundation before moving to core operations!

---

### 2️⃣ Challenge 2: Inserting and Heapifying Up in MinHeap

#### ❓ Problem

➕ Add `insert(self, value)` and `_heapify_up(self, index)` so each insertion **preserves** the min-heap property.

#### 📜 Description

* 🛠️ `insert(value)` appends to `self.heap`.
* ⬆️ `_heapify_up(index)` swaps node with parent while child < parent.
* 📐 Parent index = `(index - 1) // 2`.

#### 🧩 Base Code

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Insert value and maintain heap property
        pass

    def _heapify_up(self, index):
        # Move the value up to restore heap
        pass

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])
    # 🍀 Test 5: parent ≤ children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True)
        and (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

test_min_heap_insert()
```

#### 💡 Tips

* 🔁 Use a loop to percolate up.
* ✅ Stop when at root or no swap needed.

#### 🧠 Motivation

🌪️ Insertion + percolate-up = heart of priority queues!

---

### 3️⃣ Challenge 3: Removing the Minimum and Heapifying Down

#### ❓ Problem

❌🆙 Implement `delete_min(self)` and `_heapify_down(self, index)` to remove/return the smallest element and **restore** the heap.

#### 📜 Description

* 🚪 `delete_min()` pops root or returns `None` if empty.
* 🔄 Move last element to root, then `_heapify_down(0)`.
* 📏 `_heapify_down` swaps with the **smaller child** until property holds.
* ↙️ Left child = `2*i+1`, ↘️ Right child = `2*i+2`.

#### 🧩 Base Code

```python
class MinHeap:
    def delete_min(self):
        # Remove and return the smallest element
        pass

    def _heapify_down(self, index):
        # Restore heap property downward
        pass

# 🧪 Test cases
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap=[1]; print("🧹 Test 2:", h.delete_min()==1 and h.heap==[])
    h.heap=[1,3,2]; print("🧹 Test 3:", h.delete_min()==1 and h.heap==[2,3])
    h.heap=[1,3,4,5]; print("🧹 Test 4:", h.delete_min()==1 and h.heap==[3,5,4])
    h.heap=[1,2,3,4,5]
    print("🧹 Test 5:", h.delete_min()==1)

test_min_heap_delete_min()
```

#### 💡 Tips

* ⚠️ Check empty heap before delete.
* ⬇️ Always swap with **smallest** child.

#### 🧠 Motivation

⏱️ Deletion = key for scheduling & sorting tasks.

---

### 4️⃣ Challenge 4: Implementing Heapify (Building Heap from Unordered Array)

#### ❓ Problem

🏗️ Write `build_heap(self, array)` to transform any list into a valid min-heap **in-place** in O(n) time.

#### 📜 Description

* 🔄 `self.heap = array.copy()`.
* 🔨 From last non-leaf `(len//2)-1` down to `0`, call `_heapify_down`.

#### 🧩 Base Code

```python
class MinHeap:
    def build_heap(self, array):
        # Transform array into a min-heap
        pass

    def _heapify_down(self, index):
        pass

# 🧪 Test cases
def test_build_heap():
    h = MinHeap()
    h.build_heap([5,3,8,1,2]); print("🔨 Test 1:", h.heap[0]==1)
    h.build_heap([7,6,5,4,3,2,1]); print("🔨 Test 2:", h.heap[0]==1)
    h.build_heap([2,1]);           print("🔨 Test 3:", h.heap==[1,2])
    h.build_heap([10]);            print("🔨 Test 4:", h.heap==[10])
    h.build_heap([]);              print("🔨 Test 5:", h.heap==[])

test_build_heap()
```

#### 💡 Tips

* 📍 Last non-leaf = `(len(self.heap)//2)-1`.
* 🔧 Apply `_heapify_down` upwards.

#### 🧠 Motivation

🚀 Bulk heap creation fuels **heap sort** and fast PQ init.

---

### 5️⃣ Challenge 5: MaxHeap — Switching to Max-Heap Property

#### ❓ Problem

🔄 Adapt to a `MaxHeap` where **parent ≥ children** using the same indices but inverted comparisons.

#### 📜 Description

* Methods: `insert`, `_heapify_up`, `delete_max`, `_heapify_down`.
* 🔀 Replace `<` with `>` in comparisons.

#### 🧩 Base Code

```python
class MaxHeap:
    # 🦁 MaxHeap data structure using list
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Insert and heapify up for max-heap property
        pass

    def _heapify_up(self, index):
        # Move up while parent < current
        pass

    def delete_max(self):
        # Remove and return the largest (root) element
        pass

    def _heapify_down(self, index):
        # Move down while current < child
        pass

# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1);         print("🦁 Test 1:", h.heap==[1])
    for v in [3,2,8,5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0]==max(h.heap))
    h.delete_max();      print("🦁 Test 3:", h.heap[0]==max(h.heap))
    h = MaxHeap()
    for v in [5,3,1]:
        h.insert(v)
    h.delete_max();      print("🦁 Test 4:", h.heap==[3,1])
    h=MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max()==10 and h.heap==[])

test_max_heap()
```

#### 💡 Tips

* 🔁 Mirror `MinHeap` logic, just invert `<` to `>`.
* 📊 Same indexing formula applies.

#### 🧠 Motivation

🎯 Master both heap types for versatile algorithm design and interviews.

---

💡 *Created with AI support by Elliot Garamendi 👨‍💻*
🤖 *Assisted by ChatGPT – Your creative teaching co-pilot 🚀*
