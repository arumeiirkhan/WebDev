def no_teen_sum(a, b, c):
  ans = 0
  for i in [a,b,c]:
    if i!= 15 and i!=16 and i in range(13,20): i = 0
    ans+=i
  return ans
