#5.20
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
set1.difference_update(set2)
print(set1)
set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2
print(set3)
set1.symmetric_difference_update(set2)
print(set1)
