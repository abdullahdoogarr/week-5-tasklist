# Task 10: Menu-Driven Number Analysis System

even_count = 0
odd_count = 0
total = 0
count = 0
largest = None

print("Enter integers to analyze (0 to stop).")

while True:
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if num == 0:
        break
    if num < 0:
        print("Negative number ignored.")
        continue

    if num % 2 == 0:
        print(f"{num} is even.")
        even_count += 1
    else:
        print(f"{num} is odd.")
        odd_count += 1

    total += num
    count += 1
    if largest is None or num > largest:
        largest = num

print("\n--- Results ---")
if count == 0:
    print("No positive numbers were entered.")
else:
    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Largest number: {largest}")
    print(f"Sum: {total}")
    print(f"Average: {total / count:.2f}")
