def diff_keys(old_dict, new_dict):
    return {'kept': old_dict.keys() & new_dict.keys(),
            'added': new_dict.keys() - old_dict.keys(),
            'removed': old_dict.keys() - new_dict.keys()
            }

if __name__ == '__main__':

    print(diff_keys({'name': 'Bob', 'age':42},{}) ==
          {'kept': set(), 'added': set(), 'removed': {'name', 'age'}})
    print(diff_keys({}, {'name': 'Bob', 'age':42}) ==
          {'kept': set(), 'added': {'name', 'age'}, 'removed': set()})
    print(diff_keys({'a': 2}, {'a': 1}) ==
          {'kept': {'a'}, 'added': set(), 'removed': set()})
