import random

print("Guess My Number")

print("I'm thinking of a number between 1 and 100")

print("Try to guess it in as few attempts as possible")

count = 0
secret = random.randint(1, 100)

while True:
  count += 1
  guess = int(input("Guess the number from 1 to 100: "))

  match guess:
    case guess if guess < secret:
      print(str(guess) + " is too low!")
    case guess if guess > secret:
      print(str(guess) + " is too high!")
    case guess if guess == secret:
      print(f"{guess} is correct! It took you {count} guesses!")
      break

print("Goodbye")
  