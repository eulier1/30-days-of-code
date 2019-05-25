n = int(input())
result = ''
for value in reversed(str(input()).split()):
    result += value + " "
print(result)
