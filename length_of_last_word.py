def length_of_last_word(words):
    if words:
        return len(words.split()[-1])
    else:
        return 0


def test(l):
    for x in l:
        print(f'"{x}" lenght of last word is: {length_of_last_word(x)}')

if __name__ == '__main__':
    L_test = ('', 'man in Black', 'hello, world', 'hello\t\nworld')
    test(L_test)
