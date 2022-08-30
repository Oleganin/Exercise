def walk(dic, args):
    import functools, operator
    return functools.reduce(operator.getitem, args, dic)


if __name__ == '__main__':
    print(walk({'a':{7:{'b':42}}}, ['a',7,'b']))
    print(walk({'a':{7:{'b':42}}}, ['a',7]))
    print(walk({'a':{7:{'b':42}}}, ['a']))
