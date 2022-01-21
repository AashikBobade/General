'''Accept a sequence of space-separated words as input. 
Each word is either a digit from "zero" to "nine" (endpoints inclusive) or one of the two operands: "plus" or "minus". 
The operands and operators alternate in the sequence. In other words, no two consecutive words will be of the same type.

You have to find the solution of this arithmetic problem and print the answer as an integer. 
Evaluate the expression without introducing brackets anywhere. That is, minus one plus two minus three is just -1 + 2 - 3−1+2−3 '''

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
