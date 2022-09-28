def make_decart_point(x,y):
    return {'x':x, 'y':y}

def get_x(point):
    return point['x']

def get_y(point):
    return point['y']

def make_segment(point1, point2):
    return {'begin_point':point1, 'end_point':point2}

def get_mid_point_of_segment(segment):
    x1, y1 = get_x(segment['begin_point']), get_y(segment['begin_point'])
    x2, y2 = get_x(segment['end_point']), get_y(segment['end_point'])
    return make_decart_point((x1+x2)/2, (y1+y2)/2)

if __name__ == '__main__':
    segment = make_segment(make_decart_point(3,2), make_decart_point(0,0))
    print(get_mid_point_of_segment(segment))
