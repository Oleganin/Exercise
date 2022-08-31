def make_module(step =1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}


if __name__ == '__main__':
    m = make_module()
    print(m['inc'](10))
    print(m['dec'](20))
    m2 = make_module(step=2)
    m = make_module()
    print(m2['inc'](1))
