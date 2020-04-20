"""
Loops.py

Author: Justin Petluk
Date: April 19, 2020

"""

'''
Notice how I leave whitespace and comments throughout the code.
This is good to get into the habbit to early on.
Here I write bulk descriptions, but this is usually not effective
it takes long to read and a lot of room. Keep an eye on commenting
Methods I use here. Whitespace (enters) are also useful for readability.
'''

if __name__ == "__main__":

    #Declare Variables
    greetings = "Hello_World"

    print("For Loop:")

    #Loop through each letter in greetings, speparating each with '|'
    for letter in greetings:
        print(letter, end="|")


    '''
    Lets look at what happened in the for loop and it's syntax.

    A for loop iterates (looks through one at a time) the letters in the string
    it does this by assigning each character in the string to the variable letter.

    We access that variable and print it. 
    Since print is a function, it provides parameters.
    reading Documentation is very important, so looking it up at this link can be useful.
    https://docs.python.org/3.6/tutorial/index.html

    We will look into that stuff later. 
    
    The For loop initializes the variable each loop to a new value in greetings, hense the phrase "for ____ in ____:"

    Let's explore other loops
    '''

    #count from 1 to 10
    counter = 0
    while(counter < 10):
        counter = counter + 1
        print(counter)

    #TODO: FINISH THIS IM GOING TO BED. GOODNIGHT.