from utils.input_validators import (is_valid_email,
 is_valid_text_input, is_valid_roll,is_valid_phone,is_valid_cgpa)
from utils.input_helper import get_user_input
from student import Student
from utils.collectandadd import get_valid_input

class StudentManager:
    def __init__(self):
        self.students = {}
    def add_students(self,name,roll,course,phone,email,cgpa):
            student = Student(name,roll,course,phone,email,cgpa)
            self.students[roll] = student
            print(f"students {self.students}")
    def display_all(self):
        print("list of students loading........\n".title())
        if not self.students:
            print("no students in this class yet!".title())
            print("_____________________")
        else:
            for i,(roll,student) in enumerate(self.students.items(),start = 1):
                print(f"{i}.{roll} -- {student}")
          
    def search_bycourse(self):
        course_query = get_user_input("enter the name of your course")
        if course_query is None:
            return
        found = [s for s in self.students.values() if s.course == course_query]  #the calling str will trigger __str__ method of object student or s 
        if found:
            studentswithcourse = list(map(lambda s: str(s),found))
            for student in studentswithcourse:
                print(student)
        else:
            print("⚠️ no such user with this course found".title())
        
  
    def remove_student_by_roll(self):
        print("e or q to exit")
        roll_2= get_user_input("enter your roll number")
        roll = is_valid_roll(roll_2)
        if roll is not None:
            if roll in self.students:
                del self.students[roll]
            else:
                print("⚠️student not found".title())
        else:
                print("⚠️ invalid roll number".title())
        
        
    def leaderboard_by_cgpa(self):
        if not self.students:
            print("no student data right now".title())
            return
        sorted_students = sorted(self.students.values(),key = lambda s: s.cgpa,reverse = True)
        for rank,student in enumerate(sorted_students,start = 1):
            print(f"{rank}:{student}")
    def check_result_by_roll(self):
        roll_input = input("enter your roll number")
        roll = is_valid_roll(roll_input)
        if roll is None:
            print("enter a valid roll number")
            return
        student = self.students.get(roll)
        if not student:
            print("no student with this roll number")
            return
        
        print(f"{student.name}'s result: {student.result()} with CGPA {student.cgpa}")

    def edit_data(self):
        roll_input = input("Enter your roll number: ")
        roll = is_valid_roll(roll_input)

        if roll is None or roll not in self.students:
             print("❌ Invalid or unknown roll number.")
             return
        student = self.students[roll]

        

        editable_fields = {
        "name": (is_valid_text_input, "❌ Invalid name.", lambda x: x.strip().title()),
        "course": (is_valid_text_input, "❌ Invalid course name.", lambda x: x.strip().title()),
        "phone": (is_valid_phone, "❌ Invalid phone number.", str),
        "email": (is_valid_email, "❌ Invalid email address.", str),
        "cgpa": (is_valid_cgpa, "❌ Invalid CGPA.", lambda x: float(x.strip())),
        "roll": (lambda x: is_valid_roll(x) if is_valid_roll(x) not in self.students else None,
                 "❌ Invalid or duplicate roll number.", lambda x: int(x.strip()))
        }
  
        field = input("Enter the field you want to change (name, course, phone, email, cgpa, roll): ").strip().lower()

        if field in editable_fields:
            validator, error_msg, transformer = editable_fields[field]

            new_value = get_valid_input(
            f"Enter your new {field}: ",
            validator,
            error_msg,
            transform=transformer
        )

        if new_value is not None:
            if field == "roll":
                # Roll number requires key change in dictionary
                del self.students[roll]
                student.roll = new_value
                self.students[new_value] = student
            else:
                setattr(student, field, new_value)

            print(f"✅ {field.capitalize()} updated.")
        else:
            print("❌ Invalid field.")
