def flatten(args):
    res = []
    for arg in args:
        if isinstance(arg, list):
            res.extend(flatten(arg))
        else:
            res.append(arg)
    return res

if __name__ == '__main__':
    print(flatten([]))
    print(flatten([2,[3,5],[[4,3],2]]))
