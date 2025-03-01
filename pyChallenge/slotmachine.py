import random

option = ("*", "$", "#")
def spin_game():
  chosen = []

  for i in range(3):
    chosen.append(random.choice(option))

  print("------------")
  for i in chosen:
    print(i, end=" | ")
  print("\n------------")

  return chosen

def main():
 currentBalance = 100
 
 while currentBalance > 0:
   print(f"Current balance: {currentBalance}")
   bet = int(input("Enter your bet: "))
   if bet > currentBalance:
     print("Insufficient funds!")
     continue
   
   result = spin_game()
   if result.count("*") >= 2:
     print("Congratulations! You won!")
     currentBalance += bet * 3
   elif result.count("$") >= 2:
     print("Congratulations! You won!")
     currentBalance += bet * 2
   elif result.count("#") >= 2:
     print("Congratulations! You won!")
     currentBalance += bet * 1.5
   else:
     print("Sorry, you lost your bet!")
     currentBalance -= bet



if __name__ == "__main__":
  main()
