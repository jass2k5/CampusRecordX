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
        while True:
            try:
                cgpa = float(input("enter your cgpa:\n"))
                if cgpa < 0.0 or cgpa > 10.0 or round(cgpa,2) != cgpa:
                    print("invalid cgpa")
                    continue
                else:
                    print(f"{roll} is having cgpa {cgpa}")
                    break
            except ValueError:
                print("something went wrong try again")
                continue
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



        