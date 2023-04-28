import re

nameage = '''
Bhonesh is 23 and Aman is 24
Raj is 102 and Joey is 100
'''

ages = re.findall(r'\d{1,3}', nameage)
names = re.findall(r'[A-Z][a-z]*', nameage)

dic = {}

x = 0
for name in names:
    dic[name] = ages[x]
    x += 1

print(dic)