class Teacher:
    def teach(self):
        print("Teaching students")

class MathTeacher(Teacher):
    def subject(self):
        print("Teaches Mathematics")

class ScienceTeacher(Teacher):
    def subject(self):
        print("Teaches Science")


m = MathTeacher()
s = ScienceTeacher()

m.teach()
s.teach()
