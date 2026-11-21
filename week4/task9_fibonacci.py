# Task 9: Fibonacci Sequence and Sum

while True:
    try:
        n = int(input("How many terms to generate? "))
        if n >= 1:
            break
        print("Term count must be at least 1.")
    except ValueError:
        print("Please enter a whole number.")

a, b = 0, 1
terms = []
even_count = 0
odd_count = 0

for _ in range(n):
    terms.append(a)
    if a % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    a, b = b, a + b

print(" ".join(str(t) for t in terms))
print(f"Sum: {sum(terms)}")
print(f"Even terms: {even_count}")
print(f"Odd terms: {odd_count}")
