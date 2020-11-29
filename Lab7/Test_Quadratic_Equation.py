import unittest
from ExceptionTypes import NonRealException,NotQuadraticEquation
from Quadratic_Equation import solve_quadratic_equation

class Test_Quadratic_Equation(unittest.TestCase):
    def test_one_solution_1(self):
        self.assertEqual(solve_quadratic_equation(1,2,1),float(-1))

    def test_one_solution_2(self):
        self.assertEqual(solve_quadratic_equation(1,4,4),float(-2))

    def test_one_solution_3(self):
        self.assertEqual(solve_quadratic_equation(1,-4,4),float(2))


    def test_none_solution_1(self):
        self.assertRaises(NonRealException, lambda:solve_quadratic_equation(1,1,1))

    def test_none_solution_2(self):
        self.assertRaises(NonRealException, lambda:solve_quadratic_equation(1,2,3))

    def test_none_solution_3(self):
        self.assertRaises(NonRealException, lambda:solve_quadratic_equation(-11,5,-3))


    def test_not_quadratic_equation_1(self):
        self.assertRaises(NotQuadraticEquation,lambda:solve_quadratic_equation(0,5,-3))

    def test_not_quadratic_equation_2(self):
        self.assertRaises(NotQuadraticEquation,lambda:solve_quadratic_equation(0,2,3))

    def test_not_quadratic_equation_3(self):
        self.assertRaises(NotQuadraticEquation,lambda:solve_quadratic_equation(0,9,6))


    def test_quadratic_equation_1(self):
        x1,x2 = solve_quadratic_equation(1,4,3)
        self.assertEqual(x1,float(-1))
        self.assertEqual(x2,float(-3))

    def test_quadratic_equation_2(self):
        x1,x2 = solve_quadratic_equation(1,5,4)
        self.assertEqual(x1,float(-1))
        self.assertEqual(x2,float(-4))

    def test_quadratic_equation_3(self):
        x1,x2 = solve_quadratic_equation(1,2,-3)
        self.assertEqual(x1,float(1))
        self.assertEqual(x2,float(-3))

if __name__ == '__main__':
    unittest.main()
