# Task 8: Inventory Management System

stock = 100
total_sold = 0

while stock > 0:
    try:
        qty = int(input(f"\nStock: {stock}. Enter quantity sold (-1 to stop): "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if qty == -1:
        break
    if qty <= 0:
        print("Error: quantity must be greater than zero.")
        continue
    if qty > stock:
        print(f"Rejected: only {stock} units available.")
        continue

    stock -= qty
    total_sold += qty
    print(f"Sale recorded: {qty} units.")

if stock == 0:
    print("\nStock has run out.")
print(f"Total units sold: {total_sold}")
print(f"Remaining stock: {stock}")
