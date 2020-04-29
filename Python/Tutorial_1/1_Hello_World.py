"""
1_Hello_World.py

Author: Justin Petluk
Date: April 19, 2020

"""
#LOOK! Comments! We will use this syntax to make notes through our code.
#We can do single line comments with the # before we write.
"""
or we can
use """  """ or ''' ''' Before and after our words to
write comments on multiple lines!
Make sure you start and end them! (Wrap it!)
"""

#Most programs contain a "main", or a center where everything meets and runs.
#we can define a python "main" by adding this short line here:
#NOTE: most of Python's syntax is TABs, parenthesis and brackets or colons.
#Each 'Nested" parts must be indented by an additional TAB
#That's why we see the if statement one tab over than the rest of the code.
if __name__ == "__main__":

    #Let's Display a simple text.
    print("Hello World")

    #Assign a variable. Note, variable can be substituted for ANYTHING.
    #The purpose for this is simply READABILITY.
    #Variable names can help you, and other people READ the code!
    variable = "Hello World"
    print(variable)


    #This variable is stored as a string. This is a word, or a 'string' of characters.
    #You can access each character in the 'string' individually by providing
    #an index of it's location. For example, H is the first letter.
    #REMEMBER: Most languages start with a 0 index format, or you start at 0 instead of 1.
    print(variable[0])
    print(variable[1])
    print(variable[2])
    print(variable[4])
    # ...
    print(variable[10])

    #Or
    print(variable[0], variable[1], variable[2], variable[3], variable[4])

    #Python has many useful and dynamic functions. Such as Length or len(). This returns how long something is.
    #For Here, we will look at how long the 'string' is.
    #This gives us the number of charactors (letters and spaces) in the sentence!
    print(len(variable))

    #Before we get into the uses of len() and other things, lets explore other variable types 
    #and how to assign them.
    number_1 = 1
    number_2 = 2

    #Simple math
    add = number_1 + number_2       # = 3
    subtract = number_1 - number_2  # = 1
    multiply = number_1 * number_2  # = 2
    divide = number_1 * number_2    # = 0.5
    power = number_2 ** number_2    # = 4
    mod = number_1 % 2 # This should be 1. If the number is even (mod 2), it will be 0, else 1.
    #Mod is basically the remainder of long division. 3/2 is 1(*2) remainder 1

    #Extra math syntax
    add += 1 #adds 1 to itself
    subtract -= 1 #subtracts 1 itself
    multiply *= 2 #multiplies 2 to itself
    divide /= 2 #divides itself by 2


    #Boolean Variables
    Yes = True
    No = False

    #Strings
    string = "A string of letters!"
    char = string[0] #Which is also a string object in python! There's no real difference!

    #None!
    nothing = None #This is empty. Equivelant to NULL in other languages, it has no type. It's Undefined.


    #Lists! This will get a bit complecated, so read through my code, and GOOOGLE YOUR QUESTIONS!
    print("LIST \n") #\n is a NEW LINE character. It acts like ENTER would in any other text editor!
    a_list = []
    another_list = list()

    number_list = [0, 1, 2, 3, 4, 5]
    character_list = ['a', 'b', 'c']
    string_list = ['cat', "dog"] #Look, '' and "" both work!
    list_of_list = [[1], [2, 3]] # Maybe we can create a 2D grid?
    grid = [[0, 0], #OR JUST A LIST OF LISTS!
            [0, 0]]

    #Access a list's value
    print(character_list[0]) # should be 'a'

    #append a value (add to end)
    number_list.append(6)
    print(number_list) #[0, 1, 2, 3, 4, 5, 6]

    #Remove a number
    number_list.remove(6)

    #Subset a list
    #NOTE: We can do things in functions, since it RETURNS a value
    #The [:] operator acts like a from-to operator. It starts from index 0 and goes to index 3
    print(number_list[0:3]) #[3, 4, 5]
    test = number_list[3:6] #[0, 1, 2]
    print(test) #


    #WOAH! It works across lines if your syntax is proper.
    #this is a good way for complex structures to be read easily.

    #Dictionaries. 
    #Key's and Values. Imagine you have one definition, there can only be one.
    #A definition (key) is paired with it's meaning, or "value".
    #Just like an alphabetized dicitonary in real life, these dictionaries are FAST to access
    #We do not have to search for a variable like in a list to access it. Let's take a look
    print("\nDICTIONARY")
    example_dictionary = {}
    another_dictionary = dict()
    another_dictionary = {"Key":"VALUE"}

    example_dictionary["KEY"] = "VALUE"
    print(example_dictionary)

    #Add to a dictionary
    example_dictionary["NEW_KEY"] = "NEW_VALUE"
    print(example_dictionary)

    print(example_dictionary["KEY"]) #prints VALUE
    print(example_dictionary["NEW_KEY"])


    #Dictionary within a dictionary
    i_am = {"Justin": {"Birthday":0, "Age": 10, "Healthy":False, "University Degree": True}, #I Just graduated.
            "No One": {"Birthday":100, "Age": 100, "Healthy":"What's that", "University Degree":0}
            }
    
    #Adding a Key and Value to a list already made!
    i_am["You"] = {"Birthday":None, "Age": 11, "Healthy":True, "University Degree": "I don't know."}
    print(i_am["Justin"]) #Print's the dictionary about ME
    print(i_am["You"]) #and YOU

    print(i_am["You"]["Age"]) #print Your age
    print(i_am["No One"]["Healthy"]) #Prints "What's that"

    
    #Sets!
    a_set = set([1,2,3,4])
    b_set = set([3,4,5])
    
    #Tuple!
    # A Tuple is just an n-sized pair! a pair is variables, but a tuple is a pair of any size!
    example_tuple = (1,2,3,4,5)
    example_tuple = tuple(1,2,3,4,5) #These are the same!

    #a list of tuples
    tuple_list = [(1,2), (1,2), (1,2)] #This can also be a list of 2D points!
    

    print(a_set in b_set) #should print False
    print(b_set in a_set) #should print False

    print (a_set not in b_set) #should print True
    print(b_set not in a_set) #should be True

    #Notice how sets can be useful? Look up set theory for more!

    #Here we will end the "Hello World" Tutorial.

    #Let's see this code in action! Either copy this file, or entire contents and try to execute it.
    #We can do this by using the python comand we installed earlier.

    #Go into the directory of where you have this file. For example: I would have this in Github/Lessons/Tutorial_1/
    #When we are in this folder on the command line (if you have troubles, just type 
    #'cd' with a space after it, and drag and drop the file in, then hit enter)
    #type 'python Hello_Wold.py' and watch your code run!
    print("Goodbye!")