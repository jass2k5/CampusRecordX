from utils.input_validators import (is_valid_email,
 is_valid_text_input, is_valid_roll,is_valid_phone,is_valid_cgpa)
from student import Student

class StudentManager:
    def __init__(self):
        self.students = {}
    def add_students(self):
        while True:
            name = input("please enter your name here:\n").title().strip()
            if not is_valid_text_input(name):
                print("⚠️ invalid input".title())
                continue

            else:
                print(f"entered name {name}".title())
                break

        while True:
                roll_input = input("enter you roll no.").title().strip()
                roll = is_valid_roll(roll_input)
                if roll is not None:
                    print(f"entered roll number:\n {roll}")
                    break
                else:
                    print("⚠️wrong input")
                    continue
              
        while True:
            course = input("please enter your course:\n").title().strip()
            if not is_valid_text_input(course):
                print("⚠️enter a valid course name ")
                continue
            else:
                print(f"entered course:\n{course}")
                break
        while True:
            phone = input("enter your mobile number")
            if not is_valid_phone(phone):
                print("⚠️enter a valid 10 digit number please")
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
        while True:
          cgpa = input("enter your cgpa")
          if not is_valid_cgpa:
              print("⚠️invalid input try again")
              continue
          else:
              print(f"{roll}:{cgpa}")
              break

        student = Student(name,roll,course,phone,email,cgpa)
        self.students[roll] = student
        self.display_all()

    def display_all(self):
        print("list of students loading........\n".title())
        if not self.students:
            print("no students in this class yet!".title())
            print("_____________________")
        else:
            for i,(roll,student) in enumerate(self.students.items(),start = 1):
                print(f"{roll} -- {student}")
            print("total students in the class:".title())
            print(len(self.students))
            self.search_bycourse()
    def search_bycourse(self):
        course_query = input("enter the name of your course").title().strip()
        found = [s for s in self.students.values() if s.course == course_query]  #the calling str will trigger __str__ method of object student or s 
        if found:
            studentswithcourse = list(map(lambda s: str(s),found))
            for student in studentswithcourse:
                print(student)
                
   
           
btech_sec1= StudentManager()
btech_sec1.add_students()



        