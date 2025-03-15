# Lab 01: Algorithm Complexity Analysis

This laboratory explores different algorithm complexities and measures their execution times.

## Contents

- `main.py`: Python script implementing algorithms with different time complexities

## Requirements

- Python 3.x
- Matplotlib library (`pip install matplotlib`)

## Usage

1. Install the required dependencies:
   ```
   pip install matplotlib
   ```

2. Run the script and uncomment the algorithm you want to analyze:
   ```
   python main.py
   ```

## Implemented Algorithms

1. **Logarithmic complexity - O(log n)**
   - Algorithm divides n by 2 repeatedly until reaching 0
   - Tested with n values: 1, 10, 100, 1000, 10000, 100000, 1000000

2. **Simple Loop - O(n)**
   - Algorithm with a single loop executing n times
   - Tested with n values: 10^2, 10^3, 10^4, 10^5, 10^6

3. **If-then-else statements - O(n)**
   - Algorithm with conditional branches, both containing linear operations
   - Tested with n values: 1, 10, 100, 1000, 10000, 100000

4. **Nested Loops - O(n²)**
   - Algorithm with two nested loops, each executing n times
   - Tested with n values: 100, 400, 600, 800, 1000, 1100

5. **Consecutive statements - O(n + n²) = O(n²)**
   - Algorithm combining a simple loop and nested loops
   - Tested with n values: 100, 400, 600, 800, 1000, 1100

6. **Mystery Algorithms**
   - Three algorithms with unknown complexity to be analyzed

## Analysis Process

For each algorithm:
1. Execution time is measured for different input sizes
2. Results are plotted to visualize how execution time scales with input size
3. Theoretical complexity is compared with the observed performance

## Student Information

- **Name:** Elliot Leo Garamendi Sarmiento
- **Course:** Algorithms and Data Structures

## Prompt Engineering (Example for one algorithm)

### Prompt Entered
```
Implement an algorithm with logarithmic time complexity O(log n) that divides n by 2 repeatedly until reaching 0. Measure its execution time with n values: 1, 10, 100, 1000, 10000, 100000, 1000000.
```

### Prompt Analysis
The original prompt was specific about the algorithm's implementation but didn't include details about visualization or analysis.

### Improved Prompt
```
Implement a logarithmic algorithm O(log n) that divides n by 2 repeatedly. Measure its execution time with n values from 1 to 1,000,000, visualize the results, and analyze how the execution time scales in relation to the input size.
```

## Conclusions

1. The empirical results confirm the theoretical time complexity for each algorithm.
2. Logarithmic algorithms show excellent performance even with very large inputs.
3. Quadratic algorithms quickly become impractical as input size grows.
4. The choice of algorithm significantly impacts performance, especially for large datasets.
5. Understanding algorithm complexity is crucial for developing efficient software solutions.
