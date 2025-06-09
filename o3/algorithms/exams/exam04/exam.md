### o1.1 🧩 **Count Doublings to Exceed N** 📈⏱️

---

#### ❓ Problem

Implement `logarithmic_complexity(n)` to count how many times you must **double** 1 to exceed `n`, and return both the count and its execution time. 🔢⏳

---

#### 📜 Description

* **Function**: `logarithmic_complexity(n: int) → (int, float)` 🛠️
* **Inputs**:

  * `n`: positive integer (≥ 1) 🎯
* **Outputs**:

  * **count**: number of doublings required to make `value > n` 🔼
  * **time**: elapsed seconds as a float ⏱️
* **Expected Time Complexity**: **O(log n)** 📈
* **Edge cases**:

  * `n = 1` → count = 1 (1×2 = 2 > 1) ⚠️
  * Very large `n` (up to 10⁹) 🔧
* **Constraints**:

  * Must use a loop that doubles a running total ✔️
  * **Do not** use logarithm functions from `math` 🚫

---

#### 🧪 Tests to Pass

1. **o1.1.1**: Small `n`

   * `n = 1` 🔢 → returns `(1, time)` (since 1×2 > 1) ✅
2. **o1.1.2**: Moderate `n`

   * `n = 10` ➕ → returns `(4, time)` (1→2→4→8→16) ✅
3. **o1.1.3**: Larger `n`

   * `n = 100` ➕ → returns `(7, time)` (…→128) ✅
4. **o1.1.4**: Single doubling

   * `n = 2` ➕ → returns `(2, time)` (1→2→4) ✅
5. **o1.1.5**: Power of two

   * `n = 16` ✖️ ➕ → returns `(5, time)` (…→32) ✅

---

#### 💻 Base Code

```python
import time

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def logarithmic_complexity(n):
    """🔢 Count doublings of 1 to exceed n, return (count, elapsed_time)."""
    start = time.time()  # ⏱️ start timer
    # Your solution here 🛠️
    # e.g. value = 1; count = 0; while value <= n: …
    end = time.time()    # ⏱️ end timer
    elapsed = end - start
    return None, elapsed  # replace None with your count

def test_o1_1():
    # o1.1.1: n = 1
    cnt, _ = logarithmic_complexity(1)
    record_test("o1.1.1 n=1 → count=1", cnt == 1)
    # o1.1.2: n = 10
    cnt, _ = logarithmic_complexity(10)
    record_test("o1.1.2 n=10 → count=4", cnt == 4)
    # o1.1.3: n = 100
    cnt, _ = logarithmic_complexity(100)
    record_test("o1.1.3 n=100 → count=7", cnt == 7)
    # o1.1.4: n = 2
    cnt, _ = logarithmic_complexity(2)
    record_test("o1.1.4 n=2 → count=2", cnt == 2)
    # o1.1.5: n = 16
    cnt, _ = logarithmic_complexity(16)
    record_test("o1.1.5 n=16 → count=5", cnt == 5)

# 🚀 Run tests
test_o1_1()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips

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

---

#### 🧠 Motivation

* Demonstrates **logarithmic-time** growth—crucial in **binary search**, **divide-and-conquer** 🌳.
* Understanding O(log n) helps choose between iterative vs. recursive strategies 🔄.
* Real-world: doubling patterns appear in **data resizing**, **exponential backoff** 🔧.

---

### o1.2 🧩 **Sum of First N Naturals** ➕⏱️✨

---

#### ❓ Problem

Implement `constant_sum(n)` to compute the sum of the first `n` natural numbers in **constant time**, returning the result and execution time. 🔢⏳

---

#### 📜 Description

* **Function**: `constant_sum(n: int) → (int, float)` 🛠️
* **Inputs**:

  * `n`: non-negative integer (≥ 0) 🎯
* **Outputs**:

  * **sum**: `1 + 2 + … + n` ➕
  * **time**: elapsed seconds as a float ⏱️
* **Expected Time Complexity**: **O(1)** 🛑🔢
* **Edge cases**:

  * `n = 0` → sum = 0 ⚠️
  * Very large `n` (up to 10⁸) 🔧
* **Constraints**:

  * Must use the **formula** `n*(n+1)//2` ✔️
  * **Do not** loop over all numbers 🚫

---

#### 🧪 Tests to Pass

1. **o1.2.1**: Zero elements

   * `n = 0` ⚠️ → returns `(0, time)` ✅
2. **o1.2.2**: Small `n`

   * `n = 1` ➕ → returns `(1, time)` ✅
3. **o1.2.3**: Moderate `n`

   * `n = 10` ➕ → returns `(55, time)` ✅
4. **o1.2.4**: Larger `n`

   * `n = 1000` ➕ → returns `(500500, time)` ✅
5. **o1.2.5**: Type check

   * return types: `(int, float)` 🔍 ✅

---

#### 💻 Base Code

```python
import time

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

def constant_sum(n):
    """🔢 Compute sum of 1..n in O(1), return (sum, elapsed_time)."""
    start = time.time()  # ⏱️ start timer
    # Your solution here 🛠️
    end = time.time()    # ⏱️ end timer
    elapsed = end - start
    return None, elapsed  # replace None with your sum

def test_o1_2():
    # o1.2.1: n = 0
    s, _ = constant_sum(0)
    record_test("o1.2.1 n=0 → sum=0", s == 0)
    # o1.2.2: n = 1
    s, _ = constant_sum(1)
    record_test("o1.2.2 n=1 → sum=1", s == 1)
    # o1.2.3: n = 10
    s, _ = constant_sum(10)
    record_test("o1.2.3 n=10 → sum=55", s == 55)
    # o1.2.4: n = 1000
    s, _ = constant_sum(1000)
    record_test("o1.2.4 n=1000 → sum=500500", s == 500500)
    # o1.2.5: Type check
    out = constant_sum(5)
    record_test("o1.2.5 returns (int, float)", isinstance(out[0], int) and isinstance(out[1], float))

# 🚀 Run tests
test_o1_2()

# 📋 Summary
for r in test_results:
    print(r)
```

---

#### 💡 Tips

* Use the **closed-form formula**:

  ```python
  total = n * (n + 1) // 2
  ```
* No loops—ensures **O(1)** constant time 🔒.
* Measure with `time.time()` ⏱️ before/after.

---

#### 🧠 Motivation

* **Constant-time** methods underpin **direct calculations** in statistics and physics 📊🔬.
* Shows the power of **mathematical insight** vs. brute-force iteration 🧮.
* Real-world: formulae speed up large-scale data summaries in analytics 🍃.
