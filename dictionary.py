dict = {1:'ram',2:'shyam',3:'sita'}
print(dict)
print(dict[1])
print(dict.get(1))
dict[3]='laksman'
print(dict)


dict1 = {'a':1 , 'b':2}
dict2 = {'c':4, 'd':10}
dict3 = {**dict1,**dict2}
print(dict3)