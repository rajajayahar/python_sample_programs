#object - is an entity having state behaviour and adentity
#eg - pen identity - its name ,state ->colour,brand,model,behaviour -- write,draw
#class - is the group of simillar abject or its a user defind datatype

# 4 basics pillars of oops
#inheritance
#polymorphism
#abstraction
#encapsulation

class Student:
    def display(self):
        print("i am a student") 
student_object=Student()        #object creation
student_object.display()

#constructor is a special method in python
#mainly used for initialising an object
#it will be automatically called when an object is created

class Employee:
    def _init_(self):
        print("default constructor is called")
employee=Employee()