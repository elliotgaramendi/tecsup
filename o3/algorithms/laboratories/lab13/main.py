"""
Comprehensive Heap Implementations by @elliotgaramendi 👨‍💻
"""

test_results = []


def record_test(test_name, condition):
    """Run a test and record the result. ✅/❌"""
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")


# ====================================================================
# o1 Technical Challenges
# ====================================================================


# --------------------------------------------------------------------
# Challenge 1: Basic MinHeap Initialization
# --------------------------------------------------------------------
class MinHeap:
    """📦 MinHeap data structure using list."""

    def __init__(self):
        # Initialize empty list for heap
        self.heap = []

    def is_empty(self):
        # Return True if heap is empty
        return len(self.heap) == 0


def test_min_heap_init_and_empty():
    h = MinHeap()
    record_test("Challenge1 Test1", h.is_empty() == True)
    h.heap.append(1)
    record_test("Challenge1 Test2", h.is_empty() == False)
    h.heap.clear()
    record_test("Challenge1 Test3", h.is_empty() == True)
    h.heap.extend([2, 3, 4])
    record_test("Challenge1 Test4", h.is_empty() == False)
    h.heap.pop()
    h.heap.pop()
    h.heap.pop()
    record_test("Challenge1 Test5", h.is_empty() == True)


test_min_heap_init_and_empty()


# --------------------------------------------------------------------
# Challenge 2: Insert and Heapify Up in MinHeap
# --------------------------------------------------------------------
class MinHeap(MinHeap):
    def insert(self, value):
        # ➕ Insert and percolate up
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # ⬆️ Swap while child < parent
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break


def test_min_heap_insert():
    h = MinHeap()
    h.insert(5)
    record_test("Challenge2 Test1", h.heap == [5])
    h.insert(3)
    record_test("Challenge2 Test2", h.heap == [3, 5])
    h.insert(4)
    record_test("Challenge2 Test3", h.heap == [3, 5, 4])
    h.insert(1)
    record_test("Challenge2 Test4", h.heap == [1, 3, 4, 5])
    valid = all(
        (h.heap[i] <= h.heap[2 * i + 1] if 2 * i + 1 < len(h.heap) else True)
        and (h.heap[i] <= h.heap[2 * i + 2] if 2 * i + 2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    record_test("Challenge2 Test5", valid)


test_min_heap_insert()


# --------------------------------------------------------------------
# Challenge 3: Delete Min and Heapify Down in MinHeap
# --------------------------------------------------------------------
class MinHeap(MinHeap):
    def delete_min(self):
        # ❌🆙 Remove root
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        # ⬇️ Swap with smaller child
        size = len(self.heap)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break


def test_min_heap_delete_min():
    h = MinHeap()
    record_test("Challenge3 Test1", h.delete_min() is None)
    h.heap = [1]
    record_test("Challenge3 Test2", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]
    record_test("Challenge3 Test3", h.delete_min() == 1 and h.heap == [2, 3])
    h.heap = [1, 3, 4, 5]
    record_test("Challenge3 Test4", h.delete_min() == 1 and h.heap == [3, 5, 4])
    h.heap = [1, 2, 3, 4, 5]
    record_test("Challenge3 Test5", h.delete_min() == 1)


test_min_heap_delete_min()


# --------------------------------------------------------------------
# Challenge 4: build_heap (Heapify entire array)
# --------------------------------------------------------------------
class MinHeap(MinHeap):
    def build_heap(self, array):
        # 🏗️ Build from list
        self.heap = array.copy()
        for idx in range((len(self.heap) // 2) - 1, -1, -1):
            self._heapify_down(idx)


def test_build_heap():
    h = MinHeap()
    h.build_heap([5, 3, 8, 1, 2])
    record_test("Challenge4 Test1", h.heap[0] == 1)
    h.build_heap([7, 6, 5, 4, 3, 2, 1])
    record_test("Challenge4 Test2", h.heap[0] == 1)
    h.build_heap([2, 1])
    record_test("Challenge4 Test3", h.heap == [1, 2])
    h.build_heap([10])
    record_test("Challenge4 Test4", h.heap == [10])
    h.build_heap([])
    record_test("Challenge4 Test5", h.heap == [])


test_build_heap()


# --------------------------------------------------------------------
# Challenge 5: MaxHeap Implementation
# --------------------------------------------------------------------
class MaxHeap:
    """🦁 MaxHeap data structure using list."""

    def __init__(self):
        self.heap = []

    def insert(self, value):
        # ➕ Insert and percolate up
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index],
                )
                index = parent
            else:
                break

    def delete_max(self):
        # ❌🆙 Remove root
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )
                index = largest
            else:
                break


def test_max_heap():
    h = MaxHeap()
    h.insert(1)
    record_test("Challenge5 Test1", h.heap == [1])
    for v in [3, 2, 8, 5]:
        h.insert(v)
    record_test("Challenge5 Test2", h.heap[0] == max(h.heap))
    h.delete_max()
    record_test("Challenge5 Test3", h.heap[0] == max(h.heap))
    h = MaxHeap()
    for v in [5, 3, 1]:
        h.insert(v)
    h.delete_max()
    record_test("Challenge5 Test4", h.heap == [3, 1])
    h = MaxHeap()
    h.insert(10)
    record_test("Challenge5 Test5", h.delete_max() == 10 and h.heap == [])


test_max_heap()


# ====================================================================
# Final Summary 📋
# ====================================================================
print("\n# Final Test Summary 📋")
for r in test_results:
    print(r)
print(f"\nTotal Approved: {sum('✅' in r for r in test_results)} ✅")
print(f"\nTotal Failed: {sum('❌' in r for r in test_results)} ❌")
