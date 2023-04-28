from collections import deque

ls =[1,2,3,4,5,0]
d=deque(ls)
print(d)
d.appendleft(-1)
print(d)
d.pop()
print(d)
d.popleft()
print(d)