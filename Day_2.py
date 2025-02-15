import time
#INDEXING
credit_number = "1234-5678-90123-34567"

print(credit_number[0]) # prints 1
print(credit_number[0:4]) #prints 1234 (starting index is inclusive and ending index is exclusive)
print(credit_number[5:9]) # prints 5678 
print(credit_number[-1]) # prints last index
print(credit_number[::2]) # :: means beginning till end, 2 prints every second char
#practice
#reversing
credit_number = credit_number[::-1]
print(credit_number)


#FORMAT SPECIFIERS
price1 = 3.14159265
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:2f}") #places 2 decimal places
print(f"Price 2 is ${price2:10}") #space of 10
print(f"Price 2 is ${price2:010}") #space of 10 with 0s
print(f"Price 3 is ${price3:<10}") #space of 10 on left
print(f"Price 3 is ${price3:>10}") #space of 10 on right
print(f"Price 3 is ${price3:^10}") #space of 10 on center
print(f"Price 3 is ${price3:+}") #determines its sign
print(f"Price 3 is ${price3:,}") #separated with a comma
#these can be combined


#FOR LOOPS
for x in range(1,11): #prints 1-10
  print(x)
  

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1): #starts end to beg
  seconds = x % 60 
  minutes = int(x / 60) % 60
  hours = int(x / 3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}") # 02 adds two space with 0 in the start
  time.sleep(1) #waits 1 second before printing next
