s="Hello world!"
print(s[-1])
print(s[:])
print(s[::-1]) # reverse
print(s.upper())
print(s.lower())
print(s.islower())

print(s.isalpha())

# join method

print(" ".join(["A","B","C"]))


'Hello'.rjust(20, '*')
# '***************Hello'

'Hello'.ljust(20, '-')
# 'Hello---------------'

'Hello'.center(20, '=')
# '=======Hello========'

st = "  ramramramramrama    "
x=st.strip()
print(x)

a=3.1456
print(f"{a:.2f}")



