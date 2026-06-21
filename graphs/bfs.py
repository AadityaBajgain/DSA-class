from collections import deque

A = [
# A  B  C  D  E  F
 [0, 1, 1, 0, 0, 0],  # A
 [1, 0, 0, 1, 1, 0],  # B
 [1, 0, 0, 0, 0, 1],  # C
 [0, 1, 0, 0, 0, 0],  # D
 [0, 1, 0, 0, 0, 0],  # E
 [0, 0, 1, 0, 0, 0]   # F
]

def BFS(matrix, start):
    
    n = len(matrix)
    visited = [False]  * n
    
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        print(u, end=" ")
        
        for v in range(n):
            if matrix[u][v] == 1 and not visited[v]:
                visited[v] = True
                q.append(v)
    print("\n")
BFS(A, 3)
BFS(A, 5)