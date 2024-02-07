#comment
#class
class Student:
    #object1
    def __init__(self, name):
        self.name = name
    def display(self):

        print(f"Hello {self.name}")
        print(f"have a good day")

    def display_close(self):
        print("Thank you")r
#for loop
for i in range(5):
    student1 = Student(input("enter name:"))
    student1.display()
#closing line
student1.display_close()


