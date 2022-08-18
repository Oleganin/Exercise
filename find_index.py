def find_index(element, elements):
    for index,elem in enumerate(elements):
        if elem == element:
            return index
    else:
        return None

