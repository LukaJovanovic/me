"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between _ and an upper bound?")
    Number = False
    lowerBound = input("Enter an lower bound: ")
    while Number is False:
      try:
        int(lowerBound)
        print(lowerBound)
        Number = True
      except Exception:
        lowerBound = input("Enter an lower bound: ")
    print("OK then, a number between {} and _ ?".format(lowerBound))
    lowerBound = int(lowerBound)
    Num = False
    upperBound = input("Enter an upper bound: ")
    while int(upperBound) <= int(lowerBound):
      print("Upperbound must be greater than {}".format(lowerBound))
      upperBound = input("Enter an upper bound: ")
    while Num is False:
      try:
        int(upperBound)
        print(upperBound)
        Num = True
      except Exception:
        upperBound = input("Enter an upper bound: ")
        while int(upperBound) <= int(lowerBound):
          print("Upperbound must be greater than {}".format(lowerBound))
        Number = False
        upperBound = input("Enter an upper bound: ")
    print("OK then, your number is between {}".format(lowerBound) + " and {}".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)


    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
        if guessedNumber > upperBound or guessedNumber < lowerBound:
            print("Guess between {}".format(lowerBound) + " and {}".format(upperBound))
    return "You got it!"


    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
