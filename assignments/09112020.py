# Create withdraw method and should withdraw if and only if balance is sufficient
# Create a class with [name, course, fee] [__init__(self, name, course, fee), print_details(), payment(amount), due()]
class Student:
    def __init__(self, name, course, fee=0):
        self.name = name
        self.course = course
        self.fee = fee

    def print_details(self):
        print(f"Name : {self.name}")
        print(f"Course : {self.course}")
        print(f"Fee : {self.fee}")

    def payment(self, amount):
        self.fee += amount

    def due(self):
        fee = int(self.fee)
        if str(self.course).lower() == 'python':
            if fee == 4000:
                print("No due")
            elif fee < 4000:
                print(f"Due is {4000 - fee}")
        elif str(self.course).lower() == 'java':
            if fee == 4000:
                print("No due")
            elif fee < 4000:
                print(f"Due is {4000 - fee}")
        else:
            print("Unknown course")


student1 = Student("John", "Python")
student1.payment(3000)
student1.print_details()
student1.due()
student1.payment(1000)
student1.due()
student1.print_details()
student2 = Student("Peter", "Java")
student2.payment(3000)
student2.print_details()
student2.due()
student2.payment(1000)
student2.due()
student2.payment(1000)
student2.due()
student2.print_details()
