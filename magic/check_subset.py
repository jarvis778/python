# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
while t > 0:
    n = int(input())
    ls = set(list(map(int, input().split(" "))))
    n1 = int(input())
    ls1 = set(list(map(int, input().split(" "))))
    if ls.issubset(ls1):
        print("True")
    else:
        print("False")

    t -= 1