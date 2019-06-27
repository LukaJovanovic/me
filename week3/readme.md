TODO: Reflect on what you learned this week and what is still unclear.
use a def to call upon something that you want to use later
ValueError happens in the case of a wrong value and can be used to make something happen during these cases.
#everything underneath for ex 3 to continue
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    Number = False
    upperBound = input("Enter an upper bound: ")
    while Number is False:
      try:
        int(upperBound)
        print(upperBound)
        Number = True
      except ValueError:
        upperBound = input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)
    Num = False
    lowerBound = input("Enter a lower bound: ")
    while Num is False:
      try:
        int(lowerBound)
        print(lowerBound)
        Num = True
      except ValueError:
        lowerBound = input("Enter a lower bound: ")
    print("OK then, your number is between {}".format(lowerBound) + " and {}".format(upperBound))
    lowerBound = int(lowerBound)

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