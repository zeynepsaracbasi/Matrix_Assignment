import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix1 = Matrix([[1,5],[2,3],[5,5]])
        matrix2 = Matrix([[9,8],[4,5]])
        self.assertEqual(matrix1.scaler_multiplication(3), [[3, 15], [6, 9], [15, 15]])
        self.assertEqual(matrix2.scaler_multiplication(2),[[18, 16], [8,10]])

if __name__ == '__main__':
    unittest.main()
