import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_func_exists(self) :
        self.assertTrue( "linear_interpolator" in globals(), "There is no function called linear_interpolator defined in your code" )
        
    def test_func_works(self) : 
        xv1 = np.linspace(-1,1,2)
        for i in range(10) : 
            xv = xv1[0] + i*(xv1[1]-xv1[0]) / 9 
            yv = np.exp(xv1[0]) + (xv - xv1[0])*(np.exp(xv1[1])-np.exp(xv1[0])) / ( xv1[1] - xv1[0] )
            self.assertTrue( np.abs( yv - linear_interpolator( xv, xv1[0], xv1[1], np.exp ) ) <1e-7, "The function for the linear interpolation you have written does not work correctly" )
            yv = np.sin(xv1[0]) + (xv - xv1[0])*(np.sin(xv1[1])-np.sin(xv1[0])) / ( xv1[1] - xv1[0] )
            self.assertTrue( np.abs( yv - linear_interpolator( xv, xv1[0], xv1[1], np.sin ) ) <1e-7, "The function for the linear interpolation you have written does not work correctly" )
