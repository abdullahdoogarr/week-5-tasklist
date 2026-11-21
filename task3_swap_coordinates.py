# Task 3: Swap x and y for any point where x > y; leave the others unchanged.

points = [(2, 5), (8, 3), (4, 4), (9, 1)]

result = [(y, x) if x > y else (x, y) for x, y in points]

print(result)  # [(2, 5), (3, 8), (4, 4), (1, 9)]
