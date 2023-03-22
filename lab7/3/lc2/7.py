def make_chocolate(small, big, goal):
    maxbigbars = min(goal // 5, big)
    return goal - maxbigbars * 5 if goal - maxbigbars * 5 <= small else -1
