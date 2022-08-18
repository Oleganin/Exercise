def is_continuous_sequence(seq):
    if len(seq) < 2:
        return False
    for index in range(len(seq)-1):
        if seq[index] != seq[index+1] - 1:
            return False
    else:
        return True

def test(seq):
    print(f'{seq} continuous is {is_continuous_sequence(seq)}')

if __name__ == '__main__':
    L = [[10,11,12,13],[-5,-4,-3],[10,11,12,14,15],[1,2,2,3],[7],[]]
    for x in L:
        test(x)
