def collect_indexes(x):
    d = {}
    for key, value in enumerate(x):
        d.setdefault(value, []).append(key)
    return d


if __name__ == '__main__':
    t = collect_indexes('hello')
    print(t)
