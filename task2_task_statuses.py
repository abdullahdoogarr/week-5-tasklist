# Task 2: Replace every second task (from index 1) with "completed",
# then insert "audit" right after the third element.
# Constraint: mutate the original list using slice assignment.

tasks = ["done", "pending", "done", "pending", "done", "pending"]

# Extended slice assignment: the right side must have the same length.
tasks[1::2] = ["completed"] * len(tasks[1::2])

# Empty-slice assignment inserts without overwriting anything.
tasks[3:3] = ["audit"]

print(tasks)  # ['done', 'completed', 'done', 'audit', 'completed', 'done', 'completed']
