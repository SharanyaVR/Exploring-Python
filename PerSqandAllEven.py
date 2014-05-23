def isPerSqandAllEven():
  n = 1000
  flag = False
  while n < 9999:
   	c = 1 
        while c * c < x:
	      c += 1
        flag = c * c == x
	if flag :
	  while x > 0:
             if x % 2 == 1:
	        flag = False
             x = x // 10
  	  flag = True

print(isPerSqandAllEven())

