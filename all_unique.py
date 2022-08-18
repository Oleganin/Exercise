def all_unique(x):
    return len(set(x)) == len(x)

if __name__ == '__main__':
    a = [all_unique(e) for e in ('cat',[1,2,3],[1,2,1],'coc')]
    print(a == [True, True, False, False])
