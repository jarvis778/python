
#https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

import heapq

ls =[11,2,3,10]
heapq.heapify(ls)

print(ls)

heapq.heappush(ls,1)

print(ls)

print(heapq.heappop(ls)) # min element

print(ls)

print(heapq.nlargest(1,ls)[0]) # max element

print(heapq.nsmallest(1,ls))


# * with a element
a=[1,2,3]
print(a)
b=[-1 *i for i in a]
print(b)



# ls.sort(key lambda x:x[1]) 2nd key element


