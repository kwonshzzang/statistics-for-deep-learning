from itertools import combinations_with_replacement

arr = ['A', 'B', 'C']

result = list(combinations_with_replacement(arr, 2))
print(result)