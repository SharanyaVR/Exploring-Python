def getFactors(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return l

def aliquot(n):
    return sum(getFactors(n))

def areAmicablePair(n1, n2):
   return aliquot(n1) == n2 and aliquot(n2) == n1

def getAmicablePairs(n1, n2):
    amicablepairs = dict()
    for i in range(n1, n2):
        for j in range(n1, n2):
            if areAmicablePair(i, j):
                    amicablepairs[i] = j
            j += 1
        i += 1
    return amicablepairs

n1 = 200
n2 = 300
amicablepairs = getAmicablePairs(n1, n2)
print(amicablepairs)
