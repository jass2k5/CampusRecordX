from utils.input_helper import get_user_input
from utils.input_validators import (is_valid_email,
 is_valid_text_input, is_valid_roll,is_valid_phone,is_valid_cgpa)

# ⛳ FUNCTION 1: Generalized input loop
def get_valid_input(prompt, validator_function, error_message, transform_function=None):
    while True:
        user_input = get_user_input(prompt)

        if user_input is None:
            return None

        if transform_function:
            user_input = transform_function(user_input)

        validation_result = validator_function(user_input)

        if validation_result:
            return validation_result if validation_result != True else user_input
        else:
            print(error_message)

# ⛳ FUNCTION 2: Collect a single student
def collect_and_student(manager):
    name = get_valid_input(
        "Enter your name: ",
        is_valid_text_input,
        "❌ Invalid name (letters only).",
        lambda x: x.strip().title()
    )
    if name is None:
        return

    roll = get_valid_input(
        "Enter roll number: ",
        is_valid_roll,
        "❌ Invalid roll number.",
    )
    if roll is None:
        return

    if roll in manager.students:
        print("❌ Roll number already exists!")
        return

    course = get_valid_input(
        "Enter course: ",
        is_valid_text_input,
        "❌ Invalid course name.",
        lambda x: x.strip().title()
    )
    if course is None:
        return

    phone = get_valid_input(
        "Enter phone number: ",
        is_valid_phone,
        "❌ Must be a 10-digit number."
    )
    if phone is None:
        return

    email = get_valid_input(
        "Enter email: ",
        is_valid_email,
        "❌ Invalid email address."
    )
    if email is None:
        return

    cgpa = get_valid_input(
        "Enter CGPA: ",
        is_valid_cgpa,
        "❌ Must be a number from 0.0 to 10.0"
    )
    if cgpa is None:
        return
    cgpa = float(cgpa)

    # Add to your student manager
    manager.add_students(name, roll, course, phone, email, cgpa)
    print("✅ Student added successfully.")
