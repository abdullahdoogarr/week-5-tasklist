# Task 1: Student Grading and Performance Analysis

NUM_STUDENTS = 10
PASS_MARK = 50

marks = []
passed = 0
failed = 0

for student in range(1, NUM_STUDENTS + 1):
    # Keep asking until a valid mark (0-100) is entered
    while True:
        try:
            mark = float(input(f"Enter marks for student {student}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if 0 <= mark <= 100:
            break
        print("Marks must be between 0 and 100. Try again.")

    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    if mark >= PASS_MARK:
        passed += 1
    else:
        failed += 1

    marks.append(mark)
    print(f"Student {student}: {mark:g} marks -> Grade {grade}")

print("\n--- Class Summary ---")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Highest mark: {max(marks):g}")
print(f"Class average: {sum(marks) / len(marks):.2f}")
