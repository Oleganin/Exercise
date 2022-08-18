def transposed(seqs):
    len_of_column = min(len(seq) for seq in seqs)
    len_of_element = len(seqs)
    l = []
    for seq in range(len_of_column):
        l.append([])
        for index in range(len_of_element):
            l[seq].append(seqs[index][seq])
    return l
    

def test(seqs):
    for seq in range(len(seqs)):
        input_list = convert(seqs[seq])
        output_list = convert(transposed(seqs[seq]))
        for x in input_list:
            print(x[1:-1].replace(',',' ').center(20))
        print('/\\'.center(20))
        print('transposed in'.center(20))
        print('\\/'.center(20))
        for x in output_list:
            print(x[1:-1].replace(',',' ').center(20))
        print('-'*20)

def convert(l):
    return [str(x) for x in l]
        

if __name__ == '__main__':

     L = ( [[1]], [[1,2],[3,4]], [[1,2],[3,4],[5,6]],
          [[1,3,5],[2,4,5]], [[1,2,3],[4,5,6],[7,8,9]] )
     test(L)
     print(transposed(transposed([[1,2]])) == [[1,2]])
