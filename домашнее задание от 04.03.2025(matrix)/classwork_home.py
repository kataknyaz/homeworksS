class Matrix2x2:
    def __init__(self,a,b,c,d):
        # a - элемент в первой строке в первом столбце
        # b - элемент в первой строке во втором столбце
        # с - элемент во второй строке в первом столбце
        # d - элемент во второй строке во втором столбце
        self.matrix = [[a, b], [c, d]]

    def __str__(self):
        return f'Matrix2x2({self.matrix[0][0]}, {self.matrix[0][1]}, {self.matrix[1][0]}, {self.matrix[1][1]})'    
    

    def determinant(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
    
    def __add__(self, other):
        return Matrix2x2(
            self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1],
            self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1],
        )
    
    def __sub__(self, other):
        return Matrix2x2(
            self.matrix[0][0] - other.matrix[0][0], self.matrix[0][1] - other.matrix[0][1],
            self.matrix[1][0] - other.matrix[1][0], self.matrix[1][1] - other.matrix[1][1],
        )
    
    def __mul__(self, scalar):
        return Matrix2x2(
            self.matrix[0][0] * scalar, self.matrix[0][1] * scalar,
            self.matrix[1][0] * scalar, self.matrix[1][1] * scalar
        )
    
    def __eq__(self, other):
        return self.matrix == other.matrix


matrix1 = Matrix2x2(1, 2, 3, 4) 
matrix2 = Matrix2x2(5, 6, 7, 8)  

matrix3 = matrix1 + matrix2
matrix4 = matrix1 - matrix2
matrixScalar = matrix1 * 3
print(matrixScalar)

