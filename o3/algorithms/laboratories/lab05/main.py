"""Queue Data Structure Implementation in Python with practical examples and exercises."""

# ==========================================================================
# 1. UNDERSTANDING THE CONCEPT
# ==========================================================================
# A queue is a linear data structure that follows the First-In-First-Out
# (FIFO) principle, where the first element added is the first to be removed.

# ==========================================================================
# 2. QUEUE IMPLEMENTATIONS
# ==========================================================================

# 2.1 Simple List-based Implementation 📋


class SimpleQueue:
    """Basic queue implementation using a Python list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []  # Store queue elements 📦

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.items.append(item)  # Add to the end of the list 🔚

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.items.pop(0)  # Remove from the beginning 🔝

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the queue."""
        return f"Queue: {self.items}"


def test_simple_queue():
    """Test simple queue implementation."""
    # Create a new queue
    queue = SimpleQueue()
    print("Created an empty queue 🆕")

    # Test isEmpty
    print(f"Is queue empty? {queue.is_empty()} ✅")

    # Test enqueue
    print("Adding elements to queue...")
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    print(f"Queue after adding elements: {queue}")

    # Test peek
    print(f"Front element: {queue.peek()} 👀")

    # Test size
    print(f"Queue size: {queue.size()} 📏")

    # Test dequeue
    print(f"Removed element: {queue.dequeue()} ➡️")
    print(f"Queue after removing element: {queue}")

    # Dequeue all elements
    print("Removing all elements...")
    while not queue.is_empty():
        print(f"Removed: {queue.dequeue()} ➡️")

    # Test error handling
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error handling test: {e} ✅")


# 2.2 Circular Array Implementation 🔄
class CircularQueue:
    """Queue implementation using a circular array."""

    def __init__(self, capacity=10):
        """Initialize an empty queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Index of the front element ⬅️
        self.rear = -1   # Index of the rear element ➡️
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
            raise OverflowError("Queue is full! 💥")

        # If queue is empty, set front to 0 🏁
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Move rear circularly 🔄
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size_count += 1
        return True

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear the reference 🧹

        # If this is the last item
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front circularly 🔄
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

    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue: []"

        result = []
        index = self.front
        for _ in range(self.size_count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.capacity

        return f"Queue: [{', '.join(result)}]"


def test_circular_queue():
    """Test circular queue implementation."""
    # Create a circular queue with capacity 5
    queue = CircularQueue(5)
    print("Created an empty circular queue with capacity 5 🔄")

    # Test isEmpty
    print(f"Is queue empty? {queue.is_empty()} ✅")

    # Test enqueue
    print("Adding elements to queue...")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"Queue after adding elements: {queue}")

    # Test dequeue
    print(f"Removed element: {queue.dequeue()} ➡️")
    print(f"Queue after removing element: {queue}")

    # Test peek
    print(f"Front element: {queue.peek()} 👀")

    # Test circular behavior
    print("Testing circular behavior by filling the queue...")
    queue.enqueue("D")
    queue.enqueue("E")
    print(f"Queue after filling: {queue}")

    # Remove and add elements to demonstrate circularity
    print("Removing two elements...")
    queue.dequeue()
    queue.dequeue()
    print(f"Queue after removal: {queue}")

    print("Adding new elements...")
    queue.enqueue("F")
    queue.enqueue("G")
    print(f"Final queue state: {queue}")

    # Test full queue
    try:
        queue.enqueue("Overflow")
    except OverflowError as e:
        print(f"Full queue test: {e} ✅")


# 2.3 Linked List Implementation 🔗
class Node:
    """Node for a linked queue."""

    def __init__(self, data):
        """Initialize a node with data and no next reference."""
        self.data = data
        self.next = None


class LinkedQueue:
    """Queue implementation using a linked list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.front = None  # For dequeue operations ⬅️
        self.rear = None   # For enqueue operations ➡️
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)

        # If queue is empty, both front and rear point to the new node 🏁
        if self.is_empty():
            self.front = new_node
        else:
            # Link the new node at the end 🔗
            self.rear.next = new_node

        # Update rear to the new node ➡️
        self.rear = new_node
        self.size_count += 1
        return True

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        # Store the front node's data 📦
        item = self.front.data

        # Move front pointer to the next node ⬅️
        self.front = self.front.next

        # If queue becomes empty, update rear pointer too
        if self.front is None:
            self.rear = None

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.front.data

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue: []"

        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next

        return f"Queue: [{', '.join(result)}]"


def test_linked_queue():
    """Test linked queue implementation."""
    # Create a linked queue
    queue = LinkedQueue()
    print("Created an empty linked queue 🔗")

    # Test isEmpty
    print(f"Is queue empty? {queue.is_empty()} ✅")

    # Test enqueue
    print("Adding elements to queue...")
    queue.enqueue("One")
    queue.enqueue("Two")
    queue.enqueue("Three")
    print(f"Queue after adding elements: {queue}")

    # Test size
    print(f"Queue size: {queue.size()} 📏")

    # Test peek
    print(f"Front element: {queue.peek()} 👀")

    # Test dequeue
    print(f"Removed element: {queue.dequeue()} ➡️")
    print(f"Queue after removing element: {queue}")

    # Add another element
    queue.enqueue("Four")
    print(f"Queue after adding another element: {queue}")

    # Empty the queue
    print("Emptying the queue...")
    while not queue.is_empty():
        print(f"Removed: {queue.dequeue()} ➡️")

    print(f"Final queue state: {queue}")

    # Test error handling
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error handling test: {e} ✅")


# ==========================================================================
# 3. PRACTICAL APPLICATIONS
# ==========================================================================

# 3.1 Print Queue Simulation 🖨️
class PrintJob:
    """Represent a print job with a name and number of pages."""

    def __init__(self, name, pages):
        """Initialize a print job."""
        self.name = name
        self.pages = pages
        self.time_submitted = 0

    def __str__(self):
        """Return a string representation of the print job."""
        return f"{self.name} ({self.pages} pages)"


class Printer:
    """Simulate a printer that processes jobs from a queue."""

    def __init__(self, pages_per_minute):
        """Initialize a printer with a specific processing rate."""
        self.page_rate = pages_per_minute
        self.current_job = None
        self.time_remaining = 0
        self.jobs_completed = 0

    def is_busy(self):
        """Check if the printer is currently busy."""
        return self.current_job is not None

    def start_next_job(self, job):
        """Start a new print job."""
        self.current_job = job
        # Calculate time to complete the job (in seconds) ⏱️
        self.time_remaining = job.pages * 60 / self.page_rate
        print(f"Started printing: {job} 🖨️")

    def tick(self):
        """Simulate one second passing."""
        if self.is_busy():
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                print(f"Finished printing: {self.current_job} ✅")
                self.jobs_completed += 1
                self.current_job = None
                return True  # Job completed
        return False  # No job completed


def simulate_print_queue():
    """Simulate a printer processing jobs from a queue."""
    # Create print queue (using our LinkedQueue implementation)
    print_queue = LinkedQueue()

    # Create a printer that can process 10 pages per minute ⚡
    printer = Printer(10)

    # Create some print jobs 📄
    jobs = [
        PrintJob("Report", 5),
        PrintJob("Homework", 3),
        PrintJob("Article", 8),
        PrintJob("Presentation", 12),
        PrintJob("Resume", 2)
    ]

    print("Starting printer simulation... 🖨️")
    # Add jobs to the queue
    for job in jobs:
        print(f"Adding job to queue: {job}")
        print_queue.enqueue(job)

    # Simulate time passing (120 seconds = 2 minutes) ⏱️
    for second in range(1, 121):
        # Check if printer is ready for next job
        if not printer.is_busy() and not print_queue.is_empty():
            next_job = print_queue.dequeue()
            printer.start_next_job(next_job)

        # Simulate one second of time ⏱️
        printer.tick()

        # Check if all jobs are done
        if print_queue.is_empty() and not printer.is_busy():
            print(f"All jobs completed at second {second}! ✨")
            break

        # Print status every 10 seconds
        if second % 10 == 0:
            jobs_left = print_queue.size()
            print(
                f"Time: {second}s, Jobs in queue: {jobs_left}, Printer busy: {printer.is_busy()}")

    print(
        f"Simulation ended. Completed {printer.jobs_completed} out of {len(jobs)} jobs.")


# 3.2 Breadth-First Search 🔍
def breadth_first_search(graph, start_node):
    """Perform breadth-first search traversal on a graph."""
    # Use our Queue implementation
    queue = LinkedQueue()
    visited = set()  # To track visited nodes 🔍

    # Start by visiting the start node 🏁
    queue.enqueue(start_node)
    visited.add(start_node)

    result = []  # To store the traversal order

    print(f"Starting BFS from node {start_node} 🔍")

    # Process nodes in breadth-first order
    while not queue.is_empty():
        # Get the next node to process
        current = queue.dequeue()
        result.append(current)
        print(f"Visiting node: {current} 🚶")

        # Visit all unvisited neighbors 👥
        for neighbor in graph[current]:
            if neighbor not in visited:
                print(f"  Discovered neighbor: {neighbor} 👀")
                queue.enqueue(neighbor)
                visited.add(neighbor)

    return result


def demonstrate_bfs():
    """Demonstrate breadth-first search on a simple graph."""
    # Create a simple graph as an adjacency list 🕸️
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


# ==========================================================================
# 4. REAL-WORLD CASE: CUSTOMER SERVICE SYSTEM
# ==========================================================================
class SupportRequest:
    """Represent a customer support request."""

    def __init__(self, customer_id, issue_type, description, priority=2):
        """Initialize a support request."""
        self.customer_id = customer_id
        self.issue_type = issue_type  # 'technical', 'billing', 'general'
        self.description = description
        self.priority = priority  # 1 (high) to 3 (low)
        self.creation_time = 0  # Will be set when added to the system ⏱️

    def __str__(self):
        """Return a string representation of the support request."""
        return f"Customer #{self.customer_id} - {self.issue_type.capitalize()}: {self.description[:20]}..."


class CustomerServiceSystem:
    """Manage customer service requests using queues."""

    def __init__(self):
        """Initialize the customer service system."""
        # Separate queues for different types of issues 🗂️
        self.technical_queue = LinkedQueue()
        self.billing_queue = LinkedQueue()
        self.general_queue = LinkedQueue()

        self.current_time = 0
        self.requests_handled = 0

    def add_request(self, request):
        """Add a new support request to the appropriate queue."""
        # Set creation time ⏱️
        self.current_time += 1
        request.creation_time = self.current_time

        # Add to the appropriate queue based on issue type
        if request.issue_type == 'technical':
            self.technical_queue.enqueue(request)
            print(f"Technical request added: {request} 🔧")

        elif request.issue_type == 'billing':
            self.billing_queue.enqueue(request)
            print(f"Billing request added: {request} 💰")

        else:  # general
            self.general_queue.enqueue(request)
            print(f"General request added: {request} ℹ️")

    def handle_next_technical(self):
        """Handle the next technical support request."""
        if self.technical_queue.is_empty():
            print("No technical requests waiting! 🔧")
            return None

        request = self.technical_queue.dequeue()
        self.requests_handled += 1
        wait_time = self.current_time - request.creation_time

        print(
            f"Handling technical request: {request} (waited {wait_time} time units) ✅")
        return request

    def handle_next_billing(self):
        """Handle the next billing support request."""
        if self.billing_queue.is_empty():
            print("No billing requests waiting! 💰")
            return None

        request = self.billing_queue.dequeue()
        self.requests_handled += 1
        wait_time = self.current_time - request.creation_time

        print(
            f"Handling billing request: {request} (waited {wait_time} time units) ✅")
        return request

    def handle_next_general(self):
        """Handle the next general support request."""
        if self.general_queue.is_empty():
            print("No general requests waiting! ℹ️")
            return None

        request = self.general_queue.dequeue()
        self.requests_handled += 1
        wait_time = self.current_time - request.creation_time

        print(
            f"Handling general request: {request} (waited {wait_time} time units) ✅")
        return request

    def get_queue_status(self):
        """Return the current status of all support queues."""
        return {
            'technical': self.technical_queue.size(),
            'billing': self.billing_queue.size(),
            'general': self.general_queue.size(),
            'total_waiting': (self.technical_queue.size() + self.billing_queue.size() +
                              self.general_queue.size()),
            'total_handled': self.requests_handled
        }


def simulate_customer_service():
    """Simulate a customer service center operations."""
    # Create a customer service system 🏢
    service = CustomerServiceSystem()

    # Create some sample support requests 📝
    requests = [
        SupportRequest(101, 'technical', 'Cannot access my account', 1),
        SupportRequest(102, 'billing', 'Double charged on subscription', 1),
        SupportRequest(103, 'general', 'How do I change my password?', 3),
        SupportRequest(104, 'technical', 'App crashes on startup', 1),
        SupportRequest(105, 'general', 'Feature suggestion', 3),
        SupportRequest(106, 'billing', 'Refund request', 2),
        SupportRequest(107, 'technical', 'Sync issues between devices', 2)
    ]

    # Add all requests to the system
    print("Adding support requests to the system...")
    for request in requests:
        service.add_request(request)

    # Display queue status 📊
    status = service.get_queue_status()
    print("\nCurrent Queue Status:")
    print(f"Technical Queue: {status['technical']} requests 🔧")
    print(f"Billing Queue: {status['billing']} requests 💰")
    print(f"General Queue: {status['general']} requests ℹ️")
    print(f"Total Waiting: {status['total_waiting']} requests")

    # Simulate handling requests
    print("\nHandling support requests...")

    # First handle high-priority technical issues
    print("\n1. Handling technical issues:")
    for _ in range(3):  # Try to handle up to 3 technical requests
        service.handle_next_technical()

    # Then handle billing issues
    print("\n2. Handling billing issues:")
    for _ in range(2):  # Try to handle up to 2 billing requests
        service.handle_next_billing()

    # Finally handle general inquiries
    print("\n3. Handling general inquiries:")
    for _ in range(2):  # Try to handle up to 2 general requests
        service.handle_next_general()

    # Final status
    status = service.get_queue_status()
    print("\nFinal Queue Status:")
    print(f"Technical Queue: {status['technical']} requests 🔧")
    print(f"Billing Queue: {status['billing']} requests 💰")
    print(f"General Queue: {status['general']} requests ℹ️")
    print(f"Total Waiting: {status['total_waiting']} requests")
    print(f"Total Handled: {status['total_handled']} requests ✅")


# ==========================================================================
# 5. PRACTICAL EXERCISES
# ==========================================================================

# Exercise 1: Implement a Queue with Two Stacks 🔄
class QueueWithTwoStacks:
    """Queue implementation using two stacks."""

    def __init__(self):
        """Initialize two stacks for queue implementation."""
        self.stack_new = []  # For enqueue operations ⬆️
        self.stack_old = []  # For dequeue operations ⬇️

    def enqueue(self, item):
        """Add an item to the queue."""
        self.stack_new.append(item)  # Always add to the new stack ⬆️

    def _shift_stacks(self):
        """Move all elements from new stack to old stack."""
        # Only shift if old stack is empty
        if not self.stack_old:
            # Pop each item from new stack and push to old stack
            # This reverses the order, which is what we want 🔄
            while self.stack_new:
                self.stack_old.append(self.stack_new.pop())

    def dequeue(self):
        """Remove and return an item from the queue."""
        # Ensure old stack has items for dequeue
        self._shift_stacks()

        if not self.stack_old:
            raise IndexError("Queue is empty! 🚫")

        return self.stack_old.pop()  # Pop from old stack ⬇️

    def peek(self):
        """Return the front item without removing it."""
        # Ensure old stack has items for peek
        self._shift_stacks()

        if not self.stack_old:
            raise IndexError("Queue is empty! 🚫")

        return self.stack_old[-1]  # Peek at top of old stack 👀

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.stack_new and not self.stack_old

    def size(self):
        """Return the number of items in the queue."""
        return len(self.stack_new) + len(self.stack_old)


def test_queue_with_two_stacks():
    """Test queue implementation with two stacks."""
    queue = QueueWithTwoStacks()
    print("Created a queue using two stacks 🔄")

    # Test enqueue
    print("Adding elements to queue...")
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print(f"Queue size after adding elements: {queue.size()} 📏")

    # Test peek
    print(f"Front element: {queue.peek()} 👀")

    # Test dequeue
    print(f"Removed element: {queue.dequeue()} ➡️")
    print(f"Queue size after removal: {queue.size()} 📏")

    # Add more elements
    queue.enqueue("D")
    print(f"Queue size after adding another element: {queue.size()} 📏")

    # Test peek after changes
    print(f"Front element now: {queue.peek()} 👀")

    # Empty the queue
    print("Emptying the queue...")
    while not queue.is_empty():
        print(f"Removed: {queue.dequeue()} ➡️")

    # Test error handling
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error handling test: {e} ✅")


# Exercise 2: Level Order Traversal of a Binary Tree 🌳
class TreeNode:
    """Node for a binary tree."""

    def __init__(self, value):
        """Initialize a tree node with value and empty children."""
        self.value = value
        self.left = None
        self.right = None


def level_order_traversal(root):
    """Perform level-order traversal of a binary tree."""
    if not root:
        return []

    result = []  # To store traversal result
    queue = LinkedQueue()  # Use our LinkedQueue implementation

    # Start with the root node 🌱
    queue.enqueue(root)

    while not queue.is_empty():
        # Get the next node to process
        node = queue.dequeue()

        # Add node's value to result
        result.append(node.value)

        # Enqueue left child if exists 👈
        if node.left:
            queue.enqueue(node.left)

        # Enqueue right child if exists 👉
        if node.right:
            queue.enqueue(node.right)

    return result


def test_level_order_traversal():
    """Test level-order traversal on a binary tree."""
    # Create a binary tree 🌳
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Binary Tree Structure:")
    print("       1")
    print("     /   \\")
    print("    2     3")
    print("   / \\   / \\")
    print("  4   5 6   7")

    # Perform level-order traversal
    traversal = level_order_traversal(root)

    print("\nLevel-order traversal result:")
    print(" -> ".join(map(str, traversal)))

    # Verify the result
    expected = [1, 2, 3, 4, 5, 6, 7]
    print(f"Expected: {expected}")
    print(f"Traversal correct: {traversal == expected} ✅")


# Exercise 3: Hot Potato Game Simulation 🥔
def hot_potato(names, max_passes):
    """Simulate the Hot Potato game."""
    import random

    # Use our linked queue implementation 🔄
    queue = LinkedQueue()

    # Add all players to the queue
    for name in names:
        queue.enqueue(name)

    print(
        f"Starting Hot Potato game with {len(names)} players: {', '.join(names)} 🎮")

    # Continue until only one player remains
    while queue.size() > 1:
        # Determine number of passes for this round (1 to max_passes) 🎲
        passes = random.randint(1, max_passes)
        print(f"\nPassing potato {passes} times...")

        # Pass the potato (dequeue and enqueue each player)
        for _ in range(passes):
            current_player = queue.dequeue()
            print(f"  Potato passed to {current_player} 🥔")
            queue.enqueue(current_player)

        # Remove the player holding the potato 💥
        eliminated = queue.dequeue()
        print(f"BOOM! {eliminated} is out of the game! 💥")

        # Show remaining players
        players_list = []
        temp_player = queue.dequeue()
        players_list.append(temp_player)
        queue.enqueue(temp_player)

        # Collect remaining players
        for _ in range(queue.size() - 1):
            temp_player = queue.dequeue()
            players_list.append(temp_player)
            queue.enqueue(temp_player)

        print(f"Remaining players: {', '.join(players_list)} 👥")

    # Return the winner
    winner = queue.dequeue()
    print(f"\n🏆 {winner} wins the Hot Potato game! 🏆")
    return winner


def test_hot_potato():
    """Test Hot Potato game simulation."""
    players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    max_passes = 7

    winner = hot_potato(players, max_passes)
    print(f"Game winner: {winner} 🥔👑")


# Exercise 4: Sliding Window Maximum 📊
class Deque:
    """Double-ended queue implementation for sliding window."""

    def __init__(self):
        """Initialize an empty deque."""
        self.items = []

    def is_empty(self):
        """Check if deque is empty."""
        return len(self.items) == 0

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the front item from the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items.pop(0)

    def remove_rear(self):
        """Remove and return the rear item from the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items.pop()

    def peek_front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items[0]

    def peek_rear(self):
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty! 🚫")
        return self.items[-1]

    def size(self):
        """Return the number of items in the deque."""
        return len(self.items)


def sliding_window_maximum(nums, k):
    """Find maximum elements in sliding windows of size k."""
    if not nums or k <= 0:
        return []

    # Edge cases: k = 1 or k > length of array
    if k == 1:
        return nums
    if k > len(nums):
        return [max(nums)]

    result = []  # To store maximum values 📊
    deque = Deque()  # Using our Deque implementation

    # Process the first k elements (first window) 🔎
    for i in range(k):
        # Remove smaller elements from the back
        # (they won't be maximum in current window) 🧹
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()

        # Add current index to the deque
        deque.add_rear(i)

    # Process the rest of the elements
    for i in range(k, len(nums)):
        # The front of deque contains the maximum for previous window
        result.append(nums[deque.peek_front()])

        # Remove elements outside the current window 🪟
        while not deque.is_empty() and deque.peek_front() <= i - k:
            deque.remove_front()

        # Remove smaller elements from the back
        while not deque.is_empty() and nums[i] > nums[deque.peek_rear()]:
            deque.remove_rear()

        # Add current index to the deque
        deque.add_rear(i)

    # Add the maximum for the last window
    result.append(nums[deque.peek_front()])

    return result


def test_sliding_window_maximum():
    """Test sliding window maximum algorithm."""
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [4, 5, 6, 7, 8]),
        ([8, 7, 6, 5, 4, 3, 2, 1], 3, [8, 7, 6, 5, 4, 3]),
        ([1, 1, 1, 1, 1], 2, [1, 1, 1, 1])
    ]

    print("Testing sliding window maximum algorithm 🪟")
    for nums, k, expected in test_cases:
        result = sliding_window_maximum(nums, k)
        print(f"Array: {nums}")
        print(f"Window size: {k}")
        print(f"Maximum values: {result}")
        print(f"Expected: {expected}")
        print(
            f"Correct: {result == expected} {'✅' if result == expected else '❌'}\n")


# Exercise 5: Design a Supermarket Checkout System 🛒
class Customer:
    """Represent a customer in a supermarket."""

    def __init__(self, id, items_count):
        """Initialize a customer with ID and number of items."""
        self.id = id
        self.items_count = items_count
        self.arrival_time = 0  # Will be set when customer arrives ⏱️
        self.checkout_time = 0  # Will be set when customer completes checkout ⏱️

    def __str__(self):
        """Return a string representation of the customer."""
        return f"Customer #{self.id} ({self.items_count} items)"


class CheckoutLane:
    """Represent a checkout lane in a supermarket."""

    def __init__(self, id, processing_rate):
        """Initialize a checkout lane with ID and processing rate (items per time unit)."""
        self.id = id
        self.processing_rate = processing_rate  # Items processed per time unit ⚡
        self.queue = LinkedQueue()  # Queue of customers waiting in this lane
        self.current_customer = None  # Customer being processed
        self.time_remaining = 0  # Time until current customer is finished ⏱️
        self.customers_processed = 0  # Counter for statistics

    def is_busy(self):
        """Check if the checkout lane is currently processing a customer."""
        return self.current_customer is not None

    def queue_length(self):
        """Return the number of customers waiting in this lane."""
        return self.queue.size()

    def total_items_waiting(self):
        """Return the total number of items from all customers in the queue."""
        total = 0

        # Create a temporary queue to count items
        temp_queue = LinkedQueue()

        # Move all customers to temp queue while counting
        while not self.queue.is_empty():
            customer = self.queue.dequeue()
            total += customer.items_count
            temp_queue.enqueue(customer)

        # Move them back to original queue
        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())

        return total

    def add_customer(self, customer):
        """Add a customer to this checkout lane."""
        self.queue.enqueue(customer)
        return True

    def start_next_customer(self, current_time):
        """Start processing the next customer in the queue."""
        if self.queue.is_empty():
            return False

        # Get next customer from queue
        self.current_customer = self.queue.dequeue()

        # Calculate time to process this customer's items
        self.time_remaining = self.current_customer.items_count / self.processing_rate

        print(
            f"Lane #{self.id}: Started checkout for {self.current_customer} ⏳")
        return True

    def process_time_unit(self, current_time):
        """Process one time unit for this checkout lane."""
        if not self.is_busy():
            return False

        # Reduce remaining time
        self.time_remaining -= 1

        # Check if customer checkout is complete
        if self.time_remaining <= 0:
            # Record checkout completion time
            self.current_customer.checkout_time = current_time

            wait_time = self.current_customer.checkout_time - \
                self.current_customer.arrival_time
            print(
                f"Lane #{self.id}: Completed checkout for {self.current_customer} (waited {wait_time} time units) ✅")

            self.customers_processed += 1
            self.current_customer = None
            return True  # A customer finished checkout

        return False  # Customer still being processed


class Supermarket:
    """Simulate a supermarket with multiple checkout lanes."""

    def __init__(self):
        """Initialize the supermarket with checkout lanes."""
        # Create checkout lanes with different processing rates
        self.lanes = [
            CheckoutLane(1, 5),  # 5 items per time unit
            CheckoutLane(2, 3),  # 3 items per time unit
            CheckoutLane(3, 7)   # 7 items per time unit (express lane) ⚡
        ]

        self.current_time = 0
        self.customers_processed = 0
        self.total_wait_time = 0

    def select_best_lane(self, customer):
        """Select the best checkout lane for a customer."""
        best_lane = None
        min_wait_time = float('inf')

        for lane in self.lanes:
            # Estimate wait time by considering both current customer and queue
            estimated_wait = 0

            # Consider current processing customer
            if lane.is_busy():
                estimated_wait += lane.time_remaining

            # Consider total items in queue
            estimated_wait += lane.total_items_waiting() / lane.processing_rate

            # Select lane with minimum estimated wait time
            if estimated_wait < min_wait_time:
                min_wait_time = estimated_wait
                best_lane = lane

        return best_lane

    def add_customer(self, customer):
        """Add a customer to the best checkout lane."""
        # Set customer arrival time ⏱️
        customer.arrival_time = self.current_time

        # Find the best lane
        best_lane = self.select_best_lane(customer)

        # Add customer to the lane
        best_lane.add_customer(customer)
        print(f"Customer #{customer.id} joined Lane #{best_lane.id} (estimated wait: {customer.items_count / best_lane.processing_rate:.1f} time units) 🛒")

        return best_lane.id

    def simulate_time_unit(self):
        """Simulate one time unit for the supermarket."""
        self.current_time += 1

        # Process each checkout lane
        for lane in self.lanes:
            # If lane is not busy, start next customer
            if not lane.is_busy():
                lane.start_next_customer(self.current_time)

            # Process time unit for this lane
            customer_finished = lane.process_time_unit(self.current_time)

            # Update statistics if a customer finished
            if customer_finished:
                self.customers_processed += 1

        # Print status every 5 time units
        if self.current_time % 5 == 0:
            self.print_status()

    def print_status(self):
        """Print the current status of all checkout lanes."""
        print(f"\nTime: {self.current_time} ⏱️")
        for lane in self.lanes:
            if lane.is_busy():
                print(
                    f"Lane #{lane.id}: Processing {lane.current_customer}, {lane.queue_length()} waiting")
            else:
                print(f"Lane #{lane.id}: Idle, {lane.queue_length()} waiting")

    def all_lanes_empty(self):
        """Check if all checkout lanes are empty (no customers being processed or waiting)."""
        for lane in self.lanes:
            if lane.is_busy() or not lane.queue.is_empty():
                return False
        return True

    def get_statistics(self):
        """Calculate and return supermarket statistics."""
        total_processed = sum(lane.customers_processed for lane in self.lanes)

        # Calculate total wait time and average
        total_wait_time = 0
        processed_count = 0

        # We don't have the actual customers, this would need to be tracked differently
        # in a real implementation, but here we'll just return the processed count

        return {
            'total_time': self.current_time,
            'customers_processed': total_processed,
            'lanes_statistics': [
                {'lane_id': lane.id, 'customers_processed': lane.customers_processed}
                for lane in self.lanes
            ]
        }


def simulate_supermarket():
    """Run a supermarket checkout simulation."""
    # Create supermarket
    supermarket = Supermarket()

    # Create customers with random number of items
    import random
    customers = [
        Customer(1, 15),
        Customer(2, 5),
        Customer(3, 22),
        Customer(4, 3),
        Customer(5, 10),
        Customer(6, 7),
        Customer(7, 30),
        Customer(8, 2),
        Customer(9, 12),
        Customer(10, 8)
    ]

    print("Starting supermarket checkout simulation... 🛒")

    # Add all customers at the beginning (could be randomized in a more complex simulation)
    for customer in customers:
        supermarket.add_customer(customer)

    # Run simulation until all customers are processed
    time_limit = 50  # Set a time limit to avoid infinite loops

    for t in range(1, time_limit + 1):
        # Simulate one time unit
        supermarket.simulate_time_unit()

        # Check if all lanes are empty
        if supermarket.all_lanes_empty():
            print(f"\nAll customers processed at time {t}! 🎉")
            break

    # Print statistics
    stats = supermarket.get_statistics()
    print("\nSupermarket Simulation Results:")
    print(f"Total simulation time: {stats['total_time']} time units ⏱️")
    print(f"Total customers processed: {stats['customers_processed']} 👥")

    for lane_stat in stats['lanes_statistics']:
        print(
            f"Lane #{lane_stat['lane_id']}: Processed {lane_stat['customers_processed']} customers")


# ==========================================================================
# 6. IMPLEMENTATION COMPARISON
# ==========================================================================
def compare_queue_implementations():
    """Compare different queue implementations."""
    import time

    print("Comparing queue implementations for performance...")

    # Test parameters
    n = 10000  # Number of operations

    # Test SimpleQueue
    print("\nTesting SimpleQueue:")
    simple = SimpleQueue()

    # Measure enqueue time
    start_time = time.time()
    for i in range(n):
        simple.enqueue(i)
    enqueue_time = time.time() - start_time
    print(f"  Enqueue {n} items: {enqueue_time:.6f} seconds ⬆️")

    # Measure dequeue time
    start_time = time.time()
    for _ in range(n):
        simple.dequeue()
    dequeue_time = time.time() - start_time
    print(f"  Dequeue {n} items: {dequeue_time:.6f} seconds ⬇️")

    # Test CircularQueue
    print("\nTesting CircularQueue:")
    circular = CircularQueue(n)

    # Measure enqueue time
    start_time = time.time()
    for i in range(n):
        circular.enqueue(i)
    enqueue_time = time.time() - start_time
    print(f"  Enqueue {n} items: {enqueue_time:.6f} seconds ⬆️")

    # Measure dequeue time
    start_time = time.time()
    for _ in range(n):
        circular.dequeue()
    dequeue_time = time.time() - start_time
    print(f"  Dequeue {n} items: {dequeue_time:.6f} seconds ⬇️")

    # Test LinkedQueue
    print("\nTesting LinkedQueue:")
    linked = LinkedQueue()

    # Measure enqueue time
    start_time = time.time()
    for i in range(n):
        linked.enqueue(i)
    enqueue_time = time.time() - start_time
    print(f"  Enqueue {n} items: {enqueue_time:.6f} seconds ⬆️")

    # Measure dequeue time
    start_time = time.time()
    for _ in range(n):
        linked.dequeue()
    dequeue_time = time.time() - start_time
    print(f"  Dequeue {n} items: {dequeue_time:.6f} seconds ⬇️")

    # Test QueueWithTwoStacks
    print("\nTesting QueueWithTwoStacks:")
    two_stacks = QueueWithTwoStacks()

    # Measure enqueue time
    start_time = time.time()
    for i in range(n):
        two_stacks.enqueue(i)
    enqueue_time = time.time() - start_time
    print(f"  Enqueue {n} items: {enqueue_time:.6f} seconds ⬆️")

    # Measure dequeue time
    start_time = time.time()
    for _ in range(n):
        two_stacks.dequeue()
    dequeue_time = time.time() - start_time
    print(f"  Dequeue {n} items: {dequeue_time:.6f} seconds ⬇️")

    print("\nPerformance comparison complete! 📊")


# ==========================================================================
# 7. NEXT STEPS
# ==========================================================================
# Examples of advanced queue types and applications not implemented here:
#
# 1. Priority Queue: Queue where elements have a priority value and are
#    served according to their priority rather than arrival order ⭐
#
# 2. Blocking Queue: Thread-safe queue with blocking operations,
#    useful for multi-threaded producer-consumer scenarios 🔒
#
# 3. Double-ended Queue (Deque): Queue that allows insertion and removal
#    from both ends, combining features of stacks and queues 🔄
#
# 4. Delayed Queue: Queue where elements become available only after
#    a specified delay has elapsed ⏰
#
# 5. Advanced Applications:
#    - Job scheduling in operating systems ⚙️
#    - Request handling in web servers 🌐
#    - Message queues in distributed systems 📨
#    - Graph algorithms like Dijkstra's pathfinding 🗺️
#    - Process scheduling and management in OS 💻


# ==========================================================================
# 8. MAIN FUNCTION
# ==========================================================================
def main():
    """Main function to run queue implementation and tests."""
    print("===== QUEUE DATA STRUCTURE IMPLEMENTATION TESTS =====\n")

    # Test basic queue implementations
    print("\n===== BASIC IMPLEMENTATIONS =====")
    test_simple_queue()
    print("\n" + "="*50)

    test_circular_queue()
    print("\n" + "="*50)

    test_linked_queue()
    print("\n" + "="*50)

    # Test practical applications
    print("\n===== PRACTICAL APPLICATIONS =====")
    simulate_print_queue()
    print("\n" + "="*50)

    demonstrate_bfs()
    print("\n" + "="*50)

    simulate_customer_service()
    print("\n" + "="*50)

    # Test exercises
    print("\n===== PRACTICAL EXERCISES =====")
    test_queue_with_two_stacks()
    print("\n" + "="*50)

    test_level_order_traversal()
    print("\n" + "="*50)

    test_hot_potato()
    print("\n" + "="*50)

    test_sliding_window_maximum()
    print("\n" + "="*50)

    simulate_supermarket()
    print("\n" + "="*50)

    # Compare implementations
    print("\n===== IMPLEMENTATION COMPARISON =====")
    compare_queue_implementations()
    print("\n" + "="*50)

    print("\n===== ALL TESTS COMPLETED SUCCESSFULLY! =====")


if __name__ == "__main__":
    main()
