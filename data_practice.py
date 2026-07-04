print("--- Testing Python Functions ---")

# 1. We build our machine (Function)
# This machine takes a GPA input and decides if the student passed
def check_academic_status(gpa_score):
    if gpa_score >= 3.6:
        return "Passing with Honors! 🌟"
    else:
        return "Passing status: Standard"

# 2. Our Data (Dictionary)
student_profile = {
    "name": "Pawan Kumar Rai",
    "course": "B.Tech AI/ML",
    "gpa": 4.0
}

# 3. Running the machine
# We grab the GPA from the dictionary and drop it into our function slot
result = check_academic_status(student_profile["gpa"])

# Print the final output
print(f"Student Name: {student_profile['name']}")
print(f"Academic Status: {result}")