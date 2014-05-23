START = 1
END = 15

def isMultipleofn(i, n):
   return i % n == 0

i = START
while i <= END:
   if(isMultipleofn(i, 15)): # you could just check it here
      print("FizzBuzz")
   elif(isMultipleofn(i, 3)):
      print("Fizz")
   elif(isMultipleofn(i, 5)):
      print("Buzz")
   else:
      print(i)
   i += 1 
 

def getMultiples(n1, n2, d1, d2):
   x, y = n % d1 ==0, n % d2 == 0
   p = []
   while n1 <= n2:
       if (x,y) == (True, True):    
           p.append(n)
    return p
           
print(sum(range(3, 100, 3) + range (5, 100, 5 ) - range(15, 100, 15)))
