#Default Arguments
def hello(greeting, title, first, last):
  print(f"{greeting}, {title} {first} {last}!")

#keyword arguments - argument preceded by identifier *positional arguments like the hello follows keyword arguments
hello("Hello", last= "MAX", title="Mr.", first= "MIN") 


print(1,2,3,4,5, sep = " - ") #prints 1 - 2 - 3 - 4 - 5


#args and kwargs - arguments
#pass any amount of arguments
def add(*args):
  result = 0
  for num in args:
    result += num
  return result

print(add(1,2,3,4,5)) #prints 15

#pass any amount of keyword arguments
def print_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")

print_address(street="123 Main St", city="New York", state="NY") #prints street : 123 Main St, city : New York, state : NY


def shipping_lbl(*args, **kwargs):
  for arg in args:
    print(arg, end=" ")
  print()

  print(f"{kwargs.get('street')}")
  print(f"{kwargs.get('city')}")
  print(f"{kwargs.get('state')}")

shipping_lbl("Order #123", "Shipped", street="123 Main St", city="New York", state="NY") #prints Order #123 Shipped 123 Main St New York NY


#LIST COMPREHENSION - concise way to create list 
doubles = []

for x in range(1,11):
  doubles.append(x * 2)

print(doubles) #prints [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#this can be written as. follow [expression for value in iterable if condition]
doubles = [x * 2 for x in range(1,11)]

print(doubles) #prints [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numbers = [1, -2, 3, 4, -5]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums) #prints only positive nums


#MATCH-CASE STATEMENT - like switch
def is_weekend(day):
  match day:
    case "Saturday" | "Sunday":
      return True
    case "Monday" | "Tuesday"| "Wednesday"| "Thursday"| "Friday":
      return False
    case _:
      return False

print(is_weekend("Sunday")) #prints True