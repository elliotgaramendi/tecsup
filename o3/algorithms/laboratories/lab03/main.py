class Node:
    """Node in a linked list, stores data and reference to the next node."""

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        """Return a string representation of the linked list."""
        if self.head is None:
            return "Empty list"

        current = self.head
        result = ""

        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()

        return result + "None"

    def list_length(self):
        """Count and return the number of nodes in the list."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def insert_at_beginning(self, data):
        """Insert a new node with data at the beginning of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

        self.length += 1
        return True

    def insert_at_end(self, data):
        """Insert a new node with data at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            # Traverse to the last node
            while current.get_next() is not None:
                current = current.get_next()

            current.set_next(new_node)

        self.length += 1
        return True

    def insert_at_position(self, position, data):
        """Insert a new node at the specified position (0-based)."""
        # Check if position is valid
        if position < 0 or position > self.length:
            return False

        # Insert at the beginning
        if position == 0:
            return self.insert_at_beginning(data)

        # Insert at the end
        if position == self.length:
            return self.insert_at_end(data)

        # Insert at the middle
        new_node = Node(data)
        current = self.head
        count = 0

        # Traverse to the node just before the insertion point
        while count < position - 1:
            current = current.get_next()
            count += 1

        new_node.set_next(current.get_next())
        current.set_next(new_node)

        self.length += 1
        return True

    def delete_from_beginning(self):
        """Delete and return the data from the first node."""
        if self.head is None:
            return None

        data = self.head.get_data()
        self.head = self.head.get_next()
        self.length -= 1

        return data

    def delete_from_end(self):
        """Delete and return the data from the last node."""
        if self.head is None:
            return None

        # If there's only one node
        if self.head.get_next() is None:
            data = self.head.get_data()
            self.head = None
            self.length -= 1
            return data

        current = self.head

        # Traverse to the second-to-last node
        while current.get_next().get_next() is not None:
            current = current.get_next()

        data = current.get_next().get_data()
        current.set_next(None)
        self.length -= 1

        return data

    def delete_from_position(self, position):
        """Delete and return data from node at the specified position."""
        # Check if position is valid
        if position < 0 or position >= self.length or self.head is None:
            return None

        # Delete from the beginning
        if position == 0:
            return self.delete_from_beginning()

        # Delete from the end
        if position == self.length - 1:
            return self.delete_from_end()

        # Delete from the middle
        current = self.head
        count = 0

        # Traverse to the node just before the deletion point
        while count < position - 1:
            current = current.get_next()
            count += 1

        node_to_delete = current.get_next()
        data = node_to_delete.get_data()

        current.set_next(node_to_delete.get_next())
        self.length -= 1

        return data

    def search(self, data):
        """Find the position of data in the list, or return -1 if not found."""
        if self.head is None:
            return -1

        current = self.head
        position = 0

        while current is not None:
            if current.get_data() == data:
                return position
            current = current.get_next()
            position += 1

        return -1

    def get_nth_from_end(self, n):
        """Return the data of the nth node from the end (1-based indexing)."""
        if n <= 0 or n > self.length or self.head is None:
            return None

        # The nth node from the end is the (length-n+1)th node from the beginning
        position = self.length - n

        current = self.head
        count = 0

        while count < position:
            current = current.get_next()
            count += 1

        return current.get_data()

    def clear(self):
        """Remove all nodes from the list."""
        self.head = None
        self.length = 0
        return True

    def has_cycle(self):
        """Check if the list has a cycle using Floyd's algorithm."""
        if self.head is None or self.head.get_next() is None:
            return False

        # Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
        slow = self.head  # Tortoise (moves one step at a time)
        fast = self.head  # Hare (moves two steps at a time)

        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()           # Move one step
            fast = fast.get_next().get_next()  # Move two steps

            # If they meet, there's a cycle
            if slow == fast:
                return True

        # If we reach here, there's no cycle
        return False

    def reverse(self):
        """Reverse the order of nodes in the list."""
        if self.head is None or self.head.get_next() is None:
            return True  # Empty list or single node (already reversed)

        previous = None
        current = self.head

        while current is not None:
            # Store the next node
            next_node = current.get_next()

            # Reverse the link
            current.set_next(previous)

            # Move to the next nodes
            previous = current
            current = next_node

        # Update the head to the new first node (previously the last)
        self.head = previous

        return True

    def find_middle(self):
        """Find and return the data of the middle node."""
        if self.head is None:
            return None

        # Use the slow and fast pointer technique
        slow = self.head
        fast = self.head

        # When fast reaches the end, slow will be at the middle
        while fast is not None and fast.get_next() is not None:
            slow = slow.get_next()           # Move one step
            fast = fast.get_next().get_next()  # Move two steps

        return slow.get_data()

    def remove_duplicates(self):
        """Remove any duplicate values from the list."""
        if self.head is None or self.head.get_next() is None:
            return True  # Empty list or single node (no duplicates)

        # Set to keep track of values we've seen
        values_seen = set()

        current = self.head
        previous = None

        while current is not None:
            data = current.get_data()

            if data in values_seen:
                # Duplicate found, remove the node
                previous.set_next(current.get_next())
                self.length -= 1
            else:
                # New value, add to set
                values_seen.add(data)
                previous = current

            current = current.get_next()

        return True


def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into a new sorted list."""
    # Create a new list for the result
    result = LinkedList()

    # Handle empty lists
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1

    # Pointers to the current nodes in each list
    curr1 = list1.head
    curr2 = list2.head

    # Merge the lists
    while curr1 is not None and curr2 is not None:
        if curr1.get_data() <= curr2.get_data():
            result.insert_at_end(curr1.get_data())
            curr1 = curr1.get_next()
        else:
            result.insert_at_end(curr2.get_data())
            curr2 = curr2.get_next()

    # Add any remaining nodes from list1
    while curr1 is not None:
        result.insert_at_end(curr1.get_data())
        curr1 = curr1.get_next()

    # Add any remaining nodes from list2
    while curr2 is not None:
        result.insert_at_end(curr2.get_data())
        curr2 = curr2.get_next()

    return result


class Stack:
    """Stack implementation using a linked list (LIFO data structure)."""

    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        """Check if the stack is empty."""
        return self.linked_list.head is None

    def push(self, data):
        """Add an element to the top of the stack."""
        self.linked_list.insert_at_beginning(data)

    def pop(self):
        """Remove and return the element at the top of the stack."""
        return self.linked_list.delete_from_beginning()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()

    def size(self):
        """Return the number of elements in the stack."""
        return self.linked_list.length

    def display(self):
        """Display the elements in the stack."""
        return self.linked_list.display()


class Queue:
    """Queue implementation using a linked list (FIFO data structure)."""

    def __init__(self):
        self.linked_list = LinkedList()

    def is_empty(self):
        """Check if the queue is empty."""
        return self.linked_list.head is None

    def enqueue(self, data):
        """Add an element to the end of the queue."""
        self.linked_list.insert_at_end(data)

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        return self.linked_list.delete_from_beginning()

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            return None
        return self.linked_list.head.get_data()

    def size(self):
        """Return the number of elements in the queue."""
        return self.linked_list.length

    def display(self):
        """Display the elements in the queue."""
        return self.linked_list.display()


class PolynomialTerm:
    """A term in a polynomial with coefficient and exponent."""

    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent

    def __str__(self):
        if self.exponent == 0:
            return str(self.coefficient)
        elif self.exponent == 1:
            return f"{self.coefficient}x"
        else:
            return f"{self.coefficient}x^{self.exponent}"


class Polynomial:
    """A polynomial represented as a linked list of terms."""

    def __init__(self):
        self.terms = LinkedList()

    def add_term(self, coefficient, exponent):
        """Add a term to the polynomial."""
        # Skip terms with coefficient 0
        if coefficient == 0:
            return

        # Add term to the list
        term = PolynomialTerm(coefficient, exponent)
        current = self.terms.head
        prev = None

        # Find the right position based on exponent (descending order)
        while current is not None and current.get_data().exponent > exponent:
            prev = current
            current = current.get_next()

        # Check if we already have a term with this exponent
        if current is not None and current.get_data().exponent == exponent:
            # Add coefficients
            new_coef = current.get_data().coefficient + coefficient
            if new_coef != 0:
                current.get_data().coefficient = new_coef
            else:
                # If coefficient becomes 0, remove the term
                if prev is None:
                    self.terms.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                self.terms.length -= 1
        else:
            # Insert the new term at the right position
            new_node = Node(term)
            if prev is None:
                new_node.set_next(self.terms.head)
                self.terms.head = new_node
            else:
                new_node.set_next(current)
                prev.set_next(new_node)
            self.terms.length += 1

    def __str__(self):
        """Return string representation of the polynomial."""
        if self.terms.head is None:
            return "0"

        result = ""
        current = self.terms.head

        while current is not None:
            term = current.get_data()
            # Add + sign for positive terms (except the first one)
            if result and term.coefficient > 0:
                result += " + "
            # Add - sign for negative terms
            elif term.coefficient < 0:
                result += " - " if result else "-"

            # Add the term (without the sign if it's negative)
            coef = abs(term.coefficient)
            if term.exponent == 0:
                result += str(coef)
            elif term.exponent == 1:
                result += f"{coef}x"
            else:
                result += f"{coef}x^{term.exponent}"

            current = current.get_next()

        return result


class MatrixElement:
    """A non-zero element in a sparse matrix."""

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return f"({self.row}, {self.col}, {self.value})"


class SparseMatrix:
    """A sparse matrix represented using linked lists."""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = LinkedList()

    def set_element(self, row, col, value):
        """Set the value at position (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Position out of bounds")

        # If value is 0, remove the element if it exists
        if value == 0:
            self.remove_element(row, col)
            return

        # Check if element already exists
        current = self.elements.head
        prev = None

        while current is not None:
            elem = current.get_data()
            if elem.row == row and elem.col == col:
                # Update existing element
                elem.value = value
                return
            elif (elem.row > row) or (elem.row == row and elem.col > col):
                # Found position to insert (keep sorted by row, then column)
                break
            prev = current
            current = current.get_next()

        # Insert new element
        new_elem = MatrixElement(row, col, value)
        new_node = Node(new_elem)

        if prev is None:
            new_node.set_next(self.elements.head)
            self.elements.head = new_node
        else:
            new_node.set_next(current)
            prev.set_next(new_node)

        self.elements.length += 1

    def get_element(self, row, col):
        """Get the value at position (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Position out of bounds")

        current = self.elements.head

        while current is not None:
            elem = current.get_data()
            if elem.row == row and elem.col == col:
                return elem.value
            current = current.get_next()

        # If element not found, it's 0
        return 0

    def remove_element(self, row, col):
        """Remove the element at position (row, col)."""
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Position out of bounds")

        current = self.elements.head
        prev = None

        while current is not None:
            elem = current.get_data()
            if elem.row == row and elem.col == col:
                # Remove the element
                if prev is None:
                    self.elements.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
                self.elements.length -= 1
                return
            prev = current
            current = current.get_next()

    def display(self):
        """Display the matrix in a readable format."""
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.get_element(i, j))
            result.append(row)
        return result


def test_linked_list():
    """Test the LinkedList implementation with basic operations."""
    my_list = LinkedList()
    print("Created a new linked list")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.list_length()}")

    # Test insertions
    print("\nTesting insertions:")
    my_list.insert_at_beginning(5)
    print(f"After insert_at_beginning(5): {my_list.display()}")

    my_list.insert_at_beginning(10)
    print(f"After insert_at_beginning(10): {my_list.display()}")

    my_list.insert_at_end(20)
    print(f"After insert_at_end(20): {my_list.display()}")

    my_list.insert_at_position(1, 15)
    print(f"After insert_at_position(1, 15): {my_list.display()}")
    print(f"Current length: {my_list.list_length()}")

    # Test search
    print("\nTesting search:")
    print(f"Position of 15: {my_list.search(15)}")
    print(f"Position of 100: {my_list.search(100)}")

    # Test deletions
    print("\nTesting deletions:")
    deleted = my_list.delete_from_beginning()
    print(f"Deleted from beginning: {deleted}")
    print(f"After deletion: {my_list.display()}")

    deleted = my_list.delete_from_position(1)
    print(f"Deleted from position 1: {deleted}")
    print(f"After deletion: {my_list.display()}")

    deleted = my_list.delete_from_end()
    print(f"Deleted from end: {deleted}")
    print(f"After deletion: {my_list.display()}")

    # Clear the list
    print("\nTesting clear:")
    my_list.clear()
    print(f"After clear: {my_list.display()}")
    print(f"Length after clear: {my_list.list_length()}")


def test_advanced_operations():
    """Test the advanced operations of the LinkedList."""
    # Create a list for testing
    my_list = LinkedList()
    print("Created a new linked list for advanced operations")

    # Add elements
    for i in range(1, 8):
        my_list.insert_at_end(i)
    print(f"Initial list: {my_list.display()}")

    # Test find_middle
    middle = my_list.find_middle()
    print(f"Middle element: {middle}")

    # Test remove_duplicates
    my_list.insert_at_end(3)  # Add a duplicate
    my_list.insert_at_end(5)  # Add another duplicate
    print(f"List with duplicates: {my_list.display()}")

    my_list.remove_duplicates()
    print(f"After removing duplicates: {my_list.display()}")

    # Test reverse
    my_list.reverse()
    print(f"After reversing: {my_list.display()}")

    # Test cycle detection
    print("Testing cycle detection:")
    cycle_list = LinkedList()
    for i in range(1, 5):
        cycle_list.insert_at_end(i)
    print(f"List without cycle: {cycle_list.display()}")
    print(f"Has cycle: {cycle_list.has_cycle()}")

    # Create a cycle by connecting the last node to the second node
    last = cycle_list.head
    while last.get_next() is not None:
        last = last.get_next()
    second = cycle_list.head.get_next()
    last.set_next(second)

    print("After creating a cycle (can't display the full list)")
    print(f"Has cycle: {cycle_list.has_cycle()}")


def test_merge_sorted_lists():
    """Test the merge_sorted_lists function."""
    # Create two sorted linked lists
    list1 = LinkedList()
    for val in [1, 3, 5, 7]:
        list1.insert_at_end(val)

    list2 = LinkedList()
    for val in [2, 4, 6, 8]:
        list2.insert_at_end(val)

    print(f"List 1: {list1.display()}")
    print(f"List 2: {list2.display()}")

    # Merge the lists
    merged_list = merge_sorted_lists(list1, list2)

    print(f"Merged list: {merged_list.display()}")


def test_stack():
    """Test the Stack implementation."""
    stack = Stack()
    print("Created a new stack")
    print(f"Stack: {stack.display()}")

    print("\nPushing elements:")
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}, Stack: {stack.display()}")

    print(f"\nTop element (peek): {stack.peek()}")
    print(f"Stack size: {stack.size()}")

    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}, Stack: {stack.display()}")


def test_queue():
    """Test the Queue implementation."""
    queue = Queue()
    print("Created a new queue")
    print(f"Queue: {queue.display()}")

    print("\nEnqueuing elements:")
    for i in range(1, 6):
        queue.enqueue(i)
        print(f"Enqueued {i}, Queue: {queue.display()}")

    print(f"\nFront element (peek): {queue.peek()}")
    print(f"Queue size: {queue.size()}")

    print("\nDequeuing elements:")
    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}, Queue: {queue.display()}")


def test_polynomial():
    """Test the Polynomial implementation."""
    poly = Polynomial()
    print("Created an empty polynomial")
    print(f"Polynomial: {poly}")

    print("\nAdding terms:")
    poly.add_term(3, 2)  # 3x^2
    print(f"After adding 3x^2: {poly}")

    poly.add_term(-2, 1)  # -2x
    print(f"After adding -2x: {poly}")

    poly.add_term(5, 0)  # 5
    print(f"After adding 5: {poly}")

    poly.add_term(1, 2)  # Add to existing term 3x^2 + 1x^2 = 4x^2
    print(f"After adding 1x^2: {poly}")

    poly.add_term(-5, 0)  # Cancel out constant term
    print(f"After adding -5: {poly}")


def test_sparse_matrix():
    """Test the SparseMatrix implementation."""
    matrix = SparseMatrix(4, 4)
    print("Created a 4x4 sparse matrix")

    # Set some elements
    matrix.set_element(0, 0, 1)
    matrix.set_element(1, 1, 2)
    matrix.set_element(2, 2, 3)
    matrix.set_element(3, 3, 4)
    matrix.set_element(0, 3, 5)

    print("\nMatrix after adding elements:")
    for row in matrix.display():
        print(row)

    # Update an element
    matrix.set_element(0, 0, 10)

    # Remove an element
    matrix.set_element(1, 1, 0)  # Setting to 0 removes the element

    print("\nMatrix after updates:")
    for row in matrix.display():
        print(row)

    # Print all non-zero elements
    print("\nNon-zero elements:")
    current = matrix.elements.head
    while current is not None:
        print(current.get_data())
        current = current.get_next()


if __name__ == "__main__":
    print("\n===== BASIC LINKED LIST OPERATIONS =====\n")
    test_linked_list()

    print("\n===== ADVANCED LINKED LIST OPERATIONS =====\n")
    test_advanced_operations()

    print("\n===== MERGING SORTED LINKED LISTS =====\n")
    test_merge_sorted_lists()

    print("\n===== STACK IMPLEMENTATION =====\n")
    test_stack()

    print("\n===== QUEUE IMPLEMENTATION =====\n")
    test_queue()

    print("\n===== POLYNOMIAL REPRESENTATION =====\n")
    test_polynomial()

    print("\n===== SPARSE MATRIX REPRESENTATION =====\n")
    test_sparse_matrix()
