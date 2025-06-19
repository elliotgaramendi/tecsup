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
# o3 Linked Lists 📎🔗
# ====================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list with insert, display, search, delete, and length."""

    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        """Insert new node at beginning and update length."""
        if not isinstance(data, int):
            return
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert_at_end(self, data):
        """Insert new node at end and update length."""
        if not isinstance(data, int):
            return
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        self.length += 1

    def search(self, target):
        """Return True if target exists, else False."""
        if not isinstance(target, int):
            return False
        curr = self.head
        while curr:
            if curr.data == target:
                return True
            curr = curr.next
        return False

    def delete(self, target):
        """Delete first node with data == target and update length."""
        if not isinstance(target, int):
            return
        # delete head
        if self.head and self.head.data == target:
            self.head = self.head.next
            self.length -= 1
            return
        prev, curr = None, self.head
        while curr:
            if curr.data == target:
                prev.next = curr.next
                self.length -= 1
                return
            prev, curr = curr, curr.next

    def display(self):
        """Return 'Empty list' or 'val1 -> val2 -> ...'."""
        curr, vals = self.head, []
        while curr:
            vals.append(str(curr.data))
            curr = curr.next
        return " -> ".join(vals) if vals else "Empty list"


# --------------------------------------------------------------------
# o3.1 ➕ Insert at Beginning, Insert at End & Length 🏁👶➕📏
# --------------------------------------------------------------------
def test_o3_1():
    ll = LinkedList()
    # o3.1.1 Mixed single insert
    ll.insert_at_beginning(2)
    ll.insert_at_end(3)
    record_test("o3.1.1 ll.display() == '2 -> 3'", ll.display() == "2 -> 3")
    # o3.1.2 Mixed multiple inserts
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    record_test(
        "o3.1.2 ll.display() == '1 -> 2 -> 3 -> 4'", ll.display() == "1 -> 2 -> 3 -> 4"
    )
    # o3.1.3 Length tracking
    record_test("o3.1.3 ll.length == 4", ll.length == 4)
    # o3.1.4 Invalid input handling
    old_len = ll.length
    ll.insert_at_beginning(None)
    ll.insert_at_end("x")
    record_test("o3.1.4 invalid ignored", ll.length == old_len)
    # o3.1.5 Return-type verification
    record_test(
        "o3.1.5 types ok", isinstance(ll.length, int) and isinstance(ll.display(), str)
    )


# Run tests for o3.1 🚀
test_o3_1()


# --------------------------------------------------------------------
# o3.2 🔍❌ Search & Delete 🕵️‍♂️🗑️
# --------------------------------------------------------------------
def test_o3_2():
    ll = LinkedList()
    for v in [1, 2, 3, 4]:
        ll.insert_at_end(v)
    # o3.2.1 Search found
    record_test("o3.2.1 search(3) True", ll.search(3) is True)
    # o3.2.2 Delete middle
    ll.delete(2)
    record_test("o3.2.2 display == '1 -> 3 -> 4'", ll.display() == "1 -> 3 -> 4")
    # o3.2.3 Delete ends
    ll.delete(1)
    ll.delete(4)
    record_test("o3.2.3 display == '3'", ll.display() == "3")
    # o3.2.4 Invalid operations
    old = ll.length
    cond = ll.search(None) is False
    ll.delete(999)
    cond = cond and (ll.length == old)
    record_test("o3.2.4 invalid handled", cond)
    # o3.2.5 Return-type
    record_test(
        "o3.2.5 types ok", isinstance(ll.search(3), bool) and isinstance(ll.length, int)
    )


# Run tests for o3.2 🚀
test_o3_2()


# ====================================================================
# o4 Stacks 📚🧱
# ====================================================================


# --------------------------------------------------------------------
# o4.1 🧩 Array-Based Stack: is_empty, push, pop 🔄📥📤
# --------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if stack is empty."""
        return not self.items

    def push(self, data):
        """Push data onto the stack."""
        self.items.append(data)

    def pop(self):
        """Pop and return top item or None if empty."""
        if self.items:
            return self.items.pop()
        return None


def test_o4_1():
    # o4.1.1 Core operations
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

    # o4.1.2 Pop on empty
    secondary_stack = Stack()
    record_test("o4.1.2 pop on empty", secondary_stack.pop() is None)

    # o4.1.3 Mixed operations
    mixed_stack = Stack()
    mixed_stack.push(0)
    mixed_stack.push(99)
    cond_mixed = mixed_stack.pop() == 99 and mixed_stack.is_empty() is False
    record_test("o4.1.3 mixed operations", cond_mixed)

    # o4.1.4 Input-agnostic storage
    any_stack = Stack()
    any_stack.push(None)
    any_stack.push("x")
    record_test("o4.1.4 input-agnostic storage", any_stack.items == [None, "x"])

    # o4.1.5 Return-type verification
    popped_value = main_stack.pop()
    cond_types = isinstance(main_stack.is_empty(), bool) and isinstance(
        popped_value, (int, str, type(None))
    )
    record_test("o4.1.5 return-type verification", cond_types)


# Run tests for o4.1 🚀
test_o4_1()


# --------------------------------------------------------------------
# o4.2 🧩 Linked-List Stack: push, pop, peek, size 🔗👀📏
# --------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Push element using linked nodes."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Pop and return top data or None."""
        if not self.top:
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def peek(self):
        """Return top data without removing or None."""
        return self.top.data if self.top else None

    def size(self):
        """Return number of items."""
        return self._size


def test_o4_2():
    # o4.2.1 Empty behavior
    linked_stack = LinkedStack()
    cond_empty = (
        linked_stack.peek() is None
        and linked_stack.pop() is None
        and linked_stack.size() == 0
    )
    record_test("o4.2.1 empty behavior", cond_empty)

    # o4.2.2 Push & peek & size
    linked_stack.push(5)
    linked_stack.push(7)
    linked_stack.push(9)
    cond_push = linked_stack.peek() == 9 and linked_stack.size() == 3
    record_test("o4.2.2 push/peek/size", cond_push)

    # o4.2.3 After pop
    linked_stack.pop()
    cond_after_pop = linked_stack.peek() == 7 and linked_stack.size() == 2
    record_test("o4.2.3 pop adjusts", cond_after_pop)

    # o4.2.4 Mixed types
    linked_stack.push("a")
    cond_mixed = linked_stack.peek() == "a" and linked_stack.size() == 3
    record_test("o4.2.4 mixed types", cond_mixed)

    # o4.2.5 Return-type verification
    cond_types = isinstance(linked_stack.peek(), (int, str, type(None))) and isinstance(
        linked_stack.size(), int
    )
    record_test("o4.2.5 return-type verification", cond_types)


# Run tests for o4.2 🚀
test_o4_2()


# ====================================================================
# o5 Queues 🚶‍♀️🚶
# ====================================================================


# --------------------------------------------------------------------
# o5.1 🧩 Array-Based Queue: enqueue, dequeue, peek 📥📤👀
# --------------------------------------------------------------------
class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        """Add item to rear."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return front item or None if empty."""
        if self._items:
            return self._items.pop(0)
        return None

    def peek(self):
        """Return front item without removing or None if empty."""
        if self._items:
            return self._items[0]
        return None


def test_o5_1():
    queue_array = Queue()
    record_test(
        "o5.1.1 empty behavior",
        queue_array.dequeue() is None and queue_array.peek() is None,
    )

    queue_array.enqueue(1)
    queue_array.enqueue(2)
    queue_array.enqueue(3)
    record_test(
        "o5.1.2 FIFO order",
        queue_array.dequeue() == 1
        and queue_array.dequeue() == 2
        and queue_array.dequeue() == 3,
    )

    queue_array.enqueue("x")
    record_test(
        "o5.1.3 peek preserves",
        queue_array.peek() == "x" and queue_array.dequeue() == "x",
    )

    queue_array.enqueue(None)
    queue_array.enqueue("y")
    record_test(
        "o5.1.4 mixed types",
        queue_array.peek() is None and queue_array.dequeue() is None,
    )

    removed_value = queue_array.dequeue()
    peeked_value = queue_array.peek()
    record_test(
        "o5.1.5 return types",
        isinstance(removed_value, (int, str, type(None)))
        and isinstance(peeked_value, (int, str, type(None))),
    )


# Run tests for o5.1 🚀
test_o5_1()


# --------------------------------------------------------------------
# o5.2 🧩 Linked-List Queue: is_empty, enqueue, dequeue, size 🔗📏
# --------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self._front = None  # Node or None
        self._rear = None  # Node or None
        self._count = 0  # int

    def is_empty(self):
        """Return True if queue is empty."""
        return self._count == 0

    def enqueue(self, item):
        """Add item to rear."""
        new_node = Node(item)
        if self._rear is None:
            # first item
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._count += 1

    def dequeue(self):
        """Remove and return front item or None."""
        if self._front is None:
            return None
        removed_data = self._front.data
        self._front = self._front.next
        self._count -= 1
        if self._front is None:
            # queue is now empty
            self._rear = None
        return removed_data

    def size(self):
        """Return number of elements."""
        return self._count


def test_o5_2():
    queue_linked = LinkedQueue()
    record_test(
        "o5.2.1 empty", queue_linked.is_empty() is True and queue_linked.size() == 0
    )

    queue_linked.enqueue("a")
    queue_linked.enqueue("b")
    record_test(
        "o5.2.2 enqueue/dequeue",
        queue_linked.is_empty() is False
        and queue_linked.size() == 2
        and queue_linked.dequeue() == "a",
    )

    queue_linked.dequeue()
    record_test(
        "o5.2.3 drained", queue_linked.is_empty() is True and queue_linked.size() == 0
    )

    previous_size = queue_linked.size()
    record_test(
        "o5.2.4 invalid dequeue",
        queue_linked.dequeue() is None and queue_linked.size() == previous_size,
    )

    record_test(
        "o5.2.5 return types",
        isinstance(queue_linked.is_empty(), bool)
        and isinstance(queue_linked.size(), int)
        and isinstance(queue_linked.dequeue(), (int, str, type(None))),
    )


# Run tests for o5.2 🚀
test_o5_2()


# ====================================================================
# o6: Advanced Queues 🚀📊
# ====================================================================


# --------------------------------------------------------------------
# o6.1 🧩 Circular Array Queue: enqueue, dequeue, size 🔄📥📤
# --------------------------------------------------------------------
class CircularArrayQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self._queue = [None] * capacity
        self._front = 0
        self._rear = -1
        self._count = 0

    def enqueue(self, item) -> bool:
        """Add item if not full, return True; else False."""
        if self._count < self.capacity:
            self._rear = (self._rear + 1) % self.capacity  # wrap-around 🔁
            self._queue[self._rear] = item  # store 📥
            self._count += 1  # increment count
            return True  # success ✅
        return False  # full 🚫

    def dequeue(self):
        """Remove and return front item or None if empty."""
        if self._count > 0:
            item = self._queue[self._front]  # retrieve 📤
            self._front = (self._front + 1) % self.capacity  # advance front 🔁
            self._count -= 1  # decrement count
            return item
        return None  # empty 📭

    def size(self) -> int:
        """Return number of elements."""
        return self._count  # return count 📏


def test_o6_1():
    # o6.1.1 Basic enqueue/dequeue + count
    circular_array_queue = CircularArrayQueue(3)
    circular_array_queue.enqueue("A")
    circular_array_queue.enqueue("B")
    circular_array_queue.enqueue("C")
    record_test(
        "o6.1.1 basic",
        circular_array_queue.dequeue() == "A"
        and circular_array_queue.dequeue() == "B"
        and circular_array_queue.dequeue() == "C"
        and circular_array_queue.size() == 0,
    )

    # o6.1.2 Wrap-around behavior + count
    circular_array_queue = CircularArrayQueue(3)
    circular_array_queue.enqueue(1)
    circular_array_queue.enqueue(2)
    circular_array_queue.enqueue(3)
    circular_array_queue.dequeue()  # frees slot
    circular_array_queue.enqueue(4)  # wrap into idx 0 🔁
    record_test(
        "o6.1.2 wrap",
        circular_array_queue.dequeue() == 2
        and circular_array_queue.dequeue() == 3
        and circular_array_queue.dequeue() == 4
        and circular_array_queue.size() == 0,
    )

    # o6.1.3 Empty after ops + count
    circular_array_queue = CircularArrayQueue(2)
    circular_array_queue.enqueue("X")
    circular_array_queue.enqueue("Y")
    circular_array_queue.dequeue()
    circular_array_queue.dequeue()
    record_test(
        "o6.1.3 empty",
        circular_array_queue.dequeue() is None and circular_array_queue.size() == 0,
    )

    # o6.1.4 Validation: full queue + count unchanged
    circular_array_queue = CircularArrayQueue(2)
    circular_array_queue.enqueue(9)
    circular_array_queue.enqueue(8)
    record_test(
        "o6.1.4 full",
        circular_array_queue.enqueue(7) is False and circular_array_queue.size() == 2,
    )

    # o6.1.5 Return-type verification + size type
    circular_array_queue = CircularArrayQueue(1)
    record_test(
        "o6.1.5 types",
        isinstance(circular_array_queue.enqueue("Z"), bool)
        and isinstance(circular_array_queue.dequeue(), (str, type(None)))
        and isinstance(circular_array_queue.size(), int),
    )


# 🚀 Run tests
test_o6_1()


# --------------------------------------------------------------------
# o6.2 🧩 Circular Linked Queue: enqueue, dequeue, size 🔗🔄
# --------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedQueue:
    def __init__(self):
        self.rear = None  # Node or None
        self._count = 0  # int

    def enqueue(self, data) -> bool:
        """Add node at rear, return True."""
        new_node = Node(data)  # create node 🆕
        if self.rear is None:  # empty circle
            new_node.next = new_node  # point to itself 🔁
            self.rear = new_node
        else:
            new_node.next = self.rear.next  # link into circle
            self.rear.next = new_node
            self.rear = new_node  # update rear pointer 🥇
        self._count += 1  # increment count
        return True  # success ✅

    def dequeue(self):
        """Remove and return front data or None if empty."""
        if self.rear is None:
            return None  # empty 📭
        front_node = self.rear.next  # node at front
        data = front_node.data  # capture data
        if front_node is self.rear:
            self.rear = None  # single node -> empty
        else:
            self.rear.next = front_node.next  # remove front
        self._count -= 1  # decrement count
        return data

    def size(self) -> int:
        """Return number of elements."""
        return self._count  # return count 📏


def test_o6_2():
    # o6.2.1 Empty dequeue + count
    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.1 empty",
        circular_linked_queue.dequeue() is None and circular_linked_queue.size() == 0,
    )

    # o6.2.2 Single enqueue/dequeue + count
    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.2 single",
        circular_linked_queue.enqueue("A") is True
        and circular_linked_queue.dequeue() == "A"
        and circular_linked_queue.size() == 0,
    )

    # o6.2.3 Multiple FIFO + count
    circular_linked_queue = CircularLinkedQueue()
    circular_linked_queue.enqueue(1)
    circular_linked_queue.enqueue(2)
    circular_linked_queue.enqueue(3)
    record_test(
        "o6.2.3 multiple",
        circular_linked_queue.dequeue() == 1
        and circular_linked_queue.dequeue() == 2
        and circular_linked_queue.dequeue() == 3
        and circular_linked_queue.size() == 0,
    )

    # o6.2.4 Validation: empty after drain + count
    circular_linked_queue = CircularLinkedQueue()
    circular_linked_queue.enqueue("X")
    circular_linked_queue.dequeue()
    record_test(
        "o6.2.4 empty-again",
        circular_linked_queue.dequeue() is None and circular_linked_queue.size() == 0,
    )

    # o6.2.5 Return-type & size-type verification
    circular_linked_queue = CircularLinkedQueue()
    record_test(
        "o6.2.5 types",
        isinstance(circular_linked_queue.enqueue("Z"), bool)
        and isinstance(circular_linked_queue.dequeue(), (int, str, type(None)))
        and isinstance(circular_linked_queue.size(), int),
    )


# 🚀 Run tests
test_o6_2()


# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"Total Failed: {sum('❌' in r for r in test_results)} ❌")
