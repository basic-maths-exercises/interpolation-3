import numpy as np 

def linear_interpolator( x, x1, x2, func ) : 
  # Your code for doing linear interpolation goes here
  
  
# The code should not be modified from here.  I have written this part to test your implementation.
print("I have evaluated the function tanh at 0 and 1")
print("Based on the values of the function at these endpoints")
print("the interpolated value of tanh(0.5) is", linear_interpolator( 0.5, 0, 1, np.tanh) )
