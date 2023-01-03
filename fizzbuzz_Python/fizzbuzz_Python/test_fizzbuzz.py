import unittest
import Program
from Logic import logic 


class TestProgram(unittest.TestCase):
    def  test_DefaultParameters(self):
        result = logic.process(3, 5, 50)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 50)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "fizz")
        self.assertEqual(result[4], "buzz")
        self.assertEqual(result[14], "fizzbuzz")

    def  test_SameParameters(self):
        result = logic.process(3, 3, 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "fizzbuzz")

    def  test_First2ParametersSame(self):
        result = logic.process(3, 3, 50)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 50)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "fizzbuzz")

    def  test_Last2ParametersSame(self):
        result = logic.process(3, 5, 5)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "fizz")
        self.assertEqual(result[4], "buzz")

    def  test_FirstandLastParametersSame(self):
        result = logic.process(3, 5, 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "fizz")

    def  test_NegativefizzId(self):
        result = logic.process(-3, 5, 50)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Please enter all values greater than 0")

    def  test_NegativebuzzId(self):
        result = logic.process(3, -5, 50)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Please enter all values greater than 0")

    

        
        

    
       

if __name__ == '__main__':
    unittest.main()
