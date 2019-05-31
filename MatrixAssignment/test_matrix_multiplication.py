import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix1 = Matrix([[9,8],[4,5]])
        matrix2 = Matrix([[36, 32],[16, 20]])
        matrix3 = Matrix([[2,3,5],[4,5,6]])
        matrix4 = Matrix([[1,4,4],[2,3,5],[4,5,6]])
        self.assertEqual(matrix1.matrix_multiplication(matrix2),[[452, 448], [224, 228]])
        self.assertEqual(matrix2.matrix_multiplication(matrix3),[[200, 268, 372], [112, 148, 200]])
        self.assertRaises(Exception,matrix1.matrix_multiplication(matrix4))

if __name__ == '__main__':
    unittest.main()
