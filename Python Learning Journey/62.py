class Employee:
    def __init__(self, salary):
        self.__salary = salary   # Private variable

    def show_salary(self):
        print("Salary:", self.__salary)


emp1 = Employee(40000)

# This will give error
# print(emp1.__salary)

#Correct way (through method)
emp1.show_salary()
