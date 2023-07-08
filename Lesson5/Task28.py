def recursion_sum (a,b):
    if a == 0:
        return b
    return recursion_sum(a-1,b+1)