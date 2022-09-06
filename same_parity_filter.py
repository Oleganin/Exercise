def same_parity_filter(args):
    return list(filter(lambda x: not x % args[0], args))

if __name__ == '__main__':
    print(same_parity_filter([]))
    print(same_parity_filter([2,0,1,-3,10,-2]))
    print(same_parity_filter([-1,0,1,-3,10,-2]))
