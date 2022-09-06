def compose(funcF, funcG):
    def wrapper(arg):
        return funcF(funcG(arg))
    return wrapper

if __name__ == '__main__':
    def mul3(x):
        return x*3

    def add5(x):
        return x+5

    print(compose(mul3,add5)(1))
    print(compose(add5,mul3)(1))
    print(compose(mul3,str)(1))
    print(compose(str,mul3)(1))
