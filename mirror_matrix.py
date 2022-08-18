def mirror_matrix(matrix):
    for line in matrix:
        line[len(line)//2+1:] = line[len(line)//2-1::-1]



l1 = [
    [1,2,3],
    [4,5,6]
    ]

l2 = [
    [11,12,13,14,15,16],
    [21,22,23,24,25,26],
    [31,32,33,34,35,36],
    [41,42,43,44,45,46],
    [51,52,53,54,55,56],
    [61,62,63,64,65,66]
    ]

mirror_matrix(l1)
mirror_matrix(l2)

print(l1)
print(l2)
      
