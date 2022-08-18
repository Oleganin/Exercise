def rpn_calc(seq):
    result = []
    for elem in seq:
        if type(elem) is int:
            result.append(elem)
        if elem == '+':
            result.append(result.pop(-2)+result.pop(-1))
        if elem == '-':
            result.append(result.pop(-2)-result.pop(-1))
        if elem == '*':
            result.append(result.pop(-2)*result.pop(-1))
        if elem == '/':
            tmp = result.pop(-2)/result.pop(-1)
            if tmp.is_integer():
                result.append(int(tmp))
            else:
                result.append(round(tmp,3))
    return result[-1]


L_test = ([1,2,'+',4,'*',3,'+'],
        [7,2,3,'*','-'],
        [2,4,'*',8,'+'],
        [3,2,'*',11,'-'],
        [2,5,'*',4,'+',3,2,'*',1,'+','/'],
        [7,2,3,'*','/']
          )

for x in L_test:
    print(f'{x} = {rpn_calc(x)}')
