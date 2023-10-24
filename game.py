import random
print("--Number-Guessing-Game--")

def make_guess():
   global guess
   while True:
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("\033[91mEnter a valid integer.\033[0m") 
    else:
        break
    
def create_number():
  global number_magnitude
  while True:
      try:
          number_magnitude = int(input("Max value of number (int): "))
          if number_magnitude < 1:
            print("\033[91mNumber can't be smaller than 1.\033[0m")
            exit()
      except ValueError:
          print("\033[91mEnter a valid integer.\033[0m")
      else:
          break

def main():
  global guess
  global guess_count
  guess_count = 1
  create_number()
  number = random.randint(1, number_magnitude)
  print(f"Number generated (1-{number_magnitude}).")
  while True:
    make_guess()
    if guess > number_magnitude:
      print(f"\033[91mNumber can't be bigger than {number_magnitude}.\033[0m")
    elif guess < 1:
      print("\033[91mNumber can't be smaller than 1.\033[0m") 
    elif number > guess:
      print("Too low.")
      guess_count += 1
    elif number < guess:
      print("Too high.")
      guess_count += 1
    else:
      points = number_magnitude / guess_count
      print(f"\033[92mYou won with {guess_count} guesses out of {number_magnitude} numbers.\nThat's a score of {points:.0f} points.\033[0m")
      break

if __name__ == "__main__":
  main()

