def ichunks(length, iseq):
    iseq = iter(iseq)
    try:
        while iseq:
            ilist = []
            for index in range(length):
                ilist.append(iseq.__next__())
            yield ilist
    except StopIteration:
        pass
        '''for index in range(lenght):
            x = list(elem)
        yield x'''

for x in list(ichunks(2, [1,2,3,4,5])):
    print(x)
print(list(ichunks(2, [1,2,3,4,5])))

'''import intertools
list(intertools.islice(intertools.count(), 10000, 10005))
stream = ichunks(3, intertools.count())
list(intertools(stram, 10000,10002))'''
