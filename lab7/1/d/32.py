n = int(input()) 
li = [int(x) for x in input().split()] 
cnt = 0  
last = li[0] 
for x in range(1,n): 
    if li[x]>last: 
        cnt+=1 
    last=li[x] 
print(cnt)