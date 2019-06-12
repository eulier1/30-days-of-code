from math import sqrt as sq

number = int(input())

for n in range(number):
    n = int(input())
    sqrt = int(sq(n))
    
    if n == 1:
        print("Not prime")
    elif n == 2:
        print("Prime")
    else:    
        for i in range(2, sqrt + 1):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
