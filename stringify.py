def stringify(value, replacer = ' ', spaces_count = 1):
    def create_string(value, lvl=1):
        res = ''
        if isinstance(value, dict):
            res +='{'
            start = f'\n{replacer*(spaces_count)*lvl}'
            lvl+=1
            for key in value:
                res += f'{start}{key}: {create_string(value[key],lvl)}'
            lvl-=1
            res += f'\n{replacer*(spaces_count)*(lvl-1)}'
            res += '}'
        else:
            res += str(value)
        return res
    result = create_string(value)
    print(result)

if  __name__ == '__main__':
    stringify('hello')
    stringify(True)
    stringify(5)
    data = {'hello':'world', 'is':True, 'nested':{'count':5}}
    stringify(data)
    stringify(data, '|-', 2)
    data2 = {'hello':'world', 'is':True, 'nested':{'count':5}, 'list':[1,2,3]}
    stringify(data2)
    stringify(data2, '|_', 3)
