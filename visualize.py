def visualize(cen_list, bar_char = '$'):
    if 'collections' in dir():
        cnt = collections.Counter(cen_list)
    else:
        import collections
        cnt = collections.Counter(cen_list)
        
    list_keys = sorted(list(cnt.keys()))
    max_len = max(cnt.values())
    count_values = []
    for x in list_keys:
        b = (max_len-cnt[x])*[' ']
        count_values.append([str(x)]+cnt[x]*[bar_char]+[str(cnt[x])]+b)
    
    max_len_cent = max(len(str(max(cnt.keys()))), len(str(max(cnt.values()))))
    result = ''
    
    for i in range(len(count_values[-1])):
        result += '\n'
        if i == len(count_values[-1])-1:
            g = '-'*(len(result.split('\n')[-2])-1)+'\n'
            result += g
        for j in range(len(count_values)):
           s = count_values[j][-1-i]
           if s in (' ', bar_char):
               s = max_len_cent*s
           elif len(s) < max_len_cent:
               s = ' '*(max_len_cent - len(s)) + s
           result += s + ' '
           
    return result


print(visualize((10,
                 1,1,1,1,1,
                 20,20,20,
                 2,2,2,2,
                 3,3,3,3)))

print(visualize((10,
                 1,1,1,1,1,
                 20,20,20,
                 2,2,2,2,
                 3,3,3,3), bar_char='₴'))

print(visualize((10,
                 1,1,1,1,1,
                 20,20,20,
                 2,2,2,2,
                 3,3,3,3,
                 100,100,
                 50,50,50,50,50,50,50,50,50,50)))

print(visualize((10,
                 1,1,1,1,1,
                 20,20,20,
                 2,2,2,2,
                 3,3,3,3,
                 1000,1000,1000,1000,1000,1000,1000,1000)))
      
