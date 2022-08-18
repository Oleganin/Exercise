def chunked(len_of_chunk, seq):
    chunks = []
    count = 0
    if len(seq)%len_of_chunk:
        it = len(seq)//len_of_chunk+1
    else:
        it = len(seq)//len_of_chunk
    for x in range(it):
        chunks.append(seq[count:len_of_chunk + count])
        count += len_of_chunk
    return chunks

def test(l):
    for x in l:
        len_of_chunk = x[0]
        seq = x[1]
        print(f'In "{seq}" length of chunk = {len_of_chunk}\nNow is -> {chunked(len_of_chunk, seq)}')
        print('-'*20)

if __name__=='__main__':
    L_test = ((2, ['a','b','c','d','e','g','h']),
        (3, ['a','b','c','d','e','g','h']),
        (2, ['a','b','c','d']),
        (3, ['a','b','c','d']),
        (3, 'foodar'),
        (10, (42,)))
    test(L_test)
