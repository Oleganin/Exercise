def multiply(A, B):
    if len(A[0]) != len(B):
        return 'impossible'
    l = len(A)
    n = len(B[0])
    m = len(B)
    result = []
    for i in range(l):
        result.append([0])
        for j in range(n):
            if j != n-1:
                result[i].append(0)
            for r in range(m):
                result[i][j] += A[i][r]* B[r][j]
    return result



A = [[1,2],
     [3,2]]
B = [[3,2],
     [1,1]]
C = [
    [2,5],
    [6,7],
    [1,8]
    ]
D = [
    [1,2,1],
    [0,1,0]
    ]

E = [[3],
     [2],
     [0],
     [1]]
F = [[-1,1,0,2]]

G =[[1,4,3],[2,1,5],[3,2,1]]
H = [[5,2,1],[4,3,2],[2,1,5]]
print(multiply(A,B))
print(multiply(C,D))
print(multiply(A,C))
print(multiply(A,D))
print(multiply(B,C))
print(multiply(B,D))
print(multiply(E,F))
print(multiply(G,H))
