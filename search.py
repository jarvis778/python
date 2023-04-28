import re

text = "the market is down"

x = re.findall("^the",text)

if x:
    print("yes")
else:
    print("no")

text1 = "sdghsgd"

if re.findall("[abc]",text1):
    print("found")
else:
    print("not found")