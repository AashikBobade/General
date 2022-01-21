problem = input().split()
D = {'zero': 0, 'one': 1, 'two': 2,
     'three': 3, 'four': 4, 'five': 5,
     'six': 6, 'seven': 7, 'eight': 8,
     'nine': 9}

val = 0
mult = 1
for word in problem:
    if word == 'minus':
        mult = -1
    elif word == 'plus':
        mult = 1
    elif word != 'plus':
        val = val + mult * D[word]

print(val)