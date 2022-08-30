def partial_apply(func, *args):
    def inner(x):
        return func(*args,x)
    return inner

if __name__ == '__main__':
    def greet(name, surname):
        return f'Hello, {name} {surname}!'

    f = partial_apply(greet, 'Dorian')
    print(f('Grey'))
