def greet(name, *args)->str:
    '''return greeting string enumeration arguments'''
    result = ''
    for word in (name,) + args:
        if result:
            result = ' and '.join([result, word])
        else:
            result = 'Hello, '+word
    return result+'!'


if __name__ == '__main__':
    print(greet('Bob'))
    print(greet('Moe','Marry'))
    print(greet(*'ABC'))
