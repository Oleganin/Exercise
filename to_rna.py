def to_rna(dna):
    algor = dict(G='C', C='G',T='A',A='U')
    rna = ''
    for x in dna:
        rna += algor[x]
    return rna

if __name__ == '__main__':
    print(to_rna('ACGTGGTCTTAA'))
    print(to_rna('ACGTGGTCTTAA')  == 'UGCACCAGAAUU')
