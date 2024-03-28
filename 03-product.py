from itertools import product

arr = ['A', 'B', 'C']

result = list(product(arr, repeat=2))
print(result)