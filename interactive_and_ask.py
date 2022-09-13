from functools import wraps

def interactive(text):
    def wrapped(function):
        function.__doc__ = text
        @wraps(function)
        def inner():
            print(function.__doc__)
            return function(**function.__annotations__)
        return inner
    return wrapped

def ask(arg, text):
    def wrapped(func):
        @wraps(func)
        def inner():
            tmp = input(text)
            func.__annotations__.setdefault(arg, tmp)
            return func
        return inner()
    return wrapped

if __name__ == '__main__':

    @interactive('Calculator')
    @ask('x', 'Enter first number: ')
    @ask('y', 'Enter second number: ')
    def calc(x,y):
        return int(x) + int(y)
