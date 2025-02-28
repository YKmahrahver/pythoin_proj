#python banking program

def show_balance(balance):
    print(f"Your current balance is: {balance}")

def deposit(balance):
  amount = float(input("Enter the amount to deposit: "))
  balance += amount
  return balance
  print(f"Deposit successful. New balance: {balance}")

def withdraw(balance):
  amount = float(input("Enter the amount to withdraw: "))
  if amount > balance:
    print("Insufficient funds.")
  else:
    balance -= amount
  return balance
  print(f"Withdrawal successful. New balance: {balance}")

balance = 0
is_running = True

while is_running:
  print("\nWelcome to the Banking System")
  print("1. Check Balance")
  print("2. Deposit Money")
  print("3. Withdraw Money")
  print("4. Exit")
  choice = int(input("Enter your choice: "))

  match choice: #no need to put break in each case, only used for loops
    case 1:
      show_balance(balance)
      
    case 2:
      balance = deposit(balance)
      
    case 3:
      balance = withdraw(balance)
      
    case 4:
      is_running = False
      
    case _:
      print("Invalid choice. Please try again.")
