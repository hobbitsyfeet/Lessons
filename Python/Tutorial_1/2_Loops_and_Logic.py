"""
2_Loops_and_logic.py

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
        print(letter,end="|") #end="" is a python 3 version of print. Python 2 does not even use parenthesis!!
    print('\n') #end line character. print() also prints an end line because end="\n" by default!

    #Prints 1 2 3 4 5
    for i in range(5):
        print(i)

    #Range has the parameters(start, end, step)
    #Prints from 5 to 10
    for i in range(5, 10):
        print(i)

    #0, 2, 4, 6, 8, 10
    for i in range(0, 10, 2):
        print(i)

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

    #SCOPES (where variables are accessable from)
    i = 10
    for x in range(10):
        #This prints (0,10), (1,10) ... (10,10)
        print(x, i)

    #In python, the variable can be initialized within a loop and accessed outside. Other languages this is a no no.
    #This is called variable scopes, we will get into this later when we get to functions and classes.
    print(x)

    '''
    IF statements. They are true or false statements where boolean algebra takes place. Generally though, 
    this does not get that complex. Often it's to check that a value exists in a rage, or to compare values.

    This might be a bit late in the tutorial but let's get at it.
    '''

    x = 10
    y = 2
    z = x

    a = 'a'
    b = 'b'
    c = 'c'

    #Boolean values, for readability exist as True and False. In Python, and many other
    # == is 'equal to'
    # != not equal
    # ! is not (so !False is True)
    right = True
    wrong = False

    wrong_i = 0
    right_i = 1


    print(right == right_i) #Prints True

    print(right and right_i) #T
    print(right and wrong) #F
    print(right or wrong) #T
    print (wrong or wrong)#F

    print (right == 1 and wrong == 0) #T
    print(right == 1 or wrong == 0) #T
    print(right is 1 and wrong is 0 )
    

    if right:
        print ("if right is true")
    else:
        print("Wrong.")

    if wrong:
        print("This is not right, keep going")
    elif right is True:
        print("Skipped it being wrong!")

    print(not right) 
    print(not wrong) 

    print(not right or not wrong) #T
    print((right and right) or wrong) #T

    #If you're interested about learning more complex logic, look up Boolean Algebra.

    #Not that these comparing exist for anything including complex objects, strings or chars. 


    test_var = 0
    while True: #Loop something forever. This can be good at times if you want to continuously have input
        print("What value do you want to enter ? Type an input then hit <Enter>")

        test_var = input() #Input from user

        #inputs from user are always a string. We can convert this but this means that the correct user input is given!

        #this function converts whatever is there into an integer!
        #Similarly, we have str(), float(), chr() as well as int()
        test_var = int(test_var) 

        if test_var > 10:
            print("value is greater than 10")

        elif test_var <= 100:
            print("Value is less than or equal to 100")
            
            #Let's give a nested if statement
            if test_var <= 50:
                print("Value is less than or equal to 50")
            else:
                print("Value is STRICTLY greater than 50!")
        #Note that the inverse of >= is < ? This is explained clearly through set theory!
        #Don't worry, its not complecated. Look it up if you're interested!! (It's good to know!)

        #Continue skips the current loop, moving onto the next cycle and not executing the lines below.
        if test_var > 100:
            print("Value is greater than 100, continuing!")
            continue

        #Break exits a loop right then and there, no matter the value.
        if test_var <= 0:
            break
            print("Exiting loop!")

    print("I belive this is it for loops and logic! It's a simple introduction but it's enough to get you going!")
    print("Bye for now!")

 