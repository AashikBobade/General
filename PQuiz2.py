words = input().split(',')
n = len(words)
max_count = 1
for i in range(n):
    word = words[i]
    j, count = i + 1, 1
    while j < n:
        if words[j][0] == word[-1]:
            count += 1
            word = words[j]
            j += 1
        else:
            break
    if count > max_count:
        max_count = count
print(max_count)