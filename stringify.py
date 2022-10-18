def stringify(value, replacer = ' ', spaces_count = 1):
    result = ''
    if isinstance(value, dict):
        result +='{'
        start = f'\n{replacer*(spaces_count)}'
        spaces_count+=1
        for key in value:
            result += f'{start}{key}: {stringify(value[key],replacer,spaces_count)}'
        spaces_count-=1
        result += f'\n{replacer*(spaces_count)}'
        result += '}'
    else:
        result += str(value)
    return result

data = {'hello':'worls', 'is':True, 'nested':{'count':5}}
print(stringify(data))
print(stringify(data, '|-', 2))
