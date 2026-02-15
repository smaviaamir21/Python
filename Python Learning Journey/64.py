class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    def hobby(self):
        print("Playing football")


c = Child()
c.skills()
c.talent()
c.hobby()
