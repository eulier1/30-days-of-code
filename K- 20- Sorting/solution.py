def bubbleSort (a):
    swaps = 0;
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    return swaps

print ("Array is sorted in {} swaps.".format(bubbleSort(a)))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[-1]))
