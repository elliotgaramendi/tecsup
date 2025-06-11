"""
✨ Data Structures & Algorithms Exam by @elliotgaramendi 👨‍💻
"""

import time

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# o1 Algorithmic Complexity Challenges 📈⏱️
# ====================================================================


# --------------------------------------------------------------------
# o1.1 🧩 Count Doublings to Exceed N 🔢➕📈
# --------------------------------------------------------------------
def logarithmic_complexity(n):
    """🔢 Count doublings of 1 to exceed n; return (count, elapsed_time).
    If input invalid (not int or < 1), return (-1, elapsed_time). ❌"""
    start = time.time()
    # Input validation ❌
    if not isinstance(n, int) or n < 1:
        end = time.time()
        return -1, end - start

    # Doubling loop 🔄
    value = 1
    count = 0
    while value <= n:
        value *= 2  # 🔼 double
        count += 1  # ➕ increment
    end = time.time()
    elapsed = end - start
    return count, elapsed  # returns (int, float) 🆗


def test_o1_1():
    # --- Ideal cases (3 tests) 🌟 ---
    # o1.1.1: n = 1 → count = 1
    cnt, _ = logarithmic_complexity(1)
    record_test("o1.1.1 n=1 → count==1", cnt == 1)

    # o1.1.2: n = 10 → count = 4
    cnt, _ = logarithmic_complexity(10)
    record_test("o1.1.2 n=10 → count==4", cnt == 4)

    # o1.1.3: n = 100 → count = 7
    cnt, _ = logarithmic_complexity(100)
    record_test("o1.1.3 n=100 → count==7", cnt == 7)

    # --- Type check test 🧐 ---
    out = logarithmic_complexity(5)
    record_test(
        "o1.1.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float),
    )

    # --- Error handling test ⚠️ ---
    cnt_err, _ = logarithmic_complexity("a")
    record_test("o1.1.5 invalid input returns -1", cnt_err == -1)


# Run tests for o1.1 🚀
test_o1_1()


# --------------------------------------------------------------------
# o1.2 🧩 Sum of First N Naturals ➕📊⏱️
# --------------------------------------------------------------------
def constant_sum(n):
    """🔢 Compute sum of 1..n in O(1); return (sum, elapsed_time).
    If input invalid (not int or < 0), return (-1, elapsed_time). ❌"""
    start = time.time()
    # Input validation ❌
    if not isinstance(n, int) or n < 0:
        end = time.time()
        return -1, end - start

    # Closed-form formula 🔒
    total = n * (n + 1) // 2  # ➕ sum
    end = time.time()
    elapsed = end - start
    return total, elapsed  # returns (int, float) 🆗


def test_o1_2():
    # --- Ideal cases (3 tests) 🌟 ---
    # o1.2.1: n = 0 → sum = 0
    s, _ = constant_sum(0)
    record_test("o1.2.1 n=0 → sum==0", s == 0)

    # o1.2.2: n = 1 → sum = 1
    s, _ = constant_sum(1)
    record_test("o1.2.2 n=1 → sum==1", s == 1)

    # o1.2.3: n = 10 → sum = 55
    s, _ = constant_sum(10)
    record_test("o1.2.3 n=10 → sum==55", s == 55)

    # --- Type check test 🧐 ---
    out = constant_sum(5)
    record_test(
        "o1.2.4 returns (int, float)",
        isinstance(out[0], int) and isinstance(out[1], float),
    )

    # --- Error handling test ⚠️ ---
    s_err, _ = constant_sum("a")
    record_test("o1.2.5 invalid input returns -1", s_err == -1)


# Run tests for o1.2 🚀
test_o1_2()


# ====================================================================
# o2 Recursion & Backtracking 🌀🔙
# ====================================================================


# --------------------------------------------------------------------
# o2.1 🔁 Recursive Factorial 🧮✨
# --------------------------------------------------------------------
def factorial(n):
    """🔁 Compute n! recursively; return None if input invalid."""
    # Input validation ❌
    if not isinstance(n, int) or n < 0:
        return None
    # Base case 🌱
    if n == 0:
        return 1
    # Recursive case 🔄
    return n * factorial(n - 1)


def test_o2_1():
    # o2.1.1: n = 0 → 1
    record_test("o2.1.1 n=0 → 1", factorial(0) == 1)
    # o2.1.2: n = 5 → 120
    record_test("o2.1.2 n=5 → 120", factorial(5) == 120)
    # o2.1.3: n = 7 → 5040
    record_test("o2.1.3 n=7 → 5040", factorial(7) == 5040)
    # o2.1.4: type-check
    out = factorial(3)
    record_test("o2.1.4 returns int", isinstance(out, int))
    # o2.1.5: invalid input → None
    record_test(
        "o2.1.5 invalid returns None", factorial(-1) is None and factorial("a") is None
    )


# Run tests for o2.1 🚀
test_o2_1()


# --------------------------------------------------------------------
# o2.2 🔤 Generate Binary Strings of Length N 0️⃣1️⃣🛤️
# --------------------------------------------------------------------
def generate_binary_strings(n):
    """🔤 Generate all binary strings of length n via backtracking."""
    # Input validation ❌
    if not isinstance(n, int) or n < 0:
        return []
    result = []

    def backtrack(prefix):
        if len(prefix) == n:
            result.append(prefix)
            return
        backtrack(prefix + "0")
        backtrack(prefix + "1")

    backtrack("")
    return result


def test_o2_2():
    # o2.2.1: n = 2 → ['00','01','10','11']
    record_test(
        "o2.2.1 n=2 → 4 strings", generate_binary_strings(2) == ["00", "01", "10", "11"]
    )
    # o2.2.2: n = 3 → length = 8
    record_test("o2.2.2 n=3 → length=8", len(generate_binary_strings(3)) == 8)
    # o2.2.3: contains '101'
    record_test("o2.2.3 contains '101'", "101" in generate_binary_strings(3))
    # o2.2.4: type-check
    res = generate_binary_strings(1)
    record_test(
        "o2.2.4 returns list[str]",
        isinstance(res, list) and all(isinstance(s, str) for s in res),
    )
    # o2.2.5: invalid input → []
    record_test(
        "o2.2.5 invalid returns []",
        generate_binary_strings(-1) == [] and generate_binary_strings("a") == [],
    )


# Run tests for o2.2 🚀
test_o2_2()


# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")
