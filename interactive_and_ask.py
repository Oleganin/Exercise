from functools import wraps

def interactive(text):
    def wrapped(function):
        function.__doc__ = text
        @wraps(function)
        def inner():
            print(function.__doc__)
            tmp = {}
            for el in function.__code__.co_varnames:
                tmp.setdefault(el, input(function.__annotations__[el]))
            return function(**tmp)
        return inner
    return wrapped

def ask(arg, text):
    def wrapped(func):
        @wraps(func)
        def inner():
            func.__annotations__.setdefault(arg, text)
            return func
        return inner()
    return wrapped

if __name__ == '__main__':

    @interactive('Calculator')
    @ask('x', 'Enter first number: ')
    @ask('y', 'Enter second number: ')
    def calc(x,y):
        return int(x) + int(y)

    print(calc())
