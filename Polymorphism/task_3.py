import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str,self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):                                    
            for j in range(len(self.matrix[i])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(res)


m1 = [[1,2,3], [4,5,6]]
m2 = [[6,5,4], [3,2,1]]
m = Matrix(m1)
s = Matrix(m2)
print(m)
n = m + s
print('new')
print(n)
print(type(n))