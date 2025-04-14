"""This script executes the complete algorithm and data structures exam using tests."""

import time

results = []


def test(title, condition):
    """Run a test and record the result."""
    emoji = "✅" if condition else "❌"
    results.append(f"{emoji} {title}")

# 🚀✨ Group 1: Algorithm Design and Complexity Analysis ✨🚀

# ---------------------------
# 🧮 logarithmic_complexity
# ---------------------------


def logarithmic_complexity(n):
    """Return number of doublings to exceed n."""
    start = time.time()
    count = 0
    value = 1
    while value <= n:
        value *= 2
        count += 1
    end = time.time()
    return count, end - start


test("1.1.1 logarithmic_complexity(10)", logarithmic_complexity(10)[0] == 4)
test("1.1.2 logarithmic_complexity(100)", logarithmic_complexity(100)[0] == 7)
test("1.1.3 logarithmic_complexity(1000)",
     logarithmic_complexity(1000)[0] == 10)
test("1.1.4 type check int", isinstance(logarithmic_complexity(100)[0], int))
test("1.1.5 type check float", isinstance(
    logarithmic_complexity(100)[1], float))

# ---------------------------
# ➕ linear_sum_with_time
# ---------------------------


def linear_sum_with_time(n):
    """Return sum of first n natural numbers."""
    start = time.time()
    result = n * (n + 1) // 2
    end = time.time()
    return result, end - start


test("1.2.1 linear_sum_with_time(100)", linear_sum_with_time(100)[0] == 5050)
test("1.2.2 linear_sum_with_time(0)", linear_sum_with_time(0)[0] == 0)
test("1.2.3 linear_sum_with_time(10)", linear_sum_with_time(10)[0] == 55)
test("1.2.4 type check int", isinstance(linear_sum_with_time(10)[0], int))
test("1.2.5 type check float", isinstance(linear_sum_with_time(10)[1], float))

# ---------------------------
# 🔢 count_even_numbers_with_time
# ---------------------------


def count_even_numbers_with_time(n):
    """Return count of even numbers from 0 to n."""
    start = time.time()
    count = 0
    for i in range(n + 1):
        if i % 2 == 0:
            count += 1
    end = time.time()
    return count, end - start


test("1.3.1 count_even_numbers_with_time(10)",
     count_even_numbers_with_time(10)[0] == 6)
test("1.3.2 count_even_numbers_with_time(1)",
     count_even_numbers_with_time(1)[0] == 1)
test("1.3.3 count_even_numbers_with_time(20)",
     count_even_numbers_with_time(20)[0] == 11)
test("1.3.4 type check int", isinstance(
    count_even_numbers_with_time(5)[0], int))
test("1.3.5 type check float", isinstance(
    count_even_numbers_with_time(5)[1], float))

# ---------------------------
# 🧩 is_perfect_number_with_time
# ---------------------------


def is_perfect_number_with_time(n):
    """Return True if number is perfect."""
    start = time.time()
    total = sum(i for i in range(1, n) if n % i == 0)
    end = time.time()
    return total == n, end - start


test("1.4.1 is_perfect_number_with_time(6)",
     is_perfect_number_with_time(6)[0] == True)
test("1.4.2 is_perfect_number_with_time(12)",
     is_perfect_number_with_time(12)[0] == False)
test("1.4.3 is_perfect_number_with_time(28)",
     is_perfect_number_with_time(28)[0] == True)
test("1.4.4 type check bool", isinstance(
    is_perfect_number_with_time(28)[0], bool))
test("1.4.5 type check float", isinstance(
    is_perfect_number_with_time(28)[1], float))

# ---------------------------
# ♻️ has_duplicates_with_time
# ---------------------------


def has_duplicates_with_time(arr):
    """Return True if array contains duplicates."""
    start = time.time()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                end = time.time()
                return True, end - start
    end = time.time()
    return False, end - start


test("1.5.1 has_duplicates_with_time([1,2,3,4])", has_duplicates_with_time(
    [1, 2, 3, 4])[0] == False)
test("1.5.2 has_duplicates_with_time([1,2,2,3])",
     has_duplicates_with_time([1, 2, 2, 3])[0] == True)
test("1.5.3 has_duplicates_with_time([5,5,5])",
     has_duplicates_with_time([5, 5, 5])[0] == True)
test("1.5.4 type check bool", isinstance(
    has_duplicates_with_time([1, 2])[0], bool))
test("1.5.5 type check float", isinstance(
    has_duplicates_with_time([1, 2])[1], float))


# 🌱 Group 2: Recursive Algorithms and Backtracking Techniques 🌀

# ---------------------------
# 🧮 Recursive Factorial
# ---------------------------

def factorial(n):
    """Return the factorial of n using recursion."""
    return 1 if n in (0, 1) else n * factorial(n - 1)


test("2.1.1 factorial(5)", factorial(5) == 120)
test("2.1.2 factorial(0)", factorial(0) == 1)
test("2.1.3 factorial(1)", factorial(1) == 1)
test("2.1.4 factorial(7)", factorial(7) == 5040)
test("2.1.5 type check", isinstance(factorial(6), int))

# ---------------------------
# 🔢 Recursive Sum of Digits
# ---------------------------


def sum_of_digits(n):
    """Return the sum of digits of n using recursion."""
    return n if n < 10 else n % 10 + sum_of_digits(n // 10)


test("2.2.1 sum_of_digits(123)", sum_of_digits(123) == 6)
test("2.2.2 sum_of_digits(9)", sum_of_digits(9) == 9)
test("2.2.3 sum_of_digits(10)", sum_of_digits(10) == 1)
test("2.2.4 sum_of_digits(9876)", sum_of_digits(9876) == 30)
test("2.2.5 type check", isinstance(sum_of_digits(50), int))

# ---------------------------
# 🌀 fibonacci
# ---------------------------


def fibonacci(n):
    """Return the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


test("2.3.1 fibonacci(0)", fibonacci(0) == 0)
test("2.3.2 fibonacci(1)", fibonacci(1) == 1)
test("2.3.3 fibonacci(2)", fibonacci(2) == 1)
test("2.3.4 fibonacci(10)", fibonacci(10) == 55)
test("2.3.5 type check", isinstance(fibonacci(5), int))


# ---------------------------
# 💻 Generate Binary Strings
# ---------------------------

def generate_binary_strings(n):
    """Return list of binary strings of length n using backtracking."""
    if n == 0:
        return [""]
    smaller = generate_binary_strings(n - 1)
    return ["0" + s for s in smaller] + ["1" + s for s in smaller]


test("2.4.1 binary_strings(1)", generate_binary_strings(1) == ['0', '1'])
test("2.4.2 binary_strings(2)", generate_binary_strings(
    2) == ['00', '01', '10', '11'])
test("2.4.3 binary_strings(0)", generate_binary_strings(0) == [''])
test("2.4.4 binary_strings(3) length", len(generate_binary_strings(3)) == 8)
test("2.4.5 type check", isinstance(generate_binary_strings(2), list))

# ---------------------------
# 🔠 Generate T/F Combinations
# ---------------------------


def generate_tf_combinations(n):
    """Return list of all 'T'/'F' combinations of length n using backtracking."""
    if n == 0:
        return [""]
    smaller = generate_tf_combinations(n - 1)
    return ["T" + s for s in smaller] + ["F" + s for s in smaller]


test("2.5.1 tf_combinations(1)", generate_tf_combinations(1) == ['T', 'F'])
test("2.5.2 tf_combinations(2)", generate_tf_combinations(
    2) == ['TT', 'TF', 'FT', 'FF'])
test("2.5.3 tf_combinations(0)", generate_tf_combinations(0) == [''])
test("2.5.4 tf_combinations(3) length", len(generate_tf_combinations(3)) == 8)
test("2.5.5 type check", isinstance(generate_tf_combinations(2), list))


# 📎✨ Group 3: Linked Lists – Insertion, Deletion, Search and Traversal ✨📎

class Node:
    """A node for singly linked list."""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation with various operations."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, target):
        """Search for a value in the list."""
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def delete(self, target):
        """Delete the first occurrence of a value in the list."""
        current = self.head
        prev = None
        while current:
            if current.data == target:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """Return a string representation of the list."""
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty list"


# ---------------------------
# ⬅️ insert_at_beginning
# ---------------------------
ll0 = LinkedList()
ll0.insert_at_beginning(3)
test("3.1.1 insert_at_beginning: first node", ll0.display() == '3')
ll0.insert_at_beginning(2)
test("3.1.2 insert_at_beginning: second node", ll0.display() == '2 -> 3')
ll0.insert_at_beginning(1)
test("3.1.3 insert_at_beginning: third node", ll0.display() == '1 -> 2 -> 3')
ll0.insert_at_beginning(0)
test("3.1.4 insert_at_beginning: fourth node",
     ll0.display() == '0 -> 1 -> 2 -> 3')
test("3.1.5 type check", isinstance(ll0.head.data, int))

# ---------------------------
# ➡️ insert_at_end
# ---------------------------
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
test("3.2.1 insert_at_end: basic insert", ll.display() == "1 -> 2 -> 3")
ll.insert_at_beginning(0)
test("3.2.2 insert_at_beginning", ll.display() == "0 -> 1 -> 2 -> 3")
test("3.2.3 type check int", isinstance(ll.head.data, int))
ll.insert_at_end(4)
test("3.2.4 insert_at_end: final insert",
     ll.display() == "0 -> 1 -> 2 -> 3 -> 4")
test("3.2.5 type check str", isinstance(ll.display(), str))

# ---------------------------
# 📏 length
# ---------------------------
ll2 = LinkedList()
test("3.3.1 length: empty", ll2.length() == 0)
ll2.insert_at_beginning(1)
test("3.3.2 length: 1 element", ll2.length() == 1)
ll2.insert_at_beginning(2)
ll2.insert_at_beginning(3)
test("3.3.3 length: 3 elements", ll2.length() == 3)
ll2.insert_at_beginning(4)
test("3.3.4 length: 4 elements", ll2.length() == 4)
test("3.3.5 type check", isinstance(ll2.length(), int))

# ---------------------------
# 🔍 search
# ---------------------------
ll3 = LinkedList()
for v in [3, 2, 1, 0]:
    ll3.insert_at_beginning(v)
test("3.4.1 search 2", ll3.search(2))
test("3.4.2 search 0", ll3.search(0))
test("3.4.3 search 3", ll3.search(3))
test("3.4.4 search 4 (not found)", not ll3.search(4))
test("3.4.5 type check", isinstance(ll3.search(1), bool))

# ---------------------------
# 🗑️ delete
# ---------------------------
ll4 = LinkedList()
for v in [3, 2, 1, 0]:
    ll4.insert_at_beginning(v)
ll4.delete(2)
test("3.5.1 delete 2", ll4.display() == "0 -> 1 -> 3")
ll4.delete(0)
test("3.5.2 delete 0", ll4.display() == "1 -> 3")
ll4.delete(3)
test("3.5.3 delete 3", ll4.display() == "1")
ll4.delete(1)
test("3.5.4 delete 1", ll4.display() == "Empty list")
ll4.delete(4)
test("3.5.5 delete non-existent", ll4.display() == "Empty list")

# ---------------------------
# 🔁 reverse
# ---------------------------
ll5 = LinkedList()
for v in [3, 2, 1, 0]:
    ll5.insert_at_beginning(v)
ll5.reverse()
test("3.6.1 reverse 4 elements", ll5.display() == "3 -> 2 -> 1 -> 0")

ll6 = LinkedList()
ll6.insert_at_beginning(1)
ll6.reverse()
test("3.6.2 reverse 1 element", ll6.display() == "1")

ll7 = LinkedList()
ll7.reverse()
test("3.6.3 reverse empty", ll7.display() == "Empty list")

ll8 = LinkedList()
ll8.insert_at_beginning(2)
ll8.insert_at_beginning(1)
ll8.reverse()
test("3.6.4 reverse 2 elements", ll8.display() == "2 -> 1")

test("3.6.5 type check str", isinstance(ll8.display(), str))


# 📚✨ Group 4: Stack Data Structures – Array-based and Linked-based Implementation ✨📚

# ---------------------------
# 🧪 Stack Class (Array-Based)
# ---------------------------

class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.items) == 0

    def push(self, data):
        """Push an item onto the stack."""
        self.items.append(data)

    def pop(self):
        """Pop the top item from the stack and return it."""
        return self.items.pop() if self.items else None

    def peek(self):
        """Return the top item without removing it."""
        return self.items[-1] if self.items else None

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


# ---------------------------
# 🔍 Test: is_empty()
# ---------------------------
test("4.1.1 Stack is empty", Stack().is_empty() == True)
s1 = Stack()
s1.push(1)
test("4.1.2 Stack is not empty after push", s1.is_empty() == False)
s1.pop()
test("4.1.3 Stack is empty after pop", s1.is_empty() == True)
s1.push(0)
test("4.1.4 Stack is not empty again", s1.is_empty() == False)
test("4.1.5 Return type check", isinstance(s1.is_empty(), bool))


# ---------------------------
# ➕ Test: push()
# ---------------------------
s2 = Stack()
s2.push(1)
s2.push(2)
s2.push(3)
test("4.2.1 Pushing multiple values", s2.items == [1, 2, 3])
s2.push(0)
test("4.2.2 Push additional value", s2.items == [1, 2, 3, 0])
test("4.2.3 Type is list", isinstance(s2.items, list))
test("4.2.4 Top is last pushed", s2.items[-1] == 0)
test("4.2.5 Size of stack is correct", len(s2.items) == 4)


# ---------------------------
# ➖ Test: pop()
# ---------------------------
s3 = Stack()
s3.items = [1, 2, 3]
test("4.3.1 Pop last", s3.pop() == 3)
test("4.3.2 Pop second last", s3.pop() == 2)
test("4.3.3 Pop first", s3.pop() == 1)
test("4.3.4 Pop empty returns None", s3.pop() == None)
test("4.3.5 Stack is still list", isinstance(s3.items, list))


# ---------------------------
# 👁️ Test: peek()
# ---------------------------
s4 = Stack()
s4.items = [10, 20, 30]
test("4.4.1 Peek top", s4.peek() == 30)
s4.pop()
test("4.4.2 Peek after pop", s4.peek() == 20)
s4.items.clear()
test("4.4.3 Peek on empty stack", s4.peek() == None)
s4.push(99)
test("4.4.4 Peek after new push", s4.peek() == 99)
test("4.4.5 Return type check", isinstance(
    s4.peek(), int) or s4.peek() is None)


# ---------------------------
# 📦 Test: size()
# ---------------------------
s5 = Stack()
test("4.5.1 Size of empty stack", s5.size() == 0)
s5.items = [1]
test("4.5.2 Size with one item", s5.size() == 1)
s5.items = [1, 2, 3, 4]
test("4.5.3 Size with four items", s5.size() == 4)
s5.pop()
test("4.5.4 Size after pop", s5.size() == 3)
test("4.5.5 Return type is int", isinstance(s5.size(), int))


# ---------------------------
# 🔗 LinkedStack Class (Node-Based)
# ---------------------------

class Node:
    """Node class for linked stack."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    """Stack implementation using linked nodes."""

    def __init__(self):
        self.top = None

    def push(self, data):
        """Push data onto the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Remove and return the top of the stack."""
        if not self.top:
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        """Return the top value without removing it."""
        return self.top.data if self.top else None

    def display(self):
        """Return stack as a string from top to bottom."""
        current = self.top
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) if result else "Empty"


# ---------------------------
# 🧱 Test: LinkedStack push()
# ---------------------------
ls1 = LinkedStack()
ls1.push(1)
ls1.push(2)
ls1.push(3)
test("4.6.1 LinkedStack push order", ls1.display() == "3 -> 2 -> 1")
ls1.push(4)
test("4.6.2 Push another", ls1.display() == "4 -> 3 -> 2 -> 1")
test("4.6.3 Top is integer", isinstance(ls1.top.data, int))
ls1.push(5)
test("4.6.4 Top check", ls1.peek() == 5)
test("4.6.5 Return type str", isinstance(ls1.display(), str))


# ---------------------------
# 🧽 Test: LinkedStack pop()
# ---------------------------
ls2 = LinkedStack()
for val in [1, 2, 3]:
    ls2.push(val)
test("4.7.1 Pop from top", ls2.pop() == 3)
test("4.7.2 Next pop", ls2.pop() == 2)
test("4.7.3 One remains", ls2.display() == "1")
test("4.7.4 Pop last", ls2.pop() == 1)
test("4.7.5 Pop empty", ls2.pop() == None)


# ---------------------------
# 🧼 Test: LinkedStack peek()
# ---------------------------
ls3 = LinkedStack()
test("4.8.1 Peek empty", ls3.peek() == None)
ls3.push(10)
test("4.8.2 Peek 10", ls3.peek() == 10)
ls3.push(20)
test("4.8.3 Peek 20", ls3.peek() == 20)
ls3.push(30)
test("4.8.4 Peek 30", ls3.peek() == 30)
ls3.pop()
test("4.8.5 Peek after pop", ls3.peek() == 20)


# ---------------------------
# 🧾 Final Summary
# ---------------------------
print("\n# Final Test Summary")
for result in results:
    print(result)

print(f"\nTotal Approved: {sum('✅' in r for r in results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in results)} ❌")
