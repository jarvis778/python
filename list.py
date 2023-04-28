ls=[1,2,3,4]
print(ls)
ls[0]=10
print(ls)
ls.append(11)
print(ls)
ls.insert(4,12)
print(ls)
ls.sort()
print(ls)
ls.reverse()
print(ls)


# method startswith


names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol']

new_list = []
for n in names:

    if n.startswith('C'):

        new_list.append(n)

print(new_list)
