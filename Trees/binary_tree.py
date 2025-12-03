#from queues.queueBase import Queue as q

class Node():
    def __init__(self, data, left=None, right= None):
        self.data=data
        self.right=right
        self.left=left
        
class Binary_tree():
    def __init__(self) :
        self.root=None
        
    '''def create_node(self, data):
        return self.Node(data)
    '''
    def add_node(self, data):
        if self.root is None:
            node = Node(data, None, None)
            self.root = node
        else:
            node = self.root
            while(1):
                if data >= node.data:
                    if node.right != None:
                        node=node.right
                    else:
                        node.right= Node(data, None, None)
                        break
                else:
                    if node.left != None:
                        node=node.left
                    else:
                        node.left = Node(data, None, None)
                        break
    def preorder(self):
        node=self.root
        if node is None:
            return
        stack=[]
        r=[]
        stack.append(node)
        while stack:
            a=stack.pop()
            r.append(a.data)
            if a.right: stack.append(a.right)
            if a.left: stack.append(a.left)
        return r
    def preorderRecursion(self, root=None):
        node=root
        if node is None:
            return
        print(node.data)
        self.preorderRecursion(node.left)
        self.preorderRecursion(node.right)
        
    def inorderRecursion(self, node=None):
        if node is None:
            return
        self.inorderRecursion(node.left)
        print(node.data)
        self.inorderRecursion(node.right)
    
    def inorder(self):
        stack=[]
        
        node=self.root
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                print(node.data)
                node=node.right
                
    def postorderRecursion(self, root):
        
        if root is None:
            return
        self.postorderRecursion(root.right)
        self.postorderRecursion(root.left)
        print(root.data)
                    
obj=Binary_tree()
obj.add_node(5)
obj.add_node(2)
obj.add_node(8)
obj.add_node(7)
obj.add_node(1)
x=obj.root
print(obj.preorder())       
obj.preorderRecursion(x) 
obj.inorderRecursion(x)
obj.inorder() 
obj.postorderRecursion(x)   