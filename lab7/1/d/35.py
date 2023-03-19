n = int(input()) 
a = [int(i) for i in input().split()]
for i in a[::-1]:
    print(i, end=" ")