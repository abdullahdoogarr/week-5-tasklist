# Task 7: Pattern Generation (nested loops)

while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
        print("Number must be positive.")
    except ValueError:
        print("Please enter a whole number.")

print("\nPattern:")
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end="")
    print()

print("\nInverted pattern:")
for row in range(n, 0, -1):
    for col in range(1, row + 1):
        print(col, end="")
    print()

print(f"\nMultiplication table (1 to {n}):")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
