set1 = {10,10,10}
print(set1)

print(list(range(0,10)))

set1.add(11)

print(set1)

set1.update([12,13])

print(set1)



# methods - union,intersection,difference

set2 = {1,2}
set3 = {2,3}

print(set2.union(set3))
print(set2.intersection(set3))
print(set2.difference(set3))


b = {"abc", "def"}
print({s.upper() for s in b})
