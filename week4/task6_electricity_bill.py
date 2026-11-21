# Task 6: Electricity Bill Calculator
# Progressive rates:
#   First 100 units  -> Rs. 10
#   Next 100 units   -> Rs. 15
#   Next 100 units   -> Rs. 20
#   Above 300 units  -> Rs. 25

total_revenue = 0
customer = 0

while True:
    try:
        units = float(input("\nEnter units consumed (-1 to stop): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if units == -1:
        break
    if units < 0:
        print("Units cannot be negative. Try again.")
        continue

    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = 100 * 10 + (units - 100) * 15
    elif units <= 300:
        bill = 100 * 10 + 100 * 15 + (units - 200) * 20
    else:
        bill = 100 * 10 + 100 * 15 + 100 * 20 + (units - 300) * 25

    customer += 1
    total_revenue += bill
    print(f"Customer {customer}: {units:g} units -> Bill: Rs. {bill:,.2f}")

print(f"\nCustomers processed: {customer}")
print(f"Total revenue collected: Rs. {total_revenue:,.2f}")
