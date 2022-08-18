def sum_of_intervals(seqs):
    seqs = sorted(seqs)
    tmp = 0
    result = []
    for seq in seqs:
        for element in seq:
            if element >= tmp and element == seq[0]:
                tmp = element
                continue
            if element >= tmp:
                result.append(element - tmp)
                tmp = element
    return sum(result)

def test(l):
    for x in l:
        print(x, 'sum of intervals is',sum_of_intervals(x))

if __name__=='__main__':
    L_test = [[[1,1]],
              [[1,2],[50,100],[60,70]],
              [[1,2],[5,10]],
              [[50,100],[1,15],[30,70],[12,15]]
              ]
    test(L_test)
