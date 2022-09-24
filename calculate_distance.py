def calculate_distance(first, second):
    x1, y1 = first
    x2,y2 = second
    distance = (x2-x1)**2+(y2-y1)**2
    return distance**0.5


if __name__ =='__main__':
    point1 = [0,0]
    point2 = [3,4]
    print(calculate_distance(point1,point2))
    print(calculate_distance((6,4),(2,1)))
