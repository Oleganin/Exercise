def updated(dic, **kwargs):
    return {**dic,**kwargs}


if __name__ == '__main__':
    d = {'a':1, 'b':False}
    print(updated(d, a=2, b =True, c=None))
    print(d)
    print(updated(d)==d)
    print(updated(d) is d)
