from itertools import permutations
def Perm(str):
    return list(permutations(str))
str = Perm('abc')
for letter in str:
    print(letter)