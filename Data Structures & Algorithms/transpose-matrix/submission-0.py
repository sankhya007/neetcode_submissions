class Solution: 
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        # here we are just getting the number of rows and columns in the matrix
        result = [[0] * rows for _ in range(cols)]
        # here we are just creating a new matrix with the number of rows and columns swapped
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
                # here we are just swapping the rows and columns of the original matrix and storing it in the result matrix
        return result


sol = Solution()

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.transpose(matrix1))