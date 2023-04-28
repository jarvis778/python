


import math,re

print(dir(re))

ob = re.compile(r"^aaa$")
if re.findall(ob,"aaa"):
    print(re.findall(ob,"aaa"))




# ob = re.compile(r"\d{1,3}-\d-\w{1,10}")
# if re.findall(ob,"111-2-adsjdhj"):
#     print(re.findall(ob,"111-2-adbhsdsjdbsjbnd"))
# else:
#     print(False)
