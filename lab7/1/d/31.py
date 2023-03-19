n = int(input())
x = list(map(int, input().split()))
d = 0
for i in x:
    if i>0: d+=1
print(d)