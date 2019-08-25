from copy import deepcopy
import math


class Matrix(object):

    def __init__(self, liste):
        self.set_matrix(liste)

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self, liste):  # input list controls to fit matrix requirements
        if type(liste) == list:
            if len(liste) != 0:
                for row in liste:
                    if len(liste[0]) == len(row):
                        for column in row:
                            if type(column) == int or type(column) == float:
                                continue
                            else:
                                raise Exception('Matrix must be a list of digit lists.')
                    else:
                        raise Exception('Number of columns must be equal for each row')
                self.__matrix = liste
                self.row = len(liste)
                self.col = len(liste[0])
            else:
                raise Exception('Matrix must refer to a list of lists.')
        else:
            raise Exception('Matrix must be list type.')

    def scaler_multiplication(self, value):
        matrix = [[0] * self.col for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                matrix[i][j] = (self.__matrix[i][j] * value)
        return matrix

    def trace(self):
        sum = 0
        for i in range(self.row):
            for j in range(self.col):
                sum = sum + (self.__matrix[i][j])
        return sum

    def transpose(self):
        transposed_matrix = [[self.__matrix[j][i] for j in range(self.row)] for i in range(self.col)]
        return transposed_matrix

    def matrix_multiplication(self, matrix2):
        if self.col == len(matrix2.__matrix):
            rows, columns = self.row, len(matrix2.__matrix[0])
            matrix = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    matrix[i][j] = sum(
                        self.__matrix[i][k] * matrix2.__matrix[k][j] for k in range(len(matrix2.__matrix)))
            return matrix
        else:
            return ("Column number of First Matrix must be equal to row number of Second Matrix")

    def matrix_determinant(self):
        try:
            if self.row == 2:
                value = self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
                return value
            total = 0
            for fcolumn in list(range(self.row)):
                copy = deepcopy(self.__matrix)[1:]  # define submatrix for focus column
                for i in range(len(copy)):
                    copy[i] = copy[i][0:fcolumn] + copy[i][fcolumn + 1:]  # for each remaining row of submatrix ,remove the fcolumn elements
                copy = Matrix(copy)
                sign = math.pow(-1, (1 + fcolumn + 1))
                det_A1j = copy.matrix_determinant()
                total += sign * self.__matrix[0][fcolumn] * det_A1j
            return total
        except:
            return ("Dimensions must be NxN to find determinant of matrix!")

    def matrix_inverse(self):
        try:
            determinant = self.matrix_determinant()
            #matrix inversion for 2x2 matrix
            if self.row == 2:
                return [[self.__matrix[1][1] / determinant, -1 * self.__matrix[0][1] / determinant],
                        [-1 * self.__matrix[1][0] / determinant, self.__matrix[0][0] / determinant]]
            cfactors = []
            for r in range(self.row):
                Row = []
                for c in range(self.row):
                    #find minor according to current column and row
                    minor = [row[:c] + row[c + 1:] for row in (self.__matrix[:r] + self.__matrix[r + 1:])]
                    minor = Matrix(minor)
                    Row.append(((-1) ** (r + c)) * minor.matrix_determinant())
                cfactors.append(Row)
            cfactors = Matrix(cfactors)
            cfactors = cfactors.transpose()
            for row in range(len(cfactors)):
                for column in range(len(cfactors)):
                    cfactors[row][column] = cfactors[row][column] / determinant
            return cfactors
        except:
            return ("Matrix dimension must be NxN for inversion!")

#editjdgd


