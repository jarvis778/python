import re

form = re.findall("inform","this information is not good inform")

print(form)

str = "this information is not good inform"

for i in re.finditer("inform",str):
    print(i.span())

# replace

food = "hat mat cat rat"
regex = re.compile(r'[r]at')
print(regex.sub("drdfcghvgh",food ))

# remove line break

text = '''
bhonesh is cool
what do u do
i am fine
'''

reg = re.compile(r"\n")
print(reg.sub(" ",text))


text2 = "1 23 121"
print(re.findall(r"[0-9][0-9]",text2))

# d{m,n} check for m digits to n digits only


