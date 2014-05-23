SCREEN_WIDTH = 45

def endPattern(i):
   return ' '

def repeatPattern(i):   
   repeatPattern = '**'
   return ' *' * i

def startPattern(i):
   return '*'

def leadingSpaces(i):
   offset = SCREEN_WIDTH // 2
   return ' ' * (offset - i)

def line(i):
   return leadingSpaces(i) + startPattern(i) + repeatPattern(i) + endPattern(i)

def pyramid(rows):
   l = []
   for i in range(rows):
      l.append(line(i))
   return l

prevline = []
def lineForPascal(i):
    currentline = []
    if i == 0:
       currentline = [1]
       return currentline
    if i == 1:
        currentline = [1,1]
        prevline = currentline
        return currentline
    currentline.append(1)
    c = 1
    while c < len(prevline):
        currentline.append(prevline[c] + prevline[c-1])
    currentline.append(1)
    prevline = currentline
    return currentline
    
def pyramidPascal(rows):
    l = []
    cl = []
    s = ''
    for i in range(rows):
        cl = lineForPascal(i)
        for i in cl:
            s += str(i)+' '
        l.append(s)
    return l

rows = 3
l = pyramidPascal(rows)
for i in l:
   print(i)

