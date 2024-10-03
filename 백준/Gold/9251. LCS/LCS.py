str_a = ' ' + input()
str_b = ' ' + input()

N = len(str_a)
M = len(str_b)

matrix = [[0 for _ in range(N)] for _ in range(M)]
# LCS
for i in range(1, M):
    for j in range(1, N):
        if str_a[j] == str_b[i]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])