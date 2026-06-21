A = [
# A  B  C  D  E  F
 [0, 1, 1, 0, 0, 0],  # A
 [1, 0, 0, 1, 1, 0],  # B
 [1, 0, 0, 0, 0, 1],  # C
 [0, 1, 0, 0, 0, 0],  # D
 [0, 1, 0, 0, 0, 0],  # E
 [0, 0, 1, 0, 0, 0]   # F
]

visited = [False] * len(A)
def dfs(matrix, start, visited ):
    n = len(matrix)

    if not visited[start]:
        print(start, end = " ")
        visited[start] = True

        for v in range(n):
            if matrix[start][v] == 1 and not visited[v]:
                dfs(matrix, v, visited)


dfs(A, 5, visited)
