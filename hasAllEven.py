def hasAllEven(x):
    while x > 0:
       if x % 2 == 1:
          return False
       x = x // 10
    return True

def isPerfectSquare(x):
   c = 1
   while c * c < x:
      c +=1
   return c * c == x

def isArmStrong(x):
   tot = 0 
   n = x
   while x > 0:
      r = x % 10
      tot += r * r * r
      x = x // 10
   if n == tot:
      return True

for n in range(46, 94, 2):
   d = n * n
   if(hasAllEven(d)):
     print(d)

print("check armstrong numbers")
print(isArmStrong(153))
print(isArmStrong(122))
