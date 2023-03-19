def xor(x, y):
    if( x==0 and y==1 or x==1 and y==0):
        print(1)
    else: print(0)

x, y = map(int, input().split())
xor(x, y)