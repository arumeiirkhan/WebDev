n = int(input()) 
li = [int(x) for x in input().split()] 
last = li[0] 
for x in range(1,n): 
    if li[x] > 0 and last > 0 or li[x] < 0 and last < 0:
        print("YES")
        break
    last=li[x] 
else: print("NO")