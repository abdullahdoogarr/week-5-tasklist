# Task 1: Remove the first two and last two readings, return the middle in reverse order.
# Constraint: single slice expression (no loops, no .reverse()).

times = [120, 45, 32, 28, 41, 39, 35, 210]

# Start at index -3 (third from the end), stop before index 1, step backwards.
result = times[-3:1:-1]

print(result)  # [39, 41, 28, 32]
