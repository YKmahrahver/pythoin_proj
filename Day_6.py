#MODULE - file containing code to include in your program
# use import to include a module either the built-in or your own
#print(help("modules"))
#print(help("math"))
#import math
import math as m #you can rename it
from math import sqrt #or you can just import something specific

print(m.pi)

#creating a module- make new py file
import modulee
result = modulee.cube(2)
print(result)



#VARIABLE SCOPE- where a variable is visible and accesible AND 
# SCOPE RESOLUTION- LEGB or local enclosed global built-in order to locate the variable
def func1():
  a = 1          #local variable found and used only within a function
  print(a)

  def func2():   
    print(a)  #enclosed variable 

a = 3 #global variable is used outside functions
func1()


# if __name__ == '__main__': - this script can be imported or run standalone
# used for running standalone scripts or py files
#dunder = __(double underscore)
# my dumbest explanation... okay so say you have two py files (they are called scripts) when you import script1 to script2
# without creating def main() and execute using if __name__ == '__main__': main() in script1 it will run in script2 
#creating def main() and execute using if __name__ == '__main__': main() makes sure that its whole code dont run within another 
# script where it is imported