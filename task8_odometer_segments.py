# Task 8: Turn sequential odometer readings into trip segments
# (start_km, end_km, distance_traveled).
# Constraint: pair adjacent elements with odometer[:-1] and odometer[1:].

odometer = (1050, 1085, 1120, 1200, 1215)

segments = [
    (start, end, end - start)
    for start, end in zip(odometer[:-1], odometer[1:])
]

print(segments)  # [(1050, 1085, 35), (1085, 1120, 35), (1120, 1200, 80), (1200, 1215, 15)]
