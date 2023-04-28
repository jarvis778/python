# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

arr = [1,2,3]
print(arr)
arr.append(0)
print(arr)
arr.clear()
print(arr)
arr.append(1)
arr.append(2)
print(arr)
ls = arr.copy()
print(ls)
print(ls.count(1))
ls.append(2)
print(ls.count(2))
print(ls)
ls.pop()
print(ls)
ls.remove(1)
print(ls)
ls.append(2)
print(ls)
ls.remove(2)
print(ls)
ls.append(10)
ls.append(-9)
print(ls)
ls.sort()
print(ls)
ls.reverse()
print(ls)

