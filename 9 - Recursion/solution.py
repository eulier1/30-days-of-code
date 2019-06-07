# Anatomy of Recursion 
# 1. Define a base code (or stop condition)
# 2. Call a function inside
# 3. Modify the parameters passing (otherwise, you'll end up with an infinite loop)

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)
