def keep_truthful(*args):
    import operator
    return filter(operator.truth, *args)

if __name__ == '__main__':
    print(list(keep_truthful([True,False,'','foo'])))
