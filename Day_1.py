#DAY 1
import math

#typecasting
age = 2.55
age = int(age)
print(age) #will print 2

#input
name = input("what is your name? ") #input always returns a string
print(f"Hello {name}")
age = int(input("What is your age? "))#convert input to int
print(f"you age is {age}")            

#math
friends = 5
remainder = friends % 2
print(remainder)

x = 3.14
y = 4
z = 5
result = round(x)
print(result)

array = [1,2,3,4,5,6]
min = min(array)
print(min)

print(math.pi)


#conditional expression
temperature = 30
weather = "Hot" if temperature > 20 else "Cold"
print(weather)

#string methods
name = input('What is your name? ')
result = len(name)
print(result)
name = name.capitalize()  #returns 1st letter of word capitalized
print(name)
name = name.upper() #returns every letter capitalized
print(name)
phone_number = "1-2-3-4"
result = phone_number.count("-") #will count how many - is in phone number value
print(result)
result = phone_number.replace("-", "+")
print(result)
#to see all string methods use:
#print(help(str))

username = input('enter your username: ')
if len(username) > 12:
  print("no more than 12 characters")
if username.count(" ") > 0:
  print("must not contain spaces")
else:
  print('Valid username')
