# 🎓✨ Data Structures & Algorithms Exam 🌟📚

Welcome to the ultimate Python-based exam! 🚀 Each week contains 2 exciting challenges 🔥 focused on a specific topic. Students will implement functions, validate inputs, and pass the given tests. Below is Week 1 (o1) with its two lively challenges! 🎉🧩

---

## o1: Algorithmic Complexity Challenges 📈⏱️

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

### o5.1 🔄 **Array-Based Queue: `enqueue`, `dequeue`, `peek`** 📥📤👀

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
          self.items = []
  ```
* **Methods to implement**:

  1. **`enqueue(self, item)`** – append `item` to `self.items`.
  2. **`dequeue(self)`** – if `items` non‐empty, `pop(0)` and return; else return `None`.
  3. **`peek(self)`** – if `items` non‐empty, return `items[0]`; else `None`.
* **Constraints**:

  * Use only list operations.
  * Safe defaults so harness never errors.

---

#### 🧪 Tests to Pass ✅

1. **o5.1.1**: Empty queue behavior

   * `q = Queue()`
   * `q.dequeue() is None` and `q.peek() is None` ✅
2. **o5.1.2**: Enqueue/Dequeue order

   * `q.enqueue(1); q.enqueue(2); q.enqueue(3)`
   * `q.dequeue() == 1`, `q.dequeue() == 2`, `q.dequeue() == 3` ✅
3. **o5.1.3**: Peek without removing

   * on fresh `q.enqueue("x")`
   * `q.peek() == "x"` and then still `q.dequeue() == "x"` ✅
4. **o5.1.4**: Mixed‐type support

   * `q.enqueue(None); q.enqueue("y")`
   * `q.peek() is None` and subsequently `q.dequeue() == None` ✅
5. **o5.1.5**: Return‐type tests

   * `isinstance(q.dequeue(), (int,str,type(None)))`
   * `isinstance(q.peek(), (int,str,type(None)))` ✅

---

#### 💻 Base Code 🖥️

```python
test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        return      # safe default

    def dequeue(self):
        """Remove and return front item or None if empty."""
        # Your solution here 🛠️
        return None # safe default

    def peek(self):
        """Return front item without removing or None if empty."""
        # Your solution here 🛠️
        return None # safe default

def test_o5_1():
    q = Queue()
    record_test("o5.1.1 empty behavior",
        q.dequeue() is None and q.peek() is None)

    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    record_test("o5.1.2 FIFO order",
        q.dequeue() == 1 and q.dequeue() == 2 and q.dequeue() == 3)

    q.enqueue("x")
    record_test("o5.1.3 peek preserves",
        q.peek() == "x" and q.dequeue() == "x")

    q.enqueue(None); q.enqueue("y")
    record_test("o5.1.4 mixed types",
        q.peek() is None and q.dequeue() is None)

    val1 = q.dequeue(); val2 = q.peek()
    record_test("o5.1.5 return types",
        isinstance(val1, (int,str,type(None))) and isinstance(val2, (int,str,type(None))))

# 🚀 Run tests
test_o5_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* Use `self.items.append(item)` for **enqueue** 📥.
* Use `self.items.pop(0)` for **dequeue** 🔄.
* Check `if self.items:` before accessing for **peek** 🔎.

---

#### 🧠 Motivation 💭

* Queues are **FIFO**: First In, First Out ⏳.
* Foundation for **task scheduling**, **BFS** on graphs, and **producer–consumer** models 🍃.

---

### o5.2 🔗 **Linked-List Queue: `is_empty`, `enqueue`, `dequeue`, `size`** 🧩📏

---

#### ❓ Problem 🤔

Implement a linked‐list based FIFO `LinkedQueue` with methods:

1. `is_empty()` → check if queue has no elements
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
          self.front = None  # Node or None
          self.rear  = None  # Node or None
          self._size = 0     # int
  ```
* **Methods to implement**:

  1. **`is_empty(self)`** – return `True` if `_size==0`.
  2. **`enqueue(self, item)`** – create `Node(item)`, link at `rear`, adjust `front` if needed, `_size += 1`.
  3. **`dequeue(self)`** – if non‐empty, remove `front`, return its `data`, `_size -= 1`; else `None`.
  4. **`size(self)`** – return `_size`.
* **Safe defaults** to keep harness running.

---

#### 🧪 Tests to Pass ✅

1. **o5.2.1**: Empty queue

   * `q = LinkedQueue()`
   * `q.is_empty() is True` and `q.size() == 0` ✅
2. **o5.2.2**: Enqueue/Dequeue

   * `q.enqueue("a"); q.enqueue("b")`
   * `q.is_empty() is False`, `q.size() == 2`, `q.dequeue() == "a"` ✅
3. **o5.2.3**: After removing all

   * `q.dequeue()` twice
   * `q.is_empty() is True`, `q.size() == 0` ✅
4. **o5.2.4**: Invalid dequeue

   * record `old = q.size()`
   * `q.dequeue() is None` and `q.size() == old` ✅
5. **o5.2.5**: Return‐type verification

   * `isinstance(q.is_empty(), bool)` and `isinstance(q.size(), int)` and `isinstance(q.dequeue(), (int,str,type(None)))` ✅

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
        self.front = None
        self.rear  = None
        self._size = 0

    def is_empty(self):
        """Return True if queue is empty."""
        # Your solution here 🛠️
        return True  # safe default

    def enqueue(self, item):
        """Add item to rear."""
        # Your solution here 🛠️
        return       # safe default

    def dequeue(self):
        """Remove and return front item or None."""
        # Your solution here 🛠️
        return None  # safe default

    def size(self):
        """Return number of elements."""
        # Your solution here 🛠️
        return 0     # safe default

def test_o5_2():
    q = LinkedQueue()
    record_test("o5.2.1 empty", q.is_empty() is True and q.size() == 0)

    q.enqueue("a"); q.enqueue("b")
    record_test("o5.2.2 enqueue/dequeue",
        q.is_empty() is False and q.size() == 2 and q.dequeue() == "a")

    q.dequeue()
    record_test("o5.2.3 drained",
        q.is_empty() is True and q.size() == 0)

    old = q.size()
    record_test("o5.2.4 invalid dequeue",
        q.dequeue() is None and q.size() == old)

    record_test("o5.2.5 return types",
        isinstance(q.is_empty(), bool)
        and isinstance(q.size(), int)
        and isinstance(q.dequeue(), (int,str,type(None))))

# 🚀 Run tests
test_o5_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips ✨

* **is\_empty** → check `_size == 0`.
* **enqueue** → link at `rear`; init both `front` & `rear` if first item.
* **dequeue** → unlink `front`; update `rear` if now empty.
* **size** → return `_size`.

---

#### 🧠 Motivation 💭

* Queues are crucial for **BFS**, **buffering**, and **rate‐limiting** 🔄.
* Linked‐list version avoids list‐shifting cost O(n) of array‐based dequeue 🚧.
* Reinforces dynamic memory and pointer handling 🧩.
