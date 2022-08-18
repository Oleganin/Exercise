def scrabble(letters, word):
    import collections
    word = word.lower()
    cnt = collections.Counter(letters.lower())
    cnt.subtract(word)
    for letter in cnt.values():
        if letter < 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print(scrabble('rkodlw', 'world'))
    print(scrabble('avj', 'java'))
    print(scrabble('avjafff', 'java'))
    print(scrabble('', 'helxet'))
    print(scrabble('scriptingjava', 'JavaScript'))
