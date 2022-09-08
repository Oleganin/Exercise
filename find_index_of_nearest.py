def find_index_of_nearest(num, *args):
    if len(*args) == 0:
        return None
    res = []
    for y in args[-1]:
        res.append(abs(num-y))
    return res.index(min(res))

if __name__ == '__main__':
    print(find_index_of_nearest(2,[]) is None)
    print(find_index_of_nearest(0,[15,10,3,4]))
    print(find_index_of_nearest(4,[7,5,3,2]))
    print(find_index_of_nearest(4,[7,5,4,4,3]))
