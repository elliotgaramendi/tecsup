"""
Recursion and Backtracking Algorithms - Implementation
"""

# Recursion Exercises


def factorial(n):
    """Calculate n! using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n-1)


def power(x, n):
    """Calculate x^n using recursion"""
    if n == 0:
        return 1
    return x * power(x, n-1)


def sum_digits(n):
    """Sum the digits of n recursively"""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def is_palindrome(text):
    """Check if text is a palindrome recursively"""
    text = text.lower().replace(" ", "")
    if len(text) <= 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


def reverse_string(s):
    """Reverse a string using recursion"""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


def sum_list(arr):
    """Sum elements of a list recursively"""
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1:])


def fibonacci(n):
    """Calculate the nth Fibonacci number recursively"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def towers_of_hanoi(n, source="A", auxiliary="B", target="C"):
    """Solve Tower of Hanoi puzzle for n disks"""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    towers_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n-1, auxiliary, source, target)


# Backtracking Exercises

def generate_binary_strings(n, current=""):
    """Generate all binary strings of length n"""
    if len(current) == n:
        print(current)
        return

    generate_binary_strings(n, current + "0")
    generate_binary_strings(n, current + "1")


def generate_tf_combinations(n, current=""):
    """Generate all T/F combinations of length n"""
    if len(current) == n:
        print(current)
        return

    generate_tf_combinations(n, current + "T")
    generate_tf_combinations(n, current + "F")


def generate_123_numbers(n, current=""):
    """Generate all numbers of length n using digits 1,2,3"""
    if len(current) == n:
        print(current)
        return

    generate_123_numbers(n, current + "1")
    generate_123_numbers(n, current + "2")
    generate_123_numbers(n, current + "3")


def find_subsets_with_sum(numbers, target_sum, current=None, index=0):
    """Find all subsets of numbers that sum to target_sum"""
    if current is None:
        current = []

    if sum(current) == target_sum:
        print(current)

    if index >= len(numbers) or sum(current) > target_sum:
        return

    # Include current number
    current.append(numbers[index])
    find_subsets_with_sum(numbers, target_sum, current, index + 1)

    # Exclude current number (backtrack)
    current.pop()
    find_subsets_with_sum(numbers, target_sum, current, index + 1)


# Test cases
if __name__ == "__main__":
    # Recursion tests
    print("=== Factorial ===")
    print(f"factorial(0) = {factorial(0)}")      # 1
    print(f"factorial(5) = {factorial(5)}")      # 120
    print(f"factorial(10) = {factorial(10)}")    # 3628800

    print("\n=== Power ===")
    print(f"power(2, 0) = {power(2, 0)}")        # 1
    print(f"power(2, 10) = {power(2, 10)}")      # 1024
    print(f"power(5, 3) = {power(5, 3)}")        # 125

    print("\n=== Sum of Digits ===")
    print(f"sum_digits(7) = {sum_digits(7)}")         # 7
    print(f"sum_digits(123) = {sum_digits(123)}")     # 6
    print(f"sum_digits(9999) = {sum_digits(9999)}")   # 36

    print("\n=== Palindrome Check ===")
    print(f"is_palindrome('radar') = {is_palindrome('radar')}")  # True
    # True
    print(
        f"is_palindrome('A man a plan a canal Panama') = {is_palindrome('A man a plan a canal Panama')}")
    print(f"is_palindrome('hello') = {is_palindrome('hello')}")  # False

    print("\n=== String Reversal ===")
    print(f"reverse_string('hello') = {reverse_string('hello')}")    # olleh
    print(f"reverse_string('Python') = {reverse_string('Python')}")  # nohtyP

    print("\n=== Sum of List ===")
    print(f"sum_list([1, 2, 3, 4, 5]) = {sum_list([1, 2, 3, 4, 5])}")  # 15
    print(f"sum_list([-1, 10, -5, 6]) = {sum_list([-1, 10, -5, 6])}")  # 10

    print("\n=== Fibonacci ===")
    print(f"fibonacci(7) = {fibonacci(7)}")  # 13

    print("\n=== Towers of Hanoi ===")
    print("towers_of_hanoi(3):")
    towers_of_hanoi(3)

    # Backtracking tests
    print("\n=== Binary Strings ===")
    print("generate_binary_strings(2):")
    generate_binary_strings(2)

    print("\n=== T/F Combinations ===")
    print("generate_tf_combinations(2):")
    generate_tf_combinations(2)

    print("\n=== 1,2,3 Numbers ===")
    print("generate_123_numbers(2):")
    generate_123_numbers(2)

    print("\n=== Subset Sum ===")
    print("find_subsets_with_sum([1, 2, 3], 3):")
    find_subsets_with_sum([1, 2, 3], 3)
