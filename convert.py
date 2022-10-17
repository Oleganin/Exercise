def convert(pair_list):
    result = {}
    for arg in pair_list:
        if isinstance(arg[-1] ,list):
            res = {arg[0]: convert(arg[-1])}
            result.update(res)
        else:
            result.update({arg[0]:arg[1]})
    return result


if __name__ == '__main__':
    print(convert([]))
    print(convert([('key2','value2'), ('key','value')]))
    print(convert([
        ('key',[('key2', 'anotherValue')]),
        ('key2','value2')
    ]))
