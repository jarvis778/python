def spam():
    global eggs
    eggs = "wow"

eggs = 'global'
spam()
print(eggs)



ls = ['a','b']

for index,element in enumerate(ls):
    print(index,element)

a=[]
for i in range(3):
    ls=[]
    for j in range(3):
        ls.append(i+j)
    a.append(ls)
print(a)

print(list(zip(*a)))

pp = ['A','a','z','Z']
pp.sort(key=str.lower())




