import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix1 = Matrix([[9,8],[4,5]])
        matrix2 = Matrix([[36,32], [16,20]])
        matrix3 = Matrix([[2,3,5],[4,5,6]])
        matrix4 = Matrix([[1, 4, 4, 4], [2, 3, 5, 4], [4, 5, 6, 4], [2, 3, 4, 4]])
        self.assertEqual(matrix1.matrix_determinant(),13)
        self.assertEqual(matrix2.matrix_determinant(),208)
        self.assertEqual(matrix4.matrix_determinant(),16)
        self.assertRaises(Exception,matrix3.matrix_determinant())

if __name__ == '__main__':
    unittest.main()
