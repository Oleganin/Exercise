def histo(*args, bar_char = '#', min_value=-1, max_value=-1):
    if args[0]==[] and (min_value== -1 or max_value== -1):
        return '|'
    if max_value == -1:
        max_value = max(*args)
    if min_value == -1:
        min_value = min(*args)
    from collections import Counter
    tmp = Counter(*args)
    res = map(lambda x: str(x)+'|'+bar_char*tmp[x],range(min_value, max_value+1))
    return '\n'.join(res)

if __name__ == '__main__':
    print(histo([1, 1, 3, 4, 5]))
    print(histo([1, 1, 3, 4, 5], bar_char = '*'))
    print(histo([1, 1, 3, 4, 5], min_value = 3, max_value = 4))
    print(histo([], min_value = 1, max_value = 5))
