nums = list(range(1, 21))
kvadrat = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(kvadrat)