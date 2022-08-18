def enlarge(image):
    result = [[]]
    for index, line in enumerate(image):
        if index:
            result.append([])
        for elem in line:
            result[index].append(elem*2)
        result[index] = ''.join(result[index])
    for line in range(len(result)):
        result.append(result.pop(0))
        result.append(result[-1])
    return '\n'.join(result)

print(enlarge(['@']))
print(enlarge(['****',
              '*  *',
              '*  *',
              '****']))
