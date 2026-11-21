# Task 6: For every contiguous window of length k, produce
# (window_start_index, average_price) rounded to 2 decimal places.
# Constraint: single list comprehension with range() and slicing.

prices = [100, 102, 104, 103, 105, 110]
k = 3

averages = [
    (i, round(sum(prices[i:i + k]) / k, 2))
    for i in range(len(prices) - k + 1)
]

print(averages)  # [(0, 102.0), (1, 103.0), (2, 104.0), (3, 106.0)]
