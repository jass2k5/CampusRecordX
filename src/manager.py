from utils.input_validators import (is_valid_email,
 is_valid_text_input, is_valid_roll,is_valid_phone,is_valid_cgpa)
from utils.input_helper import get_user_input
from student import Student

class StudentManager:
    def __init__(self):
        self.students = {}
    def add_students(self):
        print("enter q to exit other wise your name")
        while True:
            name = get_user_input("please enter your name here:\n")
            if name is None:
                return
            name = name.title().strip()
            if not is_valid_text_input(name):
                print("⚠️ invalid input".title())
                continue

            else:
                print(f"entered name {name}".title())
                break

        while True:
                roll_input = get_user_input("enter you roll no.")
                if roll_input is None:
                    return
                roll_input = roll_input.strip()
                roll = is_valid_roll(roll_input)
                if roll is not None:
                    print(f"entered roll number:\n {roll}".title())
                    break
                else:
                    print("⚠️wrong input")
                    continue
              
        while True:
            course = get_user_input("please enter your course:\n")
            if course is None:
                return
            course = course.title().strip()
            if not is_valid_text_input(course):
                print("⚠️enter a valid course name ".title())
                continue
            else:
                print(f"entered course:\n{course}")
                break
        while True:
            phone = get_user_input("enter your mobile number")
            if phone is None:
                return
            if not is_valid_phone(phone):
                print("⚠️enter a valid 10 digit number please".title())
                continue
            else:
                print(f"entered phone number is:\n{phone}".title())
                break
        while True:
            email = get_user_input("enter your email")
            if email is None:
                return
            if is_valid_email(email):
                print("valid email ✅.".title())
                break
            else:
                print("invalid email❌".title())
                continue
        while True:
          cgpa = get_user_input("enter your cgpa")
          if cgpa is None:
               return
          if not is_valid_cgpa:
              print("⚠️invalid input try again".title())
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
        self.leaderboard_by_cgpa()   
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
            ("⚠️ invalid roll number".title())
        
        
    def leaderboard_by_cgpa(self):
        if not self.students:
            print("no student data right now".title())
            return
        sorted_students = sorted(self.students.values(),key = lambda s: s.cgpa,reverse = True)
        for rank,student in enumerate(sorted_students,start = 1):
            print(f"{rank}:{student}")

           
btech_sec1= StudentManager()
btech_sec1.add_students()



        