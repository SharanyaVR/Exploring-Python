def isPowerof2(n):
    if n == 1: 
        return True
    if n % 2 == 1:
        return False
    print(n)
    return isPowerof2(n//2)

n = 14
print(isPowerof2(n))
