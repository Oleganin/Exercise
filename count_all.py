def count_all(ls):
    d = {}
    for x in ls:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d


print(count_all(['cat', 'dog', 'cat']))

print(count_all('hello'))

print(count_all('*' * 20))
