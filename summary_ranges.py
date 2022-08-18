def summary_ranges(seq):
    if len(seq) <= 1:
        return []
    else:
        result = [[seq[0]]]
        count = 0
        for index in range(1,len(seq)):
            if seq[index] == result[-1][-1]+1:
                result[-1].append(seq[index])
            else:
                result.append([seq[index]])
        result = list(f'{line[0]}->{line[-1]}' for line in result
                       if len(line) > 1)
        return result


print(summary_ranges([]))
print(summary_ranges([1]))
print(summary_ranges([1,2,3]))
print(summary_ranges([0,1,2,4,5,7]))
print(summary_ranges([110,111,112,111,-5,-4,-2,-3,-4,-5]))
print(summary_ranges([6,0,1,2,3,4,5,7]))
