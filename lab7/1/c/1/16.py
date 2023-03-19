a = input() 
d ="" 
for i in a[::-1]: 
    d+=i 
cnt = 0 
while d[cnt] == "0": 
    cnt+=1 
print(d[cnt::])
