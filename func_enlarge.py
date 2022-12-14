def enlarge(args):
    m_d = curry(map)(dup)
    l_m_d = compose(''.join)(m_d)
    arg = curry(map)(l_m_d)(args)
    j_p = compose('\n'.join)(pair)
    m_j_p = curry(map)(j_p)(arg)
    return '\n'.join(m_j_p)


def compose(fn1):
    def wrapped(fn2):
        def inner(*arg):
            return(fn1(fn2(*arg)))
        return inner
    return wrapped

def curry(func):
    def cacher1(arg):
        def cacher2(*args):
            return func(arg, *args)
        return cacher2
    return cacher1

pair = lambda x: [x,x]
dup = lambda x: x + x

if __name__ == '__main__':
     glider = [' * ', '  *','***']

     def display(image):
         for line in image:
             print(line)

     display(glider)
     print('-'*10)
     print(enlarge(glider))
