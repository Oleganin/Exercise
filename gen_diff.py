def gen_diff(first, second)->dict:
    '''function finds the difference between two dictionaries
     -> { 'key' : marker('added', 'deleted', 'changed', 'unchanged') }'''
    first_keys = set(first.keys())
    second_keys = set(second.keys())
    added = second_keys - first_keys
    deleted = first_keys - second_keys
    anther_keys = (first_keys | second_keys) ^ (added  | deleted)
    result = {}
    for keys in deleted, anther_keys, added:
        for key in keys:
            if key in added:
                result[key] = 'added'
            if key in deleted:
                result[key] = 'deleted'
            if key in anther_keys:
                if first[key] == second[key]:
                    result[key] = 'unchanged'
                else:
                    result[key] = 'changed'
    return result


if __name__ == '__main__':
    print(gen_diff({'one': 'eon', 'two':'two', 'four':True},
                   {'two':'own', 'zero':4, 'four':True}))
