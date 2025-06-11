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
    pass

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
