id1 = input("Enter Student 1 ID: ")
id2 = input("Enter Student 2 ID: ")

last1 = int(id1[-2:])# Extract last two digits and convert to integer
last2 = int(id2[-2:])

# Generate unique value using formula
unique_value = (last1 + last2) % 10

print("Unique Value Generated:", unique_value)

# Step 2: Store student names in dictionary
students = {}

while True:
    name = input("Enter student name or type 'exit' to stop: ")

    # Stop condition
    if name.lower() == "exit":
        break

    # Skip blank names
    if name.strip() == "":
        print("Warning: Name cannot be empty. Skipping...")
        continue

    # Add name to dictionary with initial score 0
    students[name] = 0

# Display all student names
print("\nList of Students:")
for student in students:
    print(student)

# Step 3: Conduct quiz for each student
for student in students:
    print(f"\nQuiz for {student}:")

    score = 0

    # Question 1
    ans1 = int(input(f"Q1: {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1

    # Question 2
    ans2 = int(input(f"Q2: {unique_value} * 3 = "))
    if ans2 == unique_value * 3:
        score += 1

    # Question 3
    ans3 = int(input(f"Q3: {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1

    # Store score
    students[student] = score

# Step 4: Evaluate performance
for student, score in students.items():
    print(f"\nResults for {student}:")
    print("Score:", score)

    # Warning for zero score
    if score == 0:
        print("Very low performance!")

    # Performance level
    if score == 3:
        print("Performance: Excellent")
    elif score == 2:
        print("Performance: Good")
    elif score == 1:
        print("Performance: Average")
    else:
        print("Performance: Poor")

    # Certificate eligibility
    if score >= 2:
        print("You are eligible")
    else:
        print("You are not eligible")

    # Step 5: Pattern printing
    print("Score Pattern:")
    if score > 0:
        for i in range(score):
            print("*" * score)
    else:
        print("(No stars)")
