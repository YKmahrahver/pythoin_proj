import random

#Dictionary
capitals = {"USA" : "washington", "India": "new delhi"}

print(capitals.get("USA"))
#insert or update new element
capitals.update({"japan": "tokyo"})
print(capitals)
#remove is pop, popitem for latest element
#keys() for get key

for key in capitals.keys():
  print(key, end= " ")
for value in capitals.values():
  print(value, end= " ")
for key, value in capitals.items():
  print(f"{key} : {value}", end = " ")



#RANDOM NUMBER
number = random.randint(1,3) #prints either 123
print(number)
options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)