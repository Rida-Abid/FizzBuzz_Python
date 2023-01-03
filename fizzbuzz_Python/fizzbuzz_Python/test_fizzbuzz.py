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

if __name__ == '__main__':
    unittest.main()
