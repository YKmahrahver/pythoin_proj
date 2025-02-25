import random

random = random.randint(0, 10)
guess = 0
is_running = True

while is_running:
  guess  = int(input("Guess the random number generator: "))
  if guess < random:
    print("Too low! Try again.")
  elif guess > random:
      print("Too high! Try again.")
  else:
      print("Wow you guessed it")
      is_running = False