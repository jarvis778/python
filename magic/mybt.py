class Node:
    def __init__(self,v):
        self.l=None
        self.r=None
        self.v=v
class Tree:
    def __init__(self):
        self.root=None

    def add(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val,self.root)
    def _add(self,val,node):
        if val<node.v:
            if node.l is None:
                node.l=Node(val)
            else:
                self._add(val,node.l)

        else:
            if node.r is None:
                node.r = Node(val)
            else:
                self._add(val,node.r)

    def find(self,val):
        if self.root is None:
            return None
        else:
            return self._find(val,self.root)

    def _find(self,val,node):
        if val == node.v:
            return node
        elif (val>node.v and node.r is not None):
            return self._find(val,node.r)
        elif (val<node.v and node.l is not None):
            return self._find(val,node.l)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

#tree.printTree()

#print(tree.find(3).v)
tree.printTree()






