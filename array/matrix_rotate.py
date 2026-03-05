def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)-1):
        for j in range(1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            
        
    return matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(mat))

# mat.reverse()
# print(mat)