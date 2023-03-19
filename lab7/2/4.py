from collections import OrderedDict

n = int(input())
words_dict = OrderedDict()

for i in range(n):
    word = input().strip()
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

print(len(words_dict))
print(' '.join([str(val) for val in words_dict.values()]))
