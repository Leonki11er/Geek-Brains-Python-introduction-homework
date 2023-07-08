def recursion_pow (a,b):
    if b == 0:
        return 1
    return a  * recursion_pow(a,b-1)