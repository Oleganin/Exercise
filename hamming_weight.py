def hamming_weight(number):
    return bin(number).count('1')

if __name__ == '__main__':
    for x in range(110):
        print(f'{x} weight {hamming_weight(x)}')
