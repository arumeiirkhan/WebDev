n = int(input())
x = list(map(int, input().split()))
d = 0
for i in x:
    if d%2==0: print(i, end=" ")
    d += 1