def is_valid_ipv6(ipv6):
    tmp = ipv6.split(':')
    if len(tmp) > 8 or (len(tmp)<8 and not '' in tmp):
        return False
    from string import hexdigits
    df = lambda x: True if x != '' else False
    rtmp = filter(df , tmp)
    r = [all(map(lambda x: x in hexdigits, xt)) for xt in rtmp]
    return all(r)



if __name__ == '__main__':
    print(is_valid_ipv6('10:d3:2d06:24:400c:5EE0:be:3d'))
    print(is_valid_ipv6('::1'))
    print(is_valid_ipv6('2607:G8B0:4010:801::1004'))
    print(is_valid_ipv6('2.001::'))
