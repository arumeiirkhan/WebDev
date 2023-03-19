def sort_string(s):
    lower = []
    upper = []
    odd = []
    even = []
    for char in s:
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0:
                even.append(char)
            else:
                odd.append(char)
    sorted_string = ''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even))
    return sorted_string

s = input()
print(sort_string(s))
