from collections import Counter

a=[1,2,1,2,3,3,4]
c=Counter(a)
print(c)
print(list(c.elements()))
sub={1:1,2:1}
print(c.subtract(sub))
print(c)
