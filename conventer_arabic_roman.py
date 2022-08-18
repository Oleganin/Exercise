def to_roman(arabic_int)->str:
    '''Convert Arabic numerals 1...3999 in Roman numerals'''
    if arabic_int > 3999 or arabic_int < 1:
        raise TypeError('Check the data')
    roman_dict = {1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}
    roman_ints = iter(roman_dict)
    roman_int = next(roman_ints)
    result = ''
    i = 0
    while arabic_int > 0:
        if arabic_int//roman_int:
            i+=1
            if i == 4:
                if len(result)>3 and result[-4] == roman_dict[5*roman_int]:
                    result = result[:-4]
                    result += roman_dict[roman_int]+roman_dict[10*roman_int]
                else:
                    result = result[:-3]
                    result += roman_dict[roman_int]+roman_dict[5*roman_int]
                arabic_int -= roman_int
                i = 0
            else:
                result += roman_dict[roman_int]
                arabic_int -= roman_int
        else:
            roman_int = next(roman_ints)
            i = 0
    return result

def to_arabic(roman_int)->int:
    result = []
    arabic_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    index = 0
    i = 0
    while index < len(roman_int):
        if roman_int[index] in arabic_dict:
            if len(result) and result[-1] < arabic_dict[roman_int[index]]:
                cnt = arabic_dict[roman_int[index]] - result[-1]
                if cnt/result[-1] in (4,9) :
                    result[-1] = cnt
                else:
                   return False 
            else:
                result.append(arabic_dict[roman_int[index]])
            if len(result)==1 and result[-1] == arabic_dict[roman_int[index]]:
                i+=1
            else:
                i = 0
        else:
            return False
        if i == 4:
            return False
        index += 1
    return sum(result)


def test(ran=20):
    for x in range(1,ran+1):
        k = to_roman(x)
        print(f'{x} -> roman: {k} -> arabic: {to_arabic(k)}')

if __name__ == '__main__':
    print('ROMAN'.center(20))
    print(to_roman(1))
    print(to_roman(59))
    print(to_roman(3000))
    print('-'*20)
    print('ARABIC'.center(20))
    print(to_arabic('I'))
    print(to_arabic('LIX'))
    print(to_arabic('MMM'))
    print(to_arabic('VX'))
    print(to_arabic('IIII'))
    print('-'*20)
    test(50)
