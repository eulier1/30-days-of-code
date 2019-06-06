/** 
* Consecutives ones in a binary number from a decimal
* input : int() base 10
* output: int()
*/
def consecutives_one (num):
    counter = 0
    max_value = 0

    while num > 0:
        if num % 2 == 1:
            counter += 1
            if counter > max_value:
                max_value = counter
        else:
            counter = 0
    
        num //= 2
    
return max_value
