def ip2int(s_ip):
    tmp = map( hex, map(int, s_ip.split('.')))
    return int(''.join(
        map(
            lambda x: '0'+x.split('x')[-1] if len(x)<4 else x.split('x')[-1], tmp
            )
        ),16)

if __name__ == '__main__':
    print(ip2int('128.32.10.1'))
    print(ip2int('255.255.255.255'))
