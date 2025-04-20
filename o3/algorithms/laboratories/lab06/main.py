"""Circular Queue Implementation with practical applications and exercises."""

# ===================================================
# 1. UNDERSTANDING THE FUNDAMENTAL CONCEPT
# ===================================================


class CircularQueue:
    """Queue implementation using a circular array."""

    def __init__(self, capacity=5):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of front element
        self.rear = -1   # Index of rear element
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        if self.is_full():
            raise IndexError("Queue is full! 💥")

        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference

        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def display(self):
        """Display the queue elements for debugging."""
        if self.is_empty():
            return "Queue: []"

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity

        return f"Queue: [{', '.join(result)}]"


# ===================================================
# 2. PROGRESSIVE IMPLEMENTATIONS
# ===================================================

class DynamicCircularQueue:
    """Queue implementation with a dynamically resizing circular array."""

    def __init__(self, initial_capacity=5):
        """Initialize an empty queue with dynamic capacity."""
        self.capacity = initial_capacity
        self.queue = [None] * initial_capacity
        self.front = -1
        self.rear = -1
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size_count == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size_count == self.capacity

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        # If queue is full, resize it
        if self.is_full():
            self._resize()

        # If queue is empty, set front to 0
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference

        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.queue[self.front]

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def _resize(self):
        """Double the queue capacity."""
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity

        # Copy elements to the new array
        if not self.is_empty():
            i = 0
            index = self.front

            # Copy elements from front to rear
            while i < self.size_count:
                new_queue[i] = self.queue[index]
                index = (index + 1) % self.capacity
                i += 1

            # Update queue parameters
            self.queue = new_queue
            self.capacity = new_capacity
            self.front = 0
            self.rear = self.size_count - 1


class Node:
    """Node for a circular linked list queue."""

    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None


class CircularLinkedQueue:
    """Queue implementation using a circular linked list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.rear = None  # We only need to track rear in circular linked list
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.rear is None

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)

        # If queue is empty
        if self.is_empty():
            # Point to itself to form a circle
            new_node.next = new_node
        else:
            # Insert after rear, connecting to front
            new_node.next = self.rear.next  # Connect to front
            self.rear.next = new_node       # Connect rear to new node

        # Update rear to the new node
        self.rear = new_node
        self.size_count += 1

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        # If there's only one node
        if self.rear.next == self.rear:
            item = self.rear.data
            self.rear = None
        else:
            # Remove front node (next to rear)
            front = self.rear.next
            item = front.data
            self.rear.next = front.next

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.rear.next.data  # Front is next to rear

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count


# ===================================================
# 3. PRACTICAL APPLICATIONS
# ===================================================

class PrintJob:
    """Represent a print job with name and pages."""

    def __init__(self, name, pages):
        """Initialize a print job."""
        self.name = name
        self.pages = pages

    def __str__(self):
        """Return a string representation."""
        return f"{self.name} ({self.pages} pages)"


class Printer:
    """Simulate a printer that processes jobs from a queue."""

    def __init__(self, pages_per_minute):
        """Initialize a printer with a processing rate."""
        self.page_rate = pages_per_minute
        self.current_job = None
        self.time_remaining = 0
        self.total_jobs = 0
        self.total_pages = 0

    def is_busy(self):
        """Check if the printer is currently busy."""
        return self.current_job is not None

    def start_next_job(self, job):
        """Start a new print job."""
        self.current_job = job
        # Calculate time to complete (in seconds)
        self.time_remaining = job.pages * 60 / self.page_rate
        print(f"Started printing: {job} 🖨️")

    def tick(self):
        """Simulate one second passing."""
        if self.is_busy():
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                print(f"Finished printing: {self.current_job} ✅")
                self.total_jobs += 1
                self.total_pages += self.current_job.pages
                self.current_job = None
                return True  # Job completed
        return False  # No job completed


def simulate_print_queue():
    """Simulate a printer processing jobs from a queue."""
    # Create print queue
    print_queue = CircularQueue(10)  # Using our circular queue

    # Create a printer (10 pages/minute)
    printer = Printer(10)

    # Create some print jobs
    jobs = [
        PrintJob("Research Paper", 8),
        PrintJob("Resume", 2),
        PrintJob("Presentation Slides", 15),
        PrintJob("Meeting Notes", 4),
        PrintJob("Financial Report", 12),
    ]

    print("Starting printer simulation... 🖨️")
    # Add jobs to the queue
    for job in jobs:
        print(f"Adding job to queue: {job}")
        print_queue.enqueue(job)

    # Simulate time passing (180 seconds = 3 minutes)
    for second in range(1, 181):
        # Check if printer is ready for next job
        if not printer.is_busy() and not print_queue.is_empty():
            next_job = print_queue.dequeue()
            printer.start_next_job(next_job)

        # Simulate one second of time
        printer.tick()

        # Check if all jobs are done
        if print_queue.is_empty() and not printer.is_busy():
            print(f"All jobs completed at second {second}! ✨")
            print(f"Total jobs printed: {printer.total_jobs}")
            print(f"Total pages printed: {printer.total_pages}")
            break

        # Print status every 30 seconds
        if second % 30 == 0:
            jobs_left = print_queue.size()
            print(f"Time: {second}s, Jobs in queue: {jobs_left}")

    # Ensure all jobs are printed (in case we ran out of time)
    if printer.total_jobs == len(jobs):
        return True
    else:
        # Continue processing until all jobs are done
        while printer.total_jobs < len(jobs):
            if not printer.is_busy() and not print_queue.is_empty():
                next_job = print_queue.dequeue()
                printer.start_next_job(next_job)
            printer.tick()
        return True  # All jobs completed eventually


def breadth_first_search(graph, start_node):
    """Perform breadth-first search on a graph using a circular queue."""
    # Create a queue with sufficient capacity
    queue = CircularQueue(len(graph))
    visited = set()  # Track visited nodes

    # Start with the start node
    queue.enqueue(start_node)
    visited.add(start_node)

    result = []  # Store traversal order

    print(f"Starting BFS from node {start_node} 🔍")

    # Process nodes in breadth-first order
    while not queue.is_empty():
        # Get the next node to process
        current = queue.dequeue()
        result.append(current)
        print(f"Visiting: {current} 🚶")

        # Visit all unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                print(f"  Discovered: {neighbor} 👀")
                queue.enqueue(neighbor)
                visited.add(neighbor)

    return result


def demonstrate_bfs():
    """Demonstrate breadth-first search on a simple graph."""
    # Create a simple graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Graph structure:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {', '.join(neighbors)}")

    # Perform BFS starting from node 'A'
    traversal = breadth_first_search(graph, 'A')

    print("\nBFS traversal order:")
    print(" -> ".join(traversal))

    # Verify correct BFS traversal (may vary depending on neighbor order)
    expected_first = 'A'
    return traversal[0] == expected_first and len(traversal) == len(graph)


# ===================================================
# 4. REAL-WORLD CASE STUDY
# ===================================================

class Customer:
    """Represent a bank customer."""

    def __init__(self, id, service_type):
        """Initialize a customer with ID and service type."""
        self.id = id
        self.service_type = service_type  # 'deposit', 'withdrawal', 'info'
        self.arrival_time = 0
        self.priority = 2  # Default priority (1=high, 3=low)

        # Set priority based on service type
        if service_type == 'withdrawal':
            self.priority = 1  # Higher priority
        elif service_type == 'info':
            self.priority = 3  # Lower priority

    def __str__(self):
        """Return a string representation of the customer."""
        return f"Customer #{self.id} - {self.service_type} (Priority {self.priority})"


class BankServiceSystem:
    """Manage bank customer service using circular queues."""

    def __init__(self):
        """Initialize the bank service system."""
        # Separate queues for different services
        self.deposit_queue = CircularQueue(10)
        self.withdrawal_queue = CircularQueue(10)
        self.info_queue = CircularQueue(10)

        self.current_time = 0
        self.customers_served = 0
        self.average_wait_time = 0
        self.total_wait_time = 0

    def add_customer(self, customer):
        """Add a new customer to the appropriate queue."""
        # Set arrival time
        self.current_time += 1
        customer.arrival_time = self.current_time

        # Add to the appropriate queue based on service type
        if customer.service_type == 'deposit':
            self.deposit_queue.enqueue(customer)
            print(f"Customer added to deposit queue: {customer} 💰")

        elif customer.service_type == 'withdrawal':
            self.withdrawal_queue.enqueue(customer)
            print(f"Customer added to withdrawal queue: {customer} 💸")

        else:  # info
            self.info_queue.enqueue(customer)
            print(f"Customer added to information queue: {customer} ℹ️")

    def serve_next_customer(self):
        """Serve the next customer based on priority."""
        # First try to serve withdrawal (highest priority)
        if not self.withdrawal_queue.is_empty():
            return self._serve_from_queue(self.withdrawal_queue, "withdrawal")

        # Then try deposit
        elif not self.deposit_queue.is_empty():
            return self._serve_from_queue(self.deposit_queue, "deposit")

        # Finally try info
        elif not self.info_queue.is_empty():
            return self._serve_from_queue(self.info_queue, "info")

        else:
            print("No customers waiting! 🕒")
            return None

    def _serve_from_queue(self, queue, queue_name):
        """Serve a customer from the specified queue."""
        customer = queue.dequeue()
        self.customers_served += 1
        wait_time = self.current_time - customer.arrival_time

        # Update statistics
        self.total_wait_time += wait_time
        self.average_wait_time = self.total_wait_time / self.customers_served

        print(
            f"Serving {queue_name}: {customer} (waited {wait_time} time units) ✅")
        return customer

    def get_queue_status(self):
        """Return the current status of all service queues."""
        return {
            'deposit': self.deposit_queue.size(),
            'withdrawal': self.withdrawal_queue.size(),
            'info': self.info_queue.size(),
            'total_waiting': (self.deposit_queue.size() +
                              self.withdrawal_queue.size() +
                              self.info_queue.size()),
            'total_served': self.customers_served,
            'average_wait_time': round(self.average_wait_time, 2)
        }


def simulate_bank_service():
    """Simulate a bank's customer service operations."""
    # Create a bank service system
    bank = BankServiceSystem()

    # Create some customers
    customers = [
        Customer(101, 'deposit'),
        Customer(102, 'withdrawal'),
        Customer(103, 'info'),
        Customer(104, 'deposit'),
        Customer(105, 'info'),
        Customer(106, 'withdrawal'),
        Customer(107, 'deposit')
    ]

    # Add all customers to the system
    print("Customers arriving at the bank...")
    for customer in customers:
        bank.add_customer(customer)

    # Display queue status
    status = bank.get_queue_status()
    print("\nCurrent Queue Status:")
    print(f"Withdrawal Queue: {status['withdrawal']} customers 💸")
    print(f"Deposit Queue: {status['deposit']} customers 💰")
    print(f"Information Queue: {status['info']} customers ℹ️")
    print(f"Total Waiting: {status['total_waiting']} customers")

    # Simulate serving customers
    print("\nServing customers by priority...")

    # Serve customers until all queues are empty
    while status['total_waiting'] > 0:
        bank.serve_next_customer()
        status = bank.get_queue_status()

    # Final statistics
    print("\nFinal Queue Status:")
    print(f"Total Served: {status['total_served']} customers ✅")
    print(f"Average Wait Time: {status['average_wait_time']} time units ⏱️")

    # Return if all customers were served
    return status['total_served'] == len(customers)


# ===================================================
# 5. TECHNICAL CHALLENGES
# ===================================================

def sliding_window_maximum(nums, k):
    """Find maximum elements in sliding windows of size k."""
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    deque = []  # Store indices, not values

    for i in range(len(nums)):
        # Remove elements outside current window
        while deque and deque[0] < i - k + 1:
            deque.pop(0)

        # Remove smaller elements (they won't be maximum)
        while deque and nums[deque[-1]] < nums[i]:
            deque.pop()

        # Add current element
        deque.append(i)

        # Add to result if we've processed at least k elements
        if i >= k - 1:
            result.append(nums[deque[0]])

    return result


def rotate_array(nums, k):
    """Rotate array to the right by k steps using circular queue."""
    if not nums or k <= 0:
        return nums

    n = len(nums)
    k = k % n  # Handle case where k > n

    # Use a circular queue to handle rotation
    queue = CircularQueue(n)

    # Fill the queue
    for num in nums:
        queue.enqueue(num)

    # Rotate by dequeuing from the end and enqueueing at the beginning
    # This is more efficient than doing k individual rotations
    result = []

    # First, grab the last k elements (which will move to the front)
    # We'll temporarily store them in a separate list
    to_front = []
    for _ in range(n - k):
        result.append(queue.dequeue())

    # The remaining elements go to the front
    while not queue.is_empty():
        to_front.append(queue.dequeue())

    # Combine the two parts: elements to move to front + remaining elements
    return to_front + result


class Process:
    """Represent a process in a task scheduler."""

    def __init__(self, id, burst_time):
        """Initialize a process with ID and CPU burst time."""
        self.id = id
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def __str__(self):
        """Return a string representation of the process."""
        return f"Process #{self.id} (Remaining: {self.remaining_time})"


def round_robin_scheduler(processes, time_quantum):
    """Simulate round-robin scheduling using a circular queue."""
    if not processes or time_quantum <= 0:
        return []

    # Create a circular queue for processes
    n = len(processes)
    queue = CircularQueue(n)

    # Add all processes to the queue
    for process in processes:
        queue.enqueue(process)

    current_time = 0
    completion_times = {}

    print("Starting Round Robin scheduling simulation... ⏱️")

    # Process until queue is empty
    while not queue.is_empty():
        # Get the next process
        process = queue.dequeue()

        # Determine execution time for this quantum
        execution_time = min(time_quantum, process.remaining_time)

        # Update current time and process remaining time
        current_time += execution_time
        process.remaining_time -= execution_time

        print(f"Executed {process} for {execution_time} time units ⚙️")

        # If process is not complete, add it back to queue
        if process.remaining_time > 0:
            queue.enqueue(process)
        else:
            # Process is complete
            completion_times[process.id] = current_time
            print(f"Process #{process.id} completed at time {current_time} ✅")

    return completion_times


class CircularBuffer:
    """Circular buffer for streaming data."""

    def __init__(self, capacity):
        """Initialize an empty buffer with fixed capacity."""
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.write_index = 0
        self.count = 0

    def is_empty(self):
        """Check if buffer is empty."""
        return self.count == 0

    def is_full(self):
        """Check if buffer is full."""
        return self.count == self.capacity

    def add(self, item):
        """Add an item to the buffer, overwriting oldest item if full."""
        self.buffer[self.write_index] = item

        # Move write pointer circularly
        self.write_index = (self.write_index + 1) % self.capacity

        # Update count (up to capacity)
        if self.count < self.capacity:
            self.count += 1

    def get_latest(self, n=1):
        """Get the n most recent items (n <= capacity)."""
        if self.is_empty():
            return []

        n = min(n, self.count)  # Cannot get more items than we have

        result = []
        # Start from the most recent item
        read_index = (self.write_index - 1) % self.capacity

        for _ in range(n):
            result.append(self.buffer[read_index])
            read_index = (read_index - 1) % self.capacity

        return result

    def get_all(self):
        """Get all items in the buffer in order (oldest to newest)."""
        if self.is_empty():
            return []

        result = []
        # Start from the oldest item
        read_index = self.write_index if self.is_full() else 0

        for i in range(self.count):
            result.append(self.buffer[(read_index + i) % self.capacity])

        return result


# ===================================================
# 6. TESTING FUNCTIONS
# ===================================================

def test_circular_queue():
    """Test the circular queue implementation."""
    queue = CircularQueue(5)

    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.is_full() == False, "New queue should not be full"

    # Test 2: Basic operations
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.size() == 2, "Queue should have 2 items"
    assert queue.peek() == "A", "Front item should be 'A'"

    # Test 3: Circular behavior
    queue.enqueue("C")
    queue.enqueue("D")
    queue.enqueue("E")
    assert queue.is_full() == True, "Queue should be full"

    # Test 4: Dequeuing and re-enqueueing (circular behavior)
    assert queue.dequeue() == "A", "Should dequeue 'A'"
    assert queue.dequeue() == "B", "Should dequeue 'B'"
    queue.enqueue("F")
    queue.enqueue("G")
    assert queue.is_full() == True, "Queue should be full again"

    # Test 5: Verify FIFO order after wraparound
    assert queue.dequeue() == "C", "Should dequeue 'C'"
    assert queue.dequeue() == "D", "Should dequeue 'D'"
    assert queue.dequeue() == "E", "Should dequeue 'E'"
    assert queue.dequeue() == "F", "Should dequeue 'F'"
    assert queue.dequeue() == "G", "Should dequeue 'G'"
    assert queue.is_empty() == True, "Queue should be empty after all dequeues"

    print("All circular queue tests passed! ✅")
    return True


def test_dynamic_circular_queue():
    """Test the dynamic circular queue implementation."""
    queue = DynamicCircularQueue(3)  # Start with smaller capacity

    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.capacity == 3, "Initial capacity should be 3"

    # Test 2: Filling to capacity
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.is_full() == True, "Queue should be full"

    # Test 3: Automatic resizing
    queue.enqueue("D")  # This should trigger resize
    assert queue.capacity == 6, "Capacity should double to 6"
    assert queue.is_full() == False, "Queue should not be full after resize"

    # Test 4: Verify elements after resize
    assert queue.peek() == "A", "Front element should still be 'A'"
    assert queue.size() == 4, "Queue should have 4 elements"

    # Test 5: Test circular behavior with resizing
    # Dequeue some items
    assert queue.dequeue() == "A", "Should dequeue 'A'"
    assert queue.dequeue() == "B", "Should dequeue 'B'"

    # Add more items to trigger another resize
    for item in ["E", "F", "G", "H", "I"]:
        queue.enqueue(item)

    # Queue should now contain: C,D,E,F,G,H,I
    assert queue.capacity == 12, "Capacity should be 12 after second resize"
    assert queue.size() == 7, "Queue should have 7 elements"

    # Verify all elements in FIFO order
    expected = ["C", "D", "E", "F", "G", "H", "I"]
    for expected_item in expected:
        assert queue.dequeue() == expected_item, f"Expected {expected_item}"

    assert queue.is_empty() == True, "Queue should be empty after all dequeues"

    print("All dynamic circular queue tests passed! ✅")
    return True


def test_circular_linked_queue():
    """Test the circular linked list queue implementation."""
    queue = CircularLinkedQueue()

    # Test 1: Initial state
    assert queue.is_empty() == True, "New queue should be empty"
    assert queue.size() == 0, "Queue size should be 0"

    # Test 2: Basic operations
    queue.enqueue(100)
    queue.enqueue(200)
    assert queue.size() == 2, "Queue should have 2 items"
    assert queue.peek() == 100, "Front item should be 100"

    # Test 3: FIFO behavior
    assert queue.dequeue() == 100, "Should dequeue 100"
    assert queue.dequeue() == 200, "Should dequeue 200"
    assert queue.is_empty() == True, "Queue should be empty"

    # Test 4: Error handling
    try:
        queue.dequeue()
        assert False, "Should raise error on empty queue"
    except IndexError:
        pass  # Expected behavior

    # Test 5: More complex operations
    for i in range(1, 6):
        queue.enqueue(i)

    assert queue.size() == 5, "Queue should have 5 items"

    # Check circular structure works correctly
    for i in range(1, 6):
        assert queue.dequeue() == i, f"Expected {i}"

    print("All circular linked queue tests passed! ✅")
    return True


def test_sliding_window_maximum():
    """Test sliding window maximum algorithm."""
    # Test cases
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
        ([9, 8, 7, 6, 5], 3, [9, 8, 7]),
        ([1, 1, 1, 1, 1], 3, [1, 1, 1]),
        ([], 3, [])
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = sliding_window_maximum(nums, k)
        assert result == expected, f"Test case {i}: Expected {expected}, got {result}"

    print("All sliding window maximum tests passed! ✅")
    return True


def test_rotate_array():
    """Test array rotation using circular queue."""
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1], 1, [1]),
        ([1, 2], 3, [2, 1])  # k > length
    ]

    for i, (nums, k, expected) in enumerate(test_cases):
        result = rotate_array(nums, k)
        assert result == expected, f"Test case {i}: Expected {expected}, got {result}"

    print("All array rotation tests passed! ✅")
    return True


def test_round_robin_scheduler():
    """Test round-robin scheduler using circular queue."""
    # Test processes with different burst times
    processes = [
        Process(1, 10),  # Process #1 with burst time 10
        Process(2, 5),   # Process #2 with burst time 5
        Process(3, 8)    # Process #3 with burst time 8
    ]

    # Run round-robin scheduler with time quantum 2
    time_quantum = 2
    completion_times = round_robin_scheduler(processes, time_quantum)

    # Verify expected completion times (these should match our hand calculations)
    expected = {1: 23, 2: 15, 3: 21}

    # Check if completion times match expected
    for process_id, time in expected.items():
        assert completion_times[process_id] == time, f"Process {process_id} should complete at time {time}"

    print("Round-robin scheduler test passed! ✅")
    return True


def test_circular_buffer():
    """Test circular buffer for streaming data."""
    # Create a buffer with capacity 3
    buffer = CircularBuffer(3)

    # Test 1: Initial state
    assert buffer.is_empty() == True, "New buffer should be empty"
    assert buffer.get_all() == [], "Empty buffer should return empty list"

    # Test 2: Adding elements
    buffer.add(1)
    assert buffer.get_all() == [1], "Buffer should contain [1]"

    buffer.add(2)
    assert buffer.get_all() == [1, 2], "Buffer should contain [1, 2]"

    buffer.add(3)
    assert buffer.get_all() == [1, 2, 3], "Buffer should contain [1, 2, 3]"
    assert buffer.is_full() == True, "Buffer should be full"

    # Test 3: Overwriting elements when full
    buffer.add(4)
    assert buffer.get_all() == [2, 3, 4], "Buffer should contain [2, 3, 4]"

    buffer.add(5)
    assert buffer.get_all() == [3, 4, 5], "Buffer should contain [3, 4, 5]"

    # Test 4: Getting latest elements
    assert buffer.get_latest(1) == [5], "Latest 1: [5]"
    assert buffer.get_latest(2) == [5, 4], "Latest 2: [5, 4]"
    assert buffer.get_latest(3) == [5, 4, 3], "Latest 3: [5, 4, 3]"
    assert buffer.get_latest(
        4) == [5, 4, 3], "Latest 4 (limited to capacity): [5, 4, 3]"

    print("Circular buffer tests passed! ✅")
    return True


# ===================================================
# MAIN
# ===================================================

def run_all_tests():
    """Run all tests for circular queue implementations and applications."""
    print("\n===== TESTING CIRCULAR QUEUE IMPLEMENTATIONS =====\n")

    tests = [
        ("Basic Circular Queue", test_circular_queue),
        ("Dynamic Circular Queue", test_dynamic_circular_queue),
        ("Circular Linked Queue", test_circular_linked_queue),
        ("Print Queue Simulation", simulate_print_queue),
        ("Breadth-First Search", demonstrate_bfs),
        ("Bank Service System", simulate_bank_service),
        ("Sliding Window Maximum", test_sliding_window_maximum),
        ("Array Rotation", test_rotate_array),
        ("Round-Robin Scheduler", test_round_robin_scheduler),
        ("Circular Buffer", test_circular_buffer)
    ]

    results = {}

    for name, test_func in tests:
        print(f"\n----- Testing {name} -----")
        try:
            success = test_func()
            results[name] = success
            print(f"{'✅ PASSED' if success else '❌ FAILED'}: {name}")
        except Exception as e:
            results[name] = False
            print(f"❌ ERROR: {name} - {str(e)}")

    # Print summary
    print("\n===== TEST RESULTS SUMMARY =====\n")
    passed = sum(1 for success in results.values() if success)
    total = len(results)

    for name, success in results.items():
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{status}: {name}")

    print(f"\nPassed {passed} of {total} tests ({passed/total*100:.1f}%)")

    if passed == total:
        print("\n🎉 All tests passed successfully! 🎉")
    else:
        print("\n⚠️ Some tests failed! Please check the output for details.")


if __name__ == "__main__":
    run_all_tests()
