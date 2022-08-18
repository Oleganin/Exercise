def compare_version(version1, version2):
    num1 = version1.split('.')
    num2 = version2.split('.')
    for i in range(2):
        if int(num1[i]) > int(num2[i]):
            return 1
        elif int(num1[i]) < int(num2[i]):
            return -1
        elif int(num1[i]) == int(num2[i]):
            if i == 0:
                continue
            else:
                return 0

print(compare_version('0.1','0.2'))
print(compare_version('0.2','0.1'))
print(compare_version('4.2','4.2'))
