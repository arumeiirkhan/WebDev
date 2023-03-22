def make_bricks(small, big, goal):
  return goal % 5 <= small and goal <= small + big * 5
