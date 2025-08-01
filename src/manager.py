from utils.email_util import is_valid_email
from student import Student
class StudentManager:
    def __init__(self):
        self.students = {}
    def add_students(self):
        while True:
            name = input("please enter your name here:\n").title().strip()
            if not name.replace(" ","").isalpha():
                print("enter valid name")
                continue
            else:
                print(f"entered name:\n{name}")
                break

        while True:
            try:
                roll = int(input("enter your roll number:\n"))
                print(f"entered roll number:\n {roll}")
                break
            except ValueError:
                print("something went wrong try again")
                continue
        while True:
            course = input("please enter your course:\n").title().strip()
            if not course.replace(" ","").isalpha():
                print("enter a valid course name ")
                continue
            else:
                print(f"entered course:\n{course}")
                break
        while True:
            phone = input("enter your mobile number")
            if len(phone) != 10 or not phone.isdigit():
                print("enter a valid 10 digit number please")
                continue
            else:
                print(f"entered phone number is:\n{phone}")
                break
        while True:
            email = input("enter your email")
            if is_valid_email(email):
                print("valid email ✅")
                break
            else:
                print("invalid email❌")
                continue


          



manager = StudentManager()
manager.add_students()