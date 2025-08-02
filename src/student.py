class Student:
    def __init__(self,name,roll,course,phone,email,cgpa):
        self.name = name
        self.roll = roll
        self.course = course
        self.email = email
        self.phone = phone
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll: {self.roll} CGPA : {self.cgpa} Course = {self.course} Contacts:{self.email},{self.phone})"
    def __repr__(self):
        return f"Student(name = {self.name}, roll = {self.roll},cgpa = {self.cgpa},contact = {self.email},{self.phone},course:{self.course})"
    def result(self,):
        if self.cgpa >5:
            return "congratulations🥳 you are PASSED!"
        else:
            return  "Failed! 😢"