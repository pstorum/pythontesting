from random import seed
from random import randint
import time

print("Enter a range of numbers to guess from:")
range_1 = int(input())
range_2 = int(input())
random_number = int(randint(range_1, range_2))
run_loop = bool(True)
while run_loop:
    print("Enter a number to guess:")
    guessed_number = int(input())
    if range_1 <= guessed_number <= range_2:
        if guessed_number == random_number:
            print("You guessed correctly")
            time.sleep(2)
        else:
            print("You guessed wrong, the right number is", random_number)
    else:
        print("The inputted number is not in range. Please try again: ")
