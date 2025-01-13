class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print("This Person name is "+self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname, year, age):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.age = age
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
        
    def print_age(self):
        print("This student is", self.age, "years old")
        
a = Student("John", "Doe", 2021 , 25)
b = Student("John", "Doe", 2021, 25)

a.welcome()
b.print_age()