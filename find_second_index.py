from find_index import find_index as find_index

def find_second_index(element, elements):
    ie = iter(elements)
    index = 0
    for x in range(2):
        k = find_index(element, ie)
        if k is not None:
            index +=k
        else:
            return None
    return index+1

