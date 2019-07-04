# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time

def binary_search(low, high, actual_number):
    """Do a binary search.
    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
 #Guess and tries start at 0
    tries = 0
    guess = 0
#you must define 'n'(the number of elements in the array) - the inputs are the array(n).
    n = list(range(low, high + 1))

    min = 0
    max = len(n)
#Now that we have defined a bunch of stuff, we begin looking for the target (actual_number in this case)
#We start by looking for the midpoint (While loop stops when target found)
    while max >= min:
        #This while loop steps by finding the average of the minimum and the difference b/w max and min.
        MidPoint = math.floor(min + (max - min)/2)
#We check to see if the MidPoint is the answer
        if n[MidPoint] is actual_number:
            return {"guess": guess, "tries": tries}
#We now look for if the target (actual_number) is in the 1st half or 2nd half
        elif n[MidPoint] > actual_number:
            #an extra try is added to tries
            tries +=1
            #the guess is added to guess
            guess = n[MidPoint]
            #since the number is in the 1st half, the midpoint - 1 becomes the new maximum
            max = MidPoint - 1
    
        else:
            #an extra try is added
            tries += 1
            #the guess is added
            guess = n[MidPoint]
            #since the number is in the second half, the new minimum is the midpoint + 1
            min = MidPoint + 1



if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
