def calculate_distance(first, second):
    distance = (second[0]-first[0])**2+(second[1]-first[1])**2
    return distance**0.5


if __name__ =='__main__':
    point1 = [0,0]
    point2 = [3,4]
    print(calculate_distance(point1,point2))
    print(calculate_distance((6,4),(2,1)))
