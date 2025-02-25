#NESTED LOOP
for x in range(3):
  for i in range(1, 10):
    print(i, end=" ") #this is to print them horizontally
  print()

#to see all methods for list
fruits = ["apple", "orange", "banana"]
# print(dir(fruits))
# #to see description
# print(help(fruits))

#shopping card program
foods = []
prices = []
total = 0

while True:
  food = input("Enter a food to buy (q to quit): ")
  if food.lower() == "q":
    break
  else:
    price = float(input(f"Enter the price of {food}: $"))
    foods.append(food)
    prices.append(price)
  
print("-----YOUR CART-------------")
for food in foods: 
  print(food, end=", ")
for price in prices: 
  total += price

print(f"\nTotal: ${total}")


#2d list
fruits = ["banan", "apple"]
vegetables = ["celery", "carrots"]

#combine them 
groceries = [fruits, vegetables]

print(f"accessed: {groceries[0][1]} \nfull list: {groceries[1]}")
