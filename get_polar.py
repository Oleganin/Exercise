import math

def make_polar_point(x,y):
    return {'angle':math.atan2(y,x),
            'radius':math.sqrt(x**2+y**2)
            }

def get_x(point):
    angle = point['angle']
    radius = point['radius']
    return round(radius*math.cos(angle),3)

def get_y(point):
    angle = point['angle']
    radius = point['radius']
    return round(radius*math.sin(angle), 3)

if __name__ == '__main__':
    x = 4
    y = 8
    point = make_polar_point(x,y)
    print(get_x(point))
    print(get_y(point))
