def make_decart_point(x,y):
    return {'x':x, 'y':y}

def get_x(point):
    return point['x']

def get_y(point):
    return point['y']

def make_rectangle(point, width, height):
    return {'point': point, 'width':width, 'height':height}

def get_start_point(rectangle):
    return rectangle['point']

def get_width(rectangle):
    return rectangle['width']

def get_height(ractangle):
    return rectangle['height']

def contains_origin(rectangle):
    l_u_p = get_start_point(rectangle)
    l_d_p = make_decart_point(get_x(l_u_p),get_y(l_u_p) - get_height(rectangle))
    r_u_p = make_decart_point(get_x(l_u_p) + get_width(rectangle),get_y(l_u_p))
    r_d_p = make_decart_point(get_x(l_u_p) + get_width(rectangle),get_y(l_u_p) - get_height(rectangle))
    quadr = map(get_quadrant, (l_u_p, l_d_p, r_u_p, r_d_p))
    return set(quadr) == set(['I','II','III', 'IV'])
    

def get_quadrant(point):
     x = get_x(point)
     y = get_y(point)
     res = ''
     if x > 0 and y > 0:
         res = 'I'
     elif x < 0 and y > 0:
         res = 'II'
     elif x < 0 and y < 0:
         res = 'III'
     elif x > 0 and y < 0:
         res = 'IV'
     else:
         res = False
     return res


if __name__ == '__main__':
    p = make_decart_point(0,1)
    rectangle = make_rectangle(p, 4, 5)
    print(contains_origin(rectangle))
    rectangle2 = make_rectangle(make_decart_point(-4,3), 5, 4)
    print(contains_origin(rectangle2))
