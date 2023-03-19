def calculate_happiness(n, arr, like_set, dislike_set):
    happiness = 0
    for num in arr:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1
    return happiness

n, m = map(int, input().split())
arr = list(map(int, input().split()))
like_set = set(map(int, input().split()))
dislike_set = set(map(int, input().split()))

happiness = calculate_happiness(n, arr, like_set, dislike_set)
print(happiness)
