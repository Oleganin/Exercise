import math
def make_rational(numer, denom):
    if denom == 0:
        raise ZeroDivisionError('denom can not be zero')
    return {'numer': numer, 'denom': denom}

def get_numer(rational):
    rational = rat_normal(rational)
    return rational['numer']

def get_denom(rational):
    rational = rat_normal(rational)
    return rational['denom']

def add(rat1, rat2):
    rat1_numer = multiply_numer_by_denom(rat1, rat2)
    rat2_numer = multiply_numer_by_denom(rat2, rat1)
    commom_denom = common_denom(rat1, rat2)
    res_numer = rat1_numer + rat2_numer
    return rat_normal(make_rational(res_numer,commom_denom))

def sub(rat1,rat2):
    rat1_numer = multiply_numer_by_denom(rat1, rat2)
    rat2_numer = multiply_numer_by_denom(rat2, rat1)
    commom_denom = common_denom(rat1, rat2)
    res_numer = rat1_numer - rat2_numer
    return rat_normal(make_rational(res_numer,commom_denom))

def rat_to_string(rational):
    return f'{get_numer(rational)}/{get_denom(rational)}'

def rat_normal(rational):
    numer = get_origin_numer(rational)
    denom = get_origin_denom(rational)
    common = math.gcd(numer, denom)
    return make_rational(int(numer/common), int(denom/common))

def common_denom(rat1, rat2):
    return get_denom(rat1) * get_denom(rat2)

def multiply_numer_by_denom(rat1, rat2):
    return get_numer(rat1) * get_denom(rat2)

def get_origin_numer(rational):
    return rational['numer']

def get_origin_denom(rational):
    return rational['denom']

if __name__ == '__main__':
    rat1 = make_rational(3,9)
    print(get_numer(rat1))
    print(get_denom(rat1))
    rat2 = make_rational(10,3)
    rat3 = add(rat1, rat2)
    print(rat_to_string(rat3))
    rat4 = sub(rat1, rat2)
    print(rat_to_string(rat4))
