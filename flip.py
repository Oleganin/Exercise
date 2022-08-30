def flip(func):
    def inner(*args):
        return func(*args[::-1])
    return inner

if __name__ == '__main__':
    def greet(name, surname):
        return f'Hello, {name} {surname}!'

    f = flip(greet)
    print(f('Christian','Teodor'))
