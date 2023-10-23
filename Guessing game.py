import random
guess_count = 1
global guess

def make_guess():
   global guess
   while True:
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("\033[91mInvalid input type.\033[0m") 
    else:
        break

while True:
    try:
        number_magnitude = int(input("Enter max value (int): "))
        if number_magnitude == 0:
           print("\033[91mNumber can't be smaller than 1.\033[0m")
           exit()
    except ValueError:
        print("\033[91mInvalid input type.\033[0m")
    else:
        break

number = random.randint(1, number_magnitude)
print(f"Number generated (1-{number_magnitude}).")
make_guess()
while True:
  if guess > number_magnitude:
    print(f"\033[91mThe number can't be bigger than {number_magnitude}.\033[0m")
    make_guess()
    guess_count += 1
  elif guess < 1:
    print("\033[91mThe number can't be smaller than 1.\033[0m")
    make_guess()
    guess_count += 1  
  elif number > guess:
    print("Too low.")
    make_guess()
    guess_count += 1
  elif number < guess:
    print("Too high.")
    make_guess()
    guess_count += 1
  else:
    points = number_magnitude / guess_count
    print(f"\033[92mYou won with {guess_count} guesses out of {number_magnitude} numbers.\nThat's a score of {points:.0f} points.\033[0m")
    break
