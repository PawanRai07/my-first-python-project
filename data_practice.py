print("--- Learning Python Functions ---")

# 1. Defining our reusable function (The Juicer)
# It takes one ingredient: the gpa_score
def check_academic_status(gpa_score):
    if gpa_score >= 3.6:
        return "Excellent! Made the Dean's List."
    else:
        return "Good standing."

# 2. Our student data
students = [
    {"name": "Pawan", "gpa": 4.0},
    {"name": "Rajat", "gpa": 3.8},
    {"name": "Garvit", "gpa": 3.5}
]

# 3. Using the function inside our loop
for student in students:
    # We pass the student's GPA into our function machine
    status = check_academic_status(student["gpa"])
    print(f"Student: {student['name']} | Status: {status}")