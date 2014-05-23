#working
def hasHorizontalPattern(s, j):
    return s[j : j + 3] =='011'
#working
def hasVerticalPattern(lst, i, j):
    return lst[i][j]=='0' and lst[i+1][j]=='1' and lst[i+2][j]=='1'

#working
def mark(s, j, count):
    return s.replace(s[j], str(count), 1)

def numberAGrid(lst):
    count = 2
    j = 0
    for i in range(len(lst)):
        while j < len(lst[i])-2:

            if(hasHorizontalPattern(lst[i],j)):
                print("has h pattern")
                lst[i] = mark(lst[i], j+1, count)
                count += 1

            if(hasVerticalPattern(lst, i, j)):
                lst[i+1] = mark(lst[i+1], j, count)
                count += 1
            j += 1
        i += 1
    return lst
  
grid = []
for line in open("/home/sharanyavr93/docs/crossword"):
    grid.append(line.strip())
numgrid = numberAGrid(grid)

s = "hello"
for i in numgrid:
    print(i)
#li = ["011110","111111","100001"]
#print(hasVerticalPattern(li, 0, 5))



    
