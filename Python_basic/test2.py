class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def print_info(self):
        print(f"name: {self.name}, add: {self.address}")
        
class Student(School):
    def __init__(self, name, address, student_id):
        super().__init__(name, address)
        self.student_id = student_id

    def print_info(self):
        super().print_info()
        print(f"id: {self.student_id}")

# Create an instance of Student outside the class definition
a = Student("ana", "YGN", "20210001")
a.print_info()
b = School("bmt", "MDY")
b.print_info()

