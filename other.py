expense = [2200, 2350, 2600, 2130, 2190]

feb = expense[1] - expense[0]
print(f"in Feb I have spent extra {feb} expense")
print(f"during jan,feb and march, i have spent {expense[0]+expense[1]+expense[2]}")
expense.append(1980)
for i in expense:
  if i == 2000:
   print("exactly spent {i} dollars")

  


for i in expense:
  print(i)