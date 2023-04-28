# ls=[(1,4),(2,3),(4,5)]
# s = {0}
# for i in ls:
#     l=i[0]
#     r=i[1]
#     for k in (l,r+1):
#         s.add(k)
# s.remove(0)
# print(len(s))
#
#
#
# (1,4) , (2,3) , (4,5)
#
# a[1]++
# a[5]--
#
# 0 , 1 , 2 , 3 , 4 , 5 , 6
#
# 0 , 1 , 1 , 0 , 0 , -1 , -1
#
# 0 , 1 , 2 , 2 , 2 , 1

# Input: {1, 7, 4, 3, 4, 8, 7}, k = 2

ls=[1,7,4,3,4,8,7]
k=2

ma={}
fl=0
for i in ls:
    if i in ma:
        ma[i]+=1
    else:
        ma[i]=1

    if ma[i]==k:
        fl=1

if fl:
    for p in ls:
        if ma[p]==k:
            print(p)
            break


else:
    print(-1)





