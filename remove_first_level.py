def remove_first_level(tree, deep = 0, depth = 1):
    res = []
    for node in tree:
        if depth == deep:
            res.append(node)
        elif isinstance(node,list):
            deep +=1
            elem = remove_first_level(node, deep, depth)
            res.extend(elem)
            deep -=1
    return res

    
if __name__ == '__main__':
    tree1 = [[5], 1, [3,4]]
    print(remove_first_level(tree1))
    tree2 = [1,2, [3, 5], [[4,3], 2]]
    print(remove_first_level(tree2))
    print(remove_first_level(tree2, deep = 0, depth = 2))
