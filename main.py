import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "utils")))

from src.manager import StudentManager
from utils.input_helper import get_user_input
from utils.input_validators import (is_valid_cgpa,is_valid_email,is_valid_phone,is_valid_roll,is_valid_text_input)
from utils.collectandadd import collect_and_student
def main():
    manager = StudentManager()
    while True:
       choice = input("choose 1 to add students\n choose 2 to display students\n choose 3 to search by course\n choose 4 for remove student\n choose 5 for leaderboard\n choose 6 for check result\n choose 7 for edit the student info.")
       if choice == "1":
            collect_and_student(manager)
       elif choice == "2":
            manager.display_all()
       elif choice == "3":
           manager.search_bycourse()
       elif choice == "4":
           manager.remove_student_by_roll()
       elif choice == "5":
           manager.leaderboard_by_cgpa()
       elif choice == "6":
           manager.check_result_by_roll()
       elif choice == "7":
           manager.edit_data()
       else:
           print("wrong input please try again")
           continue
            



if __name__ == "__main__":
     main()