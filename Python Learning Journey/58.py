"""
Program: Student Class and Object Example
Author: Samvia Amir
Description:
This program demonstrates the use of classes and objects in Python.
"""

class Student:
    def __init__(self, name, roll_no, marks):
        # Instance variables
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 50:
            print("Result: Pass ")
        else:
            print("Result: Fail ")


# Creating objects of the class
student1 = Student("Ali", 101, 78)
student2 = Student("Sara", 102, 45)

# Calling methods using objects
student1.display_info()
student1.check_result()

student2.display_info()
student2.check_result()
