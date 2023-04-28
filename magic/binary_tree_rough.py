#
# # includes tree addition , finding , printing , height ,  left view , level order traversal
#
# class node:
#     def __init__(self,data):
#         self.l=self.r=None
#         self.v=data
# class tree:
#     def __init__(self):
#         self.root = None
#
#     def find(self,data):
#         if self.root is None:
#             return None
#         else:
#             return self.findf(data,self.root)
#
#     def findf(self,data,node):
#         if node.v==data:
#             return node
#         elif node.v<data:
#             if node.r:
#                 return self.findf(data,node.r)
#         else:
#             if node.l:
#                 return self.findf(data,node.l)
#
#     def add(self,data):
#         if self.root is None:
#             self.root = node(data)
#         else:
#             self.addf(data,self.root)
#     def addf(self,data,x):
#         if x.v<data:
#             if x.r:
#                 self.addf(data,x.r)
#             else:
#                 x.r=node(data)
#         else:
#             if x.l:
#                 self.addf(data,x.l)
#             else:
#                 x.l = node(data)
#     def pf(self):
#         if self.root:
#             self.ppf(self.root)
#     def ppf(self,node):
#         if node:
#             print(node.v)
#             self.ppf(node.l)
#             self.ppf(node.r)
#     def height(self):
#         if self.root is None:
#             return 0
#         else:
#             return self.fheight(self.root)
#
#     def fheight(self,node):
#         if node:
#             return max(self.fheight(node.l),self.fheight(node.r))+1
#         else:
#             return 0
#     def ll(self):
#         if self.root is None:
#             return None
#         else:
#             return self.llf(self.root)
#
#     def llf(self,node):
#         q=[]
#         q.append(node)
#         q.append(None)
#         l=0
#         p=0
#         ls=[]
#         ls.append(node.v)
#         while len(q)!=0:
#             x=q.pop(0)
#
#             if x is None:
#                 l+=1
#                 print("level bd gya")
#                 if len(q)!=0:
#                     q.append(None)
#             else:
#                 if p<l:
#                     p=l
#                     ls.append(x.v)
#                 print("data is ",x.v,"level is",l)
#                 if x.l:
#                     q.append(x.l)
#                 if x.r:
#                     q.append(x.r)
#         print("left view of tree is ",ls)
#
# tree = tree()
# tree.add(5)
# tree.add(4)
# tree.add(6)
# tree.add(10)
# tree.add(8)
# tree.add(12)
#
#
# print("height of tree is ",tree.height())
#
# #tree.pf()
#
# tree.ll()
#
# # if tree.find(2):
# #     n=tree.find(2)
# #     if n.l:
# #         print(n.l.v)
# #     elif n.l is None:
# #         print("left is none")
# #
# #     #print(tree.find(2).v)
# #     print("Yes")
# # else:
# #     print("No")
#

class node:
    def __init__(self,data):
        self.l=self.r=None
        self.v=data

class Tree:
    def __init__(self):
        self.root = None

    # def bfs(self):
    #     q=[]
    #     ma={}
    #
    #     q.append(self.root)
    #     q.append(None)
    #     l=0
    #
    #     while len(q)!=0:
    #
    #         x=q.pop(0)
    #
    #         if x is None:
    #             l+=1
    #             if len(q)!=0:
    #                 q.append(None)
    #         else:
    #
    #             if l in ma:
    #                 ma[l].append(x.v)
    #             else:
    #                 ma[l]=[x.v]
    #             #ls.append([x.v,l])
    #             #print("nodes at level "+str(l)+" are " +str(x.v))
    #
    #             if x.l:
    #                 q.append(x.l)
    #             if x.r:
    #                 q.append(x.r)
    #
    #     print(ma)
    #
    #     for k,v in ma.items():
    #         for j in v:
    #             print(j,end=' ')
    #         print()


    def add(self,data):
        if self.root is None:
            self.root = node(data)
        else:
            self.addf(data,self.root)

    def addf(self,data,x):

        if x.v < data:
            if x.r is None:
                x.r = node(data)
            else:
                self.addf(data,x.r)
        else:
            if x.l is None:
                x.l = node(data)
            else:
                self.addf(data,x.l)

    def pf(self):
        if self.root is None:
            return None
        else:
            self.pff(self.root)

    def pff(self,node):
        if node:
            print(node.v)
            self.pff(node.l)
            self.pff(node.r)

    def find(self,data):
        if self.root is None:
            return None
        else:
            return self.findf(data,self.root)

    def findf(self,data,x):
        if x.v == data:
            #print("hi")
            return x
        elif x.v<data:
            if x.r:
                #print("hi")
                return self.findf(data,x.r)
        else:
            if x.l:
                #print("hi")
                return self.findf(data,x.l)
tree = Tree()
tree.add(100)
tree.add(101)
tree.add(30)
tree.add(40)
# tree.pf()
#
# if tree.find(100):
#     n=tree.find(100)
#     if n.l:
#         print(n.l.v)
#     elif n.l is None:
#         print("left is none")
#     print("Yes")
# else:
#     print("No")

tree.bfs()






















