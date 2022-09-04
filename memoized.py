def memoized(func):
    res = {}
    def inner(arg):
        if arg not in res:
            res[arg] = func(arg)
        return res[arg]
    return inner


if __name__ == '__main__':
    @memoized
    def f(x):
        print('Calculating..')
        return x*10

    for a in [1,1,42,42,4,1,4]:
        print(f(a))
