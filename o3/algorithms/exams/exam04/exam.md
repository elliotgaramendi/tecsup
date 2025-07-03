# 🎓✨ Data Structures & Algorithms Exam 🌟📚

Welcome to the ultimate Python-based exam! 🚀 Each week contains 2 exciting challenges 🔥 focused on a specific topic. Students will implement functions, validate inputs, and pass the given tests. Below is Week 1 (o1) with its two lively challenges! 🎉🧩

---

## o1: Algorithmic Complexity Challenges 📈⏱️

> Explore logarithmic vs. constant-time growth! 🔢➕📈 Implement doubling counts and closed-form sums, measure execution time ⏳, handle invalid inputs 🚫, and solidify your grasp of O(log n) vs O(1) analysis.

### o1.1 🧩 **Count Doublings to Exceed N** 🔢➕📈

---

#### ❓ Problem 🤔

Implement `logarithmic_complexity(n)` to count how many times you must **double** 1 to exceed `n`, and return both the count and its execution time. ⏳🚀

---

#### 📜 Description 📖

* **Function**: `logarithmic_complexity(n: int) → (int, float)` 🛠️
* **Inputs**:

  * `n`: positive integer (≥ 1) 🎯
* **Outputs**:

  * **count**: number of doublings required to make `value > n` 🔼
  * **time**: elapsed seconds as a float ⏱️
* **Expected Time Complexity**: **O(log n)** 📊
* **Edge cases**:

  * `n = 1` → count = 1 (1×2 = 2 > 1) ⚠️
  * Very large `n` (up to 10⁹) 🔧
* **Constraints**:

  * Must use a loop that doubles a running total ✔️
  * **Do not** use logarithm functions from `math` 🚫
* **Input validation**:

  * If `n` is not an integer or `n < 1`, return an error indicator, e.g., `-1` for count, plus the elapsed time. ❌⚙️

---

#### 🧪 Tests to Pass ✅

1. **o1.1.1**: Ideal case 1 🌱

   * Input: `n = 1` 🔢
   * Expect: returns `(1, time)` (since 1×2 > 1) 🎉
2. **o1.1.2**: Ideal case 2 🌟

   * Input: `n = 10` ➕
   * Expect: returns `(4, time)` (1→2→4→8→16) 🚀
3. **o1.1.3**: Ideal case 3 🔥

   * Input: `n = 100` ➕
   * Expect: returns `(7, time)` (…→128) 📈
4. **o1.1.4**: Type-check test 🧐

   * Input: a valid integer, e.g. `n = 5`
   * Verify: return types: first element is `int` 🆗, second is `float` 🆗
5. **o1.1.5**: Error-handling test ⚠️

   * Input: invalid, e.g. `n = "a"` or `n = -3`
   * Expect: returns `-1` for the count ❌ and a float for time ⏱️

---

#### 💻 Base Code 🖥️

```python
import time

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def logarithmic_complexity(n):
    """🔢 Count doublings of 1 to exceed n; return (count, elapsed_time).
    If input invalid (not int or < 1), return (-1, elapsed_time)."""
    start = time.time()
    # Your solution here 🛠️
    end = time.time()
    elapsed = end - start
    return None, elapsed  # replace None with your count or -1 on invalid

def test_o1_1():
    # o1.1.1: n = 1 → count = 1
    cnt, _ = logarithmic_complexity(1)
    record_test("o1.1.1 n=1 → count==1", cnt == 1)
    # o1.1.2: n = 10 → count = 4
    cnt, _ = logarithmic_complexity(10)
    record_test("o1.1.2 n=10 → count==4", cnt == 4)
    # o1.1.3: n = 100 → count = 7
    cnt, _ = logarithmic_complexity(100)
    record_test("o1.1.3 n=100 → count==7", cnt == 7)
    # o1.1.4: Type-check test
    out = logarithmic_complexity(5)
    record_test(
        "o1.1.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float)
    )
    # o1.1.5: Error-handling test
    cnt_err, _ = logarithmic_complexity("a")
    record_test("o1.1.5 invalid input returns -1", cnt_err == -1)

# 🚀 Run tests
test_o1_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Use a **while** loop:

  ```python
  value = 1
  count = 0
  while value <= n:
      value *= 2  # 🔼 double
      count += 1  # ➕ increment
  ```
* **Measure** before/after with `time.time()` ⏱️.
* **O(log n)** because you double each iteration 🔍.
* **Validate** input at the start:

  ```python
  if not isinstance(n, int) or n < 1:
      return -1, elapsed
  ```
* Add print/debugging only for development; remove in final solution. 🛠️

---

#### 🧠 Motivation 💭

* Demonstrates **logarithmic-time** growth—crucial in **binary search**, **divide-and-conquer** 🌳.
* Understanding O(log n) helps choose between iterative vs. recursive strategies 🔄.
* Real-world: doubling patterns appear in **data resizing**, **exponential backoff** 🔧.
* Builds confidence in analyzing algorithmic scaling 📏💡.

---

### o1.2 🧩 **Sum of First N Naturals** ➕📊⏱️

---

#### ❓ Problem 🤔

Implement `constant_sum(n)` to compute the sum of the first `n` natural numbers in **constant time**, returning the result and execution time. 🔢⏳

---

#### 📜 Description 📖

* **Function**: `constant_sum(n: int) → (int, float)` 🛠️
* **Inputs**:

  * `n`: non-negative integer (≥ 0) 🎯
* **Outputs**:

  * **sum**: `1 + 2 + … + n` ➕
  * **time**: elapsed seconds as a float ⏱️
* **Expected Time Complexity**: **O(1)** 🛑
* **Edge cases**:

  * `n = 0` → sum = 0 ⚠️
  * Very large `n` (up to 10⁸) 🔧
* **Constraints**:

  * Must use the **formula** `n*(n+1)//2` ✔️
  * **Do not** loop over all numbers 🚫
* **Input validation**:

  * If `n` is not an integer or `n < 0`, return an error indicator, e.g. `-1` for the sum, plus the elapsed time. ❌⏱️

---

#### 🧪 Tests to Pass ✅

1. **o1.2.1**: Ideal case 1 🌱

   * Input: `n = 0` ⚠️
   * Expect: returns `(0, time)` ✅
2. **o1.2.2**: Ideal case 2 🌟

   * Input: `n = 1` ➕
   * Expect: returns `(1, time)` ✅
3. **o1.2.3**: Ideal case 3 🔥

   * Input: `n = 10` ➕
   * Expect: returns `(55, time)` ✅
4. **o1.2.4**: Type-check test 🧐

   * Input: a valid integer, e.g. `n = 5`
   * Verify: return types: first element is `int` 🆗, second is `float` 🆗
5. **o1.2.5**: Error-handling test ⚠️

   * Input: invalid, e.g. `n = "a"` or `n = -3`
   * Expect: returns `-1` for the sum ❌ and a float for time ⏱️

---

#### 💻 Base Code 🖥️

```python
import time

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def constant_sum(n):
    """🔢 Compute sum of 1..n in O(1), return (sum, elapsed_time).
    If input invalid (not int or < 0), return (-1, elapsed_time)."""
    start = time.time()
    # Your solution here 🛠️
    end = time.time()
    elapsed = end - start
    return None, elapsed  # replace None with your sum or -1 on invalid

def test_o1_2():
    # o1.2.1: n = 0 → sum = 0
    s, _ = constant_sum(0)
    record_test("o1.2.1 n=0 → sum==0", s == 0)
    # o1.2.2: n = 1 → sum = 1
    s, _ = constant_sum(1)
    record_test("o1.2.2 n=1 → sum==1", s == 1)
    # o1.2.3: n = 10 → sum = 55
    s, _ = constant_sum(10)
    record_test("o1.2.3 n=10 → sum==55", s == 55)
    # o1.2.4: Type-check test
    out = constant_sum(5)
    record_test(
        "o1.2.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float)
    )
    # o1.2.5: Error-handling test
    s_err, _ = constant_sum("a")
    record_test("o1.2.5 invalid input returns -1", s_err == -1)

# 🚀 Run tests
test_o1_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Use the **closed-form formula**:

  ```python
  total = n * (n + 1) // 2
  ```
* No loops—ensures **O(1)** constant time 🔒.
* **Validate** input at the start:

  ```python
  if not isinstance(n, int) or n < 0:
      return -1, elapsed
  ```
* Measure with `time.time()` ⏱️ before/after.
* Add logging/print statements for debugging only; remove in final submission. 🛠️

---

#### 🧠 Motivation 💡

* **Constant-time** methods underpin **direct calculations** in statistics and physics 📊🔬.
* Shows the power of **mathematical insight** vs. brute-force iteration 🧮.
* Real-world: formulae speed up large-scale data summaries in analytics 🍃.
* Reinforces confidence in algorithm analysis and input validation ✅🔒.

---

## o2: Recursion & Backtracking 🌀🔙

> In this section you’ll implement classic recursive and backtracking algorithms—computing factorials via pure recursion and generating all binary strings of length n through backtracking. Master the call stack, base cases, and explore combinatorial branches with elegance! 🔄🌳✨

### o2.1 🔁 **Recursive Factorial** 🧮✨

---

#### ❓ Problem 🤔

Implement `factorial(n)` to compute the factorial of `n` using **recursion**, and return the result. 🔄🧮

---

#### 📜 Description 📖

* **Function**: `factorial(n: int) → int or None` 🛠️
* **Inputs**:

  * `n`: non-negative integer (≥ 0) 🎯
* **Outputs**:

  * **result**: `n!` as an integer 🔢
  * **invalid**: return `None` if input invalid ❌
* **Time Complexity**: **O(n)** 🔄
* **Edge cases**:

  * `n = 0` → returns `1` (0! = 1) ⚠️
  * Very large `n` may hit recursion limits 🌋
* **Constraints**:

  * Must use **recursion** (no loops) 🔙
* **Input validation**:

  * If `n` is not an integer or `n < 0`, return `None` ❌⚙️

---

#### 🧪 Tests to Pass ✅

1. **o2.1.1**: Base case

   * Input: `n = 0`
   * Expect: returns `1` ✅
2. **o2.1.2**: Small n

   * Input: `n = 5`
   * Expect: returns `120` ✅
3. **o2.1.3**: Larger n

   * Input: `n = 7`
   * Expect: returns `5040` ✅
4. **o2.1.4**: Type-check test

   * Input: `n = 3`
   * Verify: return type is `int` 🆗
5. **o2.1.5**: Error-handling test

   * Input: `n = -1` and `n = "a"`
   * Expect: returns `None` for both ❌

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def factorial(n):
    """🔁 Compute n! recursively; return None if input invalid."""
    # Your solution here 🛠️
    pass

def test_o2_1():
    # o2.1.1: n = 0 → result = 1
    record_test("o2.1.1 n=0 → 1", factorial(0) == 1)
    # o2.1.2: n = 5 → result = 120
    record_test("o2.1.2 n=5 → 120", factorial(5) == 120)
    # o2.1.3: n = 7 → result = 5040
    record_test("o2.1.3 n=7 → 5040", factorial(7) == 5040)
    # o2.1.4: type-check
    out = factorial(3)
    record_test("o2.1.4 returns int", isinstance(out, int))
    # o2.1.5: invalid input → None
    record_test("o2.1.5 invalid returns None",
        factorial(-1) is None and factorial("a") is None)

# 🚀 Run tests
test_o2_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* **Base case**: if `n == 0`, return `1` 🌱.
* **Recursive step**: return `n * factorial(n-1)` 🔄.
* Validate input **before** recursion to avoid errors ❌.
* Watch out for Python’s **recursion depth** on large `n` 🌋.

---

#### 🧠 Motivation 💭

* Core example of **divide-and-conquer** breaking problems into smaller subproblems 🌳.
* Foundation for **dynamic programming** and memoization techniques 💾.
* Reinforces understanding of the **call stack** and recursion mechanics 🧠.

---

### o2.2 🔤 **Generate Binary Strings of Length N** 0️⃣1️⃣🛤️

---

#### ❓ Problem 🤔

Implement `generate_binary_strings(n)` to return all binary strings of length `n` using **backtracking**. 🔄🔤

---

#### 📜 Description 📖

* **Function**: `generate_binary_strings(n: int) → list[str]` 🛠️
* **Inputs**:

  * `n`: non-negative integer (length) 🎯
* **Outputs**:

  * **result**: list of all `'0'`/`'1'` strings of length `n` 📋
  * **invalid**: return `[]` if input invalid ❌
* **Time Complexity**: **O(2ⁿ · n)** 🔍
* **Edge cases**:

  * `n = 0` → returns `['']` (one empty string) ⚠️
  * Exponential growth for large `n` 🌋
* **Constraints**:

  * Must use **backtracking** (recursive generation) 🔙
* **Input validation**:

  * If `n` is not an integer or `n < 0`, return `[]` ❌⚙️

---

#### 🧪 Tests to Pass ✅

1. **o2.2.1**: n = 2 → list of 4

   * Expect: `['00','01','10','11']` ✅
2. **o2.2.2**: n = 3 → length = 8

   * Expect: `len(...) == 8` ✅
3. **o2.2.3**: contains specific string

   * Expect: `'101' in generate_binary_strings(3)` ✅
4. **o2.2.4**: Type-check test

   * Input: `n = 1`
   * Verify: return is `list`, elements are `str` 🆗
5. **o2.2.5**: Error-handling test

   * Input: `n = -1` and `n = "a"`
   * Expect: returns `[]` ❌

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    # Your solution here 🛠️
    return []

def test_o2_2():
    # o2.2.1: n = 2 → ['00','01','10','11']
    record_test("o2.2.1 n=2 → 4 strings",
        generate_binary_strings(2) == ['00','01','10','11'])
    # o2.2.2: n = 3 → length = 8
    record_test("o2.2.2 n=3 → length=8",
        len(generate_binary_strings(3)) == 8)
    # o2.2.3: contains '101'
    record_test("o2.2.3 contains '101'",
        '101' in generate_binary_strings(3))
    # o2.2.4: type-check
    res = generate_binary_strings(1)
    record_test("o2.2.4 returns list[str]",
        isinstance(res, list) and all(isinstance(s, str) for s in res))
    # o2.2.5: invalid input → []
    record_test("o2.2.5 invalid returns []",
        generate_binary_strings(-1) == [] and generate_binary_strings("a") == [])

# 🚀 Run tests
test_o2_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Use a **helper** function `backtrack(prefix)` to build strings step-by-step 🔧.
* At each recursion, append `'0'` then `'1'` and recurse 🔄.
* When `len(prefix) == n`, add to result 🌳.
* Validate `n` first to avoid unnecessary recursion ❌.

---

#### 🧠 Motivation 💭

* Demonstrates **backtracking** exploring all combinatorial branches 🌲.
* Foundation for **combinatorial** and **constraint-satisfaction** problems 🎯.
* Reinforces mastery of **recursive patterns** and **pruning**.

---

## o3: Linked Lists 📎🔗

> In this section, you’ll build and manipulate singly linked lists using `Node` pointers—practicing insertion at both ends, length tracking, search, and deletion. 🐍✨🧩
> Master dynamic memory, pointer updates, and edge-case handling for robust list operations! 🏁🔍❌📏

### o3.1 ➕ **Insert at Beginning, Insert at End & Length** 🏁👶➕📏

---

#### ❓ Problem 🤔

Implement `insert_at_beginning(data)`, `insert_at_end(data)`, and maintain a `length` property in your `LinkedList` class. 🐍✨

---

#### 📜 Description 📖

* **Classes**:

  * `Node(data)` with attributes `data` and `next` 🧩
  * `LinkedList()` with:

    * `head` (initially `None`) 🎯
    * `length` (initially `0`) 🔢
* **Methods to implement**:

  1. **`insert_at_beginning(data)`** – create a new node at the head, update `head`, increment `length`.
  2. **`insert_at_end(data)`** – append a new node at the tail (or beginning if empty), increment `length`.
* **Helper**:

  * `display()` returns `"val1 -> val2 -> ..."` or `"Empty list"` if no nodes 🌳

---

#### 🧪 Tests to Pass ✅

1. **o3.1.1**: Mixed single insert

   * Actions:

     ```python
     ll.insert_at_beginning(2)
     ll.insert_at_end(3)
     ```
   * Expect: `ll.display()` returns `'2 -> 3'` ✅
2. **o3.1.2**: Mixed multiple inserts

   * Continuing above:

     ```python
     ll.insert_at_beginning(1)
     ll.insert_at_end(4)
     ```
   * Expect: `ll.display()` returns `'1 -> 2 -> 3 -> 4'` ✅
3. **o3.1.3**: Length tracking

   * After four successful inserts: `ll.length == 4` 🔢✅
4. **o3.1.4**: Invalid input handling

   * Record `old = ll.length` then:

     ```python
     ll.insert_at_beginning(None)
     ll.insert_at_end("x")
     ```
   * Expect: `ll.length` remains `old` (invalid ignored) ⚠️
5. **o3.1.5**: Return-type verification

   * Verify:

     ```python
     isinstance(ll.length, int)  # True 🆗  
     isinstance(ll.display(), str)  # True 🆗
     ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        """Insert new node at beginning and update length."""
        # Your solution here 🛠️
        pass

    def insert_at_end(self, data):
        """Insert new node at end and update length."""
        # Your solution here 🛠️
        pass

    def display(self):
        """Return 'Empty list' or 'val1 -> val2 -> ...'."""
        current, vals = self.head, []
        while current:
            vals.append(str(current.data))
            current = current.next
        return " -> ".join(vals) if vals else "Empty list"

def test_o3_1():
    ll = LinkedList()
    # o3.1.1 Mixed single insert
    ll.insert_at_beginning(2)
    ll.insert_at_end(3)
    record_test("o3.1.1 ll.display() == '2 -> 3'", ll.display() == '2 -> 3')
    # o3.1.2 Mixed multiple inserts
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    record_test("o3.1.2 ll.display() == '1 -> 2 -> 3 -> 4'", ll.display() == '1 -> 2 -> 3 -> 4')
    # o3.1.3 Length tracking
    record_test("o3.1.3 ll.length == 4", ll.length == 4)
    # o3.1.4 Invalid input handling
    old_len = ll.length
    ll.insert_at_beginning(None)
    ll.insert_at_end("x")
    record_test("o3.1.4 invalid ignored", ll.length == old_len)
    # o3.1.5 Return-type verification
    record_test("o3.1.5 types ok", isinstance(ll.length, int) and isinstance(ll.display(), str))

# 🚀 Run tests
test_o3_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Validate `data` (e.g., skip if `data is None`) before inserting.
* Handle **empty list** case separately in `insert_at_end`.
* Update `length` only on valid insert operations.

---

#### 🧠 Motivation 💭

* Teaches both **prepend** (stack) and **append** (queue) operations 🔄.
* Reinforces pointer updates and size tracking 🔢.
* Lays groundwork for advanced structures like **deque** and **circular lists**.

---

### o3.2 🔍❌ **Search & Delete** 🕵️‍♂️🗑️

---

#### ❓ Problem 🤔

Implement `search(target)` to check if a value exists, and `delete(target)` to remove the first matching node—updating `length`. 🔎❌

---

#### 📜 Description 📖

* **Class**: same `LinkedList` with `head`, `length`, `insert_*`, `display()`.
* **Methods to implement**:

  1. **`search(target)`** – traverse nodes, return `True` on match else `False`.
  2. **`delete(target)`** – unlink the first matching node, decrement `length`.

---

#### 🧪 Tests to Pass ✅

1. **o3.2.1**: Search found

   * Preload list with `[1,2,3,4]`
   * Expect: `ll.search(3) is True` ✅
2. **o3.2.2**: Delete middle

   * `ll.delete(2)` → `ll.display() == '1 -> 3 -> 4'` ✅
3. **o3.2.3**: Delete ends

   * `ll.delete(1)` then `ll.delete(4)` → `ll.display() == '3'` ✅
4. **o3.2.4**: Invalid operations

   * Record `old = ll.length`

     ```python
     ll.search(None) is False
     ll.delete(999)
     ll.length == old
     ```
   * Expect: no change, invalid ignored ⚠️
5. **o3.2.5**: Return-type verification

   * Verify:

     ```python
     isinstance(ll.search(3), bool)  # True 🆗  
     isinstance(ll.length, int)      # True 🆗
     ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        if data is None: return
        new = Node(data)
        new.next = self.head
        self.head = new
        self.length += 1

    def insert_at_end(self, data):
        if data is None: return
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new
        self.length += 1

    def search(self, target):
        """Return True if target exists, else False."""
        # Your solution here 🛠️
        pass

    def delete(self, target):
        """Delete first node with data == target and update length."""
        # Your solution here 🛠️
        pass

    def display(self):
        curr, vals = self.head, []
        while curr:
            vals.append(str(curr.data))
            curr = curr.next
        return " -> ".join(vals) if vals else "Empty list"

def test_o3_2():
    ll = LinkedList()
    for v in [1,2,3,4]:
        ll.insert_at_end(v)
    # o3.2.1 Search found
    record_test("o3.2.1 search(3) True", ll.search(3) is True)
    # o3.2.2 Delete middle
    ll.delete(2)
    record_test("o3.2.2 display == '1 -> 3 -> 4'", ll.display() == '1 -> 3 -> 4')
    # o3.2.3 Delete ends
    ll.delete(1)
    ll.delete(4)
    record_test("o3.2.3 display == '3'", ll.display() == '3')
    # o3.2.4 Invalid operations
    old = ll.length
    cond = (ll.search(None) is False)
    ll.delete(999)
    cond = cond and (ll.length == old)
    record_test("o3.2.4 invalid handled", cond)
    # o3.2.5 Return-type
    record_test("o3.2.5 types ok", isinstance(ll.search(3), bool) and isinstance(ll.length, int))

# 🚀 Run tests
test_o3_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* **search(target)**: iterate `while curr:`, return early on match.
* **delete(target)**: handle head removal, then unlink using `prev` & `curr`.
* Only decrement `length` when deletion occurs.

---

#### 🧠 Motivation 💭

* Combines **lookup** and **removal**—key for dynamic collections 🔄.
* Emphasizes robust **edge-case** handling (head/tail/absent) 🎯.
* Prepares for advanced list manipulations like **filter** & **splice**.

---

## o4: Stacks 📚🧱

> Dive into LIFO magic! 🪄 In this section you’ll build two stack flavors:
>
> 1. **Array-Based Stack** with `is_empty()`, `push()`, `pop()`, and `peek()` using Python list ops 🔄📥📤👀
> 2. **Linked-List Stack** with `push()`, `pop()`, `peek()`, and `size()` using Node pointers 🧩🔗📏
>
> Master constant-time operations, safe fallbacks, and both contiguous & pointer-based memory models! ⚡️✨

### o4.1 🧩 **Array-Based Stack: `is_empty`, `push`, `pop`** 🔄📥📤

---

#### ❓ Problem 🤔

Implement a `Stack` class using a Python list with methods:

* `is_empty()` → returns `True` if the stack is empty, else `False`.
* `push(data)` → adds `data` to the top of the stack.
* `pop()` → removes and returns the top element, or `None` if the stack is empty. 🚀

---

#### 📜 Description 📖

```python
class Stack:
    def __init__(self):
        self.items = []
```

* **`is_empty(self) → bool`**
  Check emptiness via `not self.items`.
* **`push(self, data) → None`**
  Append `data` to `self.items`.
* **`pop(self) → Any | None`**
  If non-empty, `return self.items.pop()`, else `return None`.

> **Constraints**
>
> * Use only list methods (`append`, `pop`).
> * No exceptions should bubble up.
> * Safe stubs (`pass`) so harness never errors.

---

#### 🧪 Tests to Pass ✅

1. **o4.1.1 Core operations**

   ```python
   main_stack = Stack()
   main_stack.is_empty() → True  
   main_stack.push(1); main_stack.push(2)  
   main_stack.items == [1, 2]  
   main_stack.pop() == 2  
   main_stack.pop() == 1
   ```
2. **o4.1.2 Pop on empty**

   ```python
   secondary = Stack()
   secondary.pop() is None
   ```
3. **o4.1.3 Mixed operations**

   ```python
   mixed = Stack()
   mixed.push(0); mixed.push(99)
   mixed.pop() == 99  
   mixed.is_empty() == False
   ```
4. **o4.1.4 Input-agnostic**

   ```python
   any_stack = Stack()
   any_stack.push(None); any_stack.push("x")
   any_stack.items == [None, "x"]
   ```
5. **o4.1.5 Return-type tests**

   ```python
   isinstance(main_stack.is_empty(), bool)  
   isinstance(main_stack.pop(), (int, str, type(None)))
   ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if stack is empty."""
        # Your solution here 🛠️
        pass

    def push(self, data):
        """Push data onto the stack."""
        # Your solution here 🛠️
        pass

    def pop(self):
        """Pop and return top item or None if empty."""
        # Your solution here 🛠️
        pass

def test_o4_1():
    main_stack = Stack()
    cond_core = (
        main_stack.is_empty() is True
        and main_stack.push(1) is None
        and main_stack.push(2) is None
        and main_stack.items == [1, 2]
        and main_stack.pop() == 2
        and main_stack.pop() == 1
    )
    record_test("o4.1.1 core operations", cond_core)

    secondary_stack = Stack()
    record_test("o4.1.2 pop on empty", secondary_stack.pop() is None)

    mixed_stack = Stack()
    mixed_stack.push(0)
    mixed_stack.push(99)
    cond_mixed = mixed_stack.pop() == 99 and mixed_stack.is_empty() is False
    record_test("o4.1.3 mixed operations", cond_mixed)

    any_stack = Stack()
    any_stack.push(None)
    any_stack.push("x")
    record_test("o4.1.4 input-agnostic storage", any_stack.items == [None, "x"])

    popped_value = main_stack.pop()
    cond_types = isinstance(main_stack.is_empty(), bool) and isinstance(
        popped_value, (int, str, type(None))
    )
    record_test("o4.1.5 return-type verification", cond_types)

# 🚀 Run tests
test_o4_1()

# 📋 Summary
for result in test_results:
    print(result)
```

---

#### 💡 Tips ✨

* Use `self.items.append(data)` for **push** 📥.
* For **pop** 🔄:

  ```python
  if self.items:
      return self.items.pop()
  return None
  ```
* Check emptiness by `not self.items` 🔍.

---

#### 🧠 Motivation 💭

* Stacks are **LIFO**: Last In, First Out 🔝.
* Core to **undo/redo**, **call stacks**, and **DFS** 🌲.

---

---

### o4.2 🧩 **Linked-List Stack: `push`, `pop`, `peek`, `size`** 🔗👀📏

---

#### ❓ Problem 🤔

Implement a `LinkedStack` using linked `Node`s with methods:

1. `push(data)` → add new node at top
2. `pop()` → remove & return top node’s data, or `None` if empty
3. `peek()` → return top node’s data without removal, or `None`
4. `size()` → return number of elements

---

#### 📜 Description 📖

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top    = None  # Node or None
        self._size = 0      # int
```

* **`push(self, data) → None`**
  Create `Node(data)`, link as new `top`, increment `_size`.
* **`pop(self) → Any | None`**
  If `top` exists, unlink it, decrement `_size`, return `data`; else `None`.
* **`peek(self) → Any | None`**
  Return `top.data` or `None`.
* **`size(self) → int`**
  Return `_size`.

> **Safe stubs** (`pass`) let the harness run even before implementation.

---

#### 🧪 Tests to Pass ✅

1. **o4.2.1 Empty behavior**

   ```python
   stack = LinkedStack()
   stack.peek() is None  
   stack.pop() is None  
   stack.size() == 0
   ```
2. **o4.2.2 Push & peek & size**

   ```python
   stack.push(5)
   stack.push(7)
   stack.push(9)
   stack.peek() == 9  
   stack.size() == 3
   ```
3. **o4.2.3 After pop**

   ```python
   stack.pop()
   stack.peek() == 7  
   stack.size() == 2
   ```
4. **o4.2.4 Mixed types allowed**

   ```python
   stack.push("a")
   stack.peek() == "a"  
   stack.size() == 3
   ```
5. **o4.2.5 Return-type verification**

   ```python
   isinstance(stack.peek(), (int, str, type(None)))  
   isinstance(stack.size(), int)
   ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top    = None
        self._size = 0

    def push(self, data):
        """Push element using linked nodes."""
        # Your solution here 🛠️
        pass

    def pop(self):
        """Pop and return top data or None."""
        # Your solution here 🛠️
        pass

    def peek(self):
        """Return top data without removing or None."""
        # Your solution here 🛠️
        pass

    def size(self):
        """Return number of items."""
        # Your solution here 🛠️
        pass

def test_o4_2():
    stack = LinkedStack()
    cond_empty = stack.peek() is None and stack.pop() is None and stack.size() == 0
    record_test("o4.2.1 empty behavior", cond_empty)

    stack.push(5)
    stack.push(7)
    stack.push(9)
    cond_push = stack.peek() == 9 and stack.size() == 3
    record_test("o4.2.2 push/peek/size", cond_push)

    stack.pop()
    cond_after_pop = stack.peek() == 7 and stack.size() == 2
    record_test("o4.2.3 pop adjusts", cond_after_pop)

    stack.push("a")
    cond_mixed = stack.peek() == "a" and stack.size() == 3
    record_test("o4.2.4 mixed types", cond_mixed)

    cond_types = isinstance(stack.peek(), (int, str, type(None))) and isinstance(stack.size(), int)
    record_test("o4.2.5 return-type verification", cond_types)

# 🚀 Run tests
test_o4_2()

# 📋 Summary
for result in test_results:
    print(result)
```

---

#### 💡 Tips ✨

* **Array stack**: use `append`/`pop` for **O(1)** at end.
* **Linked stack**: insert/remove at head in **O(1)**, track `_size`.
* `peek` doesn’t mutate; `size` returns the counter.

---

#### 🧠 Motivation 💭

* Master both **list-backed** and **node-backed** stacks 🔄.
* Understand contiguous vs. linked memory trade-offs 🚧.
* Foundations for **DFS**, **undo/redo**, **call stacks** 🌲.

---

## o5: Queues 🚶‍♀️🚶

> Practice FIFO fundamentals with both array-based and linked-list implementations—enqueue, dequeue & peek to master core queue operations! 🎯🔄

### o5.1 🧩 **Array-Based Queue: `enqueue`, `dequeue`, `peek`** 📥📤👀

---

#### ❓ Problem 🤔

Implement a simple FIFO `Queue` class using a Python list with methods:

1. `enqueue(item)` → add item at rear  
2. `dequeue()` → remove and return front element (or `None` if empty)  
3. `peek()` → return front element without removing (or `None` if empty)  

---

#### 📜 Description 📖

* **Class**:
  ```python
  class Queue:
      def __init__(self):
          self._items = []
  ```

* **Methods to implement**:

  1. **`enqueue(self, item)`** – append `item` to `self._items`.
  2. **`dequeue(self)`** – if `self._items` non‐empty, `pop(0)` and return; else implicitly return `None`.
  3. **`peek(self)`** – if `self._items` non‐empty, return `self._items[0]`; else `None`.
* **Constraints**:

  * Use only list operations.
  * Safe stubs (`pass`) so harness never errors.

---

#### 🧪 Tests to Pass ✅

1. **o5.1.1 Empty queue behavior**

   * `queue_array = Queue()`
   * `queue_array.dequeue() is None` and `queue_array.peek() is None`
2. **o5.1.2 Enqueue/Dequeue order**

   * `queue_array.enqueue(1); queue_array.enqueue(2); queue_array.enqueue(3)`
   * `queue_array.dequeue() == 1`, `queue_array.dequeue() == 2`, `queue_array.dequeue() == 3`
3. **o5.1.3 Peek without removing**

   * fresh `queue_array.enqueue("x")`
   * `queue_array.peek() == "x"` and then still `queue_array.dequeue() == "x"`
4. **o5.1.4 Mixed‐type support**

   * `queue_array.enqueue(None); queue_array.enqueue("y")`
   * `queue_array.peek() is None` and subsequently `queue_array.dequeue() is None`
5. **o5.1.5 Return‐type tests**

   * `isinstance(queue_array.dequeue(), (int, str, type(None)))`
   * `isinstance(queue_array.peek(),   (int, str, type(None)))`

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        pass

    def dequeue(self):
        """Remove and return front item or None if empty."""
        # Your solution here 🛠️
        pass

    def peek(self):
        """Return front item without removing or None if empty."""
        # Your solution here 🛠️
        pass

def test_o5_1():
    queue_array = Queue()
    record_test("o5.1.1 empty behavior",
        queue_array.dequeue() is None and queue_array.peek() is None)

    queue_array.enqueue(1)
    queue_array.enqueue(2)
    queue_array.enqueue(3)
    record_test("o5.1.2 FIFO order",
        queue_array.dequeue() == 1 and
        queue_array.dequeue() == 2 and
        queue_array.dequeue() == 3)

    queue_array.enqueue("x")
    record_test("o5.1.3 peek preserves",
        queue_array.peek() == "x" and queue_array.dequeue() == "x")

    queue_array.enqueue(None)
    queue_array.enqueue("y")
    record_test("o5.1.4 mixed types",
        queue_array.peek() is None and queue_array.dequeue() is None)

    val_removed = queue_array.dequeue()
    val_peeked  = queue_array.peek()
    record_test("o5.1.5 return types",
        isinstance(val_removed, (int, str, type(None))) and
        isinstance(val_peeked,   (int, str, type(None))))

# 🚀 Run tests
test_o5_1()

# 📋 Summary
for result in test_results:
    print(result)
```

---

#### 💡 Tips ✨

* Use `self._items.append(item)` for **enqueue** 📥.
* Use `self._items.pop(0)` for **dequeue** 🔄.
* Always check `if self._items:` before accessing for **peek** 🔎.

---

#### 🧠 Motivation 💭

* Queues are **FIFO**: First In, First Out ⏳.
* Foundation for **task scheduling**, **BFS** on graphs, and **producer–consumer** models 🍃.

---

### o5.2 🧩 **Linked-List Queue: `is_empty`, `enqueue`, `dequeue`, `size`** 🔗📏

---

#### ❓ Problem 🤔

Implement a linked‐list based FIFO `LinkedQueue` with methods:

1. `is_empty()` → return `True` if queue has no elements
2. `enqueue(item)` → add new node at rear
3. `dequeue()` → remove & return front node’s data (or `None`)
4. `size()` → return number of elements

---

#### 📜 Description 📖

* **Classes**:

  ```python
  class Node:
      def __init__(self, data):
          self.data = data
          self.next = None

  class LinkedQueue:
      def __init__(self):
          self._front = None    # Node or None
          self._rear  = None    # Node or None
          self._count = 0       # int
  ```
* **Methods to implement**:

  1. **`is_empty(self)`** – return `True` if `_count == 0`.
  2. **`enqueue(self, item)`** – create `Node(item)`, link at `_rear`, adjust `_front` if first, `_count += 1`.
  3. **`dequeue(self)`** – if non‐empty, remove `_front`, return its `data`, `_count -= 1`; else `None`.
  4. **`size(self)`** – return `_count`.
* **Constraints**:

  * Safe stubs (`pass`) so harness never errors.

---

#### 🧪 Tests to Pass ✅

1. **o5.2.1 Empty queue**

   * `queue_linked = LinkedQueue()`
   * `queue_linked.is_empty() is True` and `queue_linked.size() == 0`
2. **o5.2.2 Enqueue/Dequeue**

   * `queue_linked.enqueue("a"); queue_linked.enqueue("b")`
   * `queue_linked.is_empty() is False`, `queue_linked.size() == 2`, `queue_linked.dequeue() == "a"`
3. **o5.2.3 After removing all**

   * `queue_linked.dequeue()` twice
   * `queue_linked.is_empty() is True`, `queue_linked.size() == 0`
4. **o5.2.4 Invalid dequeue**

   * `previous_size = queue_linked.size()`
   * `queue_linked.dequeue() is None` and `queue_linked.size() == previous_size`
5. **o5.2.5 Return‐type verification**

   * `isinstance(queue_linked.is_empty(), bool)`
   * `isinstance(queue_linked.size(), int)`
   * `isinstance(queue_linked.dequeue(), (int, str, type(None)))`

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._rear  = None
        self._count = 0

    def is_empty(self):
        """Return True if queue is empty."""
        # Your solution here 🛠️
        pass

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        pass

    def dequeue(self):
        """Remove and return front item or None."""
        # Your solution here 🛠️
        pass

    def size(self):
        """Return number of elements."""
        # Your solution here 🛠️
        pass

def test_o5_2():
    queue_linked = LinkedQueue()
    record_test("o5.2.1 empty",
        queue_linked.is_empty() is True and queue_linked.size() == 0)

    queue_linked.enqueue("a")
    queue_linked.enqueue("b")
    record_test("o5.2.2 enqueue/dequeue",
        queue_linked.is_empty() is False and
        queue_linked.size() == 2 and
        queue_linked.dequeue() == "a")

    queue_linked.dequeue()
    record_test("o5.2.3 drained",
        queue_linked.is_empty() is True and queue_linked.size() == 0)

    previous_size = queue_linked.size()
    record_test("o5.2.4 invalid dequeue",
        queue_linked.dequeue() is None and queue_linked.size() == previous_size)

    record_test("o5.2.5 return types",
        isinstance(queue_linked.is_empty(), bool) and
        isinstance(queue_linked.size(), int) and
        isinstance(queue_linked.dequeue(), (int, str, type(None))))

# 🚀 Run tests
test_o5_2()

# 📋 Summary
for result in test_results:
    print(result)
```

---

#### 💡 Tips ✨

* **`is_empty`** – check `self._count == 0`.
* **`enqueue`** – link new `Node` at `self._rear`; if first, set both `self._front` and `self._rear`.
* **`dequeue`** – unlink `self._front`; if now empty, reset `self._rear` to `None`.
* **`size`** – return `self._count`.

---

#### 🧠 Motivation 💭

* Queues support **BFS**, **buffering**, and **rate‐limiting** 🔄.
* Linked‐list version avoids O(n) cost of shifting in array‐based dequeues 🚧.
* Reinforces dynamic memory and pointer handling 🧩.

---

## o6: Advanced Queues 🚀📊

> In this section, you'll master circular and dynamic queue implementations—handling wrap-around logic, capacity checks, and pointer manipulation with flair! 🎯⚙️✨

### o6.1 🧩 **Circular Array Queue: `enqueue`, `dequeue`, `size`** 🔄📥📤

---

#### ❓ Problem 🤔

Implement a fixed-capacity circular FIFO `CircularArrayQueue` with methods:

1. `enqueue(item) -> bool` → add item at rear if not full, return `True`; else `False` 🚫  
2. `dequeue() -> Any` → remove and return front element if not empty, else `None` 📭  
3. `size() -> int` → return current number of elements 📏  

Wrap-around 🔁, full 🚫, empty 📭 — make it fun!

---

#### 📜 Description 📖

* **Class**:
  ```python
  class CircularArrayQueue:
      def __init__(self, capacity: int = 5):
          self.capacity = capacity
          self._queue = [None] * capacity
          self._front = 0
          self._rear = -1
          self._count = 0
  ```

* **Methods to implement**:

  1. **`enqueue(self, item) -> bool`**

     * if `_count < capacity`:

       * `_rear = (_rear + 1) % capacity` 🔁
       * `_queue[_rear] = item` 📥
       * `_count += 1`
       * return `True` ✅
     * else return `False` 🚫
  2. **`dequeue(self) -> Any`**

     * if `_count > 0`:

       * `item = _queue[_front]` 📤
       * `_front = (_front + 1) % capacity` 🔁
       * `_count -= 1`
       * return `item`
     * else return `None` 📭
  3. **`size(self) -> int`**

     * return `_count` 📏

* **Constraints**: no external libs 🔒, safe stubs (`pass`)

---

#### 🧪 Tests to Pass ✅

- **o6.1.1 Basic FIFO behavior**  
  Enqueue three items (`"A"`, `"B"`, `"C"`), then dequeue them in the same order; at the end `size()` must be 0.

- **o6.1.2 Wrap-around correctness**  
  Fill the queue, dequeue one element to free a slot, enqueue a new item (which wraps to the freed index), then dequeue all; `size()` returns 0.

- **o6.1.3 Underflow handling**  
  After emptying the queue, an extra `dequeue()` should return `None` and `size()` must remain 0.

- **o6.1.4 Overflow protection**  
  Attempting to enqueue into a full queue returns `False` and does not change the reported size.

- **o6.1.5 Return-type verification**  
  - `enqueue(...)` returns a `bool`  
  - `dequeue()` returns the stored item (or `None`)  
  - `size()` returns an `int`  

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class CircularArrayQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self._queue = [None] * capacity
        self._front = 0
        self._rear = -1
        self._count = 0

    def enqueue(self, item) -> bool:
        """Add item if not full, return True; else False."""
        # Your solution here 🎯
        pass

    def dequeue(self):
        """Remove and return front item or None if empty."""
        # Your solution here 🔄
        pass

    def size(self) -> int:
        """Return number of elements."""
        # Your solution here 📏
        pass

def test_o6_1():
    circular_array_queue = CircularArrayQueue(3)
    circular_array_queue.enqueue("A")
    circular_array_queue.enqueue("B")
    circular_array_queue.enqueue("C")
    record_test(
        "o6.1.1 basic",
        circular_array_queue.dequeue() == "A" and
        circular_array_queue.dequeue() == "B" and
        circular_array_queue.dequeue() == "C" and
        circular_array_queue.size() == 0
    )

    circular_array_queue = CircularArrayQueue(3)
    circular_array_queue.enqueue(1)
    circular_array_queue.enqueue(2)
    circular_array_queue.enqueue(3)
    circular_array_queue.dequeue()
    circular_array_queue.enqueue(4)
    record_test(
        "o6.1.2 wrap",
        circular_array_queue.dequeue() == 2 and
        circular_array_queue.dequeue() == 3 and
        circular_array_queue.dequeue() == 4 and
        circular_array_queue.size() == 0
    )

    circular_array_queue = CircularArrayQueue(2)
    circular_array_queue.enqueue("X")
    circular_array_queue.enqueue("Y")
    circular_array_queue.dequeue()
    circular_array_queue.dequeue()
    record_test(
        "o6.1.3 empty",
        circular_array_queue.dequeue() is None and
        circular_array_queue.size() == 0
    )

    circular_array_queue = CircularArrayQueue(2)
    circular_array_queue.enqueue(9)
    circular_array_queue.enqueue(8)
    record_test(
        "o6.1.4 full",
        circular_array_queue.enqueue(7) is False and
        circular_array_queue.size() == 2
    )

    circular_array_queue = CircularArrayQueue(1)
    record_test(
        "o6.1.5 types",
        isinstance(circular_array_queue.enqueue("Z"), bool) and
        isinstance(circular_array_queue.dequeue(), (str, type(None))) and
        isinstance(circular_array_queue.size(), int)
    )

# 🚀 Run tests
test_o6_1()

# 📋 Summary
for result in test_results:
    print(result)
```

---

#### 💡 Tips ✨

* Use modulo arithmetic: `next_index = (current_index + 1) % capacity` 🔢
* Track `_count` via the `size()` getter 📏
* Initialize `_rear = -1` so first `enqueue` sets it to 0 🥇

---

#### 🧠 Motivation 💭

* Circular queues avoid wasted slots in buffers 🔄
* Core for **round-robin scheduling**, **network buffers**, **real-time systems** ⏱️
* Reinforces index arithmetic and boundary conditions 🧩

---


### o6.2 🧩 **Circular Linked Queue: `enqueue`, `dequeue`, `size`** 🔗🔄

---

#### ❓ Problem 🤔

Implement a dynamic circular FIFO `CircularLinkedQueue` using nodes with methods:

1. `enqueue(data) -> bool` → add new node at rear, return `True` ✅
2. `dequeue() -> Any` → remove and return front node’s data, or `None` if empty 📭
3. `size() -> int` → return current number of elements 📏

No fixed capacity—growable circle! 🌱

---

#### 📜 Description 📖

* **Classes**:

  ```python
  class Node:
      def __init__(self, data):
          self.data = data
          self.next = None

  class CircularLinkedQueue:
      def __init__(self):
          self.rear = None
          self._count = 0
  ```

* **Methods to implement**:

  1. **`enqueue(self, data) -> bool`**

     * Create `Node(data)` 🆕
     * If `rear is None`: `node.next = node` 🔁
     * Else: `node.next = rear.next`; `rear.next = node`
     * `rear = node`; `_count += 1`; return `True` ✅
  2. **`dequeue(self) -> Any`**

     * If `rear is None`: return `None` 📭
     * `front_node = rear.next`; capture `front_node.data`
     * If single node: `rear = None`
     * Else: `rear.next = front_node.next`
     * `_count -= 1`; return data
  3. **`size(self) -> int`**

     * return `_count` 📏

* **Constraints**: no external libs 🔒, safe stubs (`pass`)

---

#### 🧪 Tests to Pass ✅

- **o6.2.1 Empty queue behavior**  
  A fresh queue’s `dequeue()` returns `None` and `size()` is 0.

- **o6.2.2 Single-element enqueue/dequeue**  
  `enqueue("A")` returns `True`, `dequeue()` returns `"A"`, then `size()` is 0.

- **o6.2.3 Multi-element FIFO**  
  Enqueue 1, 2, 3; then dequeue them in order (1 → 2 → 3); final `size()` is 0.

- **o6.2.4 Underflow after drain**  
  After dequeuing down to empty, an extra `dequeue()` still returns `None` and `size()` stays 0.

- **o6.2.5 Return‐type verification**  
  - `enqueue(...)` returns a `bool`  
  - `dequeue()` returns the stored data (or `None`)  
  - `size()` returns an `int`  

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedQueue:
    def __init__(self):
        self.rear = None
        self._count = 0

    def enqueue(self, data) -> bool:
        """Add node at rear, return True."""
        # Your solution here 🔗
        pass

    def dequeue(self):
        """Remove and return front data or None if empty."""
        # Your solution here 🔄
        pass

    def size(self) -> int:
        """Return number of elements."""
        # Your solution here 📏
        pass

def test_o6_2():
    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.1 empty",
        circular_linked_queue.dequeue() is None and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.2 single",
        circular_linked_queue.enqueue("A") is True and
        circular_linked_queue.dequeue() == "A" and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    circular_linked_queue.enqueue(1)
    circular_linked_queue.enqueue(2)
    circular_linked_queue.enqueue(3)
    record_test(
        "o6.2.3 multiple",
        circular_linked_queue.dequeue() == 1 and
        circular_linked_queue.dequeue() == 2 and
        circular_linked_queue.dequeue() == 3 and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    circular_linked_queue.enqueue("X")
    circular_linked_queue.dequeue()
    record_test(
        "o6.2.4 empty-again",
        circular_linked_queue.dequeue() is None and
        circular_linked_queue.size() == 0
    )

    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.5 types",
        isinstance(circular_linked_queue.enqueue("Z"), bool) and
        isinstance(circular_linked_queue.dequeue(), (int, str, type(None))) and
        isinstance(circular_linked_queue.size(), int)
    )

# 🚀 Run tests
test_o6_2()

# 📋 Summary
for result in test_results:
    print(result)
```

---

#### 💡 Tips ✨

* For array queue: use `(idx + 1) % capacity` 🔢
* For linked queue: link single node to itself first 🔗
* Always update `_count` and expose via `size()` 📏
* Private `_count` is fine—clients use `size()` getter 😉

---

#### 🧠 Motivation 💭

* Count tracking is essential for **full/empty** checks 🔎
* Circular structures power **schedulers**, **buffers**, **network loops** ⏱️
* Reinforces boundary logic and pointer arithmetic 🧩

---

## o7: Binary Trees 🌳🔢

> In this section you’ll implement core binary-tree operations—dynamic insertion, update & deletion in a search tree, and classic depth-first traversals. 🚀🌱

---

### o7.1 🧩 **BinaryTree: `insert_left(parent, value)` & `insert_right(parent, value)`** 🌿➕

#### ❓ Problem 🤔  
Move the child-insertion logic into the `BinaryTree` class. Implement two methods:

1. `insert_left(self, parent, value)`  
2. `insert_right(self, parent, value)`  

Each should create a new `TreeNode(value)` and attach it to the given `parent`.  
If that slot is already occupied, the new node takes it and the old subtree becomes that child of the new node.

---

#### 📜 Description 📖  
* **Classes**:
  ```python
  class TreeNode:
      def __init__(self, value):
          self.value = value
          self.left  = None
          self.right = None

  class BinaryTree:
      def __init__(self, root=None):
          self.root = root
  ```

* **Methods to implement**:

  * `insert_left(self, parent, value)`
  * `insert_right(self, parent, value)`
* **Behavior**:

  * **Empty slot** → attach new node directly.
  * **Occupied slot** → attach new node, then shift the old child subtree under it.
* **Inputs**:

  * `parent`: an existing `TreeNode` in this tree.
  * `value`: data to store in the new node.
* **Output**:

  * The newly created node (a `TreeNode` instance).
* **Edge Cases**:

  * Shifting an existing child and its subtree.
* **Constraints**:

  * Do **not** change method signatures or class definitions.

---

#### 🧪 Tests to Pass ✅

* **o7.1.1 Left-child insertion**

  ```python
  left = tree.insert_left(tree.root, 2)
  # ✓ left is not None
  # ✓ tree.root.left.value == 2
  ```
* **o7.1.2 Right-child insertion**

  ```python
  right = tree.insert_right(tree.root, 3)
  # ✓ right is not None
  # ✓ tree.root.right.value == 3
  ```
* **o7.1.3 Independent left & right**

  ```python
  left  = tree.insert_left(tree.root, 4)
  right = tree.insert_right(tree.root, 5)
  # ✓ left/right are not None
  # ✓ tree.root.left.value == 4
  # ✓ tree.root.right.value == 5
  ```
* **o7.1.4 Shift existing subtree (left)**

  ```python
  tree.root.left = TreeNode(6)
  new_left = tree.insert_left(tree.root, 7)
  # ✓ new_left is not None
  # ✓ new_left.left.value == 6
  ```
* **o7.1.5 Return-type verification**

  ```python
  left  = tree.insert_left(tree.root, 2)
  right = tree.insert_right(tree.root, 3)
  # ✓ isinstance(left, TreeNode)
  # ✓ isinstance(right, TreeNode)
  ```

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert_left(self, parent, value):
        """Insert new node as left child of parent; shift subtree if present."""
        pass

    def insert_right(self, parent, value):
        """Insert new node as right child of parent; shift subtree if present."""
        pass

def test_o7_1():
    tree = BinaryTree(TreeNode(1))

    # o7.1.1 Left-child insertion
    left = tree.insert_left(tree.root, 2)
    record_test(
        "o7.1.1 left creation",
        left is not None and tree.root.left and tree.root.left.value == 2,
    )

    # o7.1.2 Right-child insertion
    tree = BinaryTree(TreeNode(1))
    right = tree.insert_right(tree.root, 3)
    record_test(
        "o7.1.2 right creation",
        right is not None and tree.root.right and tree.root.right.value == 3,
    )

    # o7.1.3 Independent left & right
    tree = BinaryTree(TreeNode(1))
    left = tree.insert_left(tree.root, 4)
    right = tree.insert_right(tree.root, 5)
    record_test(
        "o7.1.3 independent",
        left is not None
        and right is not None
        and tree.root.left.value == 4
        and tree.root.right.value == 5,
    )

    # o7.1.4 Shift existing subtree (left)
    tree = BinaryTree(TreeNode(1))
    tree.root.left = TreeNode(6)
    new_left = tree.insert_left(tree.root, 7)
    record_test(
        "o7.1.4 left shift",
        new_left is not None and new_left.left and new_left.left.value == 6,
    )

    # o7.1.5 Return-type verification
    tree = BinaryTree(TreeNode(1))
    left = tree.insert_left(tree.root, 2)
    right = tree.insert_right(tree.root, 3)
    record_test(
        "o7.1.5 return type", isinstance(left, TreeNode) and isinstance(right, TreeNode)
    )

# 🚀 Run tests
test_o7_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* If `parent.left` (or `parent.right`) already exists, store it, attach the new node, then reattach the old subtree under the new node’s same side.
* Always return the newly created `TreeNode` so tests can inspect it.
* Keep the `pass` stubs so the harness runs without errors until implementation.

---

#### 🧠 Motivation 💭

Centralizing insertion logic in the `BinaryTree` class sets you up for advanced tree operations—search‐tree inserts, rotations, metadata updates—while keeping manipulation rules in one place. 🌳🚀

---

### o7.2 🧩 **Tree Traversals: Preorder, Inorder & Postorder** 🔄👣

#### ❓ Problem 🤔
Implement three traversal methods in `BinaryTree`:

1. `preorder_traversal(self, node=None, result=None) -> list[int]` (root–left–right) 🌲  
2. `inorder_traversal(self, node=None, result=None) -> list[int]`  (left–root–right) 🔍  
3. `postorder_traversal(self, node=None, result=None) -> list[int]` (left–right–root) 🌴

---

#### 📜 Description 📖
* **Classes**:
  ```python
  class TreeNode:
      def __init__(self, value):
          self.value = value
          self.left  = None
          self.right = None

  class BinaryTree:
      def __init__(self, root=None):
          self.root = root
  ```

* **Methods to implement**:

  * `preorder_traversal(self, node=None, result=None) -> list[int]`
  * `inorder_traversal(self, node=None, result=None) -> list[int]`
  * `postorder_traversal(self, node=None, result=None) -> list[int]`
* **Behavior**:

  * Use `result` as an accumulator list.
  * Default `node` to `self.root` if `None`.
* **Outputs**:

  * A list of node values in the specified order.
* **Edge Cases**:

  * Empty tree ⇒ `[]`
  * Single‐node tree ⇒ `[value]`
* **Constraints**:

  * Do **not** change method signatures.

---

#### 🧪 Tests to Pass ✅

- **o7.2.1 Balanced‐tree traversals**  
  Verify that a full binary tree returns  
  - Inorder: `[4,2,5,1,3,6]`  
  - Preorder: `[1,2,4,5,3,6]`  
  - Postorder: `[4,5,2,6,3,1]`

- **o7.2.2 Single‐node tree**  
  All three traversals on a tree with one node (`42`) must return `[42]`.

- **o7.2.3 Empty tree**  
  Each traversal on an empty tree must return an empty list `[]`.

- **o7.2.4 Right‐heavy tree**  
  For a chain `1 → 2 → 3` (all to the right):  
  - Preorder: `[1,2,3]`  
  - Inorder:  `[1,2,3]`  
  - Postorder:`[3,2,1]`

- **o7.2.5 Return‐type verification**  
  Confirm that each traversal method always returns a Python `list`.  

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node=None, result=None):
        # Your solution here 🌲
        pass

    def inorder_traversal(self, node=None, result=None):
        # Your solution here 🔍
        pass

    def postorder_traversal(self, node=None, result=None):
        # Your solution here 🌴
        pass

def test_o7_2():
    # o7.2.1 Balanced Tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    tree = BinaryTree(root)
    record_test(
        "o7.2.1 balanced traversals",
        tree.inorder_traversal() == [4, 2, 5, 1, 3, 6]
        and tree.preorder_traversal() == [1, 2, 4, 5, 3, 6]
        and tree.postorder_traversal() == [4, 5, 2, 6, 3, 1],
    )

    # o7.2.2 Single Node
    single = BinaryTree(TreeNode(42))
    record_test(
        "o7.2.2 single",
        single.preorder_traversal() == [42]
        and single.inorder_traversal() == [42]
        and single.postorder_traversal() == [42],
    )

    # o7.2.3 Empty Tree
    empty = BinaryTree()
    record_test(
        "o7.2.3 empty",
        empty.preorder_traversal() == []
        and empty.inorder_traversal() == []
        and empty.postorder_traversal() == [],
    )

    # o7.2.4 Right-Heavy Tree
    rh = BinaryTree(TreeNode(1))
    rh.root.right = TreeNode(2)
    rh.root.right.right = TreeNode(3)
    record_test(
        "o7.2.4 right-heavy",
        rh.preorder_traversal() == [1, 2, 3]
        and rh.inorder_traversal() == [1, 2, 3]
        and rh.postorder_traversal() == [3, 2, 1],
    )

    # o7.2.5 Return-Type Verification
    tree2 = BinaryTree()
    record_test(
        "o7.2.5 types",
        isinstance(tree2.preorder_traversal(), list)
        and isinstance(tree2.inorder_traversal(), list)
        and isinstance(tree2.postorder_traversal(), list),
    )

# 🚀 Run tests
test_o7_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Use recursion with a `result` accumulator 😉
* Default `node = self.root` if `node` is `None` 🌳
* Follow the exact order for each traversal 🔄

---

#### 🧠 Motivation 💭

Traversals power **expression evaluation**, **tree serialization**, and many core algorithms—essential knowledge before moving on to search trees and beyond! 🌲🔄
