def memoizing(max_mem):
    from functools import wraps
    res = {}
    pos = []
    def wrapped(func):
        @wraps(func)
        def inner(arg):
            if len(pos)==max_mem+1:
                tmp = pos.pop(0)
                del res[tmp]
            if arg not in pos:
                pos.append(arg)
            if arg not in res:
                res[arg] = func(arg)
            return res[arg]
        return inner
    return wrapped


if __name__ == '__main__':
    @memoizing(3)
    def f(x):
        print('Calculating..')
        return x*10

    for a in [1,1,2,3,4,1,4]:
        print(f(a))
