# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""
#Refactoring is about having working code, but it's ugly code so you must fix the things such as repeated things.
#Functionalising code is an important part of refactoring
#Write your own functions 

# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
ready = "Getting ready to start in {}"
#num starts at 9, and makes its way down by 1 number each time. If it hits 0 it will break and print "Let's go"
def do_bunch_of_bad_things():
    num = 9
    #While loop countdown
    while num == num:
        print(ready.format(num))
        num = (num -1)
        if num == 0:
            break
            #Message after it counts down
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    trib = triangle["base"]
    trih = triangle["height"]
    triangle["hypotenuse"] = trib ** 2 + trih ** 2
    print("area = " + str((trib * trih) / 2))
    print("side lengths are:")
    print("base: {}".format(trib))
    print("height: {}".format(trih))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.

def countdown(message, start, stop, completion_message):
    start = 5
    stop = 0
    message = "Ready in {}"
    completion_message = "Blast off!"
    # do it with a for loop instead
    while True:
        print("{m} {n}".format(m=message, n=start))
        start = (start - 1)
        if start == stop:
            break
        print(completion_message)
        return completion_message

 

# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
from math import sqrt
def calculate_hypotenuse(base, height):
    ab = base ** 2 + height ** 2
    return sqrt(ab)


def calculate_area(base, height):
    return 1/2 * base * height


def calculate_perimeter(base, height):
    return base + height + calculate_hypotenuse(base, height)


def calculate_aspect(base, height):
    if base == height:
        return "equal"
    elif base > height:
        return "wide"
    elif base < height:
        return "tall"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    facts = pattern.format(**facts_dictionary)
#Checks the base and the height to see what Aspect they are and gives the result
    if facts_dictionary["base"] > facts_dictionary["height"]:
        Aspect = wide
    elif facts_dictionary["base"] < facts_dictionary["height"]:
        Aspect = tall
    elif facts_dictionary["base"] == facts_dictionary["height"]:
        Aspect = wide

    return Aspect + facts

def triangle_master(base, height, return_diagram=False, return_dictionary=False):

    facts = get_triangle_facts(base, height, units="mm")

    diagram = tell_me_about_this_right_triangle(facts)

    if return_diagram and return_dictionary:
        return diagram and facts
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return facts
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid(api_key):
    import requests

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key={api_key}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(api_key="zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = baseURL.format(api_key="zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list


def get_a_word_of_length_n(length):
    
    import requests

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key={api_key}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
    n = length
    limit = 1
    Dalist = []
    for length in range(limit):
        url = baseURL.format(api_key="zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn", length = n)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            Dalist.append(message)
            if type(message) == str:
                return ("\n".join(Dalist))
            else:
                return None



def list_of_words_with_lengths(list_of_lengths):
    import requests

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key={api_key}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(api_key="zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn", length=list_of_lengths)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list


if __name__ == "__main__":
    do_bunch_of_bad_things()
    """wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")"""
