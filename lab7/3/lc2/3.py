def lucky_sum(a, b, c):
  ans = 0
  for i in [a,b,c]:
    if i!=13: ans+=i
    else: break
  return ans
