

def push(ls,element):
    ls.append(element)

def pop(ls):
    ls.pop()


stack = []
push(stack,1)
push(stack,2)
print(stack)
pop(stack)
push(stack,3)

for i in stack:
    print(i)

