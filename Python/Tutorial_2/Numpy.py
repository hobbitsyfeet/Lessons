'''
We will get into looking at Numpy. You can look at it here https://numpy.org/devdocs/user/quickstart.html
'''

#BEFORE YOU RUN THIS, activate your environment and type 'python3 -m pip install numpy'
#This will install numpy, easy as that!

import numpy as np #we import the library and call it np, purely out of convenience when we acces it.

"""
Numpy is like 
"""

if __name__ == "__main__":
    # A numpy array is like a list with a fixed size where all the values inside are the
    #same type

    #A numpy array can be created by inserting a simple list
    numpy_array = np.array([1,2,3])
    print("Simple numpy array", numpy_array)
    #and we can assign and return the types of values

    #we can set the type, and use a list of tuples and set it's datatype
    numpy_array = np.array([(1,2,3), 
                            (4,5,6)], dtype=np.float64)
    print(numpy_array)


    #Some useful commands can help describe the arrays
    print("Number of Dimenstions:", numpy_array.ndim)
    print("Numpy Shape:", numpy_array.shape) #Note that on a 2D array, it returns (y, x)
    print("Datatype:",numpy_array.dtype)

    #initialize 2x2 array of zeros
    zeros = np.zeros((2,2))
    print("Zeros:", zeros)
    #This looks like
    #[0 ,0]
    #[0 ,0]

    #and similarly 2x2 of 1's
    ones = np.ones((2, 2))
    print("Ones", ones)
    #[1, 1]
    #[1, 1]

    ten_ones = np.ones((1,10))
    print("Ten ones in an array:", ten_ones)
    ten_ones = ten_ones.reshape(5,2) #This reshapes the array into a 5 row 2 column array
    print("Reshaped (2x5) array:", ten_ones)


    #This is just a short lesson. Next we will go into how to fill an array dynamically
    #and iterating through an array to get to these indices. 
    #COMING NEXT. Thanks for waiting...