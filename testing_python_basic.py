
# a = 30 
# b = 20
# c = b
# if c > 30:
#     print("c is greater than 30")
# elif c == 30:
#     print("c is equal to 30")  
# else:
#     print("c is not defined")


# a = 330
# b = 350
# print("A") if a > b else print("=") if a == b else print("B")

# i = 0
# while i <= 10:
#   print(i)
#   if i== 7:
#     break
#   i += 1
  
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     print("skipping 3")
#     continue
#   print(i)

# def test(name):
#     print(name +"Hello")
    
# test("John")
# test ("Doe")
    
# def calculate(a,b):
#     print (a+b)   
# calculate(10,20)

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# class Family:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name+ " and I am " + self.agee)
        
#     def mykids(self):
#         print("Hello my kids" + self.name+ " and they" + self.age)

# p1 = Family("John", "36")
# p2 = Family("Doe", "30")
# p1.myfunc()
# p1.mykids()


class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)