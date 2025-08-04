from utils.input_helper import get_user_input
from utils.input_validators import (is_valid_email,
 is_valid_text_input, is_valid_roll,is_valid_phone,is_valid_cgpa)
def collect_and_student(manager):
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
          manager.add_students(name,roll,course,phone,email,cgpa)
