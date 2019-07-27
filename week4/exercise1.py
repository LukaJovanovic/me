#"""All about IO."""


import json
import os
import requests
import inspect
import sys

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()

    data = json.loads(json_data)

    this = data["results"][0]

    lastName = this["name"]["last"]
    password = this["login"]["password"]
    the_id = this["id"]["value"]
    postcode = this["location"]["postcode"]
    postcodePlusID = (int(data["results"][0]["location"]["postcode"]) + int(data["results"][0]["id"]["value"]))


    return {"lastName": lastName, "password": password, "postcodePlusID": postcodePlusID}


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    http://api.wordnik.com/v4/words.json/randomWords?api_key=zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn&minLength=10&maxLength=10&limit=1
    The arguments that the generator takes is the minLength and maxLength of the word
    as well as the limit, which is the the number of words. 
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &minLength=
    """
    #Change the min and max words to the count of the word needed on the line, it adds till 20 and goes back to 3
    number = 3
    pyraList = []
    i = 0
    while number < 20:
        url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn&minLength={}".format(number) + "&maxLength={}&limit=1".format(number)
        r = requests.get(url)
        response_json = json.loads(r.text)
        pyraList.append(response_json[0]["word"])
        print(pyraList)
        number = number + 2
    if number > 3:
        url = "http://api.wordnik.com/v4/words.json/randomWords?api_key=zau1khp6480m0ik9quh0pkcel471yx59gmv2wtnznfgn41nxn&minLength={amount}".format(number) + "&maxLength={amount}&limit=1".format(number)
        r = requests.get(url)
        response_json = json.loads(r.text)
        pyraList.append(response_json[i]["word"])
        print(pyraList)
        number = number - 2
            

def pokedex(low=1, high=5):
    """ Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.
    
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    template = "https://pokeapi.co/api/v2/pokemon/{id}"

    all_the_pokemon = []

    index_of_tallest = -1

    tallest = None

    for pokeID in range(low, high):
        print(pokeID)

        url = template.format(base=template, id=pokeID)
        r = requests.get(url)
        #if status code is okay, keep going
        if r.status_code is 200:
            #this is a wall of text
            the_json = json.loads(r.text)
            all_the_pokemon.append(the_json)

    tallest_pokemon_height = -1

    for one_poke in all_the_pokemon:
        if one_poke["height"] > tallest_pokemon_height:
            tallest = one_poke
            tallest_pokemon_height = one_poke["height"]

    print(tallest)
    return {"name": tallest["name"], "weight": tallest["weight"], "height": tallest["height"]}


def diarist():
    #gcode is a file type wich robots such as 3d printers and laser cutters use.
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.
    """
    #Open the file and read the lines
    a = open(LOCAL + "/Trispokedovetiles(laser).gcode").read()
    #count f
    c = a.count("M10 P1")
    print(c)
    #storage place
    s = open("lasers.pew", "w+")
    #Write the number to the new file "lasers.pew"
    s.write(str(c))
    #Close the new file created
    s.close()

if __name__ == "__main__":
    functions = [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj))
    ]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print("diarist did not create lasers.pew")