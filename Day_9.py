#ACCESS MODIFIERS
# Public	variable or method()	- Accessible from anywhere (default in Python).
# Private	_variable or __variable	- Intended for internal use only (not strictly enforced).
# Protected	_variable	- Intended for use within the class and subclasses.
# Static	@staticmethod	- Belongs to the class itself, not an instance. a general utility method, the class itself and not an object from that class
# Instance	Defined inside __init__() with self.	- Unique to each object.

#Instance method vs static method

class Employee:

  def __init__(self, name, position):
    
    self.name = name
    self.position = position

  def get_info(self):
    return f"Name: {self.name}, Position: {self.position}"
  
  @staticmethod #decorator
  def is_valid_position(position):
    valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
    return position in valid_positions
  

print(Employee.is_valid_position("Manager")) #print true


#CLASS METHOD
#self - refers to any object created from that class
#cls - refers to class not object

class Student:
  count = 0
  def __init__(self, name):
    self._name = name
    Student.count += 1 #everytime you create instance it adds one

  #INSTANCE METHOD
  def get_info(self):
    return f"Name: {self._name}"
  
  @classmethod 
  def get_student_count(cls): #cls means class
    return f"Total Number of Students: {cls.count}"
  
student1 = Student("YEN")
student2 = Student("MIN")
student3 = Student("YOON")

print(Student.get_student_count())


#MAGIC METHODS / DUNDER METHODS i.e. __init__ etc. - They’re called "magic" because Python automatically calls them in specific situations — you don’t call them directly.

class BOOK:
  def __init__(self, title, author): #Called when an object is created (initializer)
    self.title = title
    self.author = author

  def __str__(self): #Controls what print() shows for an object
    return f"{self.title} by {self.author}"
  
  def __eq__(self, value):
    return self.title == value.title and self.author == value.author
  
  def __contains__(self, keyword):
    return keyword in self.title or keyword in self.author
  
book1 = BOOK("The Hobbit", "JK. not rowling")
book2 = BOOK("Twilight", "A teenager")
book3 = BOOK("The Hobbit", "JK. not rowling")

print(book1) #The Hobbit by J.K. Rowling
print(book1 == book3) #true
print("JK" in book1)#true

#for more go to website 
#https://docs.python.org/3/reference/datamodel.html#special-method-names


#PYTHON FILE DETECTION

import os

def check_file_exists(file_path):
  if os.path.isfile(file_path):
    return True
  
print(check_file_exists("Day_8.py")) #true


#PYTHON writing files
txt_data = "I like Min yoongi <3"
file_path = "output.txt" #you can put it in different locations

with open(file_path, "w") as file: #w means write
  file.write(txt_data)
  print(f"txt file '{file_path}' was created")


#PYTHON deleting files

file_path = "output.txt"

if os.path.exists(file_path):
  os.remove(file_path)
  print(f"txt file '{file_path}' was deleted")

#PYTHON reading files

file_path = "output.txt"

with open(file_path, "r") as file: #r means read
  content = file.read()
  print(content)

