


# height of tree
def height(self, root):
    if root is None:
        return 0
    else:
        return max(self.height(root.left) ,self.height(root.right) ) +1


# count leaves of tree
def countLeaves(root):
    if root is None:
        return 0
    else:
        if root.left is None and root.right is None:
            return 1
        else:
            return countLeaves(root.left)+countLeaves(root.right)


def isBalanced(self, root):
    if root is None:
        return True
    l = self.height(root.left)
    r = self.height(root.right)

    if abs(l - r) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
        return True
    return False

def isIdentical(self,r1, r2):
    if r1 is None and r2 is None:
        return True
    elif r1 is not None and r2 is None:
        return False
    elif r2 is not None and r1 is None:
        return False
    elif r1.data==r2.data and self.isIdentical(r1.left, r2.left) and self.isIdentical(r1.right, r2.right):
        return True

def LeftView(root):
    if root is None:
        return []
    q = []
    q.append(root)
    q.append(None)
    ls=[]
    ls.append(root.data)
    l=1
    p=1
    while len(q)!=0:
        x=q.pop(0)
        if x is None:
            l+=1
            if len(q)!=0:
                q.append(None)
        else:
            if l>p:
                p=l
                ls.append(x.data)
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
    return ls