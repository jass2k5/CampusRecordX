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
          cgpa_input = get_user_input("enter your cgpa")
          if cgpa_input is None:
               return
          if not is_valid_cgpa(cgpa_input):
              print("⚠️invalid input try again".title())
              continue
          else:
              cgpa = float(cgpa_input)
              print(f"{roll}:{cgpa}")
              break
           

        student = Student(name,roll,course,phone,email,cgpa)
        self.students[roll] = student
        self.edit_data()
         
    def display_all(self):
        print("list of students loading........\n".title())
        if not self.students:
            print("no students in this class yet!".title())
            print("_____________________")
        else:
            for i,(roll,student) in enumerate(self.students.items(),start = 1):
                print(f"{roll} -- {student}")
          
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

        field = input("Enter the field you want to change (name, course, phone, email, cgpa, roll): ").strip().lower()
        new_value = input("Enter your new value: ").strip()

        if field == "phone":
            if is_valid_phone(new_value):
             student.phone = new_value
             print("✅ Phone updated.")
            else:
                print("❌ Invalid phone number.")
        elif field == "cgpa":
            try:
                new_cgpa = float(new_value)
                if is_valid_cgpa(new_cgpa):
                    student.cgpa = new_cgpa
                    print("✅ CGPA updated.")
                else:
                    print("❌ Invalid CGPA.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif field == "roll":
            new_roll = is_valid_roll(new_value)
            if new_roll is None:
                print("❌ Invalid roll number.")
            elif new_roll in self.students:
                print("❌ Roll number already in use.")
            else:
            # Update roll: change key and attribute
                del self.students[roll]
                student.roll = new_roll
                self.students[new_roll] = student
                print("✅ Roll number updated.")

        elif field == "name":
            if is_valid_text_input(new_value):
                student.name = new_value.title().strip()
                print("✅ Name updated.")
            else:
                print("❌ Invalid name.")

        elif field == "course":
            if is_valid_text_input(new_value):
                student.course = new_value.title().strip()
                print("✅ Course updated.")
            else:
                print("❌ Invalid course name.")

        elif field == "email":
            if is_valid_email(new_value):
                student.email = new_value
                print("✅ Email updated.")
            else:
                print("❌ Invalid email address.")

        else:
            print("❌ Invalid field.")

            
            


        
           
btech_sec1= StudentManager()
btech_sec1.add_students()



        