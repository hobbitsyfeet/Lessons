"""
2_Pandsas.py

Author: Justin Petluk
Date: April 28, 2020

"""
'''
Pandas is a package that provides spreadsheet-like methods in python.  https://pandas.pydata.org/

More specifically: https://pandas.pydata.org/docs/user_guide/index.html

I's great for working with data, and importing/exporting into excel spreadsheets.
'''

import numpy as np
import pandas as pd

from datetime import datetime #We will be creating date data.

import os #Helps us find if our data folder exists to put our dataframe in!

#Check out for more details on datetime! https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html

#One thing to note as we go forward, is a dataframe must be full, or set with default values for empty cells.
#It cannot have rows or columns that have various lengths.


def assign_nparray(input_data, nd_array):
    '''
    This assigns input data to the respective numpy array.
    This is a helper function!!
    '''
    #Let's learn a little trick. 
    #Enumerate just pairs the variable with an index number similar to how we define a number outside of the loop
    #To be zero and add it by 1. The first element will look like (0, 'Jamie'), second (1, 'Alex') and so on.
    #We can also iterate through multiple variables in a loop!
    for value in enumerate(input_data):
        index = value[0]
        index_value = value[1]
        nd_array[index] = index_value

        #we could also do 'nd_array[value[0]] = value[1]'
    return nd_array

if __name__ == "__main__":

    #Let's start out imagining we collected this data during this python project:

    headers = ["Number Data", "Float_data", "Names", "Dates"] #Let's make some column titles
    numbers = np.array([1,2,3,4,5,6,7,8,9,10]) #Create number data
    floats = np.array(np.random.random((50)),dtype=np.float) #Create 50 random decimal numbers
    #Lets start from today and go to next month (April 27th to the end of the month)
    dates = np.arange('2020-04-27', '2020-05', dtype='datetime64[D]') #Notice how we define the datatype to datetime (to days with [D])?
    names = ["Jamie", "Alex", "Fin"] 

    #Let's assume we have a bunch of data. All have different lengths, right?
    #So we will create empty numpy arrays filled with default NULL data

    print("Longest:",max([numbers, floats, dates, names], key=len)[:5],"...\n") #Print the first 5 elements of the longest array

    #Notice it prints floats? This is because it's the longest using the key function len()
    longest_list = len(max([numbers, floats, dates, names], key=len)) #So we get the length of the max element sorted by length

    name_data = np.full((longest_list), "NAN") #Create a text row just as long as data.
    date_data = np.full((longest_list), "2000-01-01", dtype='datetime64[D]') # Except we need to initialize it as a date datatype and can't use NAN.
    number_data = np.full(longest_list, -1, dtype=np.int32)
    float_data = np.full(longest_list, -1, dtype=np.float) #We don't NEEED to do this, but imagine we don't know.

    #Now let's assign the data to the arrays!
    name_data = assign_nparray(names, name_data)
    date_data = assign_nparray(dates, date_data)
    number_data = assign_nparray(numbers, number_data)
    float_data = assign_nparray(floats, float_data)

    #I'm Just going to leave this in here for example. I was writing these for loops for assignment
    #but then I realised I was repeating myself. Keep your code D.R.Y. Don't Repeat Yourself!
    #So I made a function called assign_nparray to replace this code:
    '''
    for name in enumerate(names):
        print("Enumerate data:", name)

        #So we access the first element for the index and second for the variable
        index = name[0]
        name = name[1]

        #Assign the numpy text_data to the name
        text_data[index] = name
    
    #Filll out the dates
    for date in enumerate(dates):
        date_data[date[0]] = date[1] # A Little less readable but you get used to it

    for num in enumerate(number_data):
        number_data[num[0]] = num[1] 
        
        .
        .
        .
    '''

    #Now that we have the data all prepared with numpy arrays, let's create a pandas dataframe!
    #We also made sure that they are the same sizes, so there's no need to worry!!!

    #Create a dictionary of all the data
    #We can create a dictionary to keep it neat? We can just insert the names from headers in here...
    #But what if we wanted to access the headers again elsewhere and renamed them? It has it's tradeoffs.

    data_dictionary = {headers[0] : number_data, headers[1] : float_data, headers[2]: name_data, headers[3] : date_data}
    dataframe = pd.DataFrame(data=data_dictionary)

    print(dataframe)

    #Lets save the file. Check if the folder exists though! otherwise it will crash!
    if not os.path.exists("./data/"):
        os.mkdir("./data")
        
    dataframe.to_csv("./data/First_Dataframe.csv", index=False) #ignore the index column

    #We can also do ...
        # dataframe.to_dense
        # dataframe.to_dict
        # dataframe.to_gbq
        # dataframe.to_html
        # dataframe.to_pickle
        # dataframe.to_hdf  
        # AND SO ON!

    '''
    So just to know, you can create pandas dataframes using a dictionary of lists {key:list} as well. 
    I just wanted to teach you the more tedious method of numpy arrays to get you used to it.
    But we also see how nicely numpy arrays are to guarantee a static length while filling out any lengths of data.
    '''