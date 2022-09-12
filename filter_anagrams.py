def filter_anagrams(anam, *args):
    return filter(lambda x: set(anam)==set(x) and len(anam)==len(x),*args)

if __name__ == '__main__':
    print(list(filter_anagrams('abba', ['aabb','abcd', 'bbaa', 'dada'])))
    print(list(filter_anagrams('racer', ['crazer','carer', 'caers', 'racer'])))
    print(list(filter_anagrams('laser', ['lazing','lazy', 'lacer'])))
    print(list(filter_anagrams([1,2], [[2,1],[2,2], [1,2]])))
