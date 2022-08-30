def abs_sum(*args):
    return sum(map(abs,*args))

if __name__ == '__main__':
    print(abs_sum([-3,7]))
    print(abs_sum([]))
    print(abs_sum([42]))
