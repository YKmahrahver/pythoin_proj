from Day_7car import Car

#OOP
#object = bundle of related attributes and methods
# you need class to create many objects
#class = blueprint - used to design the structure and layout of an object 

# class Car:
#   def __init__(self, model, year, color, for_sale): #constructor method (self means the object were creating rn)
#     self.model = model
#     self.year = year
#     self.color = color
#     self.for_sale = for_sale

#make an object or instance of a class
car1 = Car("Mustang", 2024, "red", False)

print(car1) #prints the car1's memory address
print(car1.model) #prints the car1's model
car1.drive()

#place the class in different file for better organization



#CLASS VARIABLES
# - can be found within the class, INSTANCE VARIABLES are defined within the constructor

#INHERITANCE

class Animal():
  def __init__(self, name):
    self.name = name
  
class Dog(Animal):
  def bark(self):
    print(f"{self.name} barks")

dog1 = Dog("Buddy")
dog1.bark()


#MULTIPLE INHERITANCE - inherit from more than one class A(B, C)

#MULTILEVEL INHERITANCE - inherit from a parent which inherits from another parent A -> B(A) -> C(B)