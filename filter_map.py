def filter_map(func, args):
    result = []
    for arg in args:
        res = func(arg)
        if res[0]:
            result.append(res[-1])  
    return result

if __name__ == '__main__':
    def make_stars(x):
        if x > 0:
            return True, '*'*x
        return False, ''

    for s in filter_map(make_stars,[1,0,5,-5,2]):
        print(s)
