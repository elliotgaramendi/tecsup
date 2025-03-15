"""
Time Complexity Analysis

Note: Before running this script, install matplotlib with:
    pip install matplotlib
"""

import time
import matplotlib.pyplot as plt


def measure_time(func, n):
    """Measures execution time of a function"""
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time


def plot_times(n_values, times, title):
    """Plots execution times"""
    plt.plot(n_values, times, 'o-')
    plt.title(title)
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()


def run_algorithm(algorithm_func, n_values, title):
    """Runs algorithm and measures execution time for different n values"""
    times = []

    for n in n_values:
        time_taken = measure_time(algorithm_func, n)
        times.append(time_taken)
        print(f"n = {n}, time = {time_taken:.8f} seconds")

    plot_times(n_values, times, title)


# 1. Logarithmic complexity - O(log n)
def logarithmic_algorithm(n):
    """Algorithm with O(log n) complexity"""
    i = n
    while i > 0:
        i = i // 2


# 2. Simple Loop - O(n)
def simple_loop(n):
    """Algorithm with O(n) complexity"""
    for _ in range(n):
        pass


# 3. If-then-else statements - O(n)
def if_then_else(n):
    """Algorithm with conditional O(n) complexity"""
    if n % 2 == 0:
        for _ in range(n):
            pass
    else:
        for _ in range(n):
            pass


# 4. Nested Loops - O(n²)
def nested_loops(n):
    """Algorithm with O(n²) complexity"""
    for _ in range(n):
        for _ in range(n):
            pass


# 5. Consecutive statements - O(n + n²) = O(n²)
def consecutive_statements(n):
    """Algorithm with O(n + n²) complexity"""
    for _ in range(n):
        pass

    for _ in range(n):
        for _ in range(n):
            pass


# Mystery Algorithms
def mystery_algorithm_1(n):
    """Mystery algorithm 1"""
    found = False
    for i in range(n):
        for j in range(n):
            if j == i:
                found = True
                break
        if found:
            break
    return found


def mystery_algorithm_2(n):
    """Mystery algorithm 2"""
    count = 0
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                count += 1
    return count


def mystery_algorithm_3(n):
    """Mystery algorithm 3"""
    count = 0
    for _ in range(n):
        j = 1
        while j < n:
            count += 1
            j *= 2
    return count


# Main execution
if __name__ == "__main__":
    # Definition of n values for each algorithm
    log_n_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
    linear_n_values = [10**2, 10**3, 10**4, 10**5, 10**6]
    if_else_n_values = [1, 10, 100, 1000, 10000, 100000]
    quadratic_n_values = [100, 400, 600, 800, 1000, 1100]
    mystery1_n_values = [1, 10, 100, 1000, 10000]
    mystery2_n_values = [1, 10, 100, 1000]
    mystery3_n_values = [1, 5, 10, 50, 100,
                         500, 1000, 5000, 10000, 50000, 100000]

    # Uncomment the algorithm you want to run
    # run_algorithm(logarithmic_algorithm, log_n_values, "Logarithmic Complexity")
    # run_algorithm(simple_loop, linear_n_values, "Simple Loop - Linear Complexity")
    # run_algorithm(if_then_else, if_else_n_values, "If-then-else - Linear Complexity")
    # run_algorithm(nested_loops, quadratic_n_values, "Nested Loops - Quadratic Complexity")
    # run_algorithm(consecutive_statements, quadratic_n_values, "Consecutive Statements - Mixed Complexity")
    # run_algorithm(mystery_algorithm_1, mystery1_n_values, "Mystery Algorithm 1")
    # run_algorithm(mystery_algorithm_2, mystery2_n_values, "Mystery Algorithm 2")
    # run_algorithm(mystery_algorithm_3, mystery3_n_values, "Mystery Algorithm 3")

    print("Select an algorithm to run by uncommenting it in the code")
