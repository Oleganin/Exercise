def triangle(pos):
    tri = [[]]
    if pos==0:
        tri[0].append(1)
    if pos:
        for line in range(pos):
            tri.append([1])
            for elem in range(len(tri[line])-1):
                tri[line+1].append(tri[line][elem]+tri[line][elem+1])
            tri[line+1].append(1)
    print(tri[pos])




def triangle_alt(pos):
    import math
    L = []
    print(list(enumerate(range(pos-1,-1,-1))))
    for k, n in enumerate(range(pos-1,-1,-1)):
        #for k in range(2):
        r = int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
        L.append(r)
        print(L, n, k, r)
    print(L)


if __name__ == '__main__':
    for x in range(10):
        triangle(x)

    for x in range(10):
        triangle_alt(x)
