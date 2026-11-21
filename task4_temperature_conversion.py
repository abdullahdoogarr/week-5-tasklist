# Task 4: Keep only valid numeric readings, convert Celsius to Fahrenheit
# (F = C * 1.8 + 32), and round to 1 decimal place.
# Constraint: single list comprehension.

raw_temps = [22.5, "ERR", 18.0, None, 30.2, "ERR", 0.0]

fahrenheit = [
    round(t * 1.8 + 32, 1)
    for t in raw_temps
    if isinstance(t, (int, float)) and not isinstance(t, bool)
]

print(fahrenheit)  # [72.5, 64.4, 86.4, 32.0]
