from builtins import int
import random

won = False
guess_count = 1

random_number_magnitude = int(input("Enter max value: "))
number = random.randint(1, random_number_magnitude)
guess = int(input("Number generated. Make your first guess: "))
while not won:
  if number > guess:
      guess = int(input("Too low. Try again: "))
      guess_count += 1
  elif number < guess:
     guess = int(input("Too high. Try again: "))
     guess_count += 1
  else:
      points = random_number_magnitude / guess_count
      print(f"\033[92mYou won! {number} was the number. You won with {guess_count} guesses out of {random_number_magnitude} numbers. That's a score of {points:.0f} points.\033[0m")
      won = True
