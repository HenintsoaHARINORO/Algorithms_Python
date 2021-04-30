import random
import math


def guessing_num(lower,upper):


# generating random number between
# the lower and upper
 x = random.randint(lower, upper)
 GuessingNumber = round(math.log(upper - lower + 1, 2))
 print("\n\tYou've only ",GuessingNumber," chances to guess the integer!\n")

# Initializing the number of guesses.
 count = 0

# for calculation of minimum number of
# guesses depends upon range
 while count < GuessingNumber:
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
 if count >=GuessingNumber:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

if __name__ == '__main__':
     lower = int(input("Enter Lower bound:- "))
     upper = int(input("Enter Upper bound:- "))
     guessing_num(lower,upper)
