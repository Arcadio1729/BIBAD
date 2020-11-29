import unittest
from ExceptionTypes import NonRealException,NotQuadraticEquation,OnePointException
from Find_Line_Equation import find_line_equations

class MyTestCase(unittest.TestCase):
    def test_one_point_1(self):
        self.assertRaises(OnePointException, lambda:find_line_equations(-1,1,-1,1))

    def test_one_point_2(self):
        self.assertRaises(OnePointException, lambda:find_line_equations(-3,4,-3,4))


    def test_X_parallel(self):
        A,B,C=find_line_equations(-2,5,-2,10)

        self.assertEqual(A,1)
        self.assertEqual(B,0)
        self.assertEqual(C,2)

    def test_Y_parallel(self):
        A,B,C=find_line_equations(-2,5,2,5)

        self.assertEqual(A,0)
        self.assertEqual(B,1)
        self.assertEqual(C,-5)


    def test_two_points_1(self):
        A,B,C=find_line_equations(1,1,3,3)

        self.assertEqual(A,1)
        self.assertEqual(B,-1)
        self.assertEqual(C,0)

    def test_two_points_2(self):
        A,B,C=find_line_equations(1,2,2,1)

        self.assertEqual(A,-1)
        self.assertEqual(B,-1)
        self.assertEqual(C,3)

if __name__ == '__main__':
    unittest.main()
