from find_index import find_index

def find_longest_length(text):
    l = [text[0]]
    count = 0
    for i,ch in enumerate(text[1:]):
        if ch in l[count]:
            if l[count][-1] == ch:
                count+=1
                l.append(text[i+1])
            else:
                index = find_index(ch, l[count])+1+sum(len(l[x]) for x in range(len(l)-1))
                l.append(text[index:i+2])
                count+=1
        else:
            l[count] += ch
    #print(l)
    return max(map(len, l))

def test(text):
    print(f'In "{text}" letter sequence is "{find_longest_length(text)}"')

if __name__ == '__main__':
      test_text = ['abcdeef', 'jabjcdel', 'qweqrty', 'aaabbcsdf', 'ffffffvvvvnvdsfg5rfg']
      for x in test_text:
          test(x)
