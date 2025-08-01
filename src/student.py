class Student:
    def _init_(self,name,roll,course,email,phone,cgpa):
        self.name = name
        self.roll = roll
        self.course = course
        self.email = email
        self.phone = phone
        self.cgpa = cgpa

    def _str_(self):
        return f"{self.name} (Roll: {self.roll} CGPA : {self.cgpa} Course = {self.course} Contacts:{self.email},{self.phone})"
    def _repr_(self):
        return f"Student(name = {self.name}, roll = {self.roll},cgpa = {self.cgpa},contact = {self.email},{self.phone},course:{self.course})"
    def result(self):
        if self.cgpa >5:
            return "congratulations🥳 you are PASSED!"
        else:
            return  "Failed! 😢"