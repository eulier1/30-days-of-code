n = int(input())

for i in range(0,n):
    value = str(input())
    odd = ''
    even = ''
    for j in range(0,len(value)):
        if j % 2 > 0:
            even += value[j]
        else:
            odd += value[j]
    print("{} {}".format(odd, even))
