def rgb2hex(r:int=0,g:int=0,b:int=0)->str:
    from operator import add
    from functools import reduce
    tmp = lambda x: '0'+x[2:] if len(x)<4 else x[2:]
    res = map(tmp, map(hex,(r,g,b)))
    return reduce(add, res, '#')
    

if __name__ == '__main__':
    print(rgb2hex(36,171,0) == '#24ab00')
    print(rgb2hex(r=36,g=171,b=0) == '#24ab00')
