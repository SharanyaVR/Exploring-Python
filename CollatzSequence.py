def getNextNumber(n):
    if n % 2 == 0:
       return n // 2
    return n * 3 + 1

def collatzsequence(n):
    p = []
    while n != 4:
        p.append(n)
        n = getNextNumber(n)
    p.extend([4, 2, 1])
    return p

def collatzSequenceR(n):
    if n == 4: 
        return [4, 2, 1]
    if n % 2 == 0:
        return [n] + collatzSequence(n // 2)
    return [n] + collatzSequence(3 * n + 1)

def largestPow2inCollatz(n):
    lastOdd = 0
    inp = n
    while n != 4:
        if n % 2 == 0:
            n //= 2
        else:
            lastOdd = n
            n = 3 * n + 1
        if lastOdd == 0:
            return inp
        return 3 * lastOdd + 1



def isPowerof2(n):
    if n == 1: 
        return True
    if n <= 0:
        return False
    if n % 2 == 1:
        return False
    isPowerof2(n//2)

import sys
large = 0
for i in collatzsequence(83):
    print(i)
    if(isPowerof2(i)):
        if( large < i):
            large = i
print(large)
