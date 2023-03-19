def minim(a, b, c, d):
    minimum = a  
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    if d < minimum:
        minimum = d
    return minimum

numbers = input().split()
a, b, c, d = map(int, numbers)
print(minim(a,b,c,d))
