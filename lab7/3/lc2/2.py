def lone_sum(a, b, c):
  return sum([i for i in [a, b, c] if [a, b, c].count(i) == 1])
