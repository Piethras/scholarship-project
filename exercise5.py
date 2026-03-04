# Student Report Card

# Function to calculate grade
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

# List of students and their scores
students = [
    ["Alice", 75],
    ["Bob", 62],
    ["Clara", 48],
    ["David", 85],
    ["Eva", 33]
]

# Loop through our list
for student in students:
    name = student[0]
    score = student[1]
    grade = get_grade(score)

    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)
    print("---------------")