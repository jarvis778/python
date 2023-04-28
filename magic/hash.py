ma={}

ls = [1,2,3,1,2,4]

for i in ls:

    if i in ma:
        ma[i] += 1
    else:
        ma[i] = 1

ele=[]
freq=[]
for k,v in ma.items():
    ele.append(k)
    freq.append(v)

print("elements")
print(ele)
print("frequencies")
print(freq)
print("map")
print(ma)