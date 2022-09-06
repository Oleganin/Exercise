def decode(NRZI):
    res = []
    bs = '0'
    for sign in NRZI:
        if sign == '|':
            bs = '1'
            continue
        res.append(bs)
        bs = '0'
    return ''.join(res)

if __name__ =='__main__':
    print(decode('_|ˉ|____|ˉ|__|ˉˉˉ'))
    print(decode('|ˉ|___|ˉˉˉˉˉ|___|ˉ|_|ˉ'))
    print(decode('ˉ|___|ˉˉˉˉˉ|___|ˉ|_|ˉ'))
