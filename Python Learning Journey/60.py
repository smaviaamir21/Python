class Student:
    def __init__(self, name, marks):
        self.name = name      # Public
        self.marks = marks    # Public

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Smavia", 85)

# Accessing directly (Allowed)
print(s1.name)
print(s1.marks)

s1.display()
