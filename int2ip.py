def int2ip(i_ip):
    tmp = hex(i_ip)[2:]
    res = map(lambda x: str( int(tmp[x]+tmp[x+1],16)), range(0,len(tmp),2) )
    return '.'.join(res)

if __name__ == '__main__':
    print(int2ip(2149583361))
    print(int2ip(4294967295))
