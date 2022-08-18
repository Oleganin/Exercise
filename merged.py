def merged(first, second):
    a = {}
    for j in first,second:
        for x in j:
            a.setdefault(x, set()).add(j[x])
    return a

if __name__ == '__main__':
    print(merged({},{}) == {})
    print(merged({'a':1, 'b':2},{'b':10,'c':100}) ==
          {'a':{1},'b':{2,10},'c':{100}})
