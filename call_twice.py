def call_twice(func, *args):
    return tuple(func(*args) for x in range(2))

if __name__ == '__main__':
    call_twice(input, 'Enter value: ')
    
