'''
We will get into looking at Numpy. You can look at it here https://numpy.org/devdocs/user/quickstart.html
'''

#BEFORE YOU RUN THIS, activate your environment and type 'python3 -m pip install numpy'
#This will install numpy, easy as that!

import numpy as np #we import the library and call it np, purely out of convenience when we acces it.
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


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

    full = np.full((2,2), 4)

    ten_ones = np.ones((1,10))
    print("Ten ones in an array:", ten_ones)
    ten_ones = ten_ones.reshape(5,2) #This reshapes the array into a 5 row 2 column array
    print("Reshaped (2x5) array:\n", ten_ones)

    print("Fill a numpy array with a specific value (2x2) with 4's:\n", full)


    '''
    Let's create an array of 0's and fill it with some sort of data.
    '''
    xyz=np.array(np.random.random((20,3))) #This creates 100 points in 3 dimensions randomly
    #print(xyz)
    #We see that these random points exist between 0 and 1

    #What if we want a number between 0 and 10? 
    #Numpy random creates a random number below 0 (0.15890173903)
    #So to get a random number between 0 and 10, simply multiply by 10!

    #We will also make a plot to view the data! So let's set it up so we can load the data in as we create it!
    #This is a bit more simple than trying to parse the numpy array after.
    
    #Define an empty plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') #Define a projection in 3d, adding a subplot on the top left (the 111)
    #A subplot beside it would be 112! (maybe, look it up!) https://matplotlib.org/3.2.1/tutorials/index.html
    
    print("Random 3D points using numpy array, between 0 and 10")
    simple_counter = 0
    for x, y, z in xyz:
        #Each dimension is random between 0 and 10
        x = x*10 % 10 
        y = y*10 % 10
        z = z*10 % 10

        #Because these variables are copies (do not share the memory address as the values in xyz), we need to assign them
        xyz[simple_counter] = (x,y,z) #Assign xyz point to be equal to our new points
        ax.scatter(x, y, z) #Here we add the point to the scatter plot!
        
        simple_counter += 1 #we add one to the index used to access the points. 

    print(xyz)

    #Add the titles
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    #Show the plot!
    plt.show()

    '''
    This is a nice visual introduction to numpy, creating points that can be visualized in 3D using matplotlib.

    The reason why I do this is that we'll be using 3D data later on! I have some data of my own I can share so we can
    Work on it together to learn libraries and explore Python and how to code. 

    Learning to code without a purpose is just code. Learning to code for a purpose is learning how to use a tool to
    learn more about what you're passionate about.
    '''
