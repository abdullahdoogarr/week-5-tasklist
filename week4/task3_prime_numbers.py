# Task 3: Prime Number Analysis

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start > end:
    start, end = end, start

primes = []

for num in range(start, end + 1):
    if num < 2:
        continue  # numbers below 2 are not prime

    is_prime = True
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        primes.append(num)

if primes:
    print("Prime numbers:", " ".join(str(p) for p in primes))
else:
    print("No prime numbers found in this range.")
print(f"Total primes found: {len(primes)}")
print(f"Sum of primes: {sum(primes)}")
